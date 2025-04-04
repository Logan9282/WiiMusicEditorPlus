# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FirstSetup(object):
    def setupUi(self, FirstSetup):
        FirstSetup.setObjectName("FirstSetup")
        FirstSetup.setWindowModality(QtCore.Qt.ApplicationModal)
        FirstSetup.resize(404, 294)
        FirstSetup.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: white;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:images/images/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: #121212;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"    padding-left: 1px;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:images/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    background-color: #404040;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:images/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QWidget[error=\"true\"]\n"
"{\n"
"    border: 1px solid red;\n"
"}\n"
"\n"
"QWidget[error=\"true\"]\n"
"{\n"
"    border: 1px solid red;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(FirstSetup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainWidget = QtWidgets.QStackedWidget(FirstSetup)
        self.MainWidget.setObjectName("MainWidget")
        self.Title = QtWidgets.QWidget()
        self.Title.setObjectName("Title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Title)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainTitle = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setFamily("Continuum Medium")
        font.setPointSize(14)
        self.MainTitle.setFont(font)
        self.MainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.MainTitle.setObjectName("MainTitle")
        self.verticalLayout_2.addWidget(self.MainTitle)
        self.TitleLine = QtWidgets.QFrame(self.Title)
        self.TitleLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.TitleLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TitleLine.setObjectName("TitleLine")
        self.verticalLayout_2.addWidget(self.TitleLine)
        self.Desc = QtWidgets.QLabel(self.Title)
        self.Desc.setObjectName("Desc")
        self.verticalLayout_2.addWidget(self.Desc)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.LanguageLayout = QtWidgets.QHBoxLayout()
        self.LanguageLayout.setObjectName("LanguageLayout")
        self.LanguageLabel = QtWidgets.QLabel(self.Title)
        self.LanguageLabel.setObjectName("LanguageLabel")
        self.LanguageLayout.addWidget(self.LanguageLabel)
        self.LanguageBox = QtWidgets.QComboBox(self.Title)
        self.LanguageBox.setObjectName("LanguageBox")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(0, "English")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(1, "Français")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(2, "Español")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(3, "Deutsch")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(4, "Italiano")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(5, "日本")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(6, "한국인")
        self.LanguageLayout.addWidget(self.LanguageBox)
        self.verticalLayout_2.addLayout(self.LanguageLayout)
        self.MainWidget.addWidget(self.Title)
        self.Roms = QtWidgets.QWidget()
        self.Roms.setObjectName("Roms")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Roms)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.RomTitle = QtWidgets.QLabel(self.Roms)
        font = QtGui.QFont()
        font.setFamily("Continuum Medium")
        font.setPointSize(14)
        self.RomTitle.setFont(font)
        self.RomTitle.setObjectName("RomTitle")
        self.verticalLayout_4.addWidget(self.RomTitle)
        self.RomLine = QtWidgets.QFrame(self.Roms)
        self.RomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.RomLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.RomLine.setObjectName("RomLine")
        self.verticalLayout_4.addWidget(self.RomLine)
        self.RomPath = QtWidgets.QGroupBox(self.Roms)
        self.RomPath.setObjectName("RomPath")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.RomPath)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.RomPath_Label = QtWidgets.QLabel(self.RomPath)
        self.RomPath_Label.setMinimumSize(QtCore.QSize(0, 26))
        self.RomPath_Label.setMaximumSize(QtCore.QSize(16777215, 26))
        self.RomPath_Label.setStyleSheet("QLabel\n"
"{\n"
"padding: 1px;\n"
"border: 1px solid;\n"
"border-color: #1e1e1e;\n"
"background-color: #242424;\n"
"}\n"
"\n"
"QLabel[error=\"true\"]\n"
"{\n"
"padding: 1px;\n"
"border: 1px solid;\n"
"border-color: red;\n"
"background-color: #242424;\n"
"}")
        self.RomPath_Label.setObjectName("RomPath_Label")
        self.verticalLayout_7.addWidget(self.RomPath_Label)
        self.RomPath_Buttons = QtWidgets.QHBoxLayout()
        self.RomPath_Buttons.setObjectName("RomPath_Buttons")
        self.RomPath_File = QtWidgets.QPushButton(self.RomPath)
        self.RomPath_File.setObjectName("RomPath_File")
        self.RomPath_Buttons.addWidget(self.RomPath_File)
        self.RomPath_Folder = QtWidgets.QPushButton(self.RomPath)
        self.RomPath_Folder.setObjectName("RomPath_Folder")
        self.RomPath_Buttons.addWidget(self.RomPath_Folder)
        self.verticalLayout_7.addLayout(self.RomPath_Buttons)
        self.verticalLayout_4.addWidget(self.RomPath)
        self.RomSettings = QtWidgets.QGroupBox(self.Roms)
        self.RomSettings.setObjectName("RomSettings")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.RomSettings)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Region = QtWidgets.QHBoxLayout()
        self.Region.setObjectName("Region")
        self.RegionLabel = QtWidgets.QLabel(self.RomSettings)
        self.RegionLabel.setObjectName("RegionLabel")
        self.Region.addWidget(self.RegionLabel)
        self.RegionBox = QtWidgets.QComboBox(self.RomSettings)
        self.RegionBox.setMinimumSize(QtCore.QSize(60, 20))
        self.RegionBox.setObjectName("RegionBox")
        self.RegionBox.addItem("")
        self.RegionBox.addItem("")
        self.RegionBox.addItem("")
        self.RegionBox.addItem("")
        self.Region.addWidget(self.RegionBox)
        self.verticalLayout_9.addLayout(self.Region)
        self.RomLanguage = QtWidgets.QHBoxLayout()
        self.RomLanguage.setObjectName("RomLanguage")
        self.RomLanguageLabel = QtWidgets.QLabel(self.RomSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RomLanguageLabel.sizePolicy().hasHeightForWidth())
        self.RomLanguageLabel.setSizePolicy(sizePolicy)
        self.RomLanguageLabel.setObjectName("RomLanguageLabel")
        self.RomLanguage.addWidget(self.RomLanguageLabel)
        self.RomLanguageBox = QtWidgets.QComboBox(self.RomSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RomLanguageBox.sizePolicy().hasHeightForWidth())
        self.RomLanguageBox.setSizePolicy(sizePolicy)
        self.RomLanguageBox.setCurrentText("")
        self.RomLanguageBox.setObjectName("RomLanguageBox")
        self.RomLanguage.addWidget(self.RomLanguageBox)
        self.verticalLayout_9.addLayout(self.RomLanguage)
        self.verticalLayout_4.addWidget(self.RomSettings)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.MainWidget.addWidget(self.Roms)
        self.Dolphin = QtWidgets.QWidget()
        self.Dolphin.setObjectName("Dolphin")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Dolphin)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.DolphinTitle = QtWidgets.QLabel(self.Dolphin)
        font = QtGui.QFont()
        font.setFamily("Continuum Medium")
        font.setPointSize(14)
        self.DolphinTitle.setFont(font)
        self.DolphinTitle.setObjectName("DolphinTitle")
        self.verticalLayout_11.addWidget(self.DolphinTitle)
        self.DolphinLine = QtWidgets.QFrame(self.Dolphin)
        self.DolphinLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.DolphinLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DolphinLine.setObjectName("DolphinLine")
        self.verticalLayout_11.addWidget(self.DolphinLine)
        self.DolphinPath_Title = QtWidgets.QGroupBox(self.Dolphin)
        self.DolphinPath_Title.setObjectName("DolphinPath_Title")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DolphinPath_Title)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.DolphinPath_Label = QtWidgets.QLabel(self.DolphinPath_Title)
        self.DolphinPath_Label.setMinimumSize(QtCore.QSize(0, 26))
        self.DolphinPath_Label.setMaximumSize(QtCore.QSize(16777215, 26))
        self.DolphinPath_Label.setStyleSheet("QLabel\n"
"{\n"
"padding: 1px;\n"
"border: 1px solid;\n"
"border-color: #1e1e1e;\n"
"background-color: #242424;\n"
"}\n"
"\n"
"QLabel[error=\"true\"]\n"
"{\n"
"padding: 1px;\n"
"border: 1px solid;\n"
"border-color: red;\n"
"background-color: #242424;\n"
"}")
        self.DolphinPath_Label.setObjectName("DolphinPath_Label")
        self.verticalLayout_5.addWidget(self.DolphinPath_Label)
        self.DolphinPath_Browse = QtWidgets.QPushButton(self.DolphinPath_Title)
        self.DolphinPath_Browse.setObjectName("DolphinPath_Browse")
        self.verticalLayout_5.addWidget(self.DolphinPath_Browse)
        self.verticalLayout_11.addWidget(self.DolphinPath_Title)
        self.Dolphin_Geckocodes_Title = QtWidgets.QGroupBox(self.Dolphin)
        self.Dolphin_Geckocodes_Title.setObjectName("Dolphin_Geckocodes_Title")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Dolphin_Geckocodes_Title)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Dolphon_Geckocodes = QtWidgets.QCheckBox(self.Dolphin_Geckocodes_Title)
        self.Dolphon_Geckocodes.setChecked(True)
        self.Dolphon_Geckocodes.setObjectName("Dolphon_Geckocodes")
        self.verticalLayout_10.addWidget(self.Dolphon_Geckocodes)
        self.DolphinEnableCheats = QtWidgets.QCheckBox(self.Dolphin_Geckocodes_Title)
        self.DolphinEnableCheats.setChecked(True)
        self.DolphinEnableCheats.setObjectName("DolphinEnableCheats")
        self.verticalLayout_10.addWidget(self.DolphinEnableCheats)
        self.verticalLayout_11.addWidget(self.Dolphin_Geckocodes_Title)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.MainWidget.addWidget(self.Dolphin)
        self.End = QtWidgets.QWidget()
        self.End.setObjectName("End")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.End)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.EndTitle = QtWidgets.QLabel(self.End)
        font = QtGui.QFont()
        font.setFamily("Continuum Medium")
        font.setPointSize(20)
        self.EndTitle.setFont(font)
        self.EndTitle.setObjectName("EndTitle")
        self.verticalLayout_6.addWidget(self.EndTitle)
        self.EndLine = QtWidgets.QFrame(self.End)
        self.EndLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.EndLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.EndLine.setObjectName("EndLine")
        self.verticalLayout_6.addWidget(self.EndLine)
        self.EndDesc = QtWidgets.QLabel(self.End)
        self.EndDesc.setObjectName("EndDesc")
        self.verticalLayout_6.addWidget(self.EndDesc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.EndLinks = QtWidgets.QLabel(self.End)
        self.EndLinks.setOpenExternalLinks(True)
        self.EndLinks.setObjectName("EndLinks")
        self.verticalLayout_6.addWidget(self.EndLinks)
        self.MainWidget.addWidget(self.End)
        self.verticalLayout.addWidget(self.MainWidget)
        self.BottomLine = QtWidgets.QFrame(FirstSetup)
        self.BottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.BottomLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BottomLine.setObjectName("BottomLine")
        self.verticalLayout.addWidget(self.BottomLine)
        self.MenuButtons = QtWidgets.QHBoxLayout()
        self.MenuButtons.setObjectName("MenuButtons")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.MenuButtons.addItem(spacerItem4)
        self.BackButton = QtWidgets.QPushButton(FirstSetup)
        self.BackButton.setMinimumSize(QtCore.QSize(70, 0))
        self.BackButton.setObjectName("BackButton")
        self.MenuButtons.addWidget(self.BackButton)
        self.NextButton = QtWidgets.QPushButton(FirstSetup)
        self.NextButton.setMinimumSize(QtCore.QSize(70, 0))
        self.NextButton.setObjectName("NextButton")
        self.MenuButtons.addWidget(self.NextButton)
        self.verticalLayout.addLayout(self.MenuButtons)

        self.retranslateUi(FirstSetup)
        self.MainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FirstSetup)

    def retranslateUi(self, FirstSetup):
        _translate = QtCore.QCoreApplication.translate
        FirstSetup.setWindowTitle(_translate("FirstSetup", "First Setup"))
        self.MainTitle.setText(_translate("FirstSetup", "Thanks for downloading the\n"
"Wii Music Editor Plus!"))
        self.Desc.setText(_translate("FirstSetup", "Let\'s help you setup the essentials!"))
        self.LanguageLabel.setText(_translate("FirstSetup", "Language:"))
        self.RomTitle.setText(_translate("FirstSetup", "Loading Roms"))
        self.RomPath.setTitle(_translate("FirstSetup", "Rom Path"))
        self.RomPath_Label.setText(_translate("FirstSetup", "No Specified Path"))
        self.RomPath_File.setText(_translate("FirstSetup", "Load From File"))
        self.RomPath_Folder.setText(_translate("FirstSetup", "Load From Folder"))
        self.RomSettings.setTitle(_translate("FirstSetup", "Rom Settings"))
        self.RegionLabel.setText(_translate("FirstSetup", "Fallback Region (Used if rom region can\'t be determinded):"))
        self.RegionBox.setItemText(0, _translate("FirstSetup", "U.S."))
        self.RegionBox.setItemText(1, _translate("FirstSetup", "Europe"))
        self.RegionBox.setItemText(2, _translate("FirstSetup", "Japan"))
        self.RegionBox.setItemText(3, _translate("FirstSetup", "Korea"))
        self.RomLanguageLabel.setText(_translate("FirstSetup", "Rom Language:"))
        self.DolphinTitle.setText(_translate("FirstSetup", "Setting Up Dolphin"))
        self.DolphinPath_Title.setTitle(_translate("FirstSetup", "Dolphin Path"))
        self.DolphinPath_Label.setText(_translate("FirstSetup", "No Specified Path"))
        self.DolphinPath_Browse.setText(_translate("FirstSetup", "Browse"))
        self.Dolphin_Geckocodes_Title.setTitle(_translate("FirstSetup", "Gecko Codes"))
        self.Dolphon_Geckocodes.setText(_translate("FirstSetup", "Copy Gecko codes to Dolphin save directory"))
        self.DolphinEnableCheats.setText(_translate("FirstSetup", "Force Enable Cheats when launching Dolphin"))
        self.EndTitle.setText(_translate("FirstSetup", "<html><head/><body><p align=\"center\">All Done!</p></body></html>"))
        self.EndDesc.setText(_translate("FirstSetup", "Enjoy modding Wii Music!"))
        self.EndLinks.setText(_translate("FirstSetup", "<html><head/><body><p>YouTube: <a href=\"https://www.youtube.com/BenjaminHalko\"><span style=\" text-decoration: underline; color:#ffaa00;\">https://www.youtube.com/BenjaminHalko</span></a></p><p>Donate: <a href=\"https://ko-fi.com/benjaminhalko\"><span style=\" text-decoration: underline; color:#ffaa00;\">https://ko-fi.com/benjaminhalko</span></a></p><p>Wiki: <a href=\"https://github.com/BenjaminHalko/WiiMusicEditorPlus/wiki\"><span style=\" text-decoration: underline; color:#ffaa00;\">https://github.com/BenjaminHalko/WiiMusicEditorPlus/wiki</span></a></p><p>Discord: <a href=\"https://discord.gg/NC3wYAeCDs\"><span style=\" text-decoration: underline; color:#ffaa00;\">https://discord.gg/NC3wYAeCDs</span></a></p></body></html>"))
        self.BackButton.setText(_translate("FirstSetup", "Back"))
        self.NextButton.setText(_translate("FirstSetup", "Next"))
import resources_rc
