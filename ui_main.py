# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASElsUPua.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget

import files_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1034, 780)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-speedometer.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)

        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.HomeFrame = QFrame(self.page_home)
        self.HomeFrame.setObjectName(u"HomeFrame")
        self.HomeFrame.setFrameShape(QFrame.StyledPanel)
        self.HomeFrame.setFrameShadow(QFrame.Raised)
        self.circularProgressBar_Main = QFrame(self.HomeFrame)
        self.circularProgressBar_Main.setObjectName(u"circularProgressBar_Main")
        self.circularProgressBar_Main.setGeometry(QRect(30, 29, 241, 241))
        self.circularProgressBar_Main.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QFrame.StyledPanel)
        self.circularProgressBar_Main.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBar_Main)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg.setFrameShape(QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.circularProgressBar_Main)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer.setFrameShape(QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.circularContainer)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-17, 29, 211, 131))
        self.infoLayout = QGridLayout(self.gridLayoutWidget)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName = QLabel(self.gridLayoutWidget)
        self.labelAplicationName.setObjectName(u"labelAplicationName")
        font2 = QFont()
        font2.setPointSize(10)
        self.labelAplicationName.setFont(font2)
        self.labelAplicationName.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)

        self.labelPercentageHZ = QLabel(self.gridLayoutWidget)
        self.labelPercentageHZ.setObjectName(u"labelPercentageHZ")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(25)
        self.labelPercentageHZ.setFont(font3)
        self.labelPercentageHZ.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageHZ.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelPercentageHZ, 1, 0, 1, 1)

        self.circularProgressHZ = QFrame(self.circularProgressBar_Main)
        self.circularProgressHZ.setObjectName(u"circularProgressHZ")
        self.circularProgressHZ.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressHZ.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:1 rgba(85, 255, 127, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressHZ.setFrameShape(QFrame.StyledPanel)
        self.circularProgressHZ.setFrameShadow(QFrame.Raised)
        self.circularProgressHZ.raise_()
        self.circularBg.raise_()
        self.circularContainer.raise_()
        self.circularProgressBar_Main1 = QFrame(self.HomeFrame)
        self.circularProgressBar_Main1.setObjectName(u"circularProgressBar_Main1")
        self.circularProgressBar_Main1.setGeometry(QRect(270, 30, 241, 241))
        self.circularProgressBar_Main1.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main1.setFrameShape(QFrame.StyledPanel)
        self.circularProgressBar_Main1.setFrameShadow(QFrame.Raised)
        self.circularBg_1 = QFrame(self.circularProgressBar_Main1)
        self.circularBg_1.setObjectName(u"circularBg_1")
        self.circularBg_1.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_1.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_1.setFrameShape(QFrame.StyledPanel)
        self.circularBg_1.setFrameShadow(QFrame.Raised)
        self.circularContainer_1 = QFrame(self.circularProgressBar_Main1)
        self.circularContainer_1.setObjectName(u"circularContainer_1")
        self.circularContainer_1.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_1.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_1.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_1.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_6 = QWidget(self.circularContainer_1)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(-17, 29, 211, 131))
        self.infoLayout_1 = QGridLayout(self.gridLayoutWidget_6)
        self.infoLayout_1.setObjectName(u"infoLayout_1")
        self.infoLayout_1.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_1 = QLabel(self.gridLayoutWidget_6)
        self.labelAplicationName_1.setObjectName(u"labelAplicationName_1")
        self.labelAplicationName_1.setFont(font2)
        self.labelAplicationName_1.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_1.setAlignment(Qt.AlignCenter)

        self.infoLayout_1.addWidget(self.labelAplicationName_1, 0, 0, 1, 1)

        self.labelWaterFlow = QLabel(self.gridLayoutWidget_6)
        self.labelWaterFlow.setObjectName(u"labelWaterFlow")
        self.labelWaterFlow.setFont(font3)
        self.labelWaterFlow.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelWaterFlow.setAlignment(Qt.AlignCenter)

        self.infoLayout_1.addWidget(self.labelWaterFlow, 1, 0, 1, 1)

        self.circularProgressWaterFlow = QFrame(self.circularProgressBar_Main1)
        self.circularProgressWaterFlow.setObjectName(u"circularProgressWaterFlow")
        self.circularProgressWaterFlow.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressWaterFlow.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:1 rgba(85, 255, 127, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressWaterFlow.setFrameShape(QFrame.StyledPanel)
        self.circularProgressWaterFlow.setFrameShadow(QFrame.Raised)
        self.circularProgressWaterFlow.raise_()
        self.circularBg_1.raise_()
        self.circularContainer_1.raise_()
        self.frame_div_render_time = QFrame(self.HomeFrame)
        self.frame_div_render_time.setObjectName(u"frame_div_render_time")
        self.frame_div_render_time.setGeometry(QRect(550, 20, 341, 561))
        self.frame_div_render_time.setMinimumSize(QSize(0, 160))
        self.frame_div_render_time.setStyleSheet(u"border-radius: 5px;")
        self.frame_div_render_time.setFrameShape(QFrame.StyledPanel)
        self.frame_div_render_time.setFrameShadow(QFrame.Plain)
        self.label_tank_tempn = QLabel(self.frame_div_render_time)
        self.label_tank_tempn.setObjectName(u"label_tank_tempn")
        self.label_tank_tempn.setGeometry(QRect(0, 0, 174, 16))
        self.label_tank_tempn.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.label_tank_tempn.setFont(font4)
        self.label_tank_tempn.setStyleSheet(u"")
        self.label_tank_tempn.setLineWidth(1)
        self.label_tank_tempn.setAlignment(Qt.AlignCenter)
        self.label_inlet_tempn = QLabel(self.frame_div_render_time)
        self.label_inlet_tempn.setObjectName(u"label_inlet_tempn")
        self.label_inlet_tempn.setGeometry(QRect(160, 0, 173, 17))
        self.label_inlet_tempn.setMaximumSize(QSize(16777215, 20))
        self.label_inlet_tempn.setFont(font4)
        self.label_inlet_tempn.setStyleSheet(u"")
        self.label_inlet_tempn.setLineWidth(1)
        self.label_inlet_tempn.setAlignment(Qt.AlignCenter)
        self.label_tank_tempV = QLabel(self.frame_div_render_time)
        self.label_tank_tempV.setObjectName(u"label_tank_tempV")
        self.label_tank_tempV.setGeometry(QRect(0, 20, 181, 51))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(25)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_tank_tempV.setFont(font5)
        self.label_tank_tempV.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_tank_tempV.setAlignment(Qt.AlignCenter)
        self.label_inlet_tempV = QLabel(self.frame_div_render_time)
        self.label_inlet_tempV.setObjectName(u"label_inlet_tempV")
        self.label_inlet_tempV.setGeometry(QRect(170, 20, 174, 51))
        self.label_inlet_tempV.setFont(font5)
        self.label_inlet_tempV.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_inlet_tempV.setAlignment(Qt.AlignCenter)
        self.label_flow_raten = QLabel(self.frame_div_render_time)
        self.label_flow_raten.setObjectName(u"label_flow_raten")
        self.label_flow_raten.setGeometry(QRect(0, 300, 174, 16))
        self.label_flow_raten.setMaximumSize(QSize(16777215, 20))
        self.label_flow_raten.setFont(font4)
        self.label_flow_raten.setStyleSheet(u"")
        self.label_flow_raten.setLineWidth(1)
        self.label_flow_raten.setAlignment(Qt.AlignCenter)
        self.label_flow_rateV = QLabel(self.frame_div_render_time)
        self.label_flow_rateV.setObjectName(u"label_flow_rateV")
        self.label_flow_rateV.setGeometry(QRect(10, 320, 181, 51))
        self.label_flow_rateV.setFont(font5)
        self.label_flow_rateV.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_flow_rateV.setAlignment(Qt.AlignCenter)
        self.label_3way_valven = QLabel(self.frame_div_render_time)
        self.label_3way_valven.setObjectName(u"label_3way_valven")
        self.label_3way_valven.setGeometry(QRect(160, 100, 173, 17))
        self.label_3way_valven.setMaximumSize(QSize(16777215, 20))
        self.label_3way_valven.setFont(font4)
        self.label_3way_valven.setStyleSheet(u"")
        self.label_3way_valven.setLineWidth(1)
        self.label_3way_valven.setAlignment(Qt.AlignCenter)
        self.label_3way_valveV = QLabel(self.frame_div_render_time)
        self.label_3way_valveV.setObjectName(u"label_3way_valveV")
        self.label_3way_valveV.setGeometry(QRect(160, 120, 174, 51))
        self.label_3way_valveV.setFont(font5)
        self.label_3way_valveV.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_3way_valveV.setAlignment(Qt.AlignCenter)
        self.label_mode_selectedn = QLabel(self.frame_div_render_time)
        self.label_mode_selectedn.setObjectName(u"label_mode_selectedn")
        self.label_mode_selectedn.setGeometry(QRect(80, 200, 173, 17))
        self.label_mode_selectedn.setMaximumSize(QSize(16777215, 20))
        self.label_mode_selectedn.setFont(font4)
        self.label_mode_selectedn.setStyleSheet(u"")
        self.label_mode_selectedn.setLineWidth(1)
        self.label_mode_selectedn.setAlignment(Qt.AlignCenter)
        self.label_mode_selectedV = QLabel(self.frame_div_render_time)
        self.label_mode_selectedV.setObjectName(u"label_mode_selectedV")
        self.label_mode_selectedV.setGeometry(QRect(60, 220, 211, 51))
        self.label_mode_selectedV.setFont(font5)
        self.label_mode_selectedV.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_mode_selectedV.setAlignment(Qt.AlignCenter)
        self.label_defrostn = QLabel(self.frame_div_render_time)
        self.label_defrostn.setObjectName(u"label_defrostn")
        self.label_defrostn.setGeometry(QRect(0, 100, 173, 17))
        self.label_defrostn.setMaximumSize(QSize(16777215, 20))
        self.label_defrostn.setFont(font4)
        self.label_defrostn.setStyleSheet(u"")
        self.label_defrostn.setLineWidth(1)
        self.label_defrostn.setAlignment(Qt.AlignCenter)
        self.label_defrostv = QLabel(self.frame_div_render_time)
        self.label_defrostv.setObjectName(u"label_defrostv")
        self.label_defrostv.setGeometry(QRect(0, 120, 174, 51))
        self.label_defrostv.setFont(font5)
        self.label_defrostv.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_defrostv.setAlignment(Qt.AlignCenter)
        self.label_inlet_tempn_2 = QLabel(self.frame_div_render_time)
        self.label_inlet_tempn_2.setObjectName(u"label_inlet_tempn_2")
        self.label_inlet_tempn_2.setGeometry(QRect(160, 300, 173, 17))
        self.label_inlet_tempn_2.setMaximumSize(QSize(16777215, 20))
        self.label_inlet_tempn_2.setFont(font4)
        self.label_inlet_tempn_2.setStyleSheet(u"")
        self.label_inlet_tempn_2.setLineWidth(1)
        self.label_inlet_tempn_2.setAlignment(Qt.AlignCenter)
        self.label_target_tempV = QLabel(self.frame_div_render_time)
        self.label_target_tempV.setObjectName(u"label_target_tempV")
        self.label_target_tempV.setGeometry(QRect(160, 320, 174, 51))
        self.label_target_tempV.setFont(font5)
        self.label_target_tempV.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_target_tempV.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_5 = QWidget(self.HomeFrame)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(40, 300, 144, 81))
        self.gridLayout_button = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_button.setObjectName(u"gridLayout_button")
        self.gridLayout_button.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_4 = QLabel(self.gridLayoutWidget_5)
        self.labelAplicationName_4.setObjectName(u"labelAplicationName_4")
        self.labelAplicationName_4.setFont(font2)
        self.labelAplicationName_4.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_button.addWidget(self.labelAplicationName_4, 0, 0, 1, 1)

        self.gridLayoutWidget_7 = QWidget(self.HomeFrame)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(40, 390, 151, 81))
        self.gridLayout_button_2 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_button_2.setObjectName(u"gridLayout_button_2")
        self.gridLayout_button_2.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_5 = QLabel(self.gridLayoutWidget_7)
        self.labelAplicationName_5.setObjectName(u"labelAplicationName_5")
        self.labelAplicationName_5.setFont(font2)
        self.labelAplicationName_5.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_button_2.addWidget(self.labelAplicationName_5, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.HomeFrame)

        self.stackedWidget.addWidget(self.page_home)
        self.Advanced_page = QWidget()
        self.Advanced_page.setObjectName(u"Advanced_page")
        self.tableWidget_data = QTableWidget(self.Advanced_page)
        if (self.tableWidget_data.columnCount() < 4):
            self.tableWidget_data.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_data.setObjectName(u"tableWidget_data")
        self.tableWidget_data.setGeometry(QRect(0, 40, 501, 551))
        self.tableWidget_data.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(52, 59, 72);	\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.lineEdit_search = QLineEdit(self.Advanced_page)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(0, 0, 251, 31))
        self.lineEdit_search.setFont(font2)
        self.lineEdit_search.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.formLayoutWidget = QWidget(self.Advanced_page)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(520, 40, 411, 261))
        self.formLayout_graph1 = QFormLayout(self.formLayoutWidget)
        self.formLayout_graph1.setObjectName(u"formLayout_graph1")
        self.formLayout_graph1.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = PlotWidget(self.formLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"PlotWidget {	\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.formLayout_graph1.setWidget(0, QFormLayout.SpanningRole, self.graphicsView)

        self.stackedWidget.addWidget(self.Advanced_page)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_div_table_widget = QFrame(self.frame_3)
        self.frame_div_table_widget.setObjectName(u"frame_div_table_widget")
        self.frame_div_table_widget.setEnabled(True)
        self.frame_div_table_widget.setStyleSheet(u"border-radius: 5px;")
        self.frame_div_table_widget.setFrameShape(QFrame.StyledPanel)
        self.frame_div_table_widget.setFrameShadow(QFrame.Raised)
        self.pushButton_add_render = QPushButton(self.frame_div_table_widget)
        self.pushButton_add_render.setObjectName(u"pushButton_add_render")
        self.pushButton_add_render.setGeometry(QRect(360, 10, 120, 30))
        self.pushButton_add_render.setMinimumSize(QSize(120, 30))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(9)
        self.pushButton_add_render.setFont(font6)
        self.pushButton_add_render.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_render.setIcon(icon3)
        self.lineEdit_description = QLineEdit(self.frame_div_table_widget)
        self.lineEdit_description.setObjectName(u"lineEdit_description")
        self.lineEdit_description.setGeometry(QRect(0, 10, 347, 30))
        self.lineEdit_description.setMinimumSize(QSize(0, 30))
        self.lineEdit_description.setFont(font4)
        self.lineEdit_description.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_description.setMaxLength(32)
        self.lineEdit_description.raise_()
        self.pushButton_add_render.raise_()

        self.horizontalLayout_12.addWidget(self.frame_div_table_widget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QHBoxLayout()
        self.frame_label_bottom.setSpacing(0)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setContentsMargins(10, -1, 10, -1)
        self.label_app = QLabel(self.frame_grip)
        self.label_app.setObjectName(u"label_app")
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        self.label_app.setFont(font7)
        self.label_app.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.frame_label_bottom.addWidget(self.label_app)

        self.label_status = QLabel(self.frame_grip)
        self.label_status.setObjectName(u"label_status")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy4)
        self.label_status.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.frame_label_bottom.addWidget(self.label_status)

        self.label_version = QLabel(self.frame_grip)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font7)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.frame_label_bottom.addWidget(self.label_version)


        self.horizontalLayout_6.addLayout(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.labelAplicationName.setText(QCoreApplication.translate("MainWindow", u"<strong>HZ</strong> USAGE", None))
        self.labelPercentageHZ.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:40pt;\">0</span><span style=\" font-size:30pt; vertical-align:super;\">Hz</span></p>", None))
        self.labelAplicationName_1.setText(QCoreApplication.translate("MainWindow", u"<strong>Water</strong> Outlet", None))
        self.labelWaterFlow.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:40pt;\">0</span><span style=\" font-size:30pt; vertical-align:super;\">\u00b0C</span></p>", None))
        self.label_tank_tempn.setText(QCoreApplication.translate("MainWindow", u"<strong>Tank</strong> Temperature", None))
        self.label_inlet_tempn.setText(QCoreApplication.translate("MainWindow", u"<strong>Inlet</strong> Temperature", None))
        self.label_tank_tempV.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:30pt;\">0</span><span style=\" font-size:15pt; vertical-align:super;\">\u00b0C</span></p>", None))
        self.label_inlet_tempV.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:30pt;\">0</span><span style=\" font-size:15pt; vertical-align:super;\">\u00b0C</span></p>", None))
        self.label_flow_raten.setText(QCoreApplication.translate("MainWindow", u"<strong>Flow</strong> Rate", None))
        self.label_flow_rateV.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:30pt;\">0</span><span style=\" font-size:15pt; vertical-align:super;\">l/min</span></p>", None))
        self.label_3way_valven.setText(QCoreApplication.translate("MainWindow", u"<strong>3 Way</strong> Valve", None))
        self.label_3way_valveV.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:25pt;\">Floor</span>", None))
        self.label_mode_selectedn.setText(QCoreApplication.translate("MainWindow", u"<strong>Heating</strong> Mode", None))
        self.label_mode_selectedV.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:25pt;\">Floor</span>", None))
        self.label_defrostn.setText(QCoreApplication.translate("MainWindow", u"<strong>Defrosting</strong> Stage", None))
        self.label_defrostv.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:25pt;\">OFF</span>", None))
        self.label_inlet_tempn_2.setText(QCoreApplication.translate("MainWindow", u"<strong>Target</strong> Temperature", None))
        self.label_target_tempV.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:30pt;\">0</span><span style=\" font-size:15pt; vertical-align:super;\">\u00b0C</span></p>", None))
        self.labelAplicationName_4.setText(QCoreApplication.translate("MainWindow", u"<strong>Enable</strong> QuietMode", None))
        self.labelAplicationName_5.setText(QCoreApplication.translate("MainWindow", u"<strong>Enable</strong> PowerMode", None))
        ___qtablewidgetitem = self.tableWidget_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Topic", None));
        ___qtablewidgetitem1 = self.tableWidget_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget_data.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem3 = self.tableWidget_data.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.pushButton_add_render.setText(QCoreApplication.translate("MainWindow", u"ADD API", None))
        self.lineEdit_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP ADDRESS", None))
        self.label_app.setText(QCoreApplication.translate("MainWindow", u"App Status: ", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Disconected", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

