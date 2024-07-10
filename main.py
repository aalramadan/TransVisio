from ui_main import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import ui_functions 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.loop = loop or ui_functions.get_event_loop()

        self.setupUi(self) # Initializes ui_main.py
        ui_functions.generate_prompt(self)

        # .connect can call a function, but can't pass argument to it 
        # so, we use a parameterless lambda tha wraps a call with argument
        # and then .connect ends calling the parameterless lambda
        self.btn_open.clicked.connect(lambda: ui_functions.load_template_file(self))
        self.btn_save.clicked.connect(lambda: ui_functions.save_template_file(self, False))
        self.btn_save_transcription.clicked.connect(lambda: ui_functions.save_template_file(self, True))
        self.btn_next.clicked.connect(lambda: ui_functions.check_inputs(self))
        self.btn_start.clicked.connect(lambda: ui_functions.communicate_with_api(self))    
        self.btn_back.clicked.connect(lambda: ui_functions.button_click(self, self.btn_back))   
         
        self.btn_settings.clicked.connect(lambda: ui_functions.expand_settings(self))
        self.btn_info.clicked.connect(lambda: ui_functions.expand_about(self))

        self.data_table.itemSelectionChanged.connect(lambda: ui_functions.items_selected(self))
        self.btn_delete_row.clicked.connect(lambda: ui_functions.delete_row(self))
        self.btn_reverse.clicked.connect(lambda: ui_functions.change_text_direction(self))
        self.chk_box_dark.clicked.connect(lambda: ui_functions.theme_switch(self, self.chk_box_dark))
        self.chk_box_light.clicked.connect(lambda: ui_functions.theme_switch(self, self.chk_box_light))
        self.temp_slider.valueChanged.connect(lambda: ui_functions.temp_slider_changed(self))
        self.combo_model.currentIndexChanged.connect(lambda: ui_functions.reset_temp_slider(self))
        self.combo_model_whisper.currentIndexChanged.connect(lambda: ui_functions.switch_whisper_models(self))


        self.box_genre.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))
        self.box_demo.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))
        self.box_localization.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))

        self.box_register.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))
        self.box_culture.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))
        self.box_speaker.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))

        self.box_subtitle.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))
        self.box_speed.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))
        self.box_sound.currentIndexChanged.connect(lambda: ui_functions.generate_prompt(self))

        

if __name__ == "__main__":
    app = QApplication()

    loop = ui_functions.QEventLoop(app) 
    ui_functions.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()
