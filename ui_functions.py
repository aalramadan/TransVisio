from PySide6.QtWidgets import (QMessageBox, QFileDialog, QTableWidgetItem,
                               QHeaderView,QAbstractItemView, QStyledItemDelegate, QTableWidgetItem)
from PySide6.QtCore import QSize, QEasingCurve, QPropertyAnimation, Qt, QFile, QTextStream
from PySide6.QtGui import QIcon, QMovie
from srt import parse as parse_srt, compose as compose_srt
from ass import parse as parse_ass
from openai import OpenAI
from qasync import asyncSlot
from asyncio import sleep
from audio_extract import extract_audio
from faster_whisper import WhisperModel
from datetime import timedelta
import json
import re
import google.generativeai as genai
import asyncio
import os
import uuid
import pandas as pd
import torch

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE" # Needed to get faster-whisper to work

template_file = None # Stores the loaded .srt file
template_loaded = False # Checked if template is loaded. Needed so that "Next" button doesn't keep loading the same file.
async_signal_used = False # Needed for the Start/Pause button
waiting_loop = True # Needed for the Start/Pause button
disable_delete = False # Used to disable deletetion while model is running
template_file_format = ""

class SETTINGS:
    EXPAND_WIDTH = 380
    TIME_ANIMATION = 500

    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0.2 rgb(0, 128, 255), stop:0.201 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    background-position: left center;
    """

    MODEL_MAP = {
    "GPT-4o": "gpt-4o",
    "GPT-4 Turbo": "gpt-4-turbo",
    "GPT-4": "gpt-4",
    "GPT-3.5 Turbo": "gpt-3.5-turbo",
    "Gemini 1.5 Pro": "gemini-1.5-pro",
    "Gemini 1.5 Flash": "gemini-1.5-flash",
    "Gemini 1.0 Pro": "gemini-1.0-pro"
    }

    OPENAI_MODEL = set(["gpt-4", "gpt-3.5-turbo"])
    GEMINI_MODEL = set(["gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.0-pro"])
    GEMINI_SAFETY = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]


def button_click(main_window, btn):
    btn_name = btn.objectName()
    if btn_name == "btn_back":
        main_window.StackedWidget.setCurrentWidget(main_window.Home)


def theme_switch(main_window, checkbox):
    if checkbox == main_window.chk_box_light:
        main_window.chk_box_dark.setChecked(False)
        main_window.chk_box_light.setEnabled(False)
        main_window.chk_box_dark.setEnabled(True)
        file = QFile(":/themes/theme/light.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        main_window.CentralWidget.setStyleSheet(stream.readAll())
    elif checkbox == main_window.chk_box_dark:
        main_window.chk_box_light.setChecked(False)
        main_window.chk_box_dark.setEnabled(False)
        main_window.chk_box_light.setEnabled(True)
        file = QFile(":/themes/theme/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        main_window.CentralWidget.setStyleSheet(stream.readAll())

def temp_slider_changed(main_window):
    actual_value = main_window.temp_slider.value() / 100.0  # Convert the slider value to the actual value
    main_window.lbl_temp.setText(str(actual_value))
    
def reset_temp_slider(main_window):
    if main_window.combo_model.currentIndex() <= 3:
        main_window.temp_slider.setValue(100)
        main_window.temp_slider.setMaximum(200)
    else:
        main_window.temp_slider.setValue(50)
        main_window.temp_slider.setMaximum(100)

def switch_whisper_models(main_window):
    if main_window.combo_model_whisper.currentIndex() == 0:
        main_window.api_key_whisper.setEnabled(True)
        main_window.combo_model_size.setEnabled(False)
    else:
        main_window.api_key_whisper.setEnabled(False)
        main_window.combo_model_size.setEnabled(True)


def expand_settings(main_window):
    width = main_window.SettingsExpand.width()
    if width == 0:
        widthExtended = SETTINGS.EXPAND_WIDTH 
    else:
        widthExtended = 0   
    main_window.left_box = QPropertyAnimation(main_window.SettingsExpand, b"minimumWidth")
    main_window.left_box.setDuration(SETTINGS.TIME_ANIMATION)
    main_window.left_box.setStartValue(width)
    main_window.left_box.setEndValue(widthExtended)
    main_window.left_box.setEasingCurve(QEasingCurve.InOutQuart)
    main_window.left_box.start()

def expand_about(main_window):
    width = main_window.AboutFrame.width()
    if width == 0:
        widthExtended = SETTINGS.EXPAND_WIDTH 
    else:
        widthExtended = 0   
    main_window.left_box = QPropertyAnimation(main_window.AboutFrame, b"minimumWidth")
    main_window.left_box.setDuration(SETTINGS.TIME_ANIMATION)
    main_window.left_box.setStartValue(width)
    main_window.left_box.setEndValue(widthExtended)
    main_window.left_box.setEasingCurve(QEasingCurve.InOutQuart)
    main_window.left_box.start()

def issue_warning_error(main_window, title, text): 
    QMessageBox.warning(main_window, title, text)

@asyncSlot()
async def load_template_file(main_window):
    loading_gif(main_window, 'start')
    main_window.btn_next.setEnabled(False)
    global template_loaded
    global template_file
    global template_file_format
    dialog = QFileDialog()
    dialog.setNameFilters(["Subtitle files (*.srt *.ass *.ssa)", "Video files (*.mp4 *.mkv *.webm *.flv *.avi *.mov *.wmv *.m4v)", "Audio files (*.wav *.ogg *.mp3 *.aac *.flac *.m4a *.oga *.opus)", "Excel files (*.xls *.xlsx *.csv)"])
    selected_file = ""
    if dialog.exec_(): # Open a dialog window and waits. Finishes when file is selected.
        selected_file = dialog.selectedFiles()[0]
    try:
        if selected_file != "": # Needed in case dialog was simply opened and closed without selecting a file
            main_window.input.setText(selected_file) # Show path to selected file
            if selected_file.endswith('.srt'):
                with open(selected_file, 'r', encoding="utf-8") as file:
                    template_content = file.read() 
                    template_file = list(parse_srt(template_content)) 
                    template_file_format = 'srt'
            elif selected_file.endswith('.ass') or selected_file.endswith('.ssa'):
                with open(selected_file, 'r', encoding="utf-8") as file: 
                    template_file = parse_ass(file) 
                    template_file_format = 'ass-ssa'
            elif selected_file.endswith('.xlsx') or selected_file.endswith('.xls'):
                xl = pd.ExcelFile(selected_file)
                df = xl.parse(xl.sheet_names[0]) # Get first sheet only
                template_file = df.iloc[:, 0].tolist() # Get all rows of the first column as a list
                template_file_format = 'excel'
            elif selected_file.endswith('.csv'):
                df = pd.read_csv(selected_file, header=None)
                template_file = df.iloc[:, 0].tolist()
                template_file_format = 'excel'
            else:
                api_key_whisper =  main_window.api_key_whisper.text().strip()
                if not api_key_whisper and main_window.combo_model_whisper.currentText() != "Faster-Whisper v1.0.3 (Offline)":
                    issue_warning_error(main_window, "No API Key", "Please provide an API key for the online model")
                    loading_gif(main_window, 'stop')
                    return
                
                #srt_string = await asyncio.get_event_loop().run_in_executor(None, extract_text_from_video, main_window, selected_file, api_key_whisper)  
                srt_string = extract_text_from_video(main_window, selected_file, api_key_whisper)  
                template_file = list(parse_srt(srt_string)) 

            # Only enable next button if input was processed correctly                      
            template_loaded = True
            main_window.btn_next.setEnabled(True)
    except FileNotFoundError:
        issue_warning_error(main_window, "Warning", "File not found")      
    except IsADirectoryError:
        issue_warning_error(main_window, "Error", "Can't parse directories.\nPlease select a template file")
    except Exception as e:  
        issue_warning_error(main_window, "Error", f"An error occurred: {str(e)}")
    loading_gif(main_window, 'stop')


# Extract audio. whether from a video or an audio, is stored as .wav
def extract_text_from_video(main_window, selected_file, api_key_whisper):
    unique_id = str(uuid.uuid4())
    filename = f"{unique_id}.mp3"

    duration = main_window.duration.text()
    if duration == "Max" or duration == "max":
        duration = None
    else:
        duration = float(duration)

    extract_audio(selected_file, filename, "mp3", main_window.start_time.text(), duration= duration, overwrite=True)

    if main_window.combo_model_whisper.currentText() == "Whisper v20231117 (Online)":
        # Whisper currently supports mp3, mp4, mpeg, mpga, m4a, wav, and webm
        client = OpenAI(api_key = api_key_whisper)
        with open(filename, "rb") as audio_file: # Open read-only as binary
            output = client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format='srt')  
        os.remove(filename)
        return output 
    else:
        device = 'gpu' if torch.cuda.is_available() else 'cpu'
        model = WhisperModel(main_window.combo_model_size.currentText(), device=device)
        output, info = model.transcribe(filename)
        srt_string = ""
        for i, segment in enumerate(output):
            start_seconds = int(segment.start)
            start_milliseconds = int((segment.start - start_seconds) * 1000)
            end_seconds = int(segment.end)
            end_milliseconds = int((segment.end - end_seconds) * 1000)

            start_time = f"{str(timedelta(seconds=start_seconds))},{str(start_milliseconds).zfill(3)}"
            end_time = f"{str(timedelta(seconds=end_seconds))},{str(end_milliseconds).zfill(3)}"

            text = segment.text
            srt_string += f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n"
        os.remove(filename)
        return srt_string
    
def save_template_file(main_window):
    global template_file
    options = QFileDialog.Options()

    if template_file_format == 'ass-ssa':
        filter = "SubStation Alpha (*.ssa);;Advacned SubStation Alpha (*.ass)"
        fileName, _ = QFileDialog.getSaveFileName(None,"Save File", "", filter, options=options)
        if fileName:
            for i, subtitle in enumerate(template_file.events):
                text_column = main_window.data_table.item(i, 1)
                if text_column is not None:
                    subtitle.text = text_column.text().strip()

            with open(fileName, 'w', encoding="utf-8-sig") as file:
                template_file.dump_file(file)  
            QMessageBox.information(main_window, "File Saved", "File was written successfully!")

    elif template_file_format == 'excel':
        filter = "Excel Workbook (*.xlsx);;Excel 97-2003 Workbook (*.xls);;CSV Files (*.csv)"
        fileName, _ = QFileDialog.getSaveFileName(None,"Save File", "", filter, options=options)
        if fileName:
            translated_data = []
            for i in range(len(template_file)):
                text_column = main_window.data_table.item(i, 1)
                if text_column is not None:
                    translated_data.append(text_column.text().strip())
            
            df = pd.DataFrame([template_file, translated_data]).T
            if '.csv' in fileName:
                df.to_csv(fileName, index=False, header=False, encoding="utf-8-sig")
            else:
                df.to_excel(fileName, index=False, header=False, encoding="utf-8")
            QMessageBox.information(main_window, "File Saved", "File was written successfully!")
        
    else:
        filter = "SubRip Text (*.srt);"
        fileName, _ = QFileDialog.getSaveFileName(None,"Save File", "", filter, options=options)
        if fileName:
            for i, subtitle in enumerate(template_file):
                text_column = main_window.data_table.item(i, 1)
                if text_column is not None:
                    subtitle.content = text_column.text().strip()

            with open(fileName, 'w', encoding="utf-8") as file:
                file.write(compose_srt(template_file))  

            QMessageBox.information(main_window, "File Saved", "File was written successfully!")   

def check_inputs(main_window):
    global template_loaded      
    if not main_window.input.text() :
        issue_warning_error(main_window, "Warning", "Specify a template file")    
    elif not main_window.target_language.text():
        issue_warning_error(main_window, "Warning", "Specify a target language")
    else:
        main_window.StackedWidget.setCurrentWidget(main_window.PostProcessing)
        if template_loaded == True:
            display_template_content(main_window)
            template_loaded = False


def display_template_content(main_window):
    main_window.data_table.setRowCount(0)
    main_window.data_table.setColumnCount(2)
    main_window.data_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    main_window.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    main_window.data_table.horizontalHeader().setStretchLastSection(True)
    main_window.data_table.setHorizontalHeaderLabels(["Source Text", "Target Text"])
    if template_file_format == 'ass-ssa':
        main_window.data_table.setRowCount(len(template_file.events))
        for i, sentence in enumerate(template_file.events):
            item = QTableWidgetItem(sentence.text)
            main_window.data_table.setItem(i, 0, item)
    elif template_file_format == 'excel':
        main_window.data_table.setRowCount(len(template_file))
        for i, sentence in enumerate(template_file):
            item = QTableWidgetItem(sentence)
            main_window.data_table.setItem(i, 0, item)
    else:
        main_window.data_table.setRowCount(len(template_file))
        for i, sentence in enumerate(template_file):
            item = QTableWidgetItem(sentence.content)
            main_window.data_table.setItem(i, 0, item)


def items_selected(main_window):
    selectedItems = main_window.data_table.selectedItems()
    if not disable_delete:
        # Check if any selected cell is not empty
        if any(item.text().strip() != "" for item in selectedItems):
            main_window.btn_delete_row.setEnabled(True)
        else:
            main_window.btn_delete_row.setEnabled(False)


def delete_row(main_window):
    global template_file
    # Save table
    table_data = []
    for i in range(main_window.data_table.rowCount()):
        row_data = [main_window.data_table.item(i, j).text().strip() if main_window.data_table.item(i, j) else "" for j in range(2)]
        table_data.append(row_data)

    # Mark for deletion
    selectedItems = main_window.data_table.selectedItems()
    for item in selectedItems:
        table_data[item.row()][item.column()] = None  # Mark the item for deletion
        if template_file_format == 'excel':
            if item.column() == 0:
                template_file[item.row()] = None  # Mark the item for deletion in template_file
        elif template_file_format == 'ass-ssa':
            if item.column() == 0:
                template_file.events[item.row()] = None  # Mark the item for deletion in template_file
        else:
            if item.column() == 0:
                template_file[item.row()].content = None  # Mark the item for deletion in template_file

    # Delete
    main_window.data_table.setRowCount(0)  # Clear the table
    main_window.data_table.setRowCount(len(table_data))
    for col in range(len(table_data[0])): 
        column_items = [row_data[col] for row_data in table_data if row_data[col] is not None]  # Skip deleted items
        for row, item in enumerate(column_items):
            main_window.data_table.setItem(row, col, QTableWidgetItem(item))

    for row in range(main_window.data_table.rowCount()):
        if (main_window.data_table.item(row, 0) is None or main_window.data_table.item(row, 0).text().strip() == "") and (main_window.data_table.item(row, 1) is None or main_window.data_table.item(row, 1).text().strip() == ""):
            main_window.data_table.removeRow(row)
    

    # Delete from template_file
    if template_file_format == 'ass-ssa':
        template_file.events = [event for event in template_file.events if event is not None]  # Remove deleted items
    else:
        template_file = [item for item in template_file if item is not None]  # Remove deleted items

class RTLDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.direction = Qt.RightToLeft

def change_text_direction(main_window):
    # Check the current layout direction of the second column
    delegate = main_window.data_table.itemDelegateForColumn(1)
    if isinstance(delegate, RTLDelegate):
        # If it's RTL, set it to default (LTR)
        main_window.data_table.setItemDelegateForColumn(1, QStyledItemDelegate())
    else:
        # If it's not RTL, set it to RTL
        main_window.data_table.setItemDelegateForColumn(1, RTLDelegate())

def create_sentences_dictionaries(main_window, input_size):
    num_dictionaries = 0
    num_sentences = 0

    sentences_list = {}
    sentences_list[f"{num_dictionaries}"] = {}

    for i in range(main_window.data_table.rowCount()):
        item = main_window.data_table.item(i, 0)  # Get the item in the first column
        sen = item.text().strip()  # Get the text of the item

        if num_sentences > input_size:
            num_dictionaries = num_dictionaries + 1
            sentences_list[f"{num_dictionaries}"] = {}
            num_sentences = 0
        
        sentences_list[f"{num_dictionaries}"][f"s_{i}"] = sen
        num_sentences = num_sentences + 1
    
    return sentences_list

def disable_some_buttons(main_window):
    main_window.btn_start.setIcon(QIcon(":/icons/images/icons/cil-media-pause.png"))
    main_window.btn_start.setText("Pause")
    main_window.btn_back.setEnabled(False)
    main_window.btn_settings.setEnabled(False)
    main_window.btn_delete_row.setEnabled(False)
    main_window.btn_save.setEnabled(False)
    main_window.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    main_window.data_table.setFocusPolicy(Qt.NoFocus)
    main_window.data_table.setSelectionMode(QAbstractItemView.NoSelection)


def enable_some_buttons(main_window):
    main_window.btn_start.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
    main_window.btn_start.setText("Start")
    main_window.btn_back.setEnabled(True)
    main_window.btn_settings.setEnabled(True)
    main_window.btn_delete_row.setEnabled(True)
    main_window.btn_save.setEnabled(True)

    main_window.data_table.setEditTriggers(QAbstractItemView.AllEditTriggers)
    main_window.data_table.setFocusPolicy(Qt.StrongFocus)
    main_window.data_table.setSelectionMode(QAbstractItemView.ExtendedSelection)

def gemini_call(api_client, prompt, json_string, temperature):
    generation_config = genai.types.GenerationConfig(temperature=temperature)
    return api_client.generate_content(prompt + json_string, generation_config=generation_config, safety_settings=SETTINGS.GEMINI_SAFETY)

def openai_call(api_client, model, prompt, json_string, temperature):
    return api_client.chat.completions.create (
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": json_string}
        ],
        temperature=temperature
    )  

def loading_gif(main_window, status):
    if status == 'start':
        main_window.movie = QMovie(":/loading/images/loading.gif") 
        main_window.movie.setScaledSize(QSize(45, 45))
        main_window.loading_gif.setMovie(main_window.movie) 
        main_window.loading_gif.show()
        main_window.movie.start()
    elif status == 'stop':
        main_window.loading_gif.hide()
        main_window.movie.stop()

@asyncSlot()
async def communicate_with_api(main_window):
    if int(main_window.input_size.text()) <= 0:
        issue_warning_error(main_window, "Error", "Number of input sentences must be greater than 0")  
        main_window.btn_start.setChecked(False)
        main_window.btn_start.setCheckable(True)
        return
    
    api_key =  main_window.api_key.text().strip()
    if not api_key:
        issue_warning_error(main_window, "No API Key", "Please provide an API key")
        main_window.btn_start.setChecked(False)
        main_window.btn_start.setCheckable(True)
        return


    global async_signal_used
    global waiting_loop

    if main_window.btn_start.isChecked() and not async_signal_used:
        async_signal_used = True
        disable_some_buttons(main_window)
            
        width = main_window.SettingsExpand.width()
        if width == SETTINGS.EXPAND_WIDTH:
            expand_settings(main_window)

        loading_gif(main_window, 'start')
        
        # Get the model 
        model = SETTINGS.MODEL_MAP[main_window.combo_model.currentText()]
    
        # Define prompt
        target_lang = main_window.target_language.text()
        prompt = f"""
            {main_window.prompt_edit.toPlainText()}
            The target language of translation is {target_lang}.
            This input is a JSON string. Please keep it as is and only replace the values with the translations.
            """
        if model in SETTINGS.OPENAI_MODEL:
            gpt_client = OpenAI(api_key = api_key) 
        else:
            genai.configure(api_key=api_key)
            gemini_client = genai.GenerativeModel(model_name=model)

        sentences_list = create_sentences_dictionaries(main_window, int(main_window.input_size.text()))

        row = 0 
        for _, outer_value in sentences_list.items():      
            json_string = json.dumps(outer_value)    
            try:   
                while True:       
                    # These models are stateless, meaning they don't remember the messages from previous calls,
                    # so we need to append the prompt with every call              
                    if model in SETTINGS.OPENAI_MODEL:
                        api_response = await asyncio.get_event_loop().run_in_executor(None, openai_call, gpt_client, model, prompt, json_string, (main_window.temp_slider.value() / 100.0))
                        response = api_response.choices[0].message.content      
                    else:   
                        
                        api_response = await asyncio.get_event_loop().run_in_executor(None, gemini_call, gemini_client, prompt, json_string, (main_window.temp_slider.value() / 100.0))
                        response = api_response.text
                        
                    # Extract response from JSON
                    try:
                        translations_sentences = list(json.loads(response).values())
                    except:
                        translations_sentences = re.findall(r'": "(.*?)(?="[,}])', response)
                
                    if len(translations_sentences) != len(outer_value.values()):
                        continue
                
                    for _, sentence in enumerate(translations_sentences):
                        item = QTableWidgetItem(sentence)
                        main_window.data_table.setItem(row, 1, item)
                        row = row + 1
                    main_window.repaint()
                    break     
                if not main_window.btn_start.isChecked():
                    enable_some_buttons(main_window)
                    main_window.btn_settings.setEnabled(False)
                    main_window.btn_back.setEnabled(False)
                    loading_gif(main_window, 'stop')
                    waiting_loop = True
                    main_window.btn_start.setCheckable(True)
                    while waiting_loop:
                        await sleep(1)
                    main_window.btn_start.setCheckable(True)
                    main_window.btn_start.setChecked(True)   
                    disable_some_buttons(main_window)
                    loading_gif(main_window, 'start')        

            except Exception as e:
                issue_warning_error(main_window, "Error",f"{e}")
                break
                
            
        enable_some_buttons(main_window)
        async_signal_used = False
        main_window.btn_start.setChecked(False)
        main_window.btn_start.setCheckable(True)
        loading_gif(main_window, 'stop')
    else:
        if not main_window.btn_start.isChecked():
            main_window.btn_start.setCheckable(False)
        else:
            waiting_loop = False

    