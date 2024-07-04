# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmiqYna.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(891, 655)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(u"TransVisio")
        icon = QIcon()
        icon.addFile(u":/images/images/images/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.CentralWidget.setFont(font1)
        self.CentralWidget.setStyleSheet(u"* {\n"
"	border: none;\n"
"}\n"
"\n"
"QWidget { \n"
"	font: 12pt \"Tahoma\";\n"
"}\n"
"\n"
"QFrame#loading_gif {\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame#LeftMenuBar, #AboutFrame {\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"QFrame#AboutFrame QTextBrowser{\n"
"	color: white;\n"
"}\n"
"\n"
"QFrame#SettingsExpand {\n"
"	background-color: #495474;\n"
"}\n"
"\n"
"QFrame#NextBox, #NavBox {\n"
"	border: none;\n"
"	background-color:#495474;\n"
"}\n"
"\n"
"QFrame#ModelFrame {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame#ModelFrame QLabel{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QWidget#Home, #PostProcesing{\n"
"	background-color: #495474;\n"
"}\n"
"\n"
"QFrame#ContentBox{\n"
"	background-color:#495474;\n"
"}\n"
"\n"
"QFrame#ContentBox QPushButton{\n"
"	background-color:  #6272a4;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QFrame#ContentBox QPushButton {\n"
"	background-repeat: no-repeat; \n"
"	background-position: center;\n"
"    color: #f8f8f2;\n"
"    border: none;\n"
"}\n"
"QFrame#Con"
                        "tentBox QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QFrame#ContentBox QPushButton:pressed {	\n"
"	background-color: rgb(0, 128, 255); /* Light blue*/\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QFrame#ContentBox QPushButton:disabled {\n"
"	color: gray;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QSlider::groove:horizontal {\n"
"	height: 8px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"									stop:0 green, stop:1 red);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, "
                        "y2:0,\n"
"									stop:0 lightblack, stop:1 lightblue);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"	margin: -6px 0;\n"
"	border-radius: 9px;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QPushButton {\n"
"	background-repeat: no-repeat; \n"
"	background-position: center;\n"
"    color: #f8f8f2;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 128, 255); /* Light blue*/\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled {\n"
"	color: gray;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QComboBox{\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.pn"
                        "g);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-color: white;\n"
"	color: black;\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgb(0, 128, 255); /* Light blue*/\n"
"	border: none;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QTableWidget {\n"
"	background-color: #495474;\n"
"	gridline-color: #6272a4; \n"
"	color: white\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"}\n"
"\n"
"QTableWidget QAbstractScrollArea {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	padding: 4px;\n"
"	color: white;\n"
"	border: 1px solid #495474;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #6272a4;\n"
"	border: 1px solid #495474;\n"
"}\n"
"/* ////////////////////////////"
                        "///////////////////////////////////////////////////////////////////// */\n"
"QLineEdit {\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"    color: black;\n"
"    selection-background-color: rgb(0, 128, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QPlainTextEdit {\n"
"	background-color: white;\n"
"	color: black;\n"
"	selection-background-color: rgb(0, 128, 255);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////*/\n"
"QScrollBar:vertical {\n"
"	background: rgb(52, 59, 72);\n"
"}\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(153, 204, 255);\n"
"	min-height: 40px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: rgb(55, 63, 77);\n"
"	height: 1"
                        "0px;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: rgb(55, 63, 77);\n"
"	height: 10px;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	subcontrol-position: top;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background-color: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background-color: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(153, 204, 255);\n"
"	min-width: 40px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 10px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb"
                        "(55, 63, 77);\n"
"    width: 10px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"    background-color: white;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid black;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QTextBrowser {\n"
"	background"
                        "-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.CentralWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuBar = QFrame(self.CentralWidget)
        self.LeftMenuBar.setObjectName(u"LeftMenuBar")
        self.LeftMenuBar.setMinimumSize(QSize(60, 0))
        self.LeftMenuBar.setMaximumSize(QSize(60, 16777215))
        self.LeftMenuBar.setFrameShape(QFrame.Shape.NoFrame)
        self.LeftMenuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.LeftMenuBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuBar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.loading_gif = QLabel(self.frame)
        self.loading_gif.setObjectName(u"loading_gif")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loading_gif.sizePolicy().hasHeightForWidth())
        self.loading_gif.setSizePolicy(sizePolicy1)
        self.loading_gif.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.loading_gif)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.MenuFrame = QFrame(self.LeftMenuBar)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setMinimumSize(QSize(0, 0))
        self.MenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.MenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MenuFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.MenuFrame)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font1)
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_settings.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.btn_settings)

        self.btn_info = QPushButton(self.MenuFrame)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QSize(0, 45))
        self.btn_info.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.btn_info)


        self.verticalLayout_3.addWidget(self.MenuFrame, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_2.addWidget(self.LeftMenuBar)

        self.SettingsExpand = QFrame(self.CentralWidget)
        self.SettingsExpand.setObjectName(u"SettingsExpand")
        sizePolicy.setHeightForWidth(self.SettingsExpand.sizePolicy().hasHeightForWidth())
        self.SettingsExpand.setSizePolicy(sizePolicy)
        self.SettingsExpand.setMinimumSize(QSize(0, 0))
        self.SettingsExpand.setMaximumSize(QSize(0, 16777215))
        self.SettingsExpand.setStyleSheet(u"")
        self.SettingsExpand.setFrameShape(QFrame.Shape.NoFrame)
        self.SettingsExpand.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.SettingsExpand)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.SettingsExpand)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -275, 380, 1056))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ModelFrame = QFrame(self.scrollAreaWidgetContents)
        self.ModelFrame.setObjectName(u"ModelFrame")
        sizePolicy.setHeightForWidth(self.ModelFrame.sizePolicy().hasHeightForWidth())
        self.ModelFrame.setSizePolicy(sizePolicy)
        self.ModelFrame.setMinimumSize(QSize(380, 0))
        self.ModelFrame.setMaximumSize(QSize(16777215, 16777215))
        self.ModelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ModelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.ModelFrame)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 18, 15, 6)
        self.lbl_model = QLabel(self.ModelFrame)
        self.lbl_model.setObjectName(u"lbl_model")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_model.sizePolicy().hasHeightForWidth())
        self.lbl_model.setSizePolicy(sizePolicy2)
        self.lbl_model.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_10.addWidget(self.lbl_model)

        self.combo_model = QComboBox(self.ModelFrame)
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.setObjectName(u"combo_model")
        sizePolicy2.setHeightForWidth(self.combo_model.sizePolicy().hasHeightForWidth())
        self.combo_model.setSizePolicy(sizePolicy2)
        self.combo_model.setMinimumSize(QSize(0, 50))
        self.combo_model.setMaximumSize(QSize(16777215, 16777215))
        self.combo_model.setFont(font1)

        self.verticalLayout_10.addWidget(self.combo_model)

        self.horizontalSpacer = QSpacerItem(40, 12, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer)

        self.lbl_api_key = QLabel(self.ModelFrame)
        self.lbl_api_key.setObjectName(u"lbl_api_key")
        sizePolicy2.setHeightForWidth(self.lbl_api_key.sizePolicy().hasHeightForWidth())
        self.lbl_api_key.setSizePolicy(sizePolicy2)
        self.lbl_api_key.setFont(font1)

        self.verticalLayout_10.addWidget(self.lbl_api_key)

        self.api_key = QLineEdit(self.ModelFrame)
        self.api_key.setObjectName(u"api_key")
        sizePolicy2.setHeightForWidth(self.api_key.sizePolicy().hasHeightForWidth())
        self.api_key.setSizePolicy(sizePolicy2)
        self.api_key.setMinimumSize(QSize(0, 50))
        self.api_key.setMaximumSize(QSize(16777215, 16777215))
        self.api_key.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.api_key.setEchoMode(QLineEdit.EchoMode.Password)
        self.api_key.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.api_key)

        self.textBrowser_3 = QTextBrowser(self.ModelFrame)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        sizePolicy2.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy2)
        self.textBrowser_3.setMinimumSize(QSize(0, 60))
        self.textBrowser_3.setMaximumSize(QSize(16777215, 60))
        self.textBrowser_3.setOpenExternalLinks(True)
        self.textBrowser_3.setOpenLinks(True)

        self.verticalLayout_10.addWidget(self.textBrowser_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.input_size = QLineEdit(self.ModelFrame)
        self.input_size.setObjectName(u"input_size")
        self.input_size.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.input_size.sizePolicy().hasHeightForWidth())
        self.input_size.setSizePolicy(sizePolicy2)
        self.input_size.setMinimumSize(QSize(0, 50))
        self.input_size.setReadOnly(False)

        self.gridLayout_3.addWidget(self.input_size, 1, 1, 1, 1)

        self.lbl_input_size = QLabel(self.ModelFrame)
        self.lbl_input_size.setObjectName(u"lbl_input_size")
        sizePolicy2.setHeightForWidth(self.lbl_input_size.sizePolicy().hasHeightForWidth())
        self.lbl_input_size.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.lbl_input_size, 1, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)

        self.textBrowser_5 = QTextBrowser(self.ModelFrame)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setMinimumSize(QSize(0, 25))
        self.textBrowser_5.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_10.addWidget(self.textBrowser_5)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.ModelFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.temp_slider = QSlider(self.ModelFrame)
        self.temp_slider.setObjectName(u"temp_slider")
        self.temp_slider.setMinimumSize(QSize(0, 30))
        self.temp_slider.setMaximum(200)
        self.temp_slider.setSingleStep(1)
        self.temp_slider.setSliderPosition(100)
        self.temp_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.temp_slider, 0, 1, 1, 1)

        self.lbl_temp = QLabel(self.ModelFrame)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setMinimumSize(QSize(50, 0))
        self.lbl_temp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lbl_temp, 0, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_5)

        self.textBrowser = QTextBrowser(self.ModelFrame)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setMinimumSize(QSize(0, 80))
        self.textBrowser.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_10.addWidget(self.textBrowser)

        self.lineEdit = QLineEdit(self.ModelFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMaximumSize(QSize(16777215, 2))
        self.lineEdit.setAutoFillBackground(False)

        self.verticalLayout_10.addWidget(self.lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.ModelFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.combo_model_whisper = QComboBox(self.ModelFrame)
        self.combo_model_whisper.addItem("")
        self.combo_model_whisper.addItem("")
        self.combo_model_whisper.setObjectName(u"combo_model_whisper")
        self.combo_model_whisper.setMinimumSize(QSize(0, 50))

        self.verticalLayout_10.addWidget(self.combo_model_whisper)

        self.lbl_api_key_for_whisper = QLabel(self.ModelFrame)
        self.lbl_api_key_for_whisper.setObjectName(u"lbl_api_key_for_whisper")
        sizePolicy2.setHeightForWidth(self.lbl_api_key_for_whisper.sizePolicy().hasHeightForWidth())
        self.lbl_api_key_for_whisper.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.lbl_api_key_for_whisper)

        self.api_key_whisper = QLineEdit(self.ModelFrame)
        self.api_key_whisper.setObjectName(u"api_key_whisper")
        self.api_key_whisper.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.api_key_whisper.sizePolicy().hasHeightForWidth())
        self.api_key_whisper.setSizePolicy(sizePolicy2)
        self.api_key_whisper.setMinimumSize(QSize(0, 50))
        self.api_key_whisper.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_10.addWidget(self.api_key_whisper)

        self.label_3 = QLabel(self.ModelFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.combo_model_size = QComboBox(self.ModelFrame)
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.addItem("")
        self.combo_model_size.setObjectName(u"combo_model_size")
        self.combo_model_size.setEnabled(True)
        self.combo_model_size.setMinimumSize(QSize(0, 50))

        self.verticalLayout_10.addWidget(self.combo_model_size)

        self.textBrowser_2 = QTextBrowser(self.ModelFrame)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy2.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy2)
        self.textBrowser_2.setMinimumSize(QSize(0, 75))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 75))

        self.verticalLayout_10.addWidget(self.textBrowser_2)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lbl_duration = QLabel(self.ModelFrame)
        self.lbl_duration.setObjectName(u"lbl_duration")
        sizePolicy2.setHeightForWidth(self.lbl_duration.sizePolicy().hasHeightForWidth())
        self.lbl_duration.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.lbl_duration, 0, 1, 1, 1)

        self.start_time = QLineEdit(self.ModelFrame)
        self.start_time.setObjectName(u"start_time")
        sizePolicy2.setHeightForWidth(self.start_time.sizePolicy().hasHeightForWidth())
        self.start_time.setSizePolicy(sizePolicy2)
        self.start_time.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.start_time, 1, 0, 1, 1)

        self.duration = QLineEdit(self.ModelFrame)
        self.duration.setObjectName(u"duration")
        sizePolicy2.setHeightForWidth(self.duration.sizePolicy().hasHeightForWidth())
        self.duration.setSizePolicy(sizePolicy2)
        self.duration.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.duration, 1, 1, 1, 1)

        self.lbl_start_time = QLabel(self.ModelFrame)
        self.lbl_start_time.setObjectName(u"lbl_start_time")
        sizePolicy2.setHeightForWidth(self.lbl_start_time.sizePolicy().hasHeightForWidth())
        self.lbl_start_time.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.lbl_start_time, 0, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_6)

        self.textBrowser_4 = QTextBrowser(self.ModelFrame)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        sizePolicy2.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy2)
        self.textBrowser_4.setMinimumSize(QSize(0, 60))
        self.textBrowser_4.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_10.addWidget(self.textBrowser_4)

        self.lineEdit_2 = QLineEdit(self.ModelFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMaximumSize(QSize(16777215, 2))

        self.verticalLayout_10.addWidget(self.lineEdit_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.chk_box_dark = QCheckBox(self.ModelFrame)
        self.chk_box_dark.setObjectName(u"chk_box_dark")
        self.chk_box_dark.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.chk_box_dark, 0, 2, 1, 1)

        self.lbl_theme_2 = QLabel(self.ModelFrame)
        self.lbl_theme_2.setObjectName(u"lbl_theme_2")
        self.lbl_theme_2.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_4.addWidget(self.lbl_theme_2, 0, 0, 1, 1)

        self.chk_box_light = QCheckBox(self.ModelFrame)
        self.chk_box_light.setObjectName(u"chk_box_light")
        self.chk_box_light.setEnabled(False)
        self.chk_box_light.setMinimumSize(QSize(0, 30))
        self.chk_box_light.setCheckable(True)
        self.chk_box_light.setChecked(True)

        self.gridLayout_4.addWidget(self.chk_box_light, 0, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_4)


        self.verticalLayout_8.addWidget(self.ModelFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.SettingsExpand)

        self.ContentBox = QFrame(self.CentralWidget)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.ContentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PagesContainer = QFrame(self.ContentBox)
        self.PagesContainer.setObjectName(u"PagesContainer")
        self.PagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.PagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.PagesContainer)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.StackedWidget = QStackedWidget(self.PagesContainer)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.StackedWidget.setMinimumSize(QSize(0, 0))
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        sizePolicy.setHeightForWidth(self.Home.sizePolicy().hasHeightForWidth())
        self.Home.setSizePolicy(sizePolicy)
        self.Home.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.Home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GridLayout = QGridLayout()
        self.GridLayout.setSpacing(6)
        self.GridLayout.setObjectName(u"GridLayout")
        self.GridLayout.setContentsMargins(9, 9, 9, 9)
        self.input = QLineEdit(self.Home)
        self.input.setObjectName(u"input")
        self.input.setEnabled(True)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setMinimumSize(QSize(0, 50))
        self.input.setDragEnabled(True)
        self.input.setReadOnly(True)

        self.GridLayout.addWidget(self.input, 1, 0, 1, 1)

        self.lbl_input = QLabel(self.Home)
        self.lbl_input.setObjectName(u"lbl_input")
        self.lbl_input.setMinimumSize(QSize(0, 23))
        self.lbl_input.setFont(font1)

        self.GridLayout.addWidget(self.lbl_input, 0, 0, 1, 1)

        self.btn_open = QPushButton(self.Home)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setMinimumSize(QSize(0, 50))
        self.btn_open.setMaximumSize(QSize(150, 16777215))
        self.btn_open.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_open.setIcon(icon3)

        self.GridLayout.addWidget(self.btn_open, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.GridLayout)

        self.GridLayout2 = QGridLayout()
        self.GridLayout2.setSpacing(6)
        self.GridLayout2.setObjectName(u"GridLayout2")
        self.GridLayout2.setContentsMargins(9, 9, 9, 9)
        self.lbl_language = QLabel(self.Home)
        self.lbl_language.setObjectName(u"lbl_language")

        self.GridLayout2.addWidget(self.lbl_language, 0, 0, 1, 1)

        self.target_language = QLineEdit(self.Home)
        self.target_language.setObjectName(u"target_language")
        self.target_language.setMinimumSize(QSize(0, 50))

        self.GridLayout2.addWidget(self.target_language, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.GridLayout2)

        self.GridLayout3 = QGridLayout()
        self.GridLayout3.setSpacing(6)
        self.GridLayout3.setObjectName(u"GridLayout3")
        self.GridLayout3.setContentsMargins(9, 9, 9, 9)
        self.prompt_edit = QPlainTextEdit(self.Home)
        self.prompt_edit.setObjectName(u"prompt_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.prompt_edit.sizePolicy().hasHeightForWidth())
        self.prompt_edit.setSizePolicy(sizePolicy3)
        self.prompt_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.prompt_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.prompt_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.GridLayout3.addWidget(self.prompt_edit, 1, 0, 1, 1)

        self.lbl_prompt = QLabel(self.Home)
        self.lbl_prompt.setObjectName(u"lbl_prompt")

        self.GridLayout3.addWidget(self.lbl_prompt, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.GridLayout3)

        self.NextBox = QFrame(self.Home)
        self.NextBox.setObjectName(u"NextBox")
        sizePolicy2.setHeightForWidth(self.NextBox.sizePolicy().hasHeightForWidth())
        self.NextBox.setSizePolicy(sizePolicy2)
        self.NextBox.setMinimumSize(QSize(0, 40))
        self.NextBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.NextBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.NextBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_next = QPushButton(self.NextBox)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QSize(150, 40))
        self.btn_next.setMaximumSize(QSize(150, 40))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_next)


        self.verticalLayout.addWidget(self.NextBox)

        self.StackedWidget.addWidget(self.Home)
        self.PostProcessing = QWidget()
        self.PostProcessing.setObjectName(u"PostProcessing")
        self.verticalLayout_4 = QVBoxLayout(self.PostProcessing)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea = QScrollArea(self.PostProcessing)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollAreaWidgetContents = QWidget()
        self.ScrollAreaWidgetContents.setObjectName(u"ScrollAreaWidgetContents")
        self.ScrollAreaWidgetContents.setGeometry(QRect(0, 0, 88, 76))
        self.verticalLayout_5 = QVBoxLayout(self.ScrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.data_table = QTableWidget(self.ScrollAreaWidgetContents)
        self.data_table.setObjectName(u"data_table")
        sizePolicy.setHeightForWidth(self.data_table.sizePolicy().hasHeightForWidth())
        self.data_table.setSizePolicy(sizePolicy)
        self.data_table.setMinimumSize(QSize(0, 0))
        self.data_table.horizontalHeader().setStretchLastSection(False)
        self.data_table.verticalHeader().setVisible(True)
        self.data_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.data_table)

        self.ScrollArea.setWidget(self.ScrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.ScrollArea)

        self.NavBox = QFrame(self.PostProcessing)
        self.NavBox.setObjectName(u"NavBox")
        sizePolicy.setHeightForWidth(self.NavBox.sizePolicy().hasHeightForWidth())
        self.NavBox.setSizePolicy(sizePolicy)
        self.NavBox.setMinimumSize(QSize(0, 40))
        self.NavBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.NavBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.NavBox)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.NavBox)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(0, 40))
        self.btn_back.setMaximumSize(QSize(150, 40))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_back.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.btn_delete_row = QPushButton(self.NavBox)
        self.btn_delete_row.setObjectName(u"btn_delete_row")
        self.btn_delete_row.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_delete_row.sizePolicy().hasHeightForWidth())
        self.btn_delete_row.setSizePolicy(sizePolicy)
        self.btn_delete_row.setMinimumSize(QSize(0, 40))
        self.btn_delete_row.setMaximumSize(QSize(150, 40))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_row.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.btn_delete_row)

        self.btn_start = QPushButton(self.NavBox)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 40))
        self.btn_start.setMaximumSize(QSize(150, 40))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start.setIcon(icon7)
        self.btn_start.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_start)

        self.btn_reverse = QPushButton(self.NavBox)
        self.btn_reverse.setObjectName(u"btn_reverse")
        self.btn_reverse.setMinimumSize(QSize(0, 40))
        self.btn_reverse.setMaximumSize(QSize(150, 40))
        icon8 = QIcon(QIcon.fromTheme(u"media-playlist-repeat"))
        self.btn_reverse.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.btn_reverse)

        self.btn_save = QPushButton(self.NavBox)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 40))
        self.btn_save.setMaximumSize(QSize(150, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.btn_save)


        self.verticalLayout_4.addWidget(self.NavBox)

        self.StackedWidget.addWidget(self.PostProcessing)

        self.horizontalLayout_4.addWidget(self.StackedWidget)


        self.verticalLayout_2.addWidget(self.PagesContainer)


        self.horizontalLayout_2.addWidget(self.ContentBox)

        self.AboutFrame = QFrame(self.CentralWidget)
        self.AboutFrame.setObjectName(u"AboutFrame")
        sizePolicy.setHeightForWidth(self.AboutFrame.sizePolicy().hasHeightForWidth())
        self.AboutFrame.setSizePolicy(sizePolicy)
        self.AboutFrame.setMinimumSize(QSize(0, 0))
        self.AboutFrame.setMaximumSize(QSize(0, 16777215))
        self.AboutFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.AboutFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.about_text = QTextBrowser(self.AboutFrame)
        self.about_text.setObjectName(u"about_text")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.about_text.sizePolicy().hasHeightForWidth())
        self.about_text.setSizePolicy(sizePolicy4)
        self.about_text.setMinimumSize(QSize(360, 0))

        self.verticalLayout_13.addWidget(self.about_text)


        self.horizontalLayout_2.addWidget(self.AboutFrame)

        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.loading_gif.setText("")
        self.btn_settings.setText("")
        self.btn_info.setText("")
        self.lbl_model.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Model:</p></body></html>", None))
        self.combo_model.setItemText(0, QCoreApplication.translate("MainWindow", u"GPT-4o", None))
        self.combo_model.setItemText(1, QCoreApplication.translate("MainWindow", u"GPT-4 Turbo", None))
        self.combo_model.setItemText(2, QCoreApplication.translate("MainWindow", u"GPT-4", None))
        self.combo_model.setItemText(3, QCoreApplication.translate("MainWindow", u"GPT-3.5 Turbo", None))
        self.combo_model.setItemText(4, QCoreApplication.translate("MainWindow", u"Gemini 1.5 Pro", None))
        self.combo_model.setItemText(5, QCoreApplication.translate("MainWindow", u"Gemini 1.5 Flash", None))
        self.combo_model.setItemText(6, QCoreApplication.translate("MainWindow", u"Gemini 1.0 Pro", None))

        self.lbl_api_key.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>API Key:</p></body></html>", None))
        self.api_key.setText("")
        self.api_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Check links below", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#d0d0d0;\">Go here to obtain API Keys:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#d0d0d0;\">Gemini Models: </span><a href=\"https://aistudio.google.com/app/apikey\"><span style=\" font-size:10pt; text-decoration: underline; color:#2fbdfa"
                        ";\">https://aistudio.google.com/app/apikey</span></a><span style=\" font-size:10pt;\"><br /></span><span style=\" font-size:10pt; color:#d0d0d0;\">GPT Models:</span><span style=\" font-size:10pt;\"> </span><a href=\"https://platform.openai.com/api-keys\"><span style=\" font-size:10pt; text-decoration: underline; color:#2fbdfa;\">https://platform.openai.com/api-keys</span></a></p></body></html>", None))
        self.input_size.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.input_size.setPlaceholderText("")
        self.lbl_input_size.setText(QCoreApplication.translate("MainWindow", u"Input Size (Sentences)", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#d0d0d0;\">Number of sentences to be translated at once.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.lbl_temp.setText(QCoreApplication.translate("MainWindow", u"1.00", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#d0d0d0;\">Controls the randomness of the model\u2019s output. A lower value makes the output more deterministic and focused, while a higher value makes the output more diverse and creative.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model (Video/Audio Input Only):", None))
        self.combo_model_whisper.setItemText(0, QCoreApplication.translate("MainWindow", u"Faster-Whisper v1.0.3 (Offline)", None))
        self.combo_model_whisper.setItemText(1, QCoreApplication.translate("MainWindow", u"Whisper v20231117 (Online)", None))

        self.lbl_api_key_for_whisper.setText(QCoreApplication.translate("MainWindow", u"API Key (Online Version Only):", None))
        self.api_key_whisper.setText("")
        self.api_key_whisper.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://platform.openai.com/api-keys", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Model Size (Offline Version Only):", None))
        self.combo_model_size.setItemText(0, QCoreApplication.translate("MainWindow", u"tiny", None))
        self.combo_model_size.setItemText(1, QCoreApplication.translate("MainWindow", u"base", None))
        self.combo_model_size.setItemText(2, QCoreApplication.translate("MainWindow", u"small", None))
        self.combo_model_size.setItemText(3, QCoreApplication.translate("MainWindow", u"medium", None))
        self.combo_model_size.setItemText(4, QCoreApplication.translate("MainWindow", u"large", None))
        self.combo_model_size.setItemText(5, QCoreApplication.translate("MainWindow", u"large-v1", None))
        self.combo_model_size.setItemText(6, QCoreApplication.translate("MainWindow", u"large-v2", None))
        self.combo_model_size.setItemText(7, QCoreApplication.translate("MainWindow", u"large-v3", None))
        self.combo_model_size.setItemText(8, QCoreApplication.translate("MainWindow", u"distil-large-v2", None))
        self.combo_model_size.setItemText(9, QCoreApplication.translate("MainWindow", u"distil-large-v3", None))

        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#d0d0d0;\">Used to transcribe video/audio input into text.<br />Whisper (Online) audio input is limited to 25 MB.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#d0d0d0;\">Faster-Whisper (Offline) will need to download the model on first use."
                        "</span></p></body></html>", None))
        self.lbl_duration.setText(QCoreApplication.translate("MainWindow", u"Duration (Seconds)", None))
        self.start_time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.duration.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.lbl_start_time.setText(QCoreApplication.translate("MainWindow", u"Start Time (HH:MM:SS)", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma','sans-serif'; font-size:10pt; color:#d0d0d0;\">Specifies the Start Time and Duration for Video/Audio input.<br />For example, [00:05:00 - 200] will start transcribing at minute 5 for a duration of 200 seconds.</span></p></body></html>", None))
        self.chk_box_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.lbl_theme_2.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.chk_box_light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.input.setText("")
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click open to select an input", None))
        self.lbl_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lbl_language.setText(QCoreApplication.translate("MainWindow", u"Target Language", None))
        self.target_language.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.target_language.setPlaceholderText("")
        self.prompt_edit.setPlainText(QCoreApplication.translate("MainWindow", u"As a professional subtitle translator, your task is solely to translate subtitles. \n"
"There\u2019s no need for you to reply to any messages. Please take note of the following:\n"
"1) Keep sentences separate during translation. Do not combine them.\n"
"2) Adapt any names in the subtitles to the target language.\n"
"", None))
        self.lbl_prompt.setText(QCoreApplication.translate("MainWindow", u"Edit Prompt", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btn_delete_row.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_reverse.setText(QCoreApplication.translate("MainWindow", u"Flip Text", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.about_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">TransVisio</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">V1.0.0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />TransVisio: Automating Subtitle "
                        "Translation</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project Title: TransVisio: Automating Subtitle Translation \u2013 A Leap Towards Improved Audiovisual Content Accessibility</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Main Researcher: Ahmad S Haider</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Co-researcher: Hussein Abu-Rayyash<br /> Developer: Ali Al-Ramadan</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:"
                        "0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Funding: This project is generously funded by the Abdul Hameed Shoman Foundation.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hosting Institution: The project is hosted by the English Language and Translation Department at the Applied Science Private University.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Agreement Number: 230800351</span></p></body></html>", None))
        pass
    # retranslateUi

