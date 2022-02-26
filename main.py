import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer, QThread, Slot, Signal, QRegExp)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *
import pyqtgraph as pg
import json
import requests
from queue import Queue, Empty

# GUI FILE
from ui_main import Ui_MainWindow
# IMPORT QSS CUSTOM
from ui_styles import Style
# IMPORT FUNCTIONS
from ui_functions import *
from py_toggle import PyToggle

global IP


class WorkerThread(QThread):
    measurements_signals = Signal(int, int, str, dict, str, str, float,
                                  str, str, str, int, int, int, int, str, str, name = 'm_signals')  # declare the signal

    def __init__(self, parent=None):
        QThread.__init__(self)
        self.queue = Queue()

    def run(self):
        self.keepRunning = True
        # url = "http://192.168.8.150/"
        url = f"http://{IP}/"
        quiet = None

        while self.keepRunning:
            try:
                res = requests.get(url + 'json')
                msg = res.json()
                print(msg)
                if res.status_code == 200:
                    hzPower = msg["heatpump"][8]["Value"]
                    TatgetTemp = msg["heatpump"][7]["Value"]
                    wOutTemp = msg["heatpump"][6]["Value"]
                    status = "Connected"
                    allData = msg
                    TankTemp = msg["heatpump"][10]["Value"]
                    inletTemp = msg["heatpump"][5]["Value"]
                    wflow = msg["heatpump"][1]["Value"]
                    valve3w = msg["heatpump"][20]["Description"]
                    mode = msg["heatpump"][4]["Description"]
                    curveOutHigh = msg["heatpump"][31]["Value"]
                    curveOutLow = msg["heatpump"][32]["Value"]
                    curveInHigh = msg["heatpump"][29]["Value"]
                    curveInLow = msg["heatpump"][30]["Value"]
                    defrost = msg["heatpump"][26]["Description"]
                    new = msg["heatpump"][18]["Value"]
                    if new != quiet:
                        quiet = new
                        self.measurements_signals.emit(int(hzPower), int(wOutTemp), status, allData, TankTemp,
                                                       inletTemp,
                                                       float(wflow), valve3w, quiet, mode, int(curveOutHigh),
                                                       int(curveOutLow), int(curveInHigh), int(curveInLow), defrost,
                                                       TatgetTemp)

                else:
                    print("Not Working")

            except requests.exceptions.InvalidURL or requests.exceptions.ConnectionError as err:
                print(err)

            try:
                q = self.queue.get(timeout = 6)
                if q == -1:
                    break
                cmd, value = q
                requests.request('GET', f'{url}command?{cmd}={value}')

            except Empty:
                pass

    def stop(self):
        print("stop")
        self.keepRunning = False
        self.queue.put(-1)
        self.wait()

    def setQuiet(self, state):
        self.queue.put(('SetQuietMode', int(state)))


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
        startSize = QSize(1200, 800)
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

        # ==> TOGGLE BUTTON 2

        self.togglep = PyToggle()
        self.ui.gridLayout_button_2.addWidget(self.togglep)


        # ==> IP TEXT FIELD VALIDATOR WITH INPUT MASK

        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regular expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)
        self.ui.lineEdit_description.setValidator(ipValidator)

        # ==> ADVANCED MENU FIRST PYTHOGRAPH VIEW

        self.graphWidget = self.ui.graphicsView
        self.graphWidget.setBackground((27, 29, 35))
        self.graphWidget.setTitle("<span style=\"color:white;font-size:10pt\">Heating Curve</span>")
        self.graphWidget.setLabel('left', "<span style=\"color:white;font-size:12px\">Water Temperature (°C)</span>")
        self.graphWidget.setLabel('bottom',
                                  "<span style=\"color:white;font-size:12px\">Outside Temperature (°C)</span>")

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
        # Connect the signal from the thread to the slot_method
        self.wt.measurements_signals.connect(self.slot_method)
        app.aboutToQuit.connect(self.wt.stop)  # to stop the thread when closing the GUI
        self.toggle.toggled.connect(self.wt.setQuiet)
        # it's usually better to start the thread *after* connecting signals
        self.wt.start()

    def slot_method(self, hz, wouttemp, stat, allData, tanktemp, inltemp, wflow, valve3, quiet, mode, curveOutHigh,
                    curveOutLow, curveInHigh, curveInLow, defrost, TatgetTemp):

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
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90, stop:{STOP_1} rgba(85, 255, 127, 255), stop:{STOP_2} rgba(255, 255, 255, 0));
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

        # TARGET TEMP LABEL
        newHtmlTarget = htmlTextLabels.replace("{VALUE}", TatgetTemp)
        self.ui.label_target_tempV.setText(newHtmlTarget)

        # WATER FLOW LABEL
        htmlTextLabelsFlow = """<p align="center"><span style=" font-size:25pt;">{VALUE}</span><span style=" font-size:15pt; vertical-align:super;">l/min</span></p>"""
        newHtmlWaterFlow = htmlTextLabelsFlow.replace("{VALUE}", str(wflow))
        self.ui.label_flow_rateV.setText(newHtmlWaterFlow)

        # 3 WAY VALVE LABEL
        htmlTextLabels3way = """<p align="center"><span style=" font-size:25pt;">{VALUE}</span>"""
        newHtml3wayValve = htmlTextLabels3way.replace("{VALUE}", valve3)
        self.ui.label_3way_valveV.setText(newHtml3wayValve)

        # DEFROST MODE LABEL
        newHtmlDefrost = htmlTextLabels3way.replace("{VALUE}", defrost)
        self.ui.label_defrostv.setText(newHtmlDefrost)

        # MODE LABEL
        newHtmlMode = htmlTextLabels3way.replace("{VALUE}", mode)
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
            # temporarily disconnect to avoid calling setQuiet unnecessarily
            self.toggle.toggled.disconnect(self.wt.setQuiet)
            self.toggle.setChecked(True)
            self.toggle.toggled.connect(self.wt.setQuiet)

        # UPDATE PLOT
        self.plotGraph(curveOutHigh, curveOutLow, curveInHigh, curveInLow)

    def postCommand(self):
        if self.toggle.isChecked():
            setting = "SetQuietMode=1"
        else:
            setting = "SetQuietMode=0"

        url = f"http://192.168.8.150/command?{setting}"
        r = requests.request('GET', url)

    def findName(self):
        name = self.ui.lineEdit_search.text().lower()
        for row in range(self.ui.tableWidget_data.rowCount()):
            item = self.ui.tableWidget_data.item(row, 1)
            # if the search text is not in the item's text do not hide the row #
            self.ui.tableWidget_data.setRowHidden(row, name not in item.text().lower())

    def onChanged(self, text):
        global IP
        IP = text

    def addIP(self):
        ip = self.ui.lineEdit_description.text()
        if ip != "":
            msg = QMessageBox()
            msg.setStyleSheet(
                'QMessageBox {background-color: #272c36; font-size: 10pt; color: #ffffff;}\nQPushButton{color: white; font-size: 15px; background-color: #1d1d1d; border-radius: 5px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("+Add API")
            msg.setText("<font color=\"White\">IP was added")
            msg.exec()
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

    def plotGraph(self, temp1, temp2, temp3, temp4):
        tempwater = [temp3, temp4]
        tempoutside = [temp2, temp1]
        self.graphWidget.plot(tempoutside, tempwater)

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
