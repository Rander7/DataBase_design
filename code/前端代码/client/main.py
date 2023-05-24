# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#                                               Database Course Design                                                #

#                                                    by Group 21                                                      #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import jpype
import os.path
import sys
import os
import platform

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules import *
from widgets import *
from jpype import *
import PySide6

flag = True
first = True
cnt = 0
count = 0
f1 = True
f2 = True
f3 = True
f4 = True
f5 = True
f6 = True
f7 = True
f8 = True
f9 = True
f10 = True
f11 = True
f12= True
f13 = True
f14 = True
f15 = True
f16= True
f17 = True
f18= True
f19= True
f20= True
f21= True
f22= True
f23= True
f24= True
f25= True
f26= True
f27= True
f28= True
f29= True
f30= True
f31= True
f32= True
f33= True
f34= True
f35= True
f36= True
f37= True
f38= True
f39= True
f40= True
f41= True
f42= True
f43= True
f44= True
f45= True
f46= True
f47= True
f48= True
f49= True
f50= True
f51= True
f52= True
f53= True
f54= True
f55= True
f56= True
f57= True
f58= True
f59= True
f60= True
f61= True
f62= True
f63= True
f64= True
f65= True
f66= True
f67= True
f68= True
f69= True
f70= True
f71= True

class MainWindow(QMainWindow):
    # buttons click
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_category":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_cart":
            widgets.stackedWidget.setCurrentWidget(widgets.cart)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_order":
            widgets.stackedWidget.setCurrentWidget(widgets.order)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            global first
            if first:
                first = False
                call.show_order_tg()
                ordernum = call.g_order_len
                for i in range(0,ordernum):
                    global count
                    global flag
                    if flag:
                        labels = [QLabel(str(i)) for i in range(ordernum * 3)]
                        flag = False
                    time1 = call.g_order_time1[i]
                    time2 = call.g_order_time2[i]
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

        if btnName == "btn_login":
            widgets.stackedWidget.setCurrentWidget(widgets.loginpage)

        if btnName == "btn_logon":
            widgets.stackedWidget.setCurrentWidget(widgets.logonpage)

        if btnName == "btn_logout":
            widgets.stackedWidget.setCurrentWidget(widgets.logonpage)
            widgets.btn_category.setStyleSheet(UIFunctions.deselectMenu(widgets.btn_category.styleSheet()))
            widgets.btn_cart.setStyleSheet(UIFunctions.deselectMenu(widgets.btn_category.styleSheet()))
            widgets.btn_order.setStyleSheet(UIFunctions.deselectMenu(widgets.btn_category.styleSheet()))
            widgets.btn_category.setEnabled(False)
            widgets.btn_cart.setEnabled(False)
            widgets.btn_order.setEnabled(False)
            widgets.btn_login.setEnabled(True)
            widgets.btn_logon.setEnabled(True)
            widgets.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"user_name", None))
            widgets.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"user_ID", None))

        def tel_right(s):
            left_parenthesis_index = -1
            cz_count = 0
            for i in range(len(s)):
                if s[i] == '(':
                    left_parenthesis_index = i
                elif s[i] == ')' and left_parenthesis_index != -1 and s[i + 1] == ' ':
                    cz_count = i - left_parenthesis_index - 1
                    break
            return 3 <= cz_count <= 4 if cz_count else False

        if btnName == "Surebtn":
            # get information
            name = widgets.linename.text()
            position = widgets.lineposition.text()
            company = widgets.linecompany.text()
            address = widgets.lineaddress.text()
            city = widgets.linecity.text()
            region = widgets.lineregion.text()
            postal = widgets.linepostalcode.text()
            country = widgets.linecountry.text()
            phone = widgets.linephone.text()
            fax = widgets.linefax.text()
            password = widgets.linepassword.text()
            ensure = widgets.lineensure.text()

            ppphone = call.select_worker_tel_exists(phone)
            print(phone)
            print(ppphone)
            if ppphone:
                widgets.linename.setText("")
                widgets.lineposition.setText("")
                widgets.linecompany.setText("")
                widgets.lineaddress.setText("")
                widgets.linecity.setText("")
                widgets.lineregion.setText("")
                widgets.linepostalcode.setText("")
                widgets.linecountry.setText("")
                widgets.linefax.setText("")
                widgets.linepassword.setText("")
                widgets.lineensure.setText("")
                widgets.linephone.setText("log in forbidden")
                widgets.linephone.setStyleSheet("border: 2px solid rgb(255, 0, 0);")
                widgets.linepassword.setStyleSheet("QLineEdit:hover {\n"
                                                   "	border: 2px solid rgb(64, 71, 88);\n"
                                                   "}\n"
                                                   "QLineEdit:focus {\n"
                                                   "	border: 2px solid rgb(91, 101, 124);\n"
                                                   "}\n")
            if not ppphone:

                first = False
                second = False
                if not tel_right(phone):
                    widgets.linephone.setText("")
                    widgets.linephone.setStyleSheet("border: 2px solid rgb(255, 0, 0);")

                else:
                    first = True
                    widgets.linephone.setStyleSheet("QLineEdit:hover {\n"
                                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                                       "}\n"
                                                       "QLineEdit:focus {\n"
                                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                                       "}\n")

                if not tel_right(fax):
                    widgets.linefax.setText("")
                    widgets.linefax.setStyleSheet("border: 2px solid rgb(255, 0, 0);")

                else:
                    second = True
                    widgets.linefax.setStyleSheet("QLineEdit:hover {\n"
                                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                                    "}\n"
                                                    "QLineEdit:focus {\n"
                                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                                    "}\n")

                if password != ensure:
                    widgets.linepassword.setText("")
                    widgets.lineensure.setText("")
                    widgets.linepassword.setStyleSheet("border: 2px solid rgb(255, 0, 0);")
                    widgets.lineensure.setStyleSheet("border: 2px solid rgb(255, 0, 0);")

                if password == ensure and first and second:
                    ID = str(call.add_user(company, name, position, address, city, region, postal, country, phone, fax,
                                           password))

                    widgets.linepassword.setStyleSheet("QLineEdit:hover {\n"
                                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                                       "}\n"
                                                       "QLineEdit:focus {\n"
                                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                                       "}\n")
                    widgets.lineensure.setStyleSheet("QLineEdit:hover {\n"
                                                     "	border: 2px solid rgb(64, 71, 88);\n"
                                                     "}\n"
                                                     "QLineEdit:focus {\n"
                                                     "	border: 2px solid rgb(91, 101, 124);\n"
                                                     "}\n")
                    widgets.linename.setText("")
                    widgets.lineposition.setText("")
                    widgets.linecompany.setText("")
                    widgets.lineaddress.setText("")
                    widgets.linecity.setText("")
                    widgets.lineregion.setText("")
                    widgets.linepostalcode.setText("")
                    widgets.linecountry.setText("")
                    widgets.linephone.setText("")
                    widgets.linefax.setText("")
                    widgets.linepassword.setText("")
                    widgets.lineensure.setText("")
                    UIFunctions.toggleRightBox(self, True)
                    widgets.stackedWidget.setCurrentWidget(widgets.home)
                    widgets.btn_category.setStyleSheet(UIFunctions.selectMenu(widgets.btn_category.styleSheet()))
                    widgets.btn_login.setEnabled(False)
                    widgets.btn_logon.setEnabled(False)
                    widgets.btn_category.setEnabled(True)
                    widgets.btn_cart.setEnabled(True)
                    widgets.btn_order.setEnabled(True)
                    widgets.titleLeftApp.setText(QCoreApplication.translate("MainWindow", name, None))
                    widgets.titleLeftDescription.setText(ID)
                    call.u_xiadan(ID)

        if btnName == "surebtn":
            phone = widgets.linePhone.text()
            password = widgets.linePassword.text()

            pphone = call.select_user_tel_exists(phone)
            ppphone = call.select_worker_tel_exists(phone)

            if ppphone:
                widgets.linePassword.setText("")
                widgets.linePhone.setText("log on forbidden")
                widgets.linePhone.setStyleSheet("border: 2px solid rgb(255, 0, 0);")
                widgets.linePassword.setStyleSheet("QLineEdit:hover {\n"
                                                   "	border: 2px solid rgb(64, 71, 88);\n"
                                                   "}\n"
                                                   "QLineEdit:focus {\n"
                                                   "	border: 2px solid rgb(91, 101, 124);\n"
                                                   "}\n")

            if not ppphone:

                if not pphone:
                    widgets.linePassword.setText("")
                    widgets.linePhone.setText("")

                    widgets.linePhone.setStyleSheet("border: 2px solid rgb(255, 0, 0);")
                    widgets.linePassword.setStyleSheet("QLineEdit:hover {\n"
                                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                                       "}\n"
                                                       "QLineEdit:focus {\n"
                                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                                       "}\n")

                if pphone:
                    ppassword = call.select_user_psw_true(phone, password)

                    if not ppassword:
                        widgets.linePassword.setText("")
                        widgets.linePhone.setStyleSheet("QLineEdit:hover {\n"
                                                        "	border: 2px solid rgb(64, 71, 88);\n"
                                                        "}\n"
                                                        "QLineEdit:focus {\n"
                                                        "	border: 2px solid rgb(91, 101, 124);\n"
                                                        "}\n")
                        widgets.linePassword.setStyleSheet("border: 2px solid rgb(255, 0, 0);")

                    if ppassword:
                        widgets.linePhone.setText("")
                        widgets.linePassword.setText("")
                        widgets.linePassword.setStyleSheet("QLineEdit:hover {\n"
                                                           "	border: 2px solid rgb(64, 71, 88);\n"
                                                           "}\n"
                                                           "QLineEdit:focus {\n"
                                                           "	border: 2px solid rgb(91, 101, 124);\n"
                                                           "}\n")
                        UIFunctions.toggleRightBox(self, True)
                        widgets.stackedWidget.setCurrentWidget(widgets.home)
                        widgets.btn_category.setStyleSheet(UIFunctions.selectMenu(widgets.btn_category.styleSheet()))
                        widgets.btn_login.setEnabled(False)
                        widgets.btn_logon.setEnabled(False)
                        widgets.btn_category.setEnabled(True)
                        widgets.btn_cart.setEnabled(True)
                        widgets.btn_order.setEnabled(True)

                        call.select_user_from_tel(phone)
                        ID = str(call.g_user_id[0])
                        name = str(call.g_user_name[0])
                        widgets.titleLeftApp.setText(QCoreApplication.translate("MainWindow", name, None))
                        widgets.titleLeftDescription.setText(ID)
                        call.u_xiadan(ID)
                        call.show_all_order()
                        rq1 = call.g_order_rq1[0]
                        rq2 = call.g_order_rq1[1]
                        rq3 = call.g_order_rq1[2]
                        # 任务14
                        if rq1 and rq2 and rq3:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单发货日期、到货日期、确认日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                        elif rq1 and rq2:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单发货日期、到货日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                        elif rq1 and rq3:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单到货日期、确认日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                        elif rq2 and rq3:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单发货日期、确认日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                        elif rq1:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单发货日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                        elif rq2:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单到货日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                        elif rq3:
                            msgBox = QMessageBox()
                            msgBox.setText("您的订单确认日期有误，已帮您自动改正！")
                            msgBox.setWindowTitle("错误信息提示")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()

        if btnName == "btn_yinliao":
            widgets.stackedWidget.setCurrentWidget(widgets.yinliao)

        if btnName == "btn_dianxin":
            widgets.stackedWidget.setCurrentWidget(widgets.dianxin)

        if btnName == "btn_roujiaqin":
            widgets.stackedWidget.setCurrentWidget(widgets.roujiaqin)

        if btnName == "btn_guleimaipian":
            widgets.stackedWidget.setCurrentWidget(widgets.guleimaipian)

        if btnName == "btn_haixian":
            widgets.stackedWidget.setCurrentWidget(widgets.haixian)

        if btnName == "btn_riyongpin":
            widgets.stackedWidget.setCurrentWidget(widgets.riyongpin)

        if btnName == "btn_tiaoweipin":
            widgets.stackedWidget.setCurrentWidget(widgets.tiaoweipin)

        if btnName == "btn_tezhipin":
            widgets.stackedWidget.setCurrentWidget(widgets.tezhipin)

        if btnName == "btn_yl":
            pgz = widgets.spinpgz.value()
            widgets.spinpgz.setValue(0)
            widgets.spinpgz.setMaximum(widgets.spinpgz.maximum() - pgz)
            sc = widgets.spinsc.value()
            widgets.spinsc.setValue(0)
            widgets.spinsc.setMaximum(widgets.spinsc.maximum() - sc)
            qs = widgets.spinqs.value()
            widgets.spinqs.setValue(0)
            widgets.spinqs.setMaximum(widgets.spinqs.maximum() - qs)
            pj = widgets.spinpj.value()
            widgets.spinpj.setValue(0)
            widgets.spinpj.setMaximum(widgets.spinpj.maximum() - pj)
            mtz = widgets.spinmtz.value()
            widgets.spinmtz.setValue(0)
            widgets.spinmtz.setMaximum(widgets.spinmtz.maximum() - mtz)
            lc = widgets.spinlc.value()
            widgets.spinlc.setValue(0)
            widgets.spinlc.setMaximum(widgets.spinlc.maximum() - lc)
            ydyl = widgets.spinydyl.value()
            widgets.spinydyl.setValue(0)
            widgets.spinydyl.setMaximum(widgets.spinydyl.maximum() - ydyl)
            lcz = widgets.spinlcz.value()
            widgets.spinlcz.setValue(0)
            widgets.spinlcz.setMaximum(widgets.spinlcz.maximum() - lcz)
            nn = widgets.spinnn.value()
            widgets.spinnn.setValue(0)
            widgets.spinnn.setMaximum(widgets.spinnn.maximum() - nn)

            if pgz > 0:
                call.add_product_user(1,pgz)
                global cnt
                global f1
                if f1:
                    widgets.label_500 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_500.setObjectName(u"label_500")
                    widgets.label_500.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_500.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_500, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_500.setText("苹果汁")
                    widgets.label_501 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_501.setObjectName(u"label_501")
                    widgets.label_501.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_501, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_501.setText(str(pgz))
                    f1 = False
                else:
                    pgz = pgz + int(widgets.label_501.text())
                    widgets.label_501.setText(str(pgz))

            if sc > 0:
                call.add_product_user(14,sc)
                global f2
                if f2:
                    widgets.label_502 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_502.setObjectName(u"label_502")
                    widgets.label_502.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_502.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_502, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_502.setText("沙茶")
                    widgets.label_503 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_503.setObjectName(u"label_503")
                    widgets.label_503.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_503, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_503.setText(str(sc))
                    f2 = False
                else:
                    sc = sc + int(widgets.label_503.text())
                    widgets.label_503.setText(str(sc))
                
            if qs > 0:
                call.add_product_user(24,qs)
                global f3
                if f3:
                    widgets.label_504 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_504.setObjectName(u"label_504")
                    widgets.label_504.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_504.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_504, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_504.setText("汽水")
                    widgets.label_505 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_505.setObjectName(u"label_505")
                    widgets.label_505.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_505, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_505.setText(str(qs))
                    f3 = False
                else:
                    qs = qs + int(widgets.label_505.text())
                    widgets.label_505.setText(str(qs))
                
            if pj > 0:
                call.add_product_user(34,pj)
                global f4
                if f4:
                    widgets.label_506 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_506.setObjectName(u"label_506")
                    widgets.label_506.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_506.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_506, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_506.setText("啤酒")
                    widgets.label_507 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_507.setObjectName(u"label_507")
                    widgets.label_507.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_507, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_507.setText(str(pj))
                    f4 = False
                else:
                    pj = pj + int(widgets.label_507.text())
                    widgets.label_507.setText(str(pj))
                
            if mtz > 0:
                call.add_product_user(35,mtz)
                global f5
                if f5:
                    widgets.label_508 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_508.setObjectName(u"label_508")
                    widgets.label_508.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_508.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_508, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_508.setText("蜜桃汁")
                    widgets.label_509 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_509.setObjectName(u"label_509")
                    widgets.label_509.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_509, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_509.setText(str(mtz))
                    f5 = False
                else:
                    mtz = mtz + int(widgets.label_509.text())
                    widgets.label_509.setText(str(mtz))
                
            if lc > 0:
                call.add_product_user(38,lc)
                global f6
                if f6:
                    widgets.label_510 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_510.setObjectName(u"label_510")
                    widgets.label_510.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_510.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_510, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_510.setText("绿茶")
                    widgets.label_511 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_511.setObjectName(u"label_511")
                    widgets.label_511.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_511, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_511.setText(str(lc))
                    f6 = False
                else:
                    lc = lc + int(widgets.label_511.text())
                    widgets.label_511.setText(str(lc))
                
            if ydyl > 0:
                call.add_product_user(39,ydyl)
                global f7
                if f7:
                    widgets.label_512 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_512.setObjectName(u"label_512")
                    widgets.label_512.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_512.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_512, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_512.setText("运动饮料")
                    widgets.label_513 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_513.setObjectName(u"label_513")
                    widgets.label_513.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_513, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_513.setText(str(ydyl))
                    f7 = False
                else:
                    ydyl = ydyl + int(widgets.label_513.text())
                    widgets.label_513.setText(str(ydyl))

            if lcz > 0:
                call.add_product_user(43, lcz)
                global f8
                if f8:
                    widgets.label_514 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_514.setObjectName(u"label_514")
                    widgets.label_514.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_514.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_514, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_514.setText("柳橙汁")
                    widgets.label_515 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_515.setObjectName(u"label_515")
                    widgets.label_515.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_515, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_515.setText(str(lcz))
                    f8 = False
                else:
                    lcz = lcz + int(widgets.label_515.text())
                    widgets.label_515.setText(str(lcz))
                    
            if nn > 0:
                call.add_product_user(2, nn)
                global f9
                if f9:
                    widgets.label_516 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_516.setObjectName(u"label_516")
                    widgets.label_516.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_516.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_516, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_516.setText("牛奶")
                    widgets.label_517 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_517.setObjectName(u"label_517")
                    widgets.label_517.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_517, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_517.setText(str(nn))
                    f9 = False
                else:
                    nn = nn + int(widgets.label_517.text())
                    widgets.label_517.setText(str(nn))

        if btnName == "btn_dx":
            bg = widgets.spinbg.value()
            widgets.spinbg.setValue(0)
            widgets.spinbg.setMaximum(widgets.spinbg.maximum() - bg)
            tg = widgets.spintg.value()
            widgets.spintg.setValue(0)
            widgets.spintg.setMaximum(widgets.spintg.maximum() - tg)
            ghg = widgets.spinghg.value()
            widgets.spinghg.setValue(0)
            widgets.spinghg.setMaximum(widgets.spinghg.maximum() - ghg)
            qkl = widgets.spinqkl.value()
            widgets.spinqkl.setValue(0)
            widgets.spinqkl.setMaximum(widgets.spinqkl.maximum() - qkl)
            mht = widgets.spinmht.value()
            widgets.spinmht.setValue(0)
            widgets.spinmht.setMaximum(widgets.spinmht.maximum() - mht)
            dg = widgets.spindg.value()
            widgets.spindg.setValue(0)
            widgets.spindg.setMaximum(widgets.spindg.maximum() - dg)
            st = widgets.spinydyl.value()
            widgets.spinydyl.setValue(0)
            widgets.spinydyl.setMaximum(widgets.spinydyl.maximum() - ydyl)
            szp = widgets.spinszp.value()
            widgets.spinszp.setValue(0)
            widgets.spinszp.setMaximum(widgets.spinszp.maximum() - szp)

            if bg > 0:
                call.add_product_user(16, bg)
                global f10
                if f10:
                    widgets.label_518 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_518.setObjectName(u"label_518")
                    widgets.label_518.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_518.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_518, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_518.setText("饼干")
                    widgets.label_519 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_519.setObjectName(u"label_519")
                    widgets.label_519.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_519, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_519.setText(str(bg))
                    f10 = False
                else:
                    bg = bg + int(widgets.label_519.text())
                    widgets.label_519.setText(str(bg))
            if tg > 0:
                call.add_product_user(19, tg)
                global f11
                if f11:
                    widgets.label_520 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_520.setObjectName(u"label_520")
                    widgets.label_520.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_520.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_520, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_520.setText("糖果")
                    widgets.label_521 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_521.setObjectName(u"label_521")
                    widgets.label_521.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_521, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_521.setText(str(tg))
                    f11 = False
                else:
                    tg = tg + int(widgets.label_521.text())
                    widgets.label_521.setText(str(tg))
            if ghg > 0:
                call.add_product_user(20, ghg)
                global f12
                if f12:
                    widgets.label_522 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_522.setObjectName(u"label_522")
                    widgets.label_522.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_522.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_522, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_522.setText("桂花糕")
                    widgets.label_523 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_523.setObjectName(u"label_523")
                    widgets.label_523.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_523, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_523.setText(str(ghg))
                    f12 = False
                else:
                    ghg = ghg + int(widgets.label_523.text())
                    widgets.label_523.setText(str(ghg))
            if qkl > 0:
                call.add_product_user(25, qkl)
                global f13
                if f13:
                    widgets.label_524 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_524.setObjectName(u"label_524")
                    widgets.label_524.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_524.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_524, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_524.setText("巧克力")
                    widgets.label_525 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_525.setObjectName(u"label_525")
                    widgets.label_525.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_525, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_525.setText(str(qkl))
                    f13 = False
                else:
                    qkl = qkl + int(widgets.label_525.text())
                    widgets.label_525.setText(str(qkl))
            if mht > 0:
                call.add_product_user(26, mht)
                global f14
                if f14:
                    widgets.label_526 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_526.setObjectName(u"label_526")
                    widgets.label_526.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_526.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_526, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_526.setText("棉花糖")
                    widgets.label_527 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_527.setObjectName(u"label_527")
                    widgets.label_527.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_527, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_527.setText(str(mht))
                    f14 = False
                else:
                    mht = mht + int(widgets.label_527.text())
                    widgets.label_527.setText(str(mht))
            if dg > 0:
                call.add_product_user(47, dg)
                global f15
                if f15:
                    widgets.label_528 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_528.setObjectName(u"label_528")
                    widgets.label_528.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_528.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_528, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_528.setText("蛋糕")
                    widgets.label_529 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_529.setObjectName(u"label_529")
                    widgets.label_529.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_529, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_529.setText(str(dg))
                    f15 = False
                else:
                    dg = dg + int(widgets.label_529.text())
                    widgets.label_529.setText(str(dg))
            if st > 0:
                call.add_product_user(49, st)
                global f16
                if f16:
                    widgets.label_530 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_530.setObjectName(u"label_530")
                    widgets.label_530.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_530.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_530, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_530.setText("薯条")
                    widgets.label_531 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_531.setObjectName(u"label_531")
                    widgets.label_531.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_531, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_531.setText(str(st))
                    f16 = False
                else:
                    st = st + int(widgets.label_531.text())
                    widgets.label_531.setText(str(st))
            if szp > 0:
                call.add_product_user(62, szp)
                global f17
                if f17:
                    widgets.label_532 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_532.setObjectName(u"label_532")
                    widgets.label_532.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_532.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_532, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_532.setText("山楂片")
                    widgets.label_533 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_533.setObjectName(u"label_533")
                    widgets.label_533.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_533, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_533.setText(str(szp))
                    f17 = False
                else:
                    szp = szp + int(widgets.label_533.text())
                    widgets.label_533.setText(str(szp))

        if btnName == "btn_rjq":
            j = widgets.spinj.value()
            widgets.spinj.setValue(0)
            widgets.spinj.setMaximum(widgets.spinj.maximum() - j)
            zr = widgets.spinzr.value()
            widgets.spinzr.setValue(0)
            widgets.spinzr.setMaximum(widgets.spinzr.maximum() - zr)
            nrg = widgets.spinnrg.value()
            widgets.spinnrg.setValue(0)
            widgets.spinnrg.setMaximum(widgets.spinnrg.maximum() - nrg)
            yr29 = widgets.spinyr29.value()
            widgets.spinyr29.setValue(0)
            widgets.spinyr29.setMaximum(widgets.spinyr29.maximum() - yr29)
            zrg = widgets.spinzrg.value()
            widgets.spinzrg.setValue(0)
            widgets.spinzrg.setMaximum(widgets.spinzrg.maximum() - zrg)
            ysy = widgets.spinysy.value()
            widgets.spinysy.setValue(0)
            widgets.spinysy.setMaximum(widgets.spinysy.maximum() - ysy)
            jr = widgets.spinjr.value()
            widgets.spinjr.setValue(0)
            widgets.spinjr.setMaximum(widgets.spinjr.maximum() - jr)
            yr55 = widgets.spinyr55.value()
            widgets.spinyr55.setValue(0)
            widgets.spinyr55.setMaximum(widgets.spinyr55.maximum() - yr55)

            if j > 0:
                call.add_product_user(9, j)
                global f18
                if f18:
                    widgets.label_534 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_534.setObjectName(u"label_534")
                    widgets.label_534.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_534.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_534, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_534.setText("鸡")
                    widgets.label_535 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_535.setObjectName(u"label_535")
                    widgets.label_535.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_535, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_535.setText(str(szp))
                    f18 = False
                else:
                    szp = szp + int(widgets.label_535.text())
                    widgets.label_535.setText(str(szp))
            if zr > 0:
                call.add_product_user(17, zr)
                global f19
                if f19:
                    widgets.label_536 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_536.setObjectName(u"label_536")
                    widgets.label_536.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_536.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_536, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_536.setText("猪肉")
                    widgets.label_537 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_537.setObjectName(u"label_537")
                    widgets.label_537.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_537, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_537.setText(str(zr))
                    f19 = False
                else:
                    zr = zr + int(widgets.label_537.text())
                    widgets.label_537.setText(str(zr))
            if nrg > 0:
                call.add_product_user(27, nrg)
                global f20
                if f20:
                    widgets.label_538 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_538.setObjectName(u"label_538")
                    widgets.label_538.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_538.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_538, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_538.setText("牛肉干")
                    widgets.label_539 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_539.setObjectName(u"label_539")
                    widgets.label_539.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_539, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_539.setText(str(nrg))
                    f20 = False
                else:
                    nrg = nrg + int(widgets.label_539.text())
                    widgets.label_539.setText(str(nrg))
            if yr29 > 0:
                call.add_product_user(29, yr29)
                global f21
                if f21:
                    widgets.label_540 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_540.setObjectName(u"label_540")
                    widgets.label_540.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_540.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_540, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_540.setText("鸭肉")
                    widgets.label_541 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_541.setObjectName(u"label_541")
                    widgets.label_541.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_541, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_541.setText(str(yr29))
                    f21 = False
                else:
                    yr29 = yr29 + int(widgets.label_541.text())
                    widgets.label_541.setText(str(yr29))
            if zrg > 0:
                call.add_product_user(51, zrg)
                global f22
                if f22:
                    widgets.label_542 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_542.setObjectName(u"label_542")
                    widgets.label_542.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_542.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_542, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_542.setText("猪肉干")
                    widgets.label_543 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_543.setObjectName(u"label_543")
                    widgets.label_543.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_543, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_543.setText(str(zrg))
                    f22 = False
                else:
                    zrg = zrg + int(widgets.label_543.text())
                    widgets.label_543.setText(str(zrg))
            if ysy > 0:
                call.add_product_user(53, ysy)
                global f23
                if f23:
                    widgets.label_544 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_544.setObjectName(u"label_544")
                    widgets.label_544.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_544.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_544, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_544.setText("盐水鸭")
                    widgets.label_545 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_545.setObjectName(u"label_545")
                    widgets.label_545.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_545, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_545.setText(str(ysy))
                    f23 = False
                else:
                    ysy = ysy + int(widgets.label_545.text())
                    widgets.label_545.setText(str(ysy))
            if jr > 0:
                call.add_product_user(54, jr)
                global f24
                if f24:
                    widgets.label_546 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_546.setObjectName(u"label_546")
                    widgets.label_546.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_546.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_546, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_546.setText("鸡肉")
                    widgets.label_547 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_547.setObjectName(u"label_547")
                    widgets.label_547.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_547, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_547.setText(str(jr))
                    f24 = False
                else:
                    jr = jr + int(widgets.label_547.text())
                    widgets.label_547.setText(str(jr))
            if yr55 > 0:
                call.add_product_user(55, yr55)
                global f25
                if f25:
                    widgets.label_548 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_548.setObjectName(u"label_548")
                    widgets.label_548.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_548.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_548, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_548.setText("鸭肉")
                    widgets.label_549 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_549.setObjectName(u"label_549")
                    widgets.label_549.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_549, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_549.setText(str(yr55))
                    f25 = False
                else:
                    yr55 = yr55 + int(widgets.label_549.text())
                    widgets.label_549.setText(str(yr55))

        if btnName == "btn_glmp":
            nm = widgets.spinnm.value()
            widgets.spinnm.setValue(0)
            widgets.spinnm.setMaximum(widgets.spinnm.maximum() - nm)
            ym = widgets.spinym.value()
            widgets.spinym.setValue(0)
            widgets.spinym.setMaximum(widgets.spinym.maximum() - ym)
            cm = widgets.spincm.value()
            widgets.spincm.setValue(0)
            widgets.spincm.setMaximum(widgets.spincm.maximum() - cm)
            ymp = widgets.spinymp.value()
            widgets.spinymp.setValue(0)
            widgets.spinymp.setMaximum(widgets.spinymp.maximum() - ymp)
            ymb = widgets.spinymb.value()
            widgets.spinymb.setValue(0)
            widgets.spinymb.setMaximum(widgets.spinymb.maximum() - ymb)
            shymp = widgets.spinshymp.value()
            widgets.spinshymp.setValue(0)
            widgets.spinshymp.setMaximum(widgets.spinshymp.maximum() - shymp)
            bm = widgets.spinbm.value()
            widgets.spinbm.setValue(0)
            widgets.spinbm.setMaximum(widgets.spinbm.maximum() - bm)
            xm = widgets.spinxm.value()
            widgets.spinxm.setValue(0)
            widgets.spinxm.setMaximum(widgets.spinxm.maximum() - xm)
            hd = widgets.spinhd.value()
            widgets.spinhd.setValue(0)
            widgets.spinhd.setMaximum(widgets.spinhd.maximum() - hd)

            if nm > 0:
                call.add_product_user(22, nm)
                global f26
                if f26:
                    widgets.label_550 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_550.setObjectName(u"label_550")
                    widgets.label_550.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_550.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_550, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_550.setText("糯米")
                    widgets.label_551 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_551.setObjectName(u"label_551")
                    widgets.label_551.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_551, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_551.setText(str(nm))
                    f26 = False
                else:
                    nm = nm + int(widgets.label_551.text())
                    widgets.label_551.setText(str(nm))
            if ym > 0:
                call.add_product_user(23, ym)
                global f27
                if f27:
                    widgets.label_552 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_552.setObjectName(u"label_552")
                    widgets.label_552.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_552.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_552, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_552.setText("燕麦")
                    widgets.label_553 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_553.setObjectName(u"label_553")
                    widgets.label_553.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_553, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_553.setText(str(ym))
                    f27 = False
                else:
                    ym = ym + int(widgets.label_553.text())
                    widgets.label_553.setText(str(ym))
            if cm > 0:
                call.add_product_user(42, cm)
                global f28
                if f28:
                    widgets.label_554 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_554.setObjectName(u"label_554")
                    widgets.label_554.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_554.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_554, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_554.setText("糙米")
                    widgets.label_555 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_555.setObjectName(u"label_555")
                    widgets.label_555.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_555, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_555.setText(str(cm))
                    f28 = False
                else:
                    cm = cm + int(widgets.label_555.text())
                    widgets.label_555.setText(str(cm))
            if ymp > 0:
                call.add_product_user(48, ymp)
                global f29
                if f29:
                    widgets.label_556 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_556.setObjectName(u"label_556")
                    widgets.label_556.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_556.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_556, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_556.setText("玉米片")
                    widgets.label_557 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_557.setObjectName(u"label_557")
                    widgets.label_557.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_557, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_557.setText(str(ymp))
                    f29 = False
                else:
                    ymp = ymp + int(widgets.label_557.text())
                    widgets.label_557.setText(str(ymp))
            if ymb > 0:
                call.add_product_user(50, ymb)
                global f30
                if f30:
                    widgets.label_558 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_558.setObjectName(u"label_558")
                    widgets.label_558.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_558.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_558, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_558.setText("玉米饼")
                    widgets.label_559 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_559.setObjectName(u"label_559")
                    widgets.label_559.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_559, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_559.setText(str(ymb))
                    f30 = False
                else:
                    ymb = ymb + int(widgets.label_559.text())
                    widgets.label_559.setText(str(ymb))
            if shymp > 0:
                call.add_product_user(52, shymp)
                global f31
                if f31:
                    widgets.label_560 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_560.setObjectName(u"label_560")
                    widgets.label_560.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_560.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_560, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_560.setText("三合一麦片")
                    widgets.label_561 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_561.setObjectName(u"label_561")
                    widgets.label_561.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_561, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_561.setText(str(shymp))
                    f31 = False
                else:
                    shymp = shymp + int(widgets.label_561.text())
                    widgets.label_561.setText(str(shymp))
            if bm > 0:
                call.add_product_user(56, bm)
                global f32
                if f32:
                    widgets.label_562 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_562.setObjectName(u"label_562")
                    widgets.label_562.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_562.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_562, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_562.setText("白米")
                    widgets.label_563= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_563.setObjectName(u"label_563")
                    widgets.label_563.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_563, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_563.setText(str(bm))
                    f32 = False
                else:
                    bm = bm + int(widgets.label_563.text())
                    widgets.label_563.setText(str(bm))
            if xm > 0:
                call.add_product_user(57, xm)
                global f33
                if f33:
                    widgets.label_564 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_564.setObjectName(u"label_564")
                    widgets.label_564.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_564.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_564, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_564.setText("小米")
                    widgets.label_565= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_565.setObjectName(u"label_565")
                    widgets.label_565.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_565, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_565.setText(str(xm))
                    f33 = False
                else:
                    xm = xm + int(widgets.label_565.text())
                    widgets.label_565.setText(str(xm))
            if hd > 0:
                call.add_product_user(64, hd)
                global f34
                if f34:
                    widgets.label_566 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_566.setObjectName(u"label_566")
                    widgets.label_566.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_566.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_566, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_566.setText("黄豆")
                    widgets.label_567= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_567.setObjectName(u"label_567")
                    widgets.label_567.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_567, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_567.setText(str(hd))
                    f34 = False
                else:
                    hd = hd + int(widgets.label_567.text())
                    widgets.label_567.setText(str(hd))

        if btnName == "btn_hx":
            x = widgets.spinx.value()
            widgets.spinx.setValue(0)
            widgets.spinx.setMaximum(widgets.spinx.maximum() - x)
            lx = widgets.spinlx.value()
            widgets.spinlx.setValue(0)
            widgets.spinlx.setMaximum(widgets.spinlx.maximum() - lx)
            my_2 = widgets.spinmy_2.value()
            widgets.spinmy_2.setValue(0)
            widgets.spinmy_2.setMaximum(widgets.spinmy_2.maximum() - my_2)
            hy_2 = widgets.spinhy_2.value()
            widgets.spinhy_2.setValue(0)
            widgets.spinhy_2.setMaximum(widgets.spinhy_2.maximum() - hy_2)
            yy = widgets.spinyy.value()
            widgets.spinyy.setValue(0)
            widgets.spinyy.setMaximum(widgets.spinyy.maximum() - yy)
            gb = widgets.spingb.value()
            widgets.spingb.setValue(0)
            widgets.spingb.setMaximum(widgets.spingb.maximum() - gb)
            xm_2 = widgets.spinxm_2.value()
            widgets.spinxm_2.setValue(0)
            widgets.spinxm_2.setMaximum(widgets.spinxm_2.maximum() - xm_2)
            xz = widgets.spinxz.value()
            widgets.spinxz.setValue(0)
            widgets.spinxz.setMaximum(widgets.spinxz.maximum() - xz)
            xy = widgets.spinxy.value()
            widgets.spinxy.setValue(0)
            widgets.spinxy.setMaximum(widgets.spinxy.maximum() - xy)
            k = widgets.spink.value()
            widgets.spink.setValue(0)
            widgets.spink.setMaximum(widgets.spink.maximum() - k)
            hs = widgets.spinhs.value()
            widgets.spinhs.setValue(0)
            widgets.spinhs.setMaximum(widgets.spinhs.maximum() - hs)

            if x > 0:
                call.add_product_user(10, x)
                global f35
                if f35:
                    widgets.label_568 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_568.setObjectName(u"label_568")
                    widgets.label_568.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_568.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_568, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_568.setText("蟹")
                    widgets.label_569= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_569.setObjectName(u"label_569")
                    widgets.label_569.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_569, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_569.setText(str(x))
                    f35 = False
                else:
                    x = x + int(widgets.label_569.text())
                    widgets.label_569.setText(str(x))
            if lx > 0:
                call.add_product_user(13, lx)
                global f36
                if f36:
                    widgets.label_570 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_570.setObjectName(u"label_570")
                    widgets.label_570.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_570.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_570, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_570.setText("龙虾")
                    widgets.label_571= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_571.setObjectName(u"label_571")
                    widgets.label_571.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_571, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_571.setText(str(lx))
                    f36 = False
                else:
                    lx = lx + int(widgets.label_571.text())
                    widgets.label_571.setText(str(lx))
            if my_2 > 0:
                call.add_product_user(18, my_2)
                global f71
                if f71:
                    widgets.label_572 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_572.setObjectName(u"label_572")
                    widgets.label_572.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_572.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_572, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_572.setText("墨鱼")
                    widgets.label_573= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_573.setObjectName(u"label_573")
                    widgets.label_573.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_573, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_573.setText(str(my_2))
                    f71 = False
                else:
                    my_2 = my_2 + int(widgets.label_573.text())
                    widgets.label_573.setText(str(my_2))
            if hy_2 > 0:
                call.add_product_user(30, hy_2)
                global f37
                if f37:
                    widgets.label_574 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_574.setObjectName(u"label_574")
                    widgets.label_574.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_574.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_574, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_574.setText("黄鱼")
                    widgets.label_575= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_575.setObjectName(u"label_575")
                    widgets.label_575.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_575, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_575.setText(str(hy_2))
                    f37 = False
                else:
                    hy_2 = hy_2 + int(widgets.label_575.text())
                    widgets.label_575.setText(str(hy_2))
            if yy > 0:
                call.add_product_user(36, yy)
                global f38
                if f38:
                    widgets.label_576 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_576.setObjectName(u"label_576")
                    widgets.label_576.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_576.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_576, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_576.setText("鱿鱼")
                    widgets.label_577= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_577.setObjectName(u"label_577")
                    widgets.label_577.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_577, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_577.setText(str(yy))
                    f38 = False
                else:
                    yy = yy + int(widgets.label_577.text())
                    widgets.label_577.setText(str(yy))
            if gb > 0:
                call.add_product_user(37, gb)
                global f39
                if f39:
                    widgets.label_578 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_578.setObjectName(u"label_578")
                    widgets.label_578.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_578.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_578, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_578.setText("干贝")
                    widgets.label_579= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_579.setObjectName(u"label_579")
                    widgets.label_579.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_579, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_579.setText(str(gb))
                    f39 = False
                else:
                    gb = gb + int(widgets.label_579.text())
                    widgets.label_579.setText(str(gb))
            if xm_2 > 0:
                call.add_product_user(40, xm_2)
                global f40
                if f40:
                    widgets.label_580 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_580.setObjectName(u"label_580")
                    widgets.label_580.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_580.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_580, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_580.setText("虾米")
                    widgets.label_581= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_581.setObjectName(u"label_581")
                    widgets.label_581.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_581, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_581.setText(str(xm_2))
                    f40 = False
                else:
                    xm_2 = xm_2 + int(widgets.label_581.text())
                    widgets.label_581.setText(str(xm_2))
            if xz > 0:
                call.add_product_user(41, xz)
                global f41
                if f41:
                    widgets.label_582 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_582.setObjectName(u"label_582")
                    widgets.label_582.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_582.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_582, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_582.setText("虾子")
                    widgets.label_583= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_583.setObjectName(u"label_583")
                    widgets.label_583.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_583, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_583.setText(str(xz))
                    f41 = False
                else:
                    xz = xz + int(widgets.label_583.text())
                    widgets.label_583.setText(str(xz))
            if xy > 0:
                call.add_product_user(45, xy)
                global f42
                if f42:
                    widgets.label_584 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_584.setObjectName(u"label_584")
                    widgets.label_584.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_584.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_584, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_584.setText("鳕鱼")
                    widgets.label_585= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_585.setObjectName(u"label_585")
                    widgets.label_585.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_585, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_585.setText(str(xy))
                    f42 = False
                else:
                    xy = xy + int(widgets.label_585.text())
                    widgets.label_585.setText(str(xy))
            if k > 0:
                call.add_product_user(46, k)
                global f43
                if f43:
                    widgets.label_586 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_586.setObjectName(u"label_586")
                    widgets.label_586.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_586.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_586, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_586.setText("蚵")
                    widgets.label_587= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_587.setObjectName(u"label_587")
                    widgets.label_587.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_587, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_587.setText(str(k))
                    f43 = False
                else:
                    k = k + int(widgets.label_587.text())
                    widgets.label_587.setText(str(k))
            if hs > 0:
                call.add_product_user(58, hs)
                global f44
                if f44:
                    widgets.label_588 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_588.setObjectName(u"label_588")
                    widgets.label_588.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_588.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_588, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_588.setText("海参")
                    widgets.label_589= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_589.setObjectName(u"label_589")
                    widgets.label_589.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_589, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_589.setText(str(hs))
                    f44 = False
                else:
                    hs = hs + int(widgets.label_589.text())
                    widgets.label_589.setText(str(hs))

        if btnName == "btn_ryp":
            dznl = widgets.spindznl.value()
            widgets.spindznl.setValue(0)
            widgets.spindznl.setMaximum(widgets.spindznl.maximum() - dznl)
            dgnl = widgets.spindgnl.value()
            widgets.spindgnl.setValue(0)
            widgets.spindgnl.setMaximum(widgets.spindgnl.maximum() - dgnl)
            wxnl = widgets.spinwxnl.value()
            widgets.spinwxnl.setValue(0)
            widgets.spinwxnl.setMaximum(widgets.spinwxnl.maximum() - wxnl)
            bnl = widgets.spinbnl.value()
            widgets.spinbnl.setValue(0)
            widgets.spinbnl.setMaximum(widgets.spinbnl.maximum() - bnl)
            lhnl = widgets.spinlhnl.value()
            widgets.spinlhnl.setValue(0)
            widgets.spinlhnl.setMaximum(widgets.spinlhnl.maximum() - lhnl)
            gmnl = widgets.spingmnl.value()
            widgets.spingmnl.setValue(0)
            widgets.spingmnl.setMaximum(widgets.spingmnl.maximum() - gmnl)
            hnl = widgets.spinhnl.value()
            widgets.spinhnl.setValue(0)
            widgets.spinhnl.setMaximum(widgets.spinhnl.maximum() - hnl)

            if dznl > 0:
                call.add_product_user(11, dznl)
                global f45
                if f45:
                    widgets.label_590 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_590.setObjectName(u"label_590")
                    widgets.label_590.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_590.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_590, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_590.setText("大众奶酪")
                    widgets.label_591= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_591.setObjectName(u"label_591")
                    widgets.label_591.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_591, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_591.setText(str(dznl))
                    f45 = False
                else:
                    dznl = dznl + int(widgets.label_591.text())
                    widgets.label_591.setText(str(dznl))
            if dgnl > 0:
                call.add_product_user(12, dgnl)
                global f46
                if f46:
                    widgets.label_592 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_592.setObjectName(u"label_592")
                    widgets.label_592.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_592.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_592, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_592.setText("德国奶酪")
                    widgets.label_593= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_593.setObjectName(u"label_593")
                    widgets.label_593.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_593, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_593.setText(str(dgnl))
                    f46 = False
                else:
                    dgnl = dgnl + int(widgets.label_593.text())
                    widgets.label_593.setText(str(dgnl))
            if wxnl > 0:
                call.add_product_user(31, wxnl)
                global f47
                if f47:
                    widgets.label_594 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_594.setObjectName(u"label_594")
                    widgets.label_594.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_594.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_594, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_594.setText("温馨奶酪")
                    widgets.label_595= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_595.setObjectName(u"label_595")
                    widgets.label_595.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_595, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_595.setText(str(wxnl))
                    f47 = False
                else:
                    wxnl = wxnl + int(widgets.label_595.text())
                    widgets.label_595.setText(str(wxnl))
            if bnl > 0:
                call.add_product_user(32, bnl)
                global f48
                if f48:
                    widgets.label_596 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_596.setObjectName(u"label_596")
                    widgets.label_596.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_596.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_596, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_596.setText("白奶酪")
                    widgets.label_597= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_597.setObjectName(u"label_597")
                    widgets.label_597.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_597, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_597.setText(str(bnl))
                    f48 = False
                else:
                    bnl = bnl + int(widgets.label_597.text())
                    widgets.label_597.setText(str(bnl))
            if lhnl > 0:
                call.add_product_user(33, lhnl)
                global f49
                if f49:
                    widgets.label_598 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_598.setObjectName(u"label_598")
                    widgets.label_598.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_598.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_598, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_598.setText("浪花奶酪")
                    widgets.label_599= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_599.setObjectName(u"label_599")
                    widgets.label_599.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_599, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_599.setText(str(lhnl))
                    f49 = False
                else:
                    lhnl = lhnl + int(widgets.label_599.text())
                    widgets.label_599.setText(str(lhnl))
            if gmnl > 0:
                call.add_product_user(59, gmnl)
                global f50
                if f50:
                    widgets.label_600 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_600.setObjectName(u"label_600")
                    widgets.label_600.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_600.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_600, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_600.setText("光明奶酪")
                    widgets.label_601= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_601.setObjectName(u"label_601")
                    widgets.label_601.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_601, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_601.setText(str(gmnl))
                    f50 = False
                else:
                    gmnl = gmnl + int(widgets.label_601.text())
                    widgets.label_563.setText(str(bm))
            if hnl > 0:
                call.add_product_user(60, hnl)
                global f51
                if f51:
                    widgets.label_602 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_602.setObjectName(u"label_602")
                    widgets.label_602.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_602.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_602, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_602.setText("花奶酪")
                    widgets.label_603= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_603.setObjectName(u"label_603")
                    widgets.label_603.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_603, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_603.setText(str(hnl))
                    f51 = False
                else:
                    hnl = hnl + int(widgets.label_603.text())
                    widgets.label_603.setText(str(hnl))

        if btnName == "btn_twp":
            fqj = widgets.spinfqj.value()
            widgets.spinfqj.setValue(0)
            widgets.spinfqj.setMaximum(widgets.spinfqj.maximum() - fqj)
            y = widgets.spiny.value()
            widgets.spiny.setValue(0)
            widgets.spiny.setMaximum(widgets.spiny.maximum() - y)
            my = widgets.spinmy.value()
            widgets.spinmy.setValue(0)
            widgets.spinmy.setMaximum(widgets.spinmy.maximum() - my)
            jy = widgets.spinjy.value()
            widgets.spinjy.setValue(0)
            widgets.spinjy.setMaximum(widgets.spinjy.maximum() - jy)
            hxf = widgets.spinhxf.value()
            widgets.spinhxf.setValue(0)
            widgets.spinhxf.setMaximum(widgets.spinhxf.maximum() - hxf)
            hjf = widgets.spinhjf.value()
            widgets.spinhjf.setValue(0)
            widgets.spinhjf.setMaximum(widgets.spinhjf.maximum() - hjf)
            wj = widgets.spinwj.value()
            widgets.spinwj.setValue(0)
            widgets.spinwj.setMaximum(widgets.spinwj.maximum() - wj)
            krj = widgets.spinkrj.value()
            widgets.spinkrj.setValue(0)
            widgets.spinkrj.setMaximum(widgets.spinkrj.maximum() - krj)
            hy = widgets.spinhy.value()
            widgets.spinhy.setValue(0)
            widgets.spinhy.setMaximum(widgets.spinhy.maximum() - hy)
            hxj = widgets.spinhxj.value()
            widgets.spinhxj.setValue(0)
            widgets.spinhxj.setMaximum(widgets.spinhxj.maximum() - hxj)
            tlj = widgets.spintlj.value()
            widgets.spintlj.setValue(0)
            widgets.spintlj.setMaximum(widgets.spintlj.maximum() - tlj)
            htj = widgets.spinhtj.value()
            widgets.spinhtj.setValue(0)
            widgets.spinhtj.setMaximum(widgets.spinhtj.maximum() - htj)

            if fqj > 0:
                call.add_product_user(3, fqj)
                global f52
                if f52:
                    widgets.label_604 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_604.setObjectName(u"label_604")
                    widgets.label_604.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_604.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_604, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_604.setText("番茄酱")
                    widgets.label_605= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_605.setObjectName(u"label_605")
                    widgets.label_605.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_605, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_605.setText(str(fqj))
                    f52 = False
                else:
                    fqj = fqj + int(widgets.label_605.text())
                    widgets.label_605.setText(str(fqj))
            if y > 0:
                call.add_product_user(4, y)
                global f53
                if f53:
                    widgets.label_606 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_606.setObjectName(u"label_606")
                    widgets.label_606.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_606.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_606, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_606.setText("盐")
                    widgets.label_607= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_607.setObjectName(u"label_607")
                    widgets.label_607.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_607, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_607.setText(str(y))
                    f53 = False
                else:
                    y = y + int(widgets.label_607.text())
                    widgets.label_607.setText(str(y))
            if my > 0:
                call.add_product_user(5, my)
                global f54
                if f54:
                    widgets.label_608 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_608.setObjectName(u"label_608")
                    widgets.label_608.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_608.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_608, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_608.setText("麻油")
                    widgets.label_609= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_609.setObjectName(u"label_609")
                    widgets.label_609.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_609, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_609.setText(str(my))
                    f54 = False
                else:
                    my = my + int(widgets.label_609.text())
                    widgets.label_609.setText(str(my))
            if jy > 0:
                call.add_product_user(6, jy)
                global f55
                if f55:
                    widgets.label_610 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_610.setObjectName(u"label_610")
                    widgets.label_610.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_610.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_610, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_610.setText("酱油")
                    widgets.label_611= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_611.setObjectName(u"label_611")
                    widgets.label_611.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_611, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_611.setText(str(jy))
                    f55 = False
                else:
                    jy = jy + int(widgets.label_611.text())
                    widgets.label_611.setText(str(jy))
            if hxf > 0:
                call.add_product_user(7, hxf)
                global f56
                if f56:
                    widgets.label_612 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_612.setObjectName(u"label_612")
                    widgets.label_612.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_612.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_612, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_612.setText("海鲜粉")
                    widgets.label_613= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_613.setObjectName(u"label_613")
                    widgets.label_613.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_613, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_613.setText(str(hxf))
                    f56 = False
                else:
                    hxf = hxf + int(widgets.label_613.text())
                    widgets.label_613.setText(str(hxf))
            if hjf > 0:
                call.add_product_user(8, hjf)
                global f57
                if f57:
                    widgets.label_614 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_614.setObjectName(u"label_614")
                    widgets.label_614.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_614.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_614, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_614.setText("胡椒粉")
                    widgets.label_615= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_615.setObjectName(u"label_615")
                    widgets.label_615.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_615, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_615.setText(str(hjf))
                    f57 = False
                else:
                    hjf = hjf + int(widgets.label_615.text())
                    widgets.label_615.setText(str(hjf))
            if wj > 0:
                call.add_product_user(15, wj)
                global f58
                if f58:
                    widgets.label_616 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_616.setObjectName(u"label_616")
                    widgets.label_616.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_616.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_616, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_616.setText("味精")
                    widgets.label_617= QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_617.setObjectName(u"label_617")
                    widgets.label_617.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_617, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_617.setText(str(wj))
                    f58 = False
                else:
                    wj = wj + int(widgets.label_617.text())
                    widgets.label_617.setText(str(wj))
            if krj > 0:
                call.add_product_user(28, krj)
                global f59
                if f59:
                    widgets.label_618 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_618.setObjectName(u"label_618")
                    widgets.label_618.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_618.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_618, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_618.setText("烤肉酱")
                    widgets.label_619 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_619.setObjectName(u"label_619")
                    widgets.label_619.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_619, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_619.setText(str(krj))
                    f59 = False
                else:
                    krj = krj + int(widgets.label_619.text())
                    widgets.label_619.setText(str(krj))
            if hy > 0:
                call.add_product_user(44, hy)
                global f60
                if f60:
                    widgets.label_620 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_620.setObjectName(u"label_620")
                    widgets.label_620.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_620.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_620, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_620.setText("蚝油")
                    widgets.label_621 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_621.setObjectName(u"label_621")
                    widgets.label_621.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_621, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_621.setText(str(hy))
                    f60 = False
                else:
                    hy = hy + int(widgets.label_621.text())
                    widgets.label_621.setText(str(hy))
            if hxj > 0:
                call.add_product_user(61, hxj)
                global f61
                if f61:
                    widgets.label_622 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_622.setObjectName(u"label_622")
                    widgets.label_622.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_622.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_622, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_622.setText("海鲜酱")
                    widgets.label_623 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_623.setObjectName(u"label_623")
                    widgets.label_623.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_623, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_623.setText(str(hxj))
                    f61 = False
                else:
                    hxj = hxj + int(widgets.label_623.text())
                    widgets.label_623.setText(str(hxj))
            if tlj > 0:
                call.add_product_user(63, tlj)
                global f62
                if f62:
                    widgets.label_624 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_624.setObjectName(u"label_624")
                    widgets.label_624.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_624.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_624, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_624.setText("甜辣酱")
                    widgets.label_625 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_625.setObjectName(u"label_625")
                    widgets.label_625.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_625, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_625.setText(str(tlj))
                    f62 = False
                else:
                    tlj = tlj + int(widgets.label_625.text())
                    widgets.label_625.setText(str(tlj))
            if htj > 0:
                call.add_product_user(65, htj)
                global f63
                if f63:
                    widgets.label_626 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_626.setObjectName(u"label_626")
                    widgets.label_626.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_626.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_626, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_626.setText("海苔酱")
                    widgets.label_627 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_627.setObjectName(u"label_627")
                    widgets.label_627.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_627, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_627.setText(str(htj))
                    f63 = False
                else:
                    htj = htj + int(widgets.label_627.text())
                    widgets.label_627.setText(str(htj))

        if btnName == "btn_tzp":
            hs_2 = widgets.spinhs_2.value()
            widgets.spinhs_2.setValue(0)
            widgets.spinhs_2.setMaximum(widgets.spinhs_2.maximum() - hs_2)
            xr = widgets.spinxr.value()
            widgets.spinxr.setValue(0)
            widgets.spinxr.setMaximum(widgets.spinxr.maximum() - xr)
            bg_2 = widgets.spinbg_2.value()
            widgets.spinbg_2.setValue(0)
            widgets.spinbg_2.setMaximum(widgets.spinbg_2.maximum() - bg_2)
            kxg = widgets.spinkxg.value()
            widgets.spinkxg.setValue(0)
            widgets.spinkxg.setMaximum(widgets.spinkxg.maximum() - kxg)
            gz = widgets.spingz.value()
            widgets.spingz.setValue(0)
            widgets.spingz.setMaximum(widgets.spingz.maximum() - gz)
            yg = widgets.spinyg.value()
            widgets.spinyg.setValue(0)
            widgets.spinyg.setMaximum(widgets.spinyg.maximum() - yg)
            ht = widgets.spinht.value()
            widgets.spinht.setValue(0)
            widgets.spinht.setMaximum(widgets.spinht.maximum() - ht)

            if hs_2 > 0:
                call.add_product_user(21, hs_2)
                global f64
                if f64:
                    widgets.label_628 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_628.setObjectName(u"label_628")
                    widgets.label_628.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_628.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_628, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_628.setText("花生")
                    widgets.label_629 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_629.setObjectName(u"label_629")
                    widgets.label_629.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_629, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_629.setText(str(hs_2))
                    f64 = False
                else:
                    hs_2 = hs_2 + int(widgets.label_629.text())
                    widgets.label_629.setText(str(hs_2))
            if xr > 0:
                call.add_product_user(66, xr)
                global f65
                if f65:
                    widgets.label_630 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_630.setObjectName(u"label_630")
                    widgets.label_630.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_630.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_630, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_630.setText("杏仁")
                    widgets.label_631 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_631.setObjectName(u"label_631")
                    widgets.label_631.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_631, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_631.setText(str(xr))
                    f65 = False
                else:
                    xr = xr + int(widgets.label_631.text())
                    widgets.label_631.setText(str(xr))
            if bg_2 > 0:
                call.add_product_user(67, bg_2)
                global f70
                if f70:
                    widgets.label_632 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_632.setObjectName(u"label_632")
                    widgets.label_632.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_632.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_632, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_632.setText("白果")
                    widgets.label_633 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_633.setObjectName(u"label_633")
                    widgets.label_633.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_633, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_633.setText(str(bg_2))
                    f70 = False
                else:
                    bg_2 = bg_2 + int(widgets.label_633.text())
                    widgets.label_633.setText(str(bg_2))
            if kxg > 0:
                call.add_product_user(68, kxg)
                global f66
                if f66:
                    widgets.label_634 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_634.setObjectName(u"label_634")
                    widgets.label_634.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_634.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_634, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_634.setText("开心果")
                    widgets.label_635 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_635.setObjectName(u"label_635")
                    widgets.label_635.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_635, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_635.setText(str(kxg))
                    f66 = False
                else:
                    kxg = kxg + int(widgets.label_635.text())
                    widgets.label_635.setText(str(kxg))
            if gz > 0:
                call.add_product_user(69, gz)
                global f67
                if f67:
                    widgets.label_636 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_636.setObjectName(u"label_636")
                    widgets.label_636.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_636.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_636, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_636.setText("瓜子")
                    widgets.label_637 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_637.setObjectName(u"label_637")
                    widgets.label_637.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_637, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_637.setText(str(gz))
                    f67 = False
                else:
                    gz = gz + int(widgets.label_637.text())
                    widgets.label_637.setText(str(gz))
            if yg > 0:
                call.add_product_user(70, yg)
                global f68
                if f68:
                    widgets.label_638 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_638.setObjectName(u"label_638")
                    widgets.label_638.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_638.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_638, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_638.setText("腰果")
                    widgets.label_639 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_639.setObjectName(u"label_639")
                    widgets.label_639.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_639, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_639.setText(str(yg))
                    f68 = False
                else:
                    yg = yg + int(widgets.label_639.text())
                    widgets.label_639.setText(str(yg))
            if ht > 0:
                call.add_product_user(71, ht)
                global f69
                if f69:
                    widgets.label_640 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_640.setObjectName(u"label_640")
                    widgets.label_640.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.label_640.setMinimumHeight(40)
                    cnt += 1
                    widgets.gridLayout_15.addWidget(widgets.label_640, cnt, 2, 1, 1, Qt.AlignCenter)
                    widgets.label_640.setText("核桃")
                    widgets.label_641 = QLabel(widgets.scrollAreaWidgetContents_13)
                    widgets.label_641.setObjectName(u"label_641")
                    widgets.label_641.setStyleSheet(u"font: 12pt \"Times New Roman\";")
                    widgets.gridLayout_15.addWidget(widgets.label_641, cnt, 3, 1, 1, Qt.AlignCenter)
                    widgets.label_641.setText(str(ht))
                    f69 = False
                else:
                    ht = ht + int(widgets.label_641.text())
                    widgets.label_641.setText(str(ht))

        if btnName == "btn_submit":
            cnt = 0
            if not f1:
                widgets.label_500.setText("")
                widgets.label_501.setText("")
            if not f2:
                widgets.label_502.setText("")
                widgets.label_503.setText("")
            if not f3:
                widgets.label_504.setText("")
                widgets.label_505.setText("")
            if not f4:
                widgets.label_506.setText("")
                widgets.label_507.setText("")
            if not f5:
                widgets.label_508.setText("")
                widgets.label_509.setText("")
            if not f6:
                widgets.label_510.setText("")
                widgets.label_511.setText("")
            if not f7:
                widgets.label_512.setText("")
                widgets.label_513.setText("")
            if not f8:
                widgets.label_514.setText("")
                widgets.label_515.setText("")
            if not f9:
                widgets.label_516.setText("")
                widgets.label_517.setText("")
            if not f10:
                widgets.label_518.setText("")
                widgets.label_519.setText("")
            if not f11:
                widgets.label_520.setText("")
                widgets.label_521.setText("")
            if not f12:
                widgets.label_522.setText("")
                widgets.label_523.setText("")
            if not f13:
                widgets.label_524.setText("")
                widgets.label_525.setText("")
            if not f14:
                widgets.label_526.setText("")
                widgets.label_527.setText("")
            if not f15:
                widgets.label_528.setText("")
                widgets.label_529.setText("")
            if not f16:
                widgets.label_530.setText("")
                widgets.label_531.setText("")
            if not f17:
                widgets.label_532.setText("")
                widgets.label_533.setText("")
            if not f18:
                widgets.label_534.setText("")
                widgets.label_535.setText("")
            if not f19:
                widgets.label_536.setText("")
                widgets.label_537.setText("")
            if not f20:
                widgets.label_538.setText("")
                widgets.label_539.setText("")
            if not f21:
                widgets.label_540.setText("")
                widgets.label_541.setText("")
            if not f22:
                widgets.label_542.setText("")
                widgets.label_543.setText("")
            if not f23:
                widgets.label_544.setText("")
                widgets.label_545.setText("")
            if not f24:
                widgets.label_546.setText("")
                widgets.label_547.setText("")
            if not f25:
                widgets.label_548.setText("")
                widgets.label_549.setText("")
            if not f26:
                widgets.label_550.setText("")
                widgets.label_551.setText("")
            if not f27:
                widgets.label_552.setText("")
                widgets.label_553.setText("")
            if not f28:
                widgets.label_554.setText("")
                widgets.label_555.setText("")
            if not f29:
                widgets.label_556.setText("")
                widgets.label_557.setText("")
            if not f30:
                widgets.label_558.setText("")
                widgets.label_559.setText("")
            if not f31:
                widgets.label_560.setText("")
                widgets.label_561.setText("")
            if not f32:
                widgets.label_562.setText("")
                widgets.label_563.setText("")
            if not f33:
                widgets.label_564.setText("")
                widgets.label_565.setText("")
            if not f34:
                widgets.label_566.setText("")
                widgets.label_567.setText("")
            if not f35:
                widgets.label_568.setText("")
                widgets.label_569.setText("")
            if not f36:
                widgets.label_570.setText("")
                widgets.label_571.setText("")
            if not f71:
                widgets.label_572.setText("")
                widgets.label_573.setText("")
            if not f37:
                widgets.label_574.setText("")
                widgets.label_575.setText("")
            if not f38:
                widgets.label_576.setText("")
                widgets.label_577.setText("")
            if not f39:
                widgets.label_578.setText("")
                widgets.label_579.setText("")
            if not f40:
                widgets.label_580.setText("")
                widgets.label_581.setText("")
            if not f41:
                widgets.label_582.setText("")
                widgets.label_583.setText("")
            if not f42:
                widgets.label_584.setText("")
                widgets.label_585.setText("")
            if not f43:
                widgets.label_586.setText("")
                widgets.label_587.setText("")
            if not f44:
                widgets.label_588.setText("")
                widgets.label_589.setText("")
            if not f45:
                widgets.label_590.setText("")
                widgets.label_591.setText("")
            if not f46:
                widgets.label_592.setText("")
                widgets.label_593.setText("")
            if not f47:
                widgets.label_594.setText("")
                widgets.label_595.setText("")
            if not f48:
                widgets.label_596.setText("")
                widgets.label_597.setText("")
            if not f49:
                widgets.label_598.setText("")
                widgets.label_599.setText("")
            if not f50:
                widgets.label_600.setText("")
                widgets.label_601.setText("")
            if not f51:
                widgets.label_602.setText("")
                widgets.label_603.setText("")
            if not f52:
                widgets.label_604.setText("")
                widgets.label_605.setText("")
            if not f53:
                widgets.label_606.setText("")
                widgets.label_607.setText("")
            if not f54:
                widgets.label_608.setText("")
                widgets.label_609.setText("")
            if not f55:
                widgets.label_610.setText("")
                widgets.label_611.setText("")
            if not f56:
                widgets.label_612.setText("")
                widgets.label_613.setText("")
            if not f57:
                widgets.label_614.setText("")
                widgets.label_615.setText("")
            if not f58:
                widgets.label_616.setText("")
                widgets.label_617.setText("")
            if not f59:
                widgets.label_618.setText("")
                widgets.label_619.setText("")
            if not f60:
                widgets.label_620.setText("")
                widgets.label_621.setText("")
            if not f61:
                widgets.label_622.setText("")
                widgets.label_623.setText("")
            if not f62:
                widgets.label_624.setText("")
                widgets.label_625.setText("")
            if not f63:
                widgets.label_626.setText("")
                widgets.label_627.setText("")
            if not f64:
                widgets.label_628.setText("")
                widgets.label_629.setText("")
            if not f65:
                widgets.label_630.setText("")
                widgets.label_631.setText("")
            if not f70:
                widgets.label_632.setText("")
                widgets.label_633.setText("")
            if not f66:
                widgets.label_634.setText("")
                widgets.label_635.setText("")
            if not f67:
                widgets.label_636.setText("")
                widgets.label_637.setText("")
            if not f68:
                widgets.label_638.setText("")
                widgets.label_639.setText("")
            if not f69:
                widgets.label_640.setText("")
                widgets.label_641.setText("")

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
        widgets.btn_category.clicked.connect(self.buttonClick)
        widgets.btn_cart.clicked.connect(self.buttonClick)
        widgets.btn_order.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)
        widgets.btn_logon.clicked.connect(self.buttonClick)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.Surebtn.clicked.connect(self.buttonClick)
        widgets.surebtn.clicked.connect(self.buttonClick)
        widgets.btn_yinliao.clicked.connect(self.buttonClick)
        widgets.btn_dianxin.clicked.connect(self.buttonClick)
        widgets.btn_roujiaqin.clicked.connect(self.buttonClick)
        widgets.btn_guleimaipian.clicked.connect(self.buttonClick)
        widgets.btn_haixian.clicked.connect(self.buttonClick)
        widgets.btn_riyongpin.clicked.connect(self.buttonClick)
        widgets.btn_tiaoweipin.clicked.connect(self.buttonClick)
        widgets.btn_tezhipin.clicked.connect(self.buttonClick)
        widgets.btn_yl.clicked.connect(self.buttonClick)
        widgets.btn_dx.clicked.connect(self.buttonClick)
        widgets.btn_rjq.clicked.connect(self.buttonClick)
        widgets.btn_glmp.clicked.connect(self.buttonClick)
        widgets.btn_hx.clicked.connect(self.buttonClick)
        widgets.btn_ryp.clicked.connect(self.buttonClick)
        widgets.btn_twp.clicked.connect(self.buttonClick)
        widgets.btn_tzp.clicked.connect(self.buttonClick)
        widgets.btn_submit.clicked.connect(self.buttonClick)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        # set welcome page
        widgets.stackedWidget.setCurrentWidget(widgets.welcome)

        widgets.btn_category.setEnabled(False)
        widgets.btn_cart.setEnabled(False)
        widgets.btn_order.setEnabled(False)


if __name__ == "__main__":
    # find current folder path
    jpath = os.path.abspath('.')

    # start Java virtual machine
    jpype.startJVM(r"C:\Program Files\Java\jdk-20\bin\server\jvm.dll", "-ea",
                   "-Djava.class.path=%s;%s" % (jpath + '/jbdc.jar', jpath + '/jdbc.jar'))

    # import Java api
    call = jpype.JClass("DatabaseCourseDesign.api")

    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())

    # shut down Java virtual machine
    jpype.shutdownJVM()
