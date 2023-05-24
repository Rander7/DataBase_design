# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#                                              Database Course Design                                                 #

#                                                   by Group 21                                                       #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import jpype
import os.path
import sys
import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules import *
from widgets import *
from jpype import *


flag = True
fflag = True
first = True
count = 0
ccount = 1


class MainWindow(QMainWindow):
    # buttons click
    def buttonClick(self):
        # get button inf
        btn = self.sender()
        btnName = btn.objectName()

        # judge button
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_order":
            widgets.stackedWidget.setCurrentWidget(widgets.order)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            global first
            if first:
                first = False
                call.show_all_order()
                ordernum = call.g_order_len
                for i in range(0, ordernum):
                    global count
                    global flag
                    if flag:
                        labels = [QLabel(str(i)) for i in range(ordernum * 4)]
                        flag = False
                    time1 = call.g_order_time1[i]
                    time2 = call.g_order_time2[i]
                    time3 = call.g_order_time3[i]
                    labels[i] = QLabel(widgets.scrollAreaWidgetContents_4)
                    labels[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    labels[i].setMinimumHeight(40)
                    count += 1
                    widgets.gridLayout_2.addWidget(labels[i], count, 1, 1, 1, Qt.AlignCenter)
                    labels[i].setText(str(call.g_order_id[i]))
                    i += 1
                    labels[i] = QLabel(widgets.scrollAreaWidgetContents_4)
                    labels[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    labels[i].setMinimumHeight(40)
                    widgets.gridLayout_2.addWidget(labels[i], count, 2, 1, 1, Qt.AlignCenter)
                    labels[i].setText(str(time1)[:19])
                    i += 1
                    labels[i] = QLabel(widgets.scrollAreaWidgetContents_4)
                    labels[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    labels[i].setMinimumHeight(40)
                    widgets.gridLayout_2.addWidget(labels[i], count, 3, 1, 1, Qt.AlignCenter)
                    labels[i].setText(str(time2)[:19])
                    i += 1
                    labels[i] = QLabel(widgets.scrollAreaWidgetContents_4)
                    labels[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    labels[i].setMinimumHeight(40)
                    widgets.gridLayout_2.addWidget(labels[i], count, 4, 1, 1, Qt.AlignCenter)
                    labels[i].setText(str(time3)[:19])

        if btnName == "btn_logon":
            widgets.stackedWidget.setCurrentWidget(widgets.logonpage)

        if btnName == "btn_logout":
            widgets.stackedWidget.setCurrentWidget(widgets.logonpage)
            widgets.btn_home.setStyleSheet(UIFunctions.deselectMenu(widgets.btn_home.styleSheet()))
            widgets.btn_order.setStyleSheet(UIFunctions.deselectMenu(widgets.btn_home.styleSheet()))
            widgets.btn_home.setEnabled(False)
            widgets.btn_order.setEnabled(False)
            widgets.btn_logon.setEnabled(True)

        if btnName == "surebtn":
            workerid = int(widgets.lineid.text())
            password = widgets.linePassword.text()

            iid = call.select_worker_id_exists(workerid)

            if not iid:
                widgets.linePassword.setText("")
                widgets.lineid.setText("")

                widgets.lineid.setStyleSheet("border: 2px solid rgb(255, 0, 0);")
                widgets.linePassword.setStyleSheet("QLineEdit:hover {\n"
                                                   "	border: 2px solid rgb(64, 71, 88);\n"
                                                   "}\n"
                                                   "QLineEdit:focus {\n"
                                                   "	border: 2px solid rgb(91, 101, 124);\n"
                                                   "}\n")

            if iid:
                ppassword = call.select_worker_psw_id_true(workerid, password)

                if not ppassword:
                    widgets.linePassword.setText("")
                    widgets.lineid.setStyleSheet("QLineEdit:hover {\n"
                                                 "	border: 2px solid rgb(64, 71, 88);\n"
                                                 "}\n"
                                                 "QLineEdit:focus {\n"
                                                 "	border: 2px solid rgb(91, 101, 124);\n"
                                                 "}\n")
                    widgets.linePassword.setStyleSheet("border: 2px solid rgb(255, 0, 0);")

                if ppassword:
                    call.u_worker(workerid)

                    widgets.lineid.setText("")
                    widgets.linePassword.setText("")
                    widgets.linePassword.setStyleSheet("QLineEdit:hover {\n"
                                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                                       "}\n"
                                                       "QLineEdit:focus {\n"
                                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                                       "}\n")
                    UIFunctions.toggleRightBox(self, True)
                    widgets.stackedWidget.setCurrentWidget(widgets.home)
                    widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
                    widgets.btn_logon.setEnabled(False)
                    widgets.btn_home.setEnabled(True)
                    widgets.btn_order.setEnabled(True)
                    call.show_all_xiadan()
                    xiadannum = call.g_xiadan_len
                    for i in range(0, xiadannum - 1):
                        global ccount
                        global fflag
                        if fflag:
                            label = [QLabel(str(i)) for i in range(xiadannum * 5)]
                            fflag = False

                        id = call.g_xiadan_id[i]
                        name = call.g_xiadan_name[i]
                        city = call.g_xiadan_city[i]
                        ads = call.g_xiadan_ads[i]
                        address = str(city) + str(ads)
                        otime = call.g_xiadan_xtime[i]
                        tel = call.g_xiadan_tel[i]

                        label[i] = QLabel(widgets.scrollAreaWidgetContents_2)
                        label[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                        label[i].setMinimumHeight(40)
                        ccount += 1
                        widgets.gridLayout_3.addWidget(label[i], ccount, 1, 1, 1, Qt.AlignCenter)
                        label[i].setText(str(id))
                        i += 1
                        label[i] = QLabel(widgets.scrollAreaWidgetContents_2)
                        label[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                        label[i].setMinimumHeight(40)
                        widgets.gridLayout_3.addWidget(label[i], ccount, 2, 1, 1, Qt.AlignCenter)
                        label[i].setText(str(name))
                        i += 1
                        label[i] = QLabel(widgets.scrollAreaWidgetContents_2)
                        label[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                        label[i].setMinimumHeight(40)
                        widgets.gridLayout_3.addWidget(label[i], ccount, 3, 1, 1, Qt.AlignCenter)
                        label[i].setText(address)
                        i += 1
                        label[i] = QLabel(widgets.scrollAreaWidgetContents_2)
                        label[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                        label[i].setMinimumHeight(40)
                        widgets.gridLayout_3.addWidget(label[i], ccount, 4, 1, 1, Qt.AlignCenter)
                        label[i].setText(str(otime)[:19])
                        i += 1
                        label[i] = QLabel(widgets.scrollAreaWidgetContents_2)
                        label[i].setStyleSheet(u"font: 12pt \"Times New Roman\";")
                        label[i].setMinimumHeight(40)
                        widgets.gridLayout_3.addWidget(label[i], ccount, 5, 1, 1, Qt.AlignCenter)
                        label[i].setText(str(tel))

        if btnName == "btn_allpass":
            xiadannum = call.g_xiadan_len
            for i in range(0, xiadannum - 1):
                id = call.g_xiadan_id[i]
                call.add_xiadan_worker_tg(id)
            first = True
            flag = True
            count = 0

    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # menu
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # set ui
        UIFunctions.uiDefinitions(self)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        # buttons click
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_order.clicked.connect(self.buttonClick)
        widgets.btn_logon.clicked.connect(self.buttonClick)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.surebtn.clicked.connect(self.buttonClick)
        widgets.btn_allpass.clicked.connect(self.buttonClick)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        # set welcome page
        widgets.stackedWidget.setCurrentWidget(widgets.welcome)

        widgets.btn_home.setEnabled(False)
        widgets.btn_order.setEnabled(False)


if __name__ == "__main__":
    # find current folder path
    jpath = os.path.abspath('.')
    print(jpath)


    # start Java virtual machine
    jpype.startJVM(r"C:\Program Files\Java\jdk-20\bin\server\jvm.dll", "-ea",
                   "-Djava.class.path=%s;%s" % (jpath + '/jbdc.jar', jpath + '/jdbc.jar'))

    # import Java api
    call = jpype.JClass("api")

    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())

    # shut down Java virtual machine
    jpype.shutdownJVM()



