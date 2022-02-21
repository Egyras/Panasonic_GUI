import sys
import platform
import os

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer, QThread, Slot, Signal, QRegExp)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *
# from PySide2.QtCore import QThread, Slot, Signal
import PySide2
import pyqtgraph as pg
# from pyqtgraph import PlotWidget
# from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
# from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import json
import requests
# import matplotlib
import numpy as np
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# import matplotlib.pyplot as plt

# matplotlib.use("Qt5Agg")

# GUI FILE
from ui_main import Ui_MainWindow
# IMPORT QSS CUSTOM
from ui_styles import Style
# IMPORT FUNCTIONS
from ui_functions import *
from py_toggle import PyToggle

global IP
global update


class WorkerThread(QThread):
    measurements_signals = Signal(int, int, str, dict, str, str, float, str, str, str, name = 'm_signals')  # declare the signal

    def __init__(self, parent=None):
        QThread.__init__(self)
        # super(WorkerThread, self).__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: WorkerThread.run(self))
        self.timer.setInterval(6000)  # 5000ms = 5s
        self.timer.start()
        # iTime = int(5000)

    def run(self):
        print(IP)
        # url = "http://192.168.8.150/json"
        url = f"http://{IP}/json"
        try:
            res = requests.get(url)
            msg = res.json()
            print(msg)
            try:
                if res.status_code == 200:
                    hzPower = msg["heatpump"][8]["Value"]
                    wOutTemp = msg["heatpump"][6]["Value"]
                    status = "Connected"
                    allData = msg
                    TankTemp = msg["heatpump"][10]["Value"]
                    inletTemp = msg["heatpump"][5]["Value"]
                    wflow = msg["heatpump"][1]["Value"]
                    valve3w = msg["heatpump"][20]["Description"]
                    quiet = msg["heatpump"][18]["Value"]
                    mode = msg["heatpump"][4]["Description"]
                    self.measurements_signals.emit(int(hzPower), int(wOutTemp), status, allData, TankTemp, inletTemp,
                                                   float(wflow), valve3w, quiet, mode)
                else:
                    print("Not Working")
            except requests.exceptions as err:
                print(err)

        except requests.exceptions.ConnectionError as err:
            print(err)

    def stop(self):
        self.terminate()
        print("stop")


class MainWindow(QMainWindow):  # MainWindow class that inherits all from QMainWindow

    def __init__(self):  # Class constructor
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # START - WINDOW ATTRIBUTES
        ########################################################################

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        # SET ==> WINDOW TITLE AND ICON
        self.setWindowTitle("Panasonic Aquarea Control")
        UIFunctions.labelTitle(self, "Panasonic Aquarea Control")

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1150, 800)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        # ==> CREATE MENUS

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "ADVANCED", "btn_Advanced", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        UIFunctions.addNewMenu(self, "SETTINGS", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        # ==> QTableWidget all data

        self.ui.tableWidget_data.hide()
        # self.ui.tableWidget_data.setColumnHidden(0, True) ### hide column 0
        self.ui.tableWidget_data.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_data.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_data.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_data.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_data.setColumnWidth(0, 60)
        self.ui.tableWidget_data.setColumnWidth(1, 252)
        self.ui.tableWidget_data.setColumnWidth(2, 60)
        self.ui.tableWidget_data.setColumnWidth(3, 100)
        self.ui.tableWidget_data.show()
        self.ui.tableWidget_data.setColumnCount(4)
        self.ui.tableWidget_data.setRowCount(94)
        self.ui.tableWidget_data.verticalHeader().setVisible(False)
        headerName = ["Topic", "Name", "Value", "Description"]
        self.ui.tableWidget_data.setHorizontalHeaderLabels(headerName)

        # ADVANCED MENU ==> SEARCH FIELD

        self.ui.lineEdit_search.setStyleSheet(Style.style_LineEdit)
        self.ui.lineEdit_search.setPlaceholderText("Search...")

        # ==> TOGGLE BUTTON1

        self.toggle = PyToggle()
        self.ui.gridLayout_button.addWidget(self.toggle)
        self.toggle.stateChanged.connect(self.postCommand)
        # status = self.toggle.isChecked()

        # ==> IP TEXT FIELD VALIDATOR WITH INPUT MASK

        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regular expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)
        self.ui.lineEdit_description.setValidator(ipValidator)

        # ==> ADVANCED MENU FIRST PYTHOGRAPH VIEW

        self.graphWidget = self.ui.graphicsView
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 25]
        self.graphWidget.setBackground((27, 29, 35))
        self.graphWidget.plot(hour, temperature)
        self.graphWidget.setTitle("<span style=\"color:white;font-size:10pt\">Temperatures</span>")
        self.graphWidget.setLabel('left', "<span style=\"color:white;font-size:10px\">Temperature (°C)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:white;font-size:10px\">Hour (H)</span>")
        self.graphWidget.plot(hour, temperature)

        # ==> ADD IP TO FILE
        self.ui.pushButton_add_render.clicked.connect(self.addIP)

        # # ==> ADD TO LABEL IP
        self.ui.lineEdit_description.textChanged.connect(self.onChanged)

        # ==> READ FILE AND ADD TO IP FIELD
        text = open("IPSave.txt").read()
        self.ui.lineEdit_description.setText(text)

        # ==> MOVE WINDOW / MAXIMIZE / RESTORE

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        # ==> LOAD DEFINITIONS

        UIFunctions.uiDefinitions(self)

        # ==> QTableWidget RARAMETERS

        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # SHOW ==> MAIN WINDOW

        self.show()

        # ==> Worker Thread start

        self.wt = WorkerThread()  # This is the thread object
        self.wt.start()
        # Connect the signal from the thread to the slot_method
        self.wt.measurements_signals.connect(self.slot_method)  ### 3) connect to the slot
        app.aboutToQuit.connect(self.wt.stop)  # to stop the thread when closing the GUI

    def slot_method(self, hz, wouttemp, stat, allData, tanktemp, inltemp, wflow, valve3, quiet, mode):

        htmlTextHz = """<p align="center"><span style=" font-size:30pt;">{VALUE}</span><span style=" font-size:20pt; vertical-align:super;">Hz</span></p>"""

        newHtmlHz = htmlTextHz.replace("{VALUE}", str(hz))
        self.ui.labelPercentageHZ.setText(newHtmlHz)
        hzUsage = int(hz)
        progress = (100 - hzUsage) / 100.0
        stop_2 = str(progress - 0.001)
        stop_1 = str(progress)

        styleSheetHz = """
                        QFrame{
                        border-radius: 110px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(85, 255, 127, 255), stop:{STOP_2} rgba(255, 255, 255, 0));
                        }
                    """

        newStylesheetHz = styleSheetHz.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgressHZ.setStyleSheet(newStylesheetHz)

        # WATTER OUTLET TEMP GAUGE

        htmlTextWater = """<p align="center"><span style=" font-size:25pt;">{VALUE_w}</span><span style=" font-size:20pt; vertical-align:super;">°C</span></p>"""

        newHtmlWater = htmlTextWater.replace("{VALUE_w}", str(wouttemp))
        self.ui.labelWaterFlow.setText(newHtmlWater)
        watert = int(wouttemp)
        progresw = (60 - watert) / 60
        stop_2w = str(progresw - 0.001)
        stop_1w = str(progresw)
        newStylesheetW = styleSheetHz.replace("{STOP_1}", stop_1w).replace("{STOP_2}", stop_2w)
        self.ui.circularProgressWaterFlow.setStyleSheet(newStylesheetW)

        # STATUS BAR UPDATE

        self.ui.label_status.setText(stat)

        # TANK TEMP LABEL

        htmlTextLabels = """<p align="center"><span style=" font-size:30pt;">{VALUE}</span><span style=" font-size:15pt; vertical-align:super;">°C</span></p>"""

        newHtmlTankTemp = htmlTextLabels.replace("{VALUE}", tanktemp)
        self.ui.label_tank_tempV.setText(newHtmlTankTemp)

        # INLET TEMP LABEL
        newHtmlInletTemp = htmlTextLabels.replace("{VALUE}", inltemp)
        self.ui.label_inlet_tempV.setText(newHtmlInletTemp)

        # WATER FLOW LABEL
        htmlTextLabelsFlow = """<p align="center"><span style=" font-size:25pt;">{VALUE}</span><span style=" font-size:15pt; vertical-align:super;">l/min</span></p>"""
        newHtmlWaterFlow = htmlTextLabelsFlow.replace("{VALUE}", str(wflow))
        self.ui.label_flow_rateV.setText(newHtmlWaterFlow)

        # 3 WAY VALVE LABEL
        htmlTextLabels3way = """<p align="center"><span style=" font-size:25pt;">{VALUE}</span>"""
        newHtml3wayValve = htmlTextLabels3way.replace("{VALUE}", str(valve3))
        self.ui.label_3way_valveV.setText(newHtml3wayValve)

        # MODE LABEL
        htmlTextLabelMode = """<p align="center"><span style=" font-size:25pt;">{VALUE}</span>"""
        newHtmlMode = htmlTextLabelMode.replace("{VALUE}", mode)
        self.ui.label_mode_selectedV.setText(newHtmlMode)

        # TABLE UPDATE IN ADVANCED PAGE

        d = dict(allData)
        # print(d)
        keys = "Topic", "Name", "Value", "Description"
        w = self.ui.tableWidget_data
        for row, record in enumerate(d["heatpump"]):
            # print(record)
            for column, key in enumerate(keys):
                it = QtWidgets.QTableWidgetItem(record.get(key, ""))
                w.setItem(row, column, it)
        self.ui.lineEdit_search.textChanged.connect(self.findName)  # Search field connector

        # QUIET BUTTON STATE UPDATE

        if quiet == "1":
            self.toggle.setChecked(True)

        # CREATE pyqtSlot FOR BETTER GUI HANDLING

    @Slot()
    def findName(self):
        name = self.ui.lineEdit_search.text().lower()
        for row in range(self.ui.tableWidget_data.rowCount()):
            item = self.ui.tableWidget_data.item(row, 1)
            # if the search text is not in the item's text do not hide the row #
            self.ui.tableWidget_data.setRowHidden(row, name not in item.text().lower())

    @Slot()
    def postCommand(self):
        print(f"Status: {self.toggle.isChecked()}")
        if self.toggle.isChecked():
            setting = "SetQuietMode=1"
        else:
            setting = "SetQuietMode=0"

        url = f"http://192.168.8.150/command?{setting}"
        r = requests.request('GET', url)
        # WorkerThread.updateInterval(int(8000))
        print(r)
        print(url)

    @Slot()
    def onChanged(self, text):
        global IP
        IP = text

    def addIP(self):
        ip = self.ui.label_ip.text()
        print(ip)
        if ip != "":
            with open("IPSave.txt", "w") as CurrentFile:
                CurrentFile.write(str(ip))
        else:
            print("Empty line")

    def openFile(self):
        file = "IPSave.txt"
        if file[0]:
            f = open(file[0], 'r')
            with f:
                data = f.read()
                self.ui.lineEdit_description.setText(data)

    # UPDATE TIMER FOR BETTER SYNC IF VALUE CHANGED
    # def updateTimeronChange(self, value):
    # WorkerThread.updateInterval(Signal, value)

    # MENUS ==> DYNAMIC MENUS FUNCTIONS

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            # UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_Advanced":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Advanced_page)
            UIFunctions.resetStyle(self, "btn_Advanced")
            # UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            # UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    # START ==> APP EVENTS

    # EVENT ==> MOUSE DOUBLE CLICK

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    # EVENT ==> MOUSE CLICK

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    # EVENT ==> KEY PRESSED

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    # EVENT ==> RESIZE EVENT

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
