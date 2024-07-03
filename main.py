from ui_main import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from qasync import QEventLoop
import ui_functions 
import asyncio

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.loop = loop or asyncio.get_event_loop()

        self.setupUi(self) # Initializes ui_main.py
 
        # .connect can call a function, but can't pass argument to it 
        # so, we use a parameterless lambda tha wraps a call with argument
        # and then .connect ends calling the parameterless lambda
        self.btn_open.clicked.connect(lambda: ui_functions.load_template_file(self))
        self.btn_save.clicked.connect(lambda: ui_functions.save_template_file(self))
        self.btn_next.clicked.connect(lambda: ui_functions.check_inputs(self))
        self.btn_start.clicked.connect(lambda: ui_functions.communicate_with_api(self))    
        self.btn_back.clicked.connect(lambda: ui_functions.button_click(self, self.btn_back))    
        self.btn_settings.clicked.connect(lambda: ui_functions.expand_settings(self))
        self.data_table.itemSelectionChanged.connect(lambda: ui_functions.items_selected(self))
        self.btn_delete_row.clicked.connect(lambda: ui_functions.delete_row(self))
        self.btn_info.clicked.connect(lambda: ui_functions.expand_about(self))
        self.btn_reverse.clicked.connect(lambda: ui_functions.change_text_direction(self))
        self.chk_box_dark.clicked.connect(lambda: ui_functions.theme_switch(self, self.chk_box_dark))
        self.chk_box_light.clicked.connect(lambda: ui_functions.theme_switch(self, self.chk_box_light))
        self.temp_slider.valueChanged.connect(lambda: ui_functions.temp_slider_changed(self))
        self.combo_model.currentIndexChanged.connect(lambda: ui_functions.reset_temp_slider(self))
        
if __name__ == "__main__":
    app = QApplication()

    loop = QEventLoop(app) 
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()
