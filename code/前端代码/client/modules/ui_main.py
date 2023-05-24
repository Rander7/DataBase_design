from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"#topMenu .QPushButton {	\n"
"	background-position: left cent"
                        "er;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;"
                        "\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
""
                        "#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#"
                        "themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	"
                        "padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: "
                        "rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border"
                        ": none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
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
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-lin"
                        "e:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
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
"QCheckBox::indicator:check"
                        "ed {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
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
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
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
"	border-left-styl"
                        "e: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);"
                        "\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	b"
                        "order: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setMouseTracking(False)
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.settingsTopBtn = QPushButton(self.topLogoInfo)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setGeometry(QRect(0, 0, 60, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsTopBtn.sizePolicy().hasHeightForWidth())
        self.settingsTopBtn.setSizePolicy(sizePolicy)
        self.settingsTopBtn.setMinimumSize(QSize(0, 45))
        self.settingsTopBtn.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.settingsTopBtn.setPalette(palette)
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsTopBtn.setAutoFillBackground(False)
        self.settingsTopBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.settingsTopBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy1)
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuFrame.setSizeIncrement(QSize(0, 0))
        self.leftMenuFrame.setBaseSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.topMenu)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_8.addWidget(self.label_20)

        self.btn_category = QPushButton(self.topMenu)
        self.btn_category.setObjectName(u"btn_category")
        sizePolicy.setHeightForWidth(self.btn_category.sizePolicy().hasHeightForWidth())
        self.btn_category.setSizePolicy(sizePolicy)
        self.btn_category.setMinimumSize(QSize(0, 45))
        self.btn_category.setFont(font)
        self.btn_category.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_category.setLayoutDirection(Qt.LeftToRight)
        self.btn_category.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_category)

        self.label_14 = QLabel(self.topMenu)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.btn_cart = QPushButton(self.topMenu)
        self.btn_cart.setObjectName(u"btn_cart")
        sizePolicy.setHeightForWidth(self.btn_cart.sizePolicy().hasHeightForWidth())
        self.btn_cart.setSizePolicy(sizePolicy)
        self.btn_cart.setMinimumSize(QSize(0, 45))
        self.btn_cart.setFont(font)
        self.btn_cart.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cart.setLayoutDirection(Qt.LeftToRight)
        self.btn_cart.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cart.png);")

        self.verticalLayout_8.addWidget(self.btn_cart)

        self.label_19 = QLabel(self.topMenu)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_8.addWidget(self.label_19)

        self.btn_order = QPushButton(self.topMenu)
        self.btn_order.setObjectName(u"btn_order")
        sizePolicy.setHeightForWidth(self.btn_order.sizePolicy().hasHeightForWidth())
        self.btn_order.setSizePolicy(sizePolicy)
        self.btn_order.setMinimumSize(QSize(0, 45))
        self.btn_order.setFont(font)
        self.btn_order.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_order.setLayoutDirection(Qt.LeftToRight)
        self.btn_order.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_order)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(0, 0))
        self.bottomMenu.setMaximumSize(QSize(16777215, 16777215))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Times New Roman\";\n"
"	font: 18pt\n"
"}")
        self.titleRightInfo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.pagesContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.home)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 8, 9, 9)
        self.scrollArea_2 = QScrollArea(self.home)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 600, 693))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_16, 8, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 3, 1, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 1, 3, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_17, 8, 1, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel{\n"
"	font: 18pt\n"
"}")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 3, 3, 1, 1)

        self.btn_yinliao = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_yinliao.setObjectName(u"btn_yinliao")
        self.btn_yinliao.setMinimumSize(QSize(0, 0))
        self.btn_yinliao.setMaximumSize(QSize(200, 16777215))
        self.btn_yinliao.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/images/yl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_yinliao.setIcon(icon3)
        self.btn_yinliao.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_yinliao, 0, 0, 1, 1)

        self.btn_dianxin = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_dianxin.setObjectName(u"btn_dianxin")
        self.btn_dianxin.setMinimumSize(QSize(0, 0))
        self.btn_dianxin.setMaximumSize(QSize(200, 16777215))
        self.btn_dianxin.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/images/dx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dianxin.setIcon(icon4)
        self.btn_dianxin.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_dianxin, 0, 1, 1, 1)

        self.btn_roujiaqin = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_roujiaqin.setObjectName(u"btn_roujiaqin")
        self.btn_roujiaqin.setMaximumSize(QSize(200, 16777215))
        self.btn_roujiaqin.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/images/rjq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_roujiaqin.setIcon(icon5)
        self.btn_roujiaqin.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_roujiaqin, 0, 3, 1, 1)

        self.btn_guleimaipian = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_guleimaipian.setObjectName(u"btn_guleimaipian")
        self.btn_guleimaipian.setMaximumSize(QSize(200, 16777215))
        self.btn_guleimaipian.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/images/glmp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guleimaipian.setIcon(icon6)
        self.btn_guleimaipian.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_guleimaipian, 2, 0, 1, 1)

        self.btn_haixian = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_haixian.setObjectName(u"btn_haixian")
        self.btn_haixian.setMaximumSize(QSize(200, 16777215))
        self.btn_haixian.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/images/images/hx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_haixian.setIcon(icon7)
        self.btn_haixian.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_haixian, 2, 1, 1, 1)

        self.btn_riyongpin = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_riyongpin.setObjectName(u"btn_riyongpin")
        self.btn_riyongpin.setMaximumSize(QSize(200, 16777215))
        self.btn_riyongpin.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/images/images/ryp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_riyongpin.setIcon(icon8)
        self.btn_riyongpin.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_riyongpin, 2, 3, 1, 1)

        self.btn_tiaoweipin = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_tiaoweipin.setObjectName(u"btn_tiaoweipin")
        self.btn_tiaoweipin.setMaximumSize(QSize(200, 16777215))
        self.btn_tiaoweipin.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/images/images/images/twp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tiaoweipin.setIcon(icon9)
        self.btn_tiaoweipin.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_tiaoweipin, 6, 0, 1, 1)

        self.btn_tezhipin = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_tezhipin.setObjectName(u"btn_tezhipin")
        self.btn_tezhipin.setMaximumSize(QSize(200, 16777215))
        self.btn_tezhipin.setStyleSheet(u"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/images/images/images/tzp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tezhipin.setIcon(icon10)
        self.btn_tezhipin.setIconSize(QSize(195, 195))

        self.gridLayout_4.addWidget(self.btn_tezhipin, 6, 1, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_6.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.home)
        self.tiaoweipin = QWidget()
        self.tiaoweipin.setObjectName(u"tiaoweipin")
        self.horizontalLayout_9 = QHBoxLayout(self.tiaoweipin)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scrollArea_6 = QScrollArea(self.tiaoweipin)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 903, 959))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.spinmy = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinmy.setObjectName(u"spinmy")
        self.spinmy.setMaximumSize(QSize(60, 16777215))
        self.spinmy.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinmy.setAlignment(Qt.AlignCenter)
        self.spinmy.setMaximum(0)

        self.gridLayout_8.addWidget(self.spinmy, 3, 5, 1, 1)

        self.label_91 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(0, 50))
        self.label_91.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_8.addWidget(self.label_91, 10, 1, 1, 1)

        self.label_80 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(135, 0))
        self.label_80.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_80, 8, 3, 1, 1)

        self.label_90 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(0, 50))
        self.label_90.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_8.addWidget(self.label_90, 7, 1, 1, 1)

        self.label_87 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(150, 150))
        self.label_87.setMaximumSize(QSize(150, 150))
        self.label_87.setPixmap(QPixmap(u":/images/images/images/65_\u6d77\u82d4\u9171.png"))

        self.gridLayout_8.addWidget(self.label_87, 11, 4, 1, 1)

        self.spinhxj = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinhxj.setObjectName(u"spinhxj")
        self.spinhxj.setMaximumSize(QSize(60, 16777215))
        self.spinhxj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhxj.setAlignment(Qt.AlignCenter)
        self.spinhxj.setMaximum(113)

        self.gridLayout_8.addWidget(self.spinhxj, 12, 1, 1, 1)

        self.label_68 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(135, 0))
        self.label_68.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_68, 2, 3, 1, 1)

        self.label_77 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(150, 150))
        self.label_77.setMaximumSize(QSize(150, 150))
        self.label_77.setPixmap(QPixmap(u":/images/images/images/15_\u5473\u7cbe.png"))

        self.gridLayout_8.addWidget(self.label_77, 8, 0, 1, 1)

        self.label_70 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(135, 0))
        self.label_70.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_70, 2, 5, 1, 1)

        self.label_89 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(0, 50))
        self.label_89.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_8.addWidget(self.label_89, 4, 1, 1, 1)

        self.label_76 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(135, 0))
        self.label_76.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_76, 5, 5, 1, 1)

        self.spintlj = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spintlj.setObjectName(u"spintlj")
        self.spintlj.setMaximumSize(QSize(60, 16777215))
        self.spintlj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spintlj.setAlignment(Qt.AlignCenter)
        self.spintlj.setMaximum(24)

        self.gridLayout_8.addWidget(self.spintlj, 12, 3, 1, 1)

        self.spinhjf = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinhjf.setObjectName(u"spinhjf")
        self.spinhjf.setMaximumSize(QSize(60, 16777215))
        self.spinhjf.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhjf.setAlignment(Qt.AlignCenter)
        self.spinhjf.setMaximum(6)

        self.gridLayout_8.addWidget(self.spinhjf, 6, 5, 1, 1)

        self.spinfqj = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinfqj.setObjectName(u"spinfqj")
        self.spinfqj.setMinimumSize(QSize(0, 0))
        self.spinfqj.setMaximumSize(QSize(60, 16777215))
        self.spinfqj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinfqj.setAlignment(Qt.AlignCenter)
        self.spinfqj.setMaximum(13)

        self.gridLayout_8.addWidget(self.spinfqj, 3, 1, 1, 1)

        self.label_88 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(135, 0))
        self.label_88.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_88, 11, 5, 1, 1)

        self.label_82 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(135, 0))
        self.label_82.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_82, 8, 5, 1, 1)

        self.label_69 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(150, 150))
        self.label_69.setMaximumSize(QSize(150, 150))
        self.label_69.setPixmap(QPixmap(u":/images/images/images/5_\u9ebb\u6cb9.png"))

        self.gridLayout_8.addWidget(self.label_69, 2, 4, 1, 1)

        self.spinhxf = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinhxf.setObjectName(u"spinhxf")
        self.spinhxf.setMaximumSize(QSize(60, 16777215))
        self.spinhxf.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhxf.setAlignment(Qt.AlignCenter)
        self.spinhxf.setMaximum(15)

        self.gridLayout_8.addWidget(self.spinhxf, 6, 3, 1, 1)

        self.spinkrj = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinkrj.setObjectName(u"spinkrj")
        self.spinkrj.setMaximumSize(QSize(60, 16777215))
        self.spinkrj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinkrj.setAlignment(Qt.AlignCenter)
        self.spinkrj.setMaximum(26)

        self.gridLayout_8.addWidget(self.spinkrj, 9, 3, 1, 1)

        self.label_67 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(150, 150))
        self.label_67.setMaximumSize(QSize(150, 150))
        self.label_67.setPixmap(QPixmap(u":/images/images/images/4_\u76d0.png"))

        self.gridLayout_8.addWidget(self.label_67, 2, 2, 1, 1)

        self.label_74 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(135, 0))
        self.label_74.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_74, 5, 3, 1, 1)

        self.label_85 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(150, 150))
        self.label_85.setMaximumSize(QSize(150, 150))
        self.label_85.setPixmap(QPixmap(u":/images/images/images/63_\u751c\u8fa3\u9171.png"))

        self.gridLayout_8.addWidget(self.label_85, 11, 2, 1, 1)

        self.label_84 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(135, 0))
        self.label_84.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_84, 11, 1, 1, 1)

        self.label_86 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(135, 0))
        self.label_86.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_86, 11, 3, 1, 1)

        self.spiny = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spiny.setObjectName(u"spiny")
        self.spiny.setMaximumSize(QSize(60, 16777215))
        self.spiny.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spiny.setAlignment(Qt.AlignCenter)
        self.spiny.setMaximum(53)

        self.gridLayout_8.addWidget(self.spiny, 3, 3, 1, 1)

        self.label_66 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(135, 0))
        self.label_66.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_66, 2, 1, 1, 1)

        self.label_83 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(150, 150))
        self.label_83.setMaximumSize(QSize(150, 150))
        self.label_83.setPixmap(QPixmap(u":/images/images/images/61_\u6d77\u9c9c\u9171.png"))

        self.gridLayout_8.addWidget(self.label_83, 11, 0, 1, 1)

        self.label_79 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(150, 150))
        self.label_79.setMaximumSize(QSize(150, 150))
        self.label_79.setPixmap(QPixmap(u":/images/images/images/28_\u70e4\u8089\u9171.png"))

        self.gridLayout_8.addWidget(self.label_79, 8, 2, 1, 1)

        self.label_72 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(135, 0))
        self.label_72.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_72, 5, 1, 1, 1)

        self.spinwj = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinwj.setObjectName(u"spinwj")
        self.spinwj.setMaximumSize(QSize(60, 16777215))
        self.spinwj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinwj.setAlignment(Qt.AlignCenter)
        self.spinwj.setMaximum(39)

        self.gridLayout_8.addWidget(self.spinwj, 9, 1, 1, 1)

        self.label_75 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(150, 150))
        self.label_75.setMaximumSize(QSize(150, 150))
        self.label_75.setPixmap(QPixmap(u":/images/images/images/8_\u80e1\u6912\u7c89.png"))

        self.gridLayout_8.addWidget(self.label_75, 5, 4, 1, 1)

        self.label_81 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(150, 150))
        self.label_81.setMaximumSize(QSize(150, 150))
        self.label_81.setPixmap(QPixmap(u":/images/images/images/44_\u869d\u6cb9.png"))

        self.gridLayout_8.addWidget(self.label_81, 8, 4, 1, 1)

        self.spinjy = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinjy.setObjectName(u"spinjy")
        self.spinjy.setMaximumSize(QSize(60, 16777215))
        self.spinjy.setBaseSize(QSize(0, 0))
        self.spinjy.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinjy.setAlignment(Qt.AlignCenter)
        self.spinjy.setMaximum(120)

        self.gridLayout_8.addWidget(self.spinjy, 6, 1, 1, 1)

        self.spinhy = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinhy.setObjectName(u"spinhy")
        self.spinhy.setMaximumSize(QSize(60, 16777215))
        self.spinhy.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhy.setAlignment(Qt.AlignCenter)
        self.spinhy.setMaximum(27)

        self.gridLayout_8.addWidget(self.spinhy, 9, 5, 1, 1)

        self.label_73 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(150, 150))
        self.label_73.setMaximumSize(QSize(150, 150))
        self.label_73.setPixmap(QPixmap(u":/images/images/images/7_\u6d77\u9c9c\u7c89.png"))

        self.gridLayout_8.addWidget(self.label_73, 5, 2, 1, 1)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(150, 150))
        self.label_71.setMaximumSize(QSize(150, 150))
        self.label_71.setPixmap(QPixmap(u":/images/images/images/6_\u9171\u6cb9.png"))

        self.gridLayout_8.addWidget(self.label_71, 5, 0, 1, 1)

        self.label_78 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(135, 0))
        self.label_78.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_8.addWidget(self.label_78, 8, 1, 1, 1)

        self.spinhtj = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinhtj.setObjectName(u"spinhtj")
        self.spinhtj.setMaximumSize(QSize(60, 16777215))
        self.spinhtj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhtj.setAlignment(Qt.AlignCenter)
        self.spinhtj.setMaximum(76)

        self.gridLayout_8.addWidget(self.spinhtj, 12, 5, 1, 1)

        self.label_65 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(150, 150))
        self.label_65.setMaximumSize(QSize(150, 150))
        self.label_65.setPixmap(QPixmap(u":/images/images/images/3_\u756a\u8304\u9171.png"))

        self.gridLayout_8.addWidget(self.label_65, 2, 0, 1, 1)

        self.btn_twp = QPushButton(self.scrollAreaWidgetContents_6)
        self.btn_twp.setObjectName(u"btn_twp")
        self.btn_twp.setMinimumSize(QSize(100, 25))
        self.btn_twp.setMaximumSize(QSize(100, 25))
        self.btn_twp.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.btn_twp, 1, 5, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_9.addWidget(self.scrollArea_6)

        self.stackedWidget.addWidget(self.tiaoweipin)
        self.dianxin = QWidget()
        self.dianxin.setObjectName(u"dianxin")
        self.horizontalLayout_10 = QHBoxLayout(self.dianxin)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.scrollArea_7 = QScrollArea(self.dianxin)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 903, 716))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_99 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(135, 0))
        self.label_99.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_99, 4, 1, 1, 1)

        self.spinghg = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinghg.setObjectName(u"spinghg")
        self.spinghg.setMaximumSize(QSize(60, 16777215))
        self.spinghg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinghg.setAlignment(Qt.AlignCenter)
        self.spinghg.setMaximum(40)

        self.gridLayout_9.addWidget(self.spinghg, 2, 5, 1, 1)

        self.label_165 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMinimumSize(QSize(135, 0))

        self.gridLayout_9.addWidget(self.label_165, 7, 3, 1, 1)

        self.spinbg = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinbg.setObjectName(u"spinbg")
        self.spinbg.setMaximumSize(QSize(60, 16777215))
        self.spinbg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinbg.setAlignment(Qt.AlignCenter)
        self.spinbg.setMaximum(29)

        self.gridLayout_9.addWidget(self.spinbg, 2, 1, 1, 1)

        self.label_97 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(150, 150))
        self.label_97.setMaximumSize(QSize(150, 150))
        self.label_97.setPixmap(QPixmap(u":/images/images/images/20_\u6842\u82b1\u7cd5.png"))

        self.gridLayout_9.addWidget(self.label_97, 1, 4, 1, 1)

        self.spinmht = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinmht.setObjectName(u"spinmht")
        self.spinmht.setMaximumSize(QSize(60, 16777215))
        self.spinmht.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinmht.setAlignment(Qt.AlignCenter)
        self.spinmht.setMaximum(15)

        self.gridLayout_9.addWidget(self.spinmht, 5, 3, 1, 1)

        self.label_98 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(135, 0))
        self.label_98.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_98, 1, 5, 1, 1)

        self.label_164 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMinimumSize(QSize(150, 150))
        self.label_164.setMaximumSize(QSize(150, 150))
        self.label_164.setPixmap(QPixmap(u":/images/images/images/62_\u5c71\u6e23\u7247.png"))

        self.gridLayout_9.addWidget(self.label_164, 7, 2, 1, 1)

        self.spinszp = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinszp.setObjectName(u"spinszp")
        self.spinszp.setMaximumSize(QSize(60, 16777215))
        self.spinszp.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinszp.setAlignment(Qt.AlignCenter)
        self.spinszp.setMaximum(17)

        self.gridLayout_9.addWidget(self.spinszp, 8, 3, 1, 1)

        self.label_95 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(150, 150))
        self.label_95.setMaximumSize(QSize(150, 150))
        self.label_95.setPixmap(QPixmap(u":/images/images/images/19_\u7cd6\u679c.png"))

        self.gridLayout_9.addWidget(self.label_95, 1, 2, 1, 1)

        self.label_105 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(135, 0))
        self.label_105.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_105, 7, 1, 1, 1)

        self.spinst = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinst.setObjectName(u"spinst")
        self.spinst.setMaximumSize(QSize(60, 16777215))
        self.spinst.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinst.setAlignment(Qt.AlignCenter)
        self.spinst.setMaximum(10)

        self.gridLayout_9.addWidget(self.spinst, 8, 1, 1, 1)

        self.spindg = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spindg.setObjectName(u"spindg")
        self.spindg.setMaximumSize(QSize(60, 16777215))
        self.spindg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spindg.setAlignment(Qt.AlignCenter)
        self.spindg.setMaximum(36)

        self.gridLayout_9.addWidget(self.spindg, 5, 5, 1, 1)

        self.label_103 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(135, 0))
        self.label_103.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_103, 4, 5, 1, 1)

        self.label_106 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(0, 50))
        self.label_106.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_9.addWidget(self.label_106, 3, 1, 1, 1)

        self.label_101 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(135, 0))
        self.label_101.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_101, 4, 3, 1, 1)

        self.label_102 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(150, 150))
        self.label_102.setMaximumSize(QSize(150, 150))
        self.label_102.setPixmap(QPixmap(u":/images/images/images/47_\u86cb\u7cd5.png"))

        self.gridLayout_9.addWidget(self.label_102, 4, 4, 1, 1)

        self.label_104 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(150, 150))
        self.label_104.setMaximumSize(QSize(150, 150))
        self.label_104.setPixmap(QPixmap(u":/images/images/images/49_\u85af\u6761.png"))

        self.gridLayout_9.addWidget(self.label_104, 7, 0, 1, 1)

        self.label_92 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(150, 150))
        self.label_92.setMaximumSize(QSize(150, 150))
        self.label_92.setPixmap(QPixmap(u":/images/images/images/16_\u997c\u5e72.png"))

        self.gridLayout_9.addWidget(self.label_92, 1, 0, 1, 1)

        self.label_93 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(135, 0))
        self.label_93.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_93, 1, 1, 1, 1)

        self.label_94 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(150, 150))
        self.label_94.setMaximumSize(QSize(150, 150))
        self.label_94.setPixmap(QPixmap(u":/images/images/images/25_\u5de7\u514b\u529b.png"))

        self.gridLayout_9.addWidget(self.label_94, 4, 0, 1, 1)

        self.spintg = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spintg.setObjectName(u"spintg")
        self.spintg.setMaximumSize(QSize(60, 16777215))
        self.spintg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spintg.setAlignment(Qt.AlignCenter)
        self.spintg.setMaximum(25)

        self.gridLayout_9.addWidget(self.spintg, 2, 3, 1, 1)

        self.label_100 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(150, 150))
        self.label_100.setMaximumSize(QSize(150, 150))
        self.label_100.setPixmap(QPixmap(u":/images/images/images/26_\u68c9\u82b1\u7cd6.png"))

        self.gridLayout_9.addWidget(self.label_100, 4, 2, 1, 1)

        self.spinqkl = QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinqkl.setObjectName(u"spinqkl")
        self.spinqkl.setMaximumSize(QSize(60, 16777215))
        self.spinqkl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinqkl.setAlignment(Qt.AlignCenter)
        self.spinqkl.setMaximum(76)

        self.gridLayout_9.addWidget(self.spinqkl, 5, 1, 1, 1)

        self.label_96 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(135, 0))
        self.label_96.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_9.addWidget(self.label_96, 1, 3, 1, 1)

        self.label_107 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(0, 50))
        self.label_107.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_9.addWidget(self.label_107, 6, 1, 1, 1)

        self.btn_dx = QPushButton(self.scrollAreaWidgetContents_7)
        self.btn_dx.setObjectName(u"btn_dx")
        self.btn_dx.setMinimumSize(QSize(100, 25))
        self.btn_dx.setMaximumSize(QSize(100, 25))
        self.btn_dx.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.btn_dx, 0, 5, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.horizontalLayout_10.addWidget(self.scrollArea_7)

        self.stackedWidget.addWidget(self.dianxin)
        self.guleimaipian = QWidget()
        self.guleimaipian.setObjectName(u"guleimaipian")
        self.verticalLayout_11 = QVBoxLayout(self.guleimaipian)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_9 = QScrollArea(self.guleimaipian)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 903, 716))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_142 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setPixmap(QPixmap(u":/images/images/images/64_\u9ec4\u8c46.png"))

        self.gridLayout_11.addWidget(self.label_142, 7, 4, 1, 1)

        self.label_138 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setPixmap(QPixmap(u":/images/images/images/56_\u767d\u7c73.png"))

        self.gridLayout_11.addWidget(self.label_138, 7, 0, 1, 1)

        self.label_130 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(150, 150))
        self.label_130.setMaximumSize(QSize(150, 150))
        self.label_130.setPixmap(QPixmap(u":/images/images/images/42_\u7cd9\u7c73.png"))

        self.gridLayout_11.addWidget(self.label_130, 1, 4, 1, 1)

        self.label_140 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setPixmap(QPixmap(u":/images/images/images/57_\u5c0f\u7c73.png"))

        self.gridLayout_11.addWidget(self.label_140, 7, 2, 1, 1)

        self.spinym = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinym.setObjectName(u"spinym")
        self.spinym.setMaximumSize(QSize(60, 16777215))
        self.spinym.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinym.setAlignment(Qt.AlignCenter)
        self.spinym.setMaximum(61)

        self.gridLayout_11.addWidget(self.spinym, 2, 3, 1, 1)

        self.label_136 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(150, 150))
        self.label_136.setMaximumSize(QSize(150, 150))
        self.label_136.setPixmap(QPixmap(u":/images/images/images/52_\u4e09\u5408\u4e00\u9ea6\u7247.png"))

        self.gridLayout_11.addWidget(self.label_136, 4, 4, 1, 1)

        self.label_144 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(0, 50))
        self.label_144.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_11.addWidget(self.label_144, 3, 1, 1, 1)

        self.label_141 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_141.setObjectName(u"label_141")

        self.gridLayout_11.addWidget(self.label_141, 7, 3, 1, 1)

        self.spinymb = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinymb.setObjectName(u"spinymb")
        self.spinymb.setMaximumSize(QSize(60, 16777215))
        self.spinymb.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinymb.setAlignment(Qt.AlignCenter)
        self.spinymb.setMaximum(65)

        self.gridLayout_11.addWidget(self.spinymb, 5, 3, 1, 1)

        self.label_129 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(135, 0))
        self.label_129.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_11.addWidget(self.label_129, 1, 3, 1, 1)

        self.label_127 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(135, 0))
        self.label_127.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_11.addWidget(self.label_127, 1, 1, 1, 1)

        self.label_128 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(150, 150))
        self.label_128.setMaximumSize(QSize(150, 150))
        self.label_128.setPixmap(QPixmap(u":/images/images/images/23_\u71d5\u9ea6.png"))

        self.gridLayout_11.addWidget(self.label_128, 1, 2, 1, 1)

        self.spinnm = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinnm.setObjectName(u"spinnm")
        self.spinnm.setMaximumSize(QSize(60, 16777215))
        self.spinnm.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinnm.setAlignment(Qt.AlignCenter)
        self.spinnm.setMaximum(104)

        self.gridLayout_11.addWidget(self.spinnm, 2, 1, 1, 1)

        self.label_133 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(135, 0))
        self.label_133.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_11.addWidget(self.label_133, 4, 1, 1, 1)

        self.label_139 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_11.addWidget(self.label_139, 7, 1, 1, 1)

        self.spinbm = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinbm.setObjectName(u"spinbm")
        self.spinbm.setMaximumSize(QSize(60, 16777215))
        self.spinbm.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinbm.setAlignment(Qt.AlignCenter)
        self.spinbm.setMaximum(21)

        self.gridLayout_11.addWidget(self.spinbm, 8, 1, 1, 1)

        self.spinymp = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinymp.setObjectName(u"spinymp")
        self.spinymp.setMaximumSize(QSize(60, 16777215))
        self.spinymp.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinymp.setAlignment(Qt.AlignCenter)
        self.spinymp.setMaximum(15)

        self.gridLayout_11.addWidget(self.spinymp, 5, 1, 1, 1)

        self.spinshymp = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinshymp.setObjectName(u"spinshymp")
        self.spinshymp.setMaximumSize(QSize(60, 16777215))
        self.spinshymp.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinshymp.setAlignment(Qt.AlignCenter)
        self.spinshymp.setMaximum(38)

        self.gridLayout_11.addWidget(self.spinshymp, 5, 5, 1, 1)

        self.spinxm = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinxm.setObjectName(u"spinxm")
        self.spinxm.setMaximumSize(QSize(60, 16777215))
        self.spinxm.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinxm.setAlignment(Qt.AlignCenter)
        self.spinxm.setMaximum(36)

        self.gridLayout_11.addWidget(self.spinxm, 8, 3, 1, 1)

        self.label_134 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(150, 150))
        self.label_134.setMaximumSize(QSize(150, 150))
        self.label_134.setPixmap(QPixmap(u":/images/images/images/50_\u7389\u7c73\u997c.png"))

        self.gridLayout_11.addWidget(self.label_134, 4, 2, 1, 1)

        self.spinhd = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinhd.setObjectName(u"spinhd")
        self.spinhd.setMaximumSize(QSize(60, 16777215))
        self.spinhd.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhd.setAlignment(Qt.AlignCenter)
        self.spinhd.setMaximum(22)

        self.gridLayout_11.addWidget(self.spinhd, 8, 5, 1, 1)

        self.label_137 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMinimumSize(QSize(135, 0))
        self.label_137.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_11.addWidget(self.label_137, 4, 5, 1, 1)

        self.label_145 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(0, 50))
        self.label_145.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_11.addWidget(self.label_145, 6, 1, 1, 1)

        self.label_126 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(150, 150))
        self.label_126.setMaximumSize(QSize(150, 150))
        self.label_126.setPixmap(QPixmap(u":/images/images/images/22_\u7cef\u7c73.png"))

        self.gridLayout_11.addWidget(self.label_126, 1, 0, 1, 1)

        self.spincm = QSpinBox(self.scrollAreaWidgetContents_9)
        self.spincm.setObjectName(u"spincm")
        self.spincm.setMaximumSize(QSize(60, 16777215))
        self.spincm.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spincm.setAlignment(Qt.AlignCenter)
        self.spincm.setMaximum(26)

        self.gridLayout_11.addWidget(self.spincm, 2, 5, 1, 1)

        self.label_143 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_11.addWidget(self.label_143, 7, 5, 1, 1)

        self.label_135 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(135, 0))
        self.label_135.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_11.addWidget(self.label_135, 4, 3, 1, 1)

        self.label_131 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(135, 0))
        self.label_131.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_11.addWidget(self.label_131, 1, 5, 1, 1)

        self.label_132 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(150, 150))
        self.label_132.setMaximumSize(QSize(150, 150))
        self.label_132.setPixmap(QPixmap(u":/images/images/images/48_\u7389\u7c73\u7247.png"))

        self.gridLayout_11.addWidget(self.label_132, 4, 0, 1, 1)

        self.btn_glmp = QPushButton(self.scrollAreaWidgetContents_9)
        self.btn_glmp.setObjectName(u"btn_glmp")
        self.btn_glmp.setMinimumSize(QSize(100, 25))
        self.btn_glmp.setMaximumSize(QSize(100, 25))
        self.btn_glmp.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.btn_glmp, 0, 5, 1, 1)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_11.addWidget(self.scrollArea_9)

        self.stackedWidget.addWidget(self.guleimaipian)
        self.haixian = QWidget()
        self.haixian.setObjectName(u"haixian")
        self.verticalLayout_15 = QVBoxLayout(self.haixian)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_11 = QScrollArea(self.haixian)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setStyleSheet(u"")
        self.scrollArea_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 903, 959))
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_166 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMinimumSize(QSize(150, 150))
        self.label_166.setMaximumSize(QSize(150, 150))
        self.label_166.setPixmap(QPixmap(u":/images/images/images/10_\u87f9.png"))

        self.gridLayout_13.addWidget(self.label_166, 1, 0, 1, 1)

        self.label_183 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setMinimumSize(QSize(135, 0))
        self.label_183.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_183, 7, 5, 1, 1)

        self.label_187 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setMinimumSize(QSize(135, 0))
        self.label_187.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_187, 10, 3, 1, 1)

        self.label_176 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMinimumSize(QSize(150, 150))
        self.label_176.setMaximumSize(QSize(150, 150))
        self.label_176.setPixmap(QPixmap(u":/images/images/images/37_\u5e72\u8d1d.png"))

        self.gridLayout_13.addWidget(self.label_176, 4, 4, 1, 1)

        self.label_179 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMinimumSize(QSize(135, 0))
        self.label_179.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_179, 7, 1, 1, 1)

        self.label_174 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMinimumSize(QSize(150, 150))
        self.label_174.setMaximumSize(QSize(150, 150))
        self.label_174.setPixmap(QPixmap(u":/images/images/images/36_\u9c7f\u9c7c.png"))

        self.gridLayout_13.addWidget(self.label_174, 4, 2, 1, 1)

        self.label_178 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMinimumSize(QSize(150, 150))
        self.label_178.setMaximumSize(QSize(150, 150))
        self.label_178.setPixmap(QPixmap(u":/images/images/images/40_\u867e\u7c73.png"))

        self.gridLayout_13.addWidget(self.label_178, 7, 0, 1, 1)

        self.label_177 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMinimumSize(QSize(135, 0))
        self.label_177.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_177, 4, 5, 1, 1)

        self.label_171 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMinimumSize(QSize(135, 0))
        self.label_171.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_171, 1, 3, 1, 1)

        self.spinlx = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinlx.setObjectName(u"spinlx")
        self.spinlx.setMaximumSize(QSize(60, 16777215))
        self.spinlx.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinlx.setAlignment(Qt.AlignCenter)
        self.spinlx.setMaximum(24)

        self.gridLayout_13.addWidget(self.spinlx, 2, 3, 1, 1)

        self.label_170 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMinimumSize(QSize(150, 150))
        self.label_170.setMaximumSize(QSize(150, 150))
        self.label_170.setPixmap(QPixmap(u":/images/images/images/13_\u9f99\u867e.png"))

        self.gridLayout_13.addWidget(self.label_170, 1, 2, 1, 1)

        self.label_167 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMinimumSize(QSize(135, 0))
        self.label_167.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_167, 1, 1, 1, 1)

        self.label_186 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setMinimumSize(QSize(150, 150))
        self.label_186.setMaximumSize(QSize(150, 150))
        self.label_186.setPixmap(QPixmap(u":/images/images/images/58_\u6d77\u53c2.png"))

        self.gridLayout_13.addWidget(self.label_186, 10, 2, 1, 1)

        self.spinyy = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinyy.setObjectName(u"spinyy")
        self.spinyy.setMaximumSize(QSize(60, 16777215))
        self.spinyy.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinyy.setAlignment(Qt.AlignCenter)
        self.spinyy.setMaximum(112)

        self.gridLayout_13.addWidget(self.spinyy, 5, 3, 1, 1)

        self.spingb = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spingb.setObjectName(u"spingb")
        self.spingb.setMaximumSize(QSize(60, 16777215))
        self.spingb.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spingb.setAlignment(Qt.AlignCenter)
        self.spingb.setMaximum(11)

        self.gridLayout_13.addWidget(self.spingb, 5, 5, 1, 1)

        self.label_180 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setMinimumSize(QSize(150, 0))
        self.label_180.setMaximumSize(QSize(150, 16777215))
        self.label_180.setPixmap(QPixmap(u":/images/images/images/41_\u867e\u5b50.png"))

        self.gridLayout_13.addWidget(self.label_180, 7, 2, 1, 1)

        self.label_172 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMinimumSize(QSize(150, 150))
        self.label_172.setMaximumSize(QSize(150, 150))
        self.label_172.setPixmap(QPixmap(u":/images/images/images/18_\u58a8\u9c7c.png"))

        self.gridLayout_13.addWidget(self.label_172, 1, 4, 1, 1)

        self.label_168 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMinimumSize(QSize(150, 150))
        self.label_168.setMaximumSize(QSize(150, 150))
        self.label_168.setPixmap(QPixmap(u":/images/images/images/30_\u9ec4\u9c7c.png"))

        self.gridLayout_13.addWidget(self.label_168, 4, 0, 1, 1)

        self.spink = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spink.setObjectName(u"spink")
        self.spink.setMaximumSize(QSize(60, 16777215))
        self.spink.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spink.setAlignment(Qt.AlignCenter)
        self.spink.setMaximum(95)

        self.gridLayout_13.addWidget(self.spink, 11, 1, 1, 1)

        self.label_190 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMinimumSize(QSize(0, 50))
        self.label_190.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_13.addWidget(self.label_190, 9, 1, 1, 1)

        self.label_184 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setMinimumSize(QSize(135, 0))
        self.label_184.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_184, 10, 1, 1, 1)

        self.spinhs = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinhs.setObjectName(u"spinhs")
        self.spinhs.setMaximumSize(QSize(60, 16777215))
        self.spinhs.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhs.setAlignment(Qt.AlignCenter)
        self.spinhs.setMaximum(62)

        self.gridLayout_13.addWidget(self.spinhs, 11, 3, 1, 1)

        self.label_175 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMinimumSize(QSize(135, 0))
        self.label_175.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_175, 4, 3, 1, 1)

        self.label_181 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMinimumSize(QSize(135, 0))
        self.label_181.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_181, 7, 3, 1, 1)

        self.spinxm_2 = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinxm_2.setObjectName(u"spinxm_2")
        self.spinxm_2.setMaximumSize(QSize(60, 16777215))
        self.spinxm_2.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinxm_2.setAlignment(Qt.AlignCenter)
        self.spinxm_2.setMaximum(123)

        self.gridLayout_13.addWidget(self.spinxm_2, 8, 1, 1, 1)

        self.spinmy_2 = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinmy_2.setObjectName(u"spinmy_2")
        self.spinmy_2.setMaximumSize(QSize(60, 16777215))
        self.spinmy_2.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinmy_2.setAlignment(Qt.AlignCenter)
        self.spinmy_2.setMaximum(42)

        self.gridLayout_13.addWidget(self.spinmy_2, 2, 5, 1, 1)

        self.label_182 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMinimumSize(QSize(150, 0))
        self.label_182.setMaximumSize(QSize(150, 16777215))
        self.label_182.setPixmap(QPixmap(u":/images/images/images/45_\u96ea\u9c7c.png"))

        self.gridLayout_13.addWidget(self.label_182, 7, 4, 1, 1)

        self.spinhy_2 = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinhy_2.setObjectName(u"spinhy_2")
        self.spinhy_2.setMaximumSize(QSize(60, 16777215))
        self.spinhy_2.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhy_2.setAlignment(Qt.AlignCenter)
        self.spinhy_2.setMaximum(10)

        self.gridLayout_13.addWidget(self.spinhy_2, 5, 1, 1, 1)

        self.label_173 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMinimumSize(QSize(135, 0))
        self.label_173.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_173, 1, 5, 1, 1)

        self.label_189 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMinimumSize(QSize(0, 50))
        self.label_189.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_13.addWidget(self.label_189, 6, 1, 1, 1)

        self.label_188 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setMinimumSize(QSize(0, 50))
        self.label_188.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_13.addWidget(self.label_188, 3, 1, 1, 1)

        self.label_185 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMinimumSize(QSize(150, 150))
        self.label_185.setMaximumSize(QSize(150, 150))
        self.label_185.setPixmap(QPixmap(u":/images/images/images/46_\u86b5.png"))

        self.gridLayout_13.addWidget(self.label_185, 10, 0, 1, 1)

        self.spinxy = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinxy.setObjectName(u"spinxy")
        self.spinxy.setMaximumSize(QSize(60, 16777215))
        self.spinxy.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinxy.setAlignment(Qt.AlignCenter)
        self.spinxy.setMaximum(5)

        self.gridLayout_13.addWidget(self.spinxy, 8, 5, 1, 1)

        self.spinx = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinx.setObjectName(u"spinx")
        self.spinx.setMaximumSize(QSize(60, 16777215))
        self.spinx.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinx.setAlignment(Qt.AlignCenter)
        self.spinx.setMaximum(31)

        self.gridLayout_13.addWidget(self.spinx, 2, 1, 1, 1)

        self.spinxz = QSpinBox(self.scrollAreaWidgetContents_11)
        self.spinxz.setObjectName(u"spinxz")
        self.spinxz.setMaximumSize(QSize(60, 16777215))
        self.spinxz.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinxz.setAlignment(Qt.AlignCenter)
        self.spinxz.setMaximum(85)

        self.gridLayout_13.addWidget(self.spinxz, 8, 3, 1, 1)

        self.label_169 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMinimumSize(QSize(135, 0))
        self.label_169.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_13.addWidget(self.label_169, 4, 1, 1, 1)

        self.btn_hx = QPushButton(self.scrollAreaWidgetContents_11)
        self.btn_hx.setObjectName(u"btn_hx")
        self.btn_hx.setMinimumSize(QSize(100, 25))
        self.btn_hx.setMaximumSize(QSize(100, 25))
        self.btn_hx.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_13.addWidget(self.btn_hx, 0, 5, 1, 1)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_15.addWidget(self.scrollArea_11)

        self.stackedWidget.addWidget(self.haixian)
        self.riyongpin = QWidget()
        self.riyongpin.setObjectName(u"riyongpin")
        self.verticalLayout_10 = QVBoxLayout(self.riyongpin)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_8 = QScrollArea(self.riyongpin)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 903, 716))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_113 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(135, 0))
        self.label_113.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_113, 1, 3, 1, 1)

        self.label_125 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(135, 0))
        self.label_125.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_125, 7, 1, 1, 1)

        self.label_122 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(0, 50))
        self.label_122.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_10.addWidget(self.label_122, 3, 1, 1, 1)

        self.label_120 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(150, 150))
        self.label_120.setMaximumSize(QSize(150, 150))
        self.label_120.setPixmap(QPixmap(u":/images/images/images/59_\u5149\u660e\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_120, 4, 4, 1, 1)

        self.spinlhnl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spinlhnl.setObjectName(u"spinlhnl")
        self.spinlhnl.setMaximumSize(QSize(60, 16777215))
        self.spinlhnl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinlhnl.setAlignment(Qt.AlignCenter)
        self.spinlhnl.setMaximum(112)

        self.gridLayout_10.addWidget(self.spinlhnl, 5, 3, 1, 1)

        self.spinwxnl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spinwxnl.setObjectName(u"spinwxnl")
        self.spinwxnl.setMaximumSize(QSize(60, 16777215))
        self.spinwxnl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinwxnl.setAlignment(Qt.AlignCenter)
        self.spinwxnl.setMaximum(0)

        self.gridLayout_10.addWidget(self.spinwxnl, 2, 5, 1, 1)

        self.spinbnl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spinbnl.setObjectName(u"spinbnl")
        self.spinbnl.setMaximumSize(QSize(60, 16777215))
        self.spinbnl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinbnl.setAlignment(Qt.AlignCenter)
        self.spinbnl.setMaximum(9)

        self.gridLayout_10.addWidget(self.spinbnl, 5, 1, 1, 1)

        self.label_123 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(0, 50))
        self.label_123.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_10.addWidget(self.label_123, 6, 1, 1, 1)

        self.spindgnl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spindgnl.setObjectName(u"spindgnl")
        self.spindgnl.setMaximumSize(QSize(60, 16777215))
        self.spindgnl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spindgnl.setAlignment(Qt.AlignCenter)
        self.spindgnl.setMaximum(86)

        self.gridLayout_10.addWidget(self.spindgnl, 2, 3, 1, 1)

        self.label_109 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(135, 0))
        self.label_109.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_109, 1, 1, 1, 1)

        self.label_115 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(135, 0))
        self.label_115.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_115, 1, 5, 1, 1)

        self.label_117 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(135, 0))
        self.label_117.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_117, 4, 1, 1, 1)

        self.spindznl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spindznl.setObjectName(u"spindznl")
        self.spindznl.setMaximumSize(QSize(60, 16777215))
        self.spindznl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spindznl.setAlignment(Qt.AlignCenter)
        self.spindznl.setMaximum(22)

        self.gridLayout_10.addWidget(self.spindznl, 2, 1, 1, 1)

        self.label_114 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(150, 150))
        self.label_114.setMaximumSize(QSize(150, 150))
        self.label_114.setPixmap(QPixmap(u":/images/images/images/31_\u6e29\u99a8\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_114, 1, 4, 1, 1)

        self.label_118 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(150, 150))
        self.label_118.setMaximumSize(QSize(150, 150))
        self.label_118.setPixmap(QPixmap(u":/images/images/images/33_\u6d6a\u82b1\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_118, 4, 2, 1, 1)

        self.label_112 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(150, 150))
        self.label_112.setMaximumSize(QSize(150, 150))
        self.label_112.setPixmap(QPixmap(u":/images/images/images/12_\u5fb7\u56fd\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_112, 1, 2, 1, 1)

        self.label_124 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(150, 150))
        self.label_124.setMaximumSize(QSize(150, 150))
        self.label_124.setPixmap(QPixmap(u":/images/images/images/60_\u82b1\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_124, 7, 0, 1, 1)

        self.label_116 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(150, 150))
        self.label_116.setMaximumSize(QSize(150, 150))
        self.label_116.setPixmap(QPixmap(u":/images/images/images/32_\u767d\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_116, 4, 0, 1, 1)

        self.spinhnl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spinhnl.setObjectName(u"spinhnl")
        self.spinhnl.setMaximumSize(QSize(60, 16777215))
        self.spinhnl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhnl.setAlignment(Qt.AlignCenter)
        self.spinhnl.setMaximum(19)

        self.gridLayout_10.addWidget(self.spinhnl, 8, 1, 1, 1)

        self.label_121 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(135, 0))
        self.label_121.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_121, 4, 5, 1, 1)

        self.label_108 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(150, 150))
        self.label_108.setMaximumSize(QSize(150, 150))
        self.label_108.setPixmap(QPixmap(u":/images/images/images/11_\u5927\u4f17\u5976\u916a.png"))

        self.gridLayout_10.addWidget(self.label_108, 1, 0, 1, 1)

        self.label_119 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(135, 0))
        self.label_119.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_10.addWidget(self.label_119, 4, 3, 1, 1)

        self.spingmnl = QSpinBox(self.scrollAreaWidgetContents_8)
        self.spingmnl.setObjectName(u"spingmnl")
        self.spingmnl.setMaximumSize(QSize(60, 16777215))
        self.spingmnl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spingmnl.setAlignment(Qt.AlignCenter)
        self.spingmnl.setMaximum(79)

        self.gridLayout_10.addWidget(self.spingmnl, 5, 5, 1, 1)

        self.btn_ryp = QPushButton(self.scrollAreaWidgetContents_8)
        self.btn_ryp.setObjectName(u"btn_ryp")
        self.btn_ryp.setMinimumSize(QSize(100, 25))
        self.btn_ryp.setMaximumSize(QSize(100, 25))
        self.btn_ryp.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.btn_ryp, 0, 5, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_10.addWidget(self.scrollArea_8)

        self.stackedWidget.addWidget(self.riyongpin)
        self.roujiaqin = QWidget()
        self.roujiaqin.setObjectName(u"roujiaqin")
        self.verticalLayout_12 = QVBoxLayout(self.roujiaqin)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_10 = QScrollArea(self.roujiaqin)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 903, 716))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.spinj = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinj.setObjectName(u"spinj")
        self.spinj.setMaximumSize(QSize(60, 16777215))
        self.spinj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinj.setAlignment(Qt.AlignCenter)
        self.spinj.setMaximum(29)

        self.gridLayout_12.addWidget(self.spinj, 2, 1, 1, 1)

        self.label_159 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_159.setObjectName(u"label_159")

        self.gridLayout_12.addWidget(self.label_159, 7, 1, 1, 1)

        self.label_160 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setPixmap(QPixmap(u":/images/images/images/55_\u9e2d\u8089.png"))

        self.gridLayout_12.addWidget(self.label_160, 7, 2, 1, 1)

        self.label_157 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMinimumSize(QSize(150, 0))
        self.label_157.setMaximumSize(QSize(150, 16777215))
        self.label_157.setPixmap(QPixmap(u":/images/images/images/53_\u76d0\u6c34\u9e2d.png"))

        self.gridLayout_12.addWidget(self.label_157, 4, 4, 1, 1)

        self.label_162 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMinimumSize(QSize(0, 50))
        self.label_162.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_12.addWidget(self.label_162, 3, 1, 1, 1)

        self.label_158 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setPixmap(QPixmap(u":/images/images/images/54_\u9e21\u8089.png"))

        self.gridLayout_12.addWidget(self.label_158, 7, 0, 1, 1)

        self.label_163 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMinimumSize(QSize(0, 50))
        self.label_163.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_12.addWidget(self.label_163, 6, 1, 1, 1)

        self.label_146 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(150, 150))
        self.label_146.setMaximumSize(QSize(150, 150))
        self.label_146.setPixmap(QPixmap(u":/images/images/images/9_\u9e21.png"))

        self.gridLayout_12.addWidget(self.label_146, 1, 0, 1, 1)

        self.spinzrg = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinzrg.setObjectName(u"spinzrg")
        self.spinzrg.setMaximumSize(QSize(60, 16777215))
        self.spinzrg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinzrg.setAlignment(Qt.AlignCenter)
        self.spinzrg.setMaximum(20)

        self.gridLayout_12.addWidget(self.spinzrg, 5, 3, 1, 1)

        self.label_151 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(150, 150))
        self.label_151.setMaximumSize(QSize(150, 150))
        self.label_151.setPixmap(QPixmap(u":/images/images/images/51_\u732a\u8089\u5e72.png"))

        self.gridLayout_12.addWidget(self.label_151, 4, 2, 1, 1)

        self.label_153 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(135, 0))
        self.label_153.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_12.addWidget(self.label_153, 4, 3, 1, 1)

        self.label_150 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(135, 0))
        self.label_150.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_12.addWidget(self.label_150, 1, 3, 1, 1)

        self.label_155 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMinimumSize(QSize(135, 0))
        self.label_155.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_12.addWidget(self.label_155, 1, 5, 1, 1)

        self.label_149 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(135, 0))
        self.label_149.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_12.addWidget(self.label_149, 4, 1, 1, 1)

        self.spinysy = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinysy.setObjectName(u"spinysy")
        self.spinysy.setMaximumSize(QSize(60, 16777215))
        self.spinysy.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinysy.setAlignment(Qt.AlignCenter)
        self.spinysy.setMaximum(0)

        self.gridLayout_12.addWidget(self.spinysy, 5, 5, 1, 1)

        self.spinyr55 = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinyr55.setObjectName(u"spinyr55")
        self.spinyr55.setMaximumSize(QSize(60, 16777215))
        self.spinyr55.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinyr55.setAlignment(Qt.AlignCenter)
        self.spinyr55.setMaximum(115)

        self.gridLayout_12.addWidget(self.spinyr55, 8, 3, 1, 1)

        self.label_156 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMinimumSize(QSize(135, 0))
        self.label_156.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_12.addWidget(self.label_156, 4, 5, 1, 1)

        self.label_154 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMinimumSize(QSize(150, 150))
        self.label_154.setMaximumSize(QSize(150, 150))
        self.label_154.setPixmap(QPixmap(u":/images/images/images/27_\u725b\u8089\u5e72.png"))

        self.gridLayout_12.addWidget(self.label_154, 1, 4, 1, 1)

        self.label_148 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(150, 150))
        self.label_148.setMaximumSize(QSize(150, 150))
        self.label_148.setPixmap(QPixmap(u":/images/images/images/29_\u9e2d\u8089.png"))

        self.gridLayout_12.addWidget(self.label_148, 4, 0, 1, 1)

        self.spinyr29 = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinyr29.setObjectName(u"spinyr29")
        self.spinyr29.setMaximumSize(QSize(60, 16777215))
        self.spinyr29.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinyr29.setAlignment(Qt.AlignCenter)
        self.spinyr29.setMaximum(0)

        self.gridLayout_12.addWidget(self.spinyr29, 5, 1, 1, 1)

        self.label_147 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(135, 0))
        self.label_147.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_12.addWidget(self.label_147, 1, 1, 1, 1)

        self.label_152 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(150, 150))
        self.label_152.setMaximumSize(QSize(150, 150))
        self.label_152.setPixmap(QPixmap(u":/images/images/images/17_\u732a\u8089.png"))

        self.gridLayout_12.addWidget(self.label_152, 1, 2, 1, 1)

        self.spinzr = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinzr.setObjectName(u"spinzr")
        self.spinzr.setMaximumSize(QSize(60, 16777215))
        self.spinzr.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinzr.setAlignment(Qt.AlignCenter)
        self.spinzr.setMaximum(0)

        self.gridLayout_12.addWidget(self.spinzr, 2, 3, 1, 1)

        self.spinjr = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinjr.setObjectName(u"spinjr")
        self.spinjr.setMaximumSize(QSize(60, 16777215))
        self.spinjr.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinjr.setAlignment(Qt.AlignCenter)
        self.spinjr.setMaximum(21)

        self.gridLayout_12.addWidget(self.spinjr, 8, 1, 1, 1)

        self.spinnrg = QSpinBox(self.scrollAreaWidgetContents_10)
        self.spinnrg.setObjectName(u"spinnrg")
        self.spinnrg.setMaximumSize(QSize(60, 16777215))
        self.spinnrg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinnrg.setAlignment(Qt.AlignCenter)
        self.spinnrg.setMaximum(49)

        self.gridLayout_12.addWidget(self.spinnrg, 2, 5, 1, 1)

        self.label_161 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_161.setObjectName(u"label_161")

        self.gridLayout_12.addWidget(self.label_161, 7, 3, 1, 1)

        self.btn_rjq = QPushButton(self.scrollAreaWidgetContents_10)
        self.btn_rjq.setObjectName(u"btn_rjq")
        self.btn_rjq.setMinimumSize(QSize(100, 25))
        self.btn_rjq.setMaximumSize(QSize(100, 25))
        self.btn_rjq.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.btn_rjq, 0, 5, 1, 1)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_12.addWidget(self.scrollArea_10)

        self.stackedWidget.addWidget(self.roujiaqin)
        self.tezhipin = QWidget()
        self.tezhipin.setObjectName(u"tezhipin")
        self.horizontalLayout_11 = QHBoxLayout(self.tezhipin)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.scrollArea_12 = QScrollArea(self.tezhipin)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 903, 716))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_202 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setMinimumSize(QSize(150, 150))
        self.label_202.setMaximumSize(QSize(150, 150))
        self.label_202.setPixmap(QPixmap(u":/images/images/images/70_\u8170\u679c.png"))

        self.gridLayout_14.addWidget(self.label_202, 4, 4, 1, 1)

        self.spinkxg = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spinkxg.setObjectName(u"spinkxg")
        self.spinkxg.setMaximumSize(QSize(60, 16777215))
        self.spinkxg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinkxg.setAlignment(Qt.AlignCenter)
        self.spinkxg.setMaximum(60)

        self.gridLayout_14.addWidget(self.spinkxg, 5, 1, 1, 1)

        self.label_197 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setMinimumSize(QSize(150, 150))
        self.label_197.setMaximumSize(QSize(150, 150))
        self.label_197.setPixmap(QPixmap(u":/images/images/images/71_\u6838\u6843.png"))

        self.gridLayout_14.addWidget(self.label_197, 7, 0, 1, 1)

        self.spinxr = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spinxr.setObjectName(u"spinxr")
        self.spinxr.setMaximumSize(QSize(60, 16777215))
        self.spinxr.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinxr.setAlignment(Qt.AlignCenter)
        self.spinxr.setMaximum(40)

        self.gridLayout_14.addWidget(self.spinxr, 2, 3, 1, 1)

        self.label_198 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMinimumSize(QSize(135, 0))
        self.label_198.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_198, 7, 1, 1, 1)

        self.label_193 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setMinimumSize(QSize(135, 0))
        self.label_193.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_193, 1, 1, 1, 1)

        self.spinbg_2 = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spinbg_2.setObjectName(u"spinbg_2")
        self.spinbg_2.setMaximumSize(QSize(60, 16777215))
        self.spinbg_2.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinbg_2.setAlignment(Qt.AlignCenter)
        self.spinbg_2.setMaximum(50)

        self.gridLayout_14.addWidget(self.spinbg_2, 2, 5, 1, 1)

        self.spingz = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spingz.setObjectName(u"spingz")
        self.spingz.setMaximumSize(QSize(60, 16777215))
        self.spingz.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spingz.setAlignment(Qt.AlignCenter)
        self.spingz.setMaximum(80)

        self.gridLayout_14.addWidget(self.spingz, 5, 3, 1, 1)

        self.label_203 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMinimumSize(QSize(135, 0))
        self.label_203.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_203, 1, 5, 1, 1)

        self.label_205 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setMinimumSize(QSize(0, 50))
        self.label_205.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_14.addWidget(self.label_205, 3, 1, 1, 1)

        self.label_200 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMinimumSize(QSize(135, 0))
        self.label_200.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_200, 1, 3, 1, 1)

        self.label_191 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setMinimumSize(QSize(150, 150))
        self.label_191.setMaximumSize(QSize(150, 150))
        self.label_191.setPixmap(QPixmap(u":/images/images/images/21_\u82b1\u751f.png"))

        self.gridLayout_14.addWidget(self.label_191, 1, 0, 1, 1)

        self.label_199 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMinimumSize(QSize(135, 0))
        self.label_199.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_199, 4, 3, 1, 1)

        self.label_206 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setMinimumSize(QSize(0, 50))
        self.label_206.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_14.addWidget(self.label_206, 6, 1, 1, 1)

        self.label_204 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setMinimumSize(QSize(135, 0))
        self.label_204.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_204, 4, 5, 1, 1)

        self.label_192 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setMinimumSize(QSize(150, 150))
        self.label_192.setMaximumSize(QSize(150, 150))
        self.label_192.setPixmap(QPixmap(u":/images/images/images/68_\u5f00\u5fc3\u679c.png"))

        self.gridLayout_14.addWidget(self.label_192, 4, 0, 1, 1)

        self.label_196 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setMinimumSize(QSize(150, 150))
        self.label_196.setMaximumSize(QSize(150, 150))
        self.label_196.setPixmap(QPixmap(u":/images/images/images/69_\u74dc\u5b50.png"))

        self.gridLayout_14.addWidget(self.label_196, 4, 2, 1, 1)

        self.label_201 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMinimumSize(QSize(150, 150))
        self.label_201.setMaximumSize(QSize(150, 150))
        self.label_201.setPixmap(QPixmap(u":/images/images/images/67_\u767d\u679c.png"))

        self.gridLayout_14.addWidget(self.label_201, 1, 4, 1, 1)

        self.label_195 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setMinimumSize(QSize(150, 150))
        self.label_195.setMaximumSize(QSize(150, 150))
        self.label_195.setPixmap(QPixmap(u":/images/images/images/66_\u674f\u4ec1.png"))

        self.gridLayout_14.addWidget(self.label_195, 1, 2, 1, 1)

        self.spinht = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spinht.setObjectName(u"spinht")
        self.spinht.setMaximumSize(QSize(60, 16777215))
        self.spinht.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinht.setAlignment(Qt.AlignCenter)
        self.spinht.setMaximum(20)

        self.gridLayout_14.addWidget(self.spinht, 8, 1, 1, 1)

        self.spinhs_2 = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spinhs_2.setObjectName(u"spinhs_2")
        self.spinhs_2.setMaximumSize(QSize(60, 16777215))
        self.spinhs_2.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinhs_2.setAlignment(Qt.AlignCenter)
        self.spinhs_2.setMaximum(3)

        self.gridLayout_14.addWidget(self.spinhs_2, 2, 1, 1, 1)

        self.spinyg = QSpinBox(self.scrollAreaWidgetContents_12)
        self.spinyg.setObjectName(u"spinyg")
        self.spinyg.setMaximumSize(QSize(60, 16777215))
        self.spinyg.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinyg.setAlignment(Qt.AlignCenter)
        self.spinyg.setMaximum(70)

        self.gridLayout_14.addWidget(self.spinyg, 5, 5, 1, 1)

        self.label_194 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setMinimumSize(QSize(135, 0))
        self.label_194.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_14.addWidget(self.label_194, 4, 1, 1, 1)

        self.btn_tzp = QPushButton(self.scrollAreaWidgetContents_12)
        self.btn_tzp.setObjectName(u"btn_tzp")
        self.btn_tzp.setMinimumSize(QSize(100, 25))
        self.btn_tzp.setMaximumSize(QSize(100, 25))
        self.btn_tzp.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.btn_tzp, 0, 5, 1, 1)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)

        self.horizontalLayout_11.addWidget(self.scrollArea_12)

        self.stackedWidget.addWidget(self.tezhipin)
        self.yinliao = QWidget()
        self.yinliao.setObjectName(u"yinliao")
        self.horizontalLayout_8 = QHBoxLayout(self.yinliao)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_5 = QScrollArea(self.yinliao)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 903, 716))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_38 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(135, 0))
        self.label_38.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_38, 1, 7, 1, 1)

        self.label_111 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(135, 0))
        self.label_111.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_111, 7, 7, 1, 1)

        self.label_58 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(135, 0))
        self.label_58.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_58, 4, 7, 1, 1)

        self.label_110 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(150, 150))
        self.label_110.setMaximumSize(QSize(150, 150))
        self.label_110.setPixmap(QPixmap(u":/images/images/images/2_\u725b\u5976.png"))

        self.gridLayout_7.addWidget(self.label_110, 7, 6, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 50))
        self.label_60.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_7.addWidget(self.label_60, 3, 1, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(135, 0))
        self.label_42.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_42, 4, 4, 1, 1)

        self.label_62 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setPixmap(QPixmap(u":/images/images/images/43_\u67f3\u6a59\u6c41.png"))

        self.gridLayout_7.addWidget(self.label_62, 7, 3, 1, 1)

        self.spinlc = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinlc.setObjectName(u"spinlc")
        self.spinlc.setMaximumSize(QSize(60, 16777215))
        self.spinlc.setBaseSize(QSize(0, 0))
        self.spinlc.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinlc.setAlignment(Qt.AlignCenter)
        self.spinlc.setMaximum(20)

        self.gridLayout_7.addWidget(self.spinlc, 5, 7, 1, 1)

        self.spinsc = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinsc.setObjectName(u"spinsc")
        self.spinsc.setMinimumSize(QSize(0, 0))
        self.spinsc.setMaximumSize(QSize(60, 16777215))
        self.spinsc.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinsc.setAlignment(Qt.AlignCenter)
        self.spinsc.setMaximum(17)

        self.gridLayout_7.addWidget(self.spinsc, 2, 4, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(150, 150))
        self.label_59.setMaximumSize(QSize(150, 150))
        self.label_59.setPixmap(QPixmap(u":/images/images/images/39_\u8fd0\u52a8\u996e\u6599.png"))

        self.gridLayout_7.addWidget(self.label_59, 7, 0, 1, 1)

        self.spinpgz = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinpgz.setObjectName(u"spinpgz")
        self.spinpgz.setMaximumSize(QSize(60, 16777215))
        self.spinpgz.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinpgz.setAlignment(Qt.AlignCenter)
        self.spinpgz.setMaximum(39)

        self.gridLayout_7.addWidget(self.spinpgz, 2, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 150))
        self.label.setMaximumSize(QSize(150, 150))
        self.label.setPixmap(QPixmap(u":/images/images/images/1_\u82f9\u679c\u6c41.png"))

        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)

        self.spinlcz = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinlcz.setObjectName(u"spinlcz")
        self.spinlcz.setMaximumSize(QSize(60, 16777215))
        self.spinlcz.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinlcz.setAlignment(Qt.AlignCenter)
        self.spinlcz.setMaximum(69)

        self.gridLayout_7.addWidget(self.spinlcz, 8, 4, 1, 1)

        self.spinmtz = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinmtz.setObjectName(u"spinmtz")
        self.spinmtz.setMaximumSize(QSize(60, 16777215))
        self.spinmtz.setBaseSize(QSize(0, 0))
        self.spinmtz.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinmtz.setAlignment(Qt.AlignCenter)
        self.spinmtz.setMaximum(111)

        self.gridLayout_7.addWidget(self.spinmtz, 5, 4, 1, 1)

        self.label_64 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 50))
        self.label_64.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_7.addWidget(self.label_64, 6, 1, 1, 1)

        self.spinqs = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinqs.setObjectName(u"spinqs")
        self.spinqs.setMaximumSize(QSize(60, 16777215))
        self.spinqs.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinqs.setAlignment(Qt.AlignCenter)
        self.spinqs.setMaximum(35)

        self.gridLayout_7.addWidget(self.spinqs, 2, 7, 1, 1)

        self.label_57 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(150, 150))
        self.label_57.setMaximumSize(QSize(150, 150))
        self.label_57.setPixmap(QPixmap(u":/images/images/images/38_\u7eff\u8336.png"))

        self.gridLayout_7.addWidget(self.label_57, 4, 6, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(150, 150))
        self.label_41.setMaximumSize(QSize(150, 150))
        self.label_41.setPixmap(QPixmap(u":/images/images/images/35_\u871c\u6843\u6c41.png"))

        self.gridLayout_7.addWidget(self.label_41, 4, 3, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(135, 0))
        self.label_40.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_40, 4, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(135, 0))
        self.label_9.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_9, 1, 1, 1, 1)

        self.spinpj = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinpj.setObjectName(u"spinpj")
        self.spinpj.setMaximumSize(QSize(60, 16777215))
        self.spinpj.setBaseSize(QSize(0, 0))
        self.spinpj.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinpj.setAlignment(Qt.AlignCenter)
        self.spinpj.setMaximum(20)

        self.gridLayout_7.addWidget(self.spinpj, 5, 1, 1, 1)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(150, 150))
        self.label_39.setMaximumSize(QSize(150, 150))
        self.label_39.setPixmap(QPixmap(u":/images/images/images/34_\u5564\u9152.png"))

        self.gridLayout_7.addWidget(self.label_39, 4, 0, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(150, 150))
        self.label_18.setMaximumSize(QSize(150, 150))
        self.label_18.setPixmap(QPixmap(u":/images/images/images/14_\u6c99\u8336.png"))

        self.gridLayout_7.addWidget(self.label_18, 1, 3, 1, 1)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(135, 0))
        self.label_34.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_34, 1, 4, 1, 1)

        self.label_61 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(135, 0))
        self.label_61.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_61, 7, 1, 1, 1)

        self.spinnn = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinnn.setObjectName(u"spinnn")
        self.spinnn.setMaximumSize(QSize(60, 16777215))
        self.spinnn.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinnn.setAlignment(Qt.AlignCenter)
        self.spinnn.setMaximum(17)

        self.gridLayout_7.addWidget(self.spinnn, 8, 7, 1, 1)

        self.label_63 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(135, 0))
        self.label_63.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_7.addWidget(self.label_63, 7, 4, 1, 1)

        self.spinydyl = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinydyl.setObjectName(u"spinydyl")
        self.spinydyl.setMaximumSize(QSize(60, 16777215))
        self.spinydyl.setStyleSheet(u"QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);;\n"
"    width: 12px;\n"
"    height: 20px;\n"
"}\n"
"/*\u6309\u94ae\u6309\u4e0b\u6837\u5f0f*/\n"
"QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"image: url(:/icons/images/icons/cil-plus.png);\n"
"    width: 12px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"image: url(:/icons/images/icons/cil-minus.png);\n"
"    width: "
                        "12px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"")
        self.spinydyl.setAlignment(Qt.AlignCenter)
        self.spinydyl.setMaximum(17)

        self.gridLayout_7.addWidget(self.spinydyl, 8, 1, 1, 1)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(150, 150))
        self.label_37.setMaximumSize(QSize(150, 150))
        self.label_37.setPixmap(QPixmap(u":/images/images/images/24_\u6c7d\u6c34.png"))

        self.gridLayout_7.addWidget(self.label_37, 1, 6, 1, 1)

        self.btn_yl = QPushButton(self.scrollAreaWidgetContents_5)
        self.btn_yl.setObjectName(u"btn_yl")
        self.btn_yl.setMinimumSize(QSize(100, 25))
        self.btn_yl.setMaximumSize(QSize(100, 25))
        self.btn_yl.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.btn_yl, 0, 7, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_8.addWidget(self.scrollArea_5)

        self.stackedWidget.addWidget(self.yinliao)
        self.cart = QWidget()
        self.cart.setObjectName(u"cart")
        self.cart.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.cart)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_submit = QPushButton(self.cart)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(60, 0))
        self.btn_submit.setMaximumSize(QSize(60, 16777215))
        self.btn_submit.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_submit, 0, Qt.AlignRight)

        self.scrollArea_13 = QScrollArea(self.cart)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 872, 437))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_211 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setMinimumSize(QSize(0, 40))
        self.label_211.setMaximumSize(QSize(16777215, 40))
        self.label_211.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.label_211.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_211, 0, 3, 1, 1)

        self.label_213 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_213.setObjectName(u"label_213")

        self.gridLayout_15.addWidget(self.label_213, 0, 5, 1, 1)

        self.label_216 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setMinimumSize(QSize(0, 40))
        self.label_216.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_216, 3, 0, 1, 1)

        self.label_215 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setMinimumSize(QSize(0, 40))
        self.label_215.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_215, 2, 0, 1, 1)

        self.label_210 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setMinimumSize(QSize(0, 40))
        self.label_210.setMaximumSize(QSize(16777215, 40))
        self.label_210.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.label_210.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_210, 0, 2, 1, 1)

        self.label_220 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setMinimumSize(QSize(0, 40))
        self.label_220.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_220, 7, 0, 1, 1)

        self.label_212 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_212.setObjectName(u"label_212")

        self.gridLayout_15.addWidget(self.label_212, 0, 4, 1, 1)

        self.label_214 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setMinimumSize(QSize(0, 40))
        self.label_214.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_214, 1, 0, 1, 1)

        self.label_218 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setMinimumSize(QSize(0, 40))
        self.label_218.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_218, 5, 0, 1, 1)

        self.label_209 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_15.addWidget(self.label_209, 0, 1, 1, 1)

        self.label_217 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setMinimumSize(QSize(0, 40))
        self.label_217.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_217, 4, 0, 1, 1)

        self.label_221 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setMinimumSize(QSize(0, 40))
        self.label_221.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_221, 8, 0, 1, 1)

        self.label_219 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setMinimumSize(QSize(0, 40))
        self.label_219.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_15.addWidget(self.label_219, 6, 0, 1, 1)

        self.label_208 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setMinimumSize(QSize(0, 40))
        self.label_208.setMaximumSize(QSize(16777215, 40))
        self.label_208.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.label_208.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_208, 0, 0, 1, 1)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout.addWidget(self.scrollArea_13)

        self.stackedWidget.addWidget(self.cart)
        self.order = QWidget()
        self.order.setObjectName(u"order")
        self.verticalLayout_20 = QVBoxLayout(self.order)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea_4 = QScrollArea(self.order)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 872, 465))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_227 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setMinimumSize(QSize(0, 40))
        self.label_227.setMaximumSize(QSize(16777215, 40))
        self.label_227.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.label_227.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_227, 0, 1, 1, 1)

        self.label_225 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setMinimumSize(QSize(0, 40))
        self.label_225.setMaximumSize(QSize(16777215, 40))
        self.label_225.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.label_225.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_225, 0, 3, 1, 1)

        self.label_233 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setMinimumSize(QSize(0, 40))
        self.label_233.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_233, 3, 0, 1, 1)

        self.label_222 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setMinimumSize(QSize(0, 40))
        self.label_222.setMaximumSize(QSize(100, 40))

        self.gridLayout_2.addWidget(self.label_222, 0, 0, 1, 1)

        self.label_232 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setMinimumSize(QSize(0, 40))
        self.label_232.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_232, 2, 0, 1, 1)

        self.label_236 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setMinimumSize(QSize(0, 40))
        self.label_236.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_236, 6, 0, 1, 1)

        self.label_234 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setMinimumSize(QSize(0, 40))
        self.label_234.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_234, 4, 0, 1, 1)

        self.label_231 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setMinimumSize(QSize(0, 40))
        self.label_231.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_231, 1, 0, 1, 1)

        self.label_238 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setMinimumSize(QSize(0, 40))
        self.label_238.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_238, 8, 0, 1, 1)

        self.label_224 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setMinimumSize(QSize(0, 40))
        self.label_224.setMaximumSize(QSize(16777215, 40))
        self.label_224.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.label_224.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_224, 0, 2, 1, 1)

        self.label_235 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setMinimumSize(QSize(0, 40))
        self.label_235.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_235, 5, 0, 1, 1)

        self.label_229 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setMaximumSize(QSize(16777215, 0))

        self.gridLayout_2.addWidget(self.label_229, 0, 4, 1, 1)

        self.label_237 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setMinimumSize(QSize(0, 40))
        self.label_237.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_237, 7, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_20.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.order)
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.welcome.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.welcome)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_27 = QLabel(self.welcome)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_5.addWidget(self.label_27)

        self.label_24 = QLabel(self.welcome)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Times New Roman\";\n"
"	font: 25pt\n"
"}")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_24)

        self.label_28 = QLabel(self.welcome)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_5.addWidget(self.label_28)

        self.label_25 = QLabel(self.welcome)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Times New Roman\";\n"
"	font: 18pt\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_25)

        self.label_26 = QLabel(self.welcome)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_5.addWidget(self.label_26)

        self.label_29 = QLabel(self.welcome)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_5.addWidget(self.label_29)

        self.stackedWidget.addWidget(self.welcome)
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.gridLayout_3 = QGridLayout(self.loginpage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.scrollArea_3 = QScrollArea(self.loginpage)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 568, 805))
        self.scrollAreaWidgetContents_3.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, -1, -1, 9)
        self.label_47 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_47, 10, 2, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_55.setObjectName(u"label_55")
        sizePolicy2.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy2)
        self.label_55.setMinimumSize(QSize(95, 0))

        self.gridLayout_5.addWidget(self.label_55, 1, 3, 1, 1)

        self.linecity = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linecity.setObjectName(u"linecity")
        self.linecity.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linecity, 11, 2, 1, 1)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setMinimumSize(QSize(95, 0))
        self.label_56.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.label_56, 1, 0, 1, 1)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_44, 4, 2, 1, 1)

        self.label_51 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_51, 18, 2, 1, 1)

        self.label_53 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_53, 22, 2, 1, 1)

        self.label_52 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_52, 20, 2, 1, 1)

        self.lineaddress = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineaddress.setObjectName(u"lineaddress")
        self.lineaddress.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lineaddress, 9, 2, 1, 1)

        self.linephone = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linephone.setObjectName(u"linephone")
        self.linephone.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linephone, 19, 2, 1, 1)

        self.Surebtn = QPushButton(self.scrollAreaWidgetContents_3)
        self.Surebtn.setObjectName(u"Surebtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Surebtn.sizePolicy().hasHeightForWidth())
        self.Surebtn.setSizePolicy(sizePolicy5)
        self.Surebtn.setMinimumSize(QSize(200, 0))
        self.Surebtn.setMaximumSize(QSize(200, 16777215))
        self.Surebtn.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);}\n"
"")

        self.gridLayout_5.addWidget(self.Surebtn, 27, 2, 1, 1, Qt.AlignHCenter)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_46, 8, 2, 1, 1)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_5.addWidget(self.label_43, 26, 2, 1, 1)

        self.linename = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linename.setObjectName(u"linename")
        sizePolicy.setHeightForWidth(self.linename.sizePolicy().hasHeightForWidth())
        self.linename.setSizePolicy(sizePolicy)
        self.linename.setMinimumSize(QSize(0, 0))
        self.linename.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linename, 3, 2, 1, 1)

        self.lineposition = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineposition.setObjectName(u"lineposition")
        sizePolicy.setHeightForWidth(self.lineposition.sizePolicy().hasHeightForWidth())
        self.lineposition.setSizePolicy(sizePolicy)
        self.lineposition.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lineposition, 5, 2, 1, 1)

        self.linecompany = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linecompany.setObjectName(u"linecompany")
        self.linecompany.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linecompany, 7, 2, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_48, 12, 2, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_30, 2, 2, 1, 1)

        self.linepostalcode = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linepostalcode.setObjectName(u"linepostalcode")
        self.linepostalcode.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linepostalcode, 15, 2, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_31.setObjectName(u"label_31")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy6)
        self.label_31.setMinimumSize(QSize(0, 100))
        self.label_31.setMaximumSize(QSize(16777215, 100))
        self.label_31.setStyleSheet(u"QLabel{\n"
"	font: 700 18pt \"Times New Roman\";\n"
"	font: 35pt\n"
"}")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_31, 1, 2, 1, 1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_49, 14, 2, 1, 1)

        self.label_50 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_50, 16, 2, 1, 1)

        self.lineregion = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineregion.setObjectName(u"lineregion")
        self.lineregion.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lineregion, 13, 2, 1, 1)

        self.linepassword = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linepassword.setObjectName(u"linepassword")
        self.linepassword.setMaximumSize(QSize(16777215, 16777215))
        self.linepassword.setStyleSheet(u"")
        self.linepassword.setFrame(True)
        self.linepassword.setEchoMode(QLineEdit.Password)
        self.linepassword.setDragEnabled(False)
        self.linepassword.setReadOnly(False)
        self.linepassword.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_5.addWidget(self.linepassword, 23, 2, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_45, 6, 2, 1, 1)

        self.lineensure = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineensure.setObjectName(u"lineensure")
        sizePolicy.setHeightForWidth(self.lineensure.sizePolicy().hasHeightForWidth())
        self.lineensure.setSizePolicy(sizePolicy)
        self.lineensure.setMaximumSize(QSize(16777215, 16777215))
        self.lineensure.setEchoMode(QLineEdit.Password)

        self.gridLayout_5.addWidget(self.lineensure, 25, 2, 1, 1)

        self.linefax = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linefax.setObjectName(u"linefax")
        self.linefax.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linefax, 21, 2, 1, 1)

        self.linecountry = QLineEdit(self.scrollAreaWidgetContents_3)
        self.linecountry.setObjectName(u"linecountry")
        self.linecountry.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.linecountry, 17, 2, 1, 1)

        self.label_54 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_54, 24, 2, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.loginpage)
        self.logonpage = QWidget()
        self.logonpage.setObjectName(u"logonpage")
        self.horizontalLayout_7 = QHBoxLayout(self.logonpage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea = QScrollArea(self.logonpage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 730, 284))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 8, 2, 1, 1)

        self.linePassword = QLineEdit(self.scrollAreaWidgetContents)
        self.linePassword.setObjectName(u"linePassword")
        self.linePassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.linePassword, 5, 2, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout.addWidget(self.label_36, 4, 2, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 9, 2, 1, 1)

        self.surebtn = QPushButton(self.scrollAreaWidgetContents)
        self.surebtn.setObjectName(u"surebtn")
        self.surebtn.setMinimumSize(QSize(200, 0))
        self.surebtn.setMaximumSize(QSize(200, 16777215))
        self.surebtn.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(155, 155, 155);}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);}\n"
"")

        self.gridLayout.addWidget(self.surebtn, 6, 2, 2, 1, Qt.AlignHCenter)

        self.linePhone = QLineEdit(self.scrollAreaWidgetContents)
        self.linePhone.setObjectName(u"linePhone")
        self.linePhone.setFrame(True)
        self.linePhone.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.linePhone, 3, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 11, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 10, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_35, 2, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_7.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.logonpage)

        self.gridLayout_6.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.topMenus)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_14.addWidget(self.label_22)

        self.btn_logon = QPushButton(self.topMenus)
        self.btn_logon.setObjectName(u"btn_logon")
        sizePolicy.setHeightForWidth(self.btn_logon.sizePolicy().hasHeightForWidth())
        self.btn_logon.setSizePolicy(sizePolicy)
        self.btn_logon.setMinimumSize(QSize(0, 45))
        self.btn_logon.setFont(font)
        self.btn_logon.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logon.setLayoutDirection(Qt.LeftToRight)
        self.btn_logon.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-plus.png);")

        self.verticalLayout_14.addWidget(self.btn_logon)

        self.label_21 = QLabel(self.topMenus)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_14.addWidget(self.label_21)

        self.btn_login = QPushButton(self.topMenus)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_login.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-follow.png);")

        self.verticalLayout_14.addWidget(self.btn_login)

        self.label_23 = QLabel(self.topMenus)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_14.addWidget(self.label_23)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Times New Roman\";\n"
"	font: 10pt\n"
"}")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Times New Roman\";\n"
"	font: 10pt\n"
"}")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"user_name", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"user_ID", None))
        self.settingsTopBtn.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.label_20.setText("")
        self.btn_category.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_14.setText("")
        self.btn_cart.setText(QCoreApplication.translate("MainWindow", u"Shopping Cart", None))
        self.label_19.setText("")
        self.btn_order.setText(QCoreApplication.translate("MainWindow", u"Historical Order", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Database  Course  Design", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u5473\u54c1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6d77\u9c9c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u5fc3", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u996e\u6599", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8089/\u5bb6\u79bd", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5236\u54c1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8c37\u7c7b/\u9ea6\u7247", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u7528\u54c1", None))
        self.btn_yinliao.setText("")
        self.btn_dianxin.setText("")
        self.btn_roujiaqin.setText("")
        self.btn_guleimaipian.setText("")
        self.btn_haixian.setText("")
        self.btn_riyongpin.setText("")
        self.btn_tiaoweipin.setText("")
        self.btn_tezhipin.setText("")
        self.label_91.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u70e4\u8089\u9171</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">45.60</span></p></body></html>", None))
        self.label_90.setText("")
        self.label_87.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u76d0</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">22.00</span></p></body></html>", None))
        self.label_77.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9ebb\u6cb9</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">21.35</span></p></body></html>", None))
        self.label_89.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u80e1\u6912\u7c89</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">40.00</span></p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6d77\u82d4\u9171</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">21.05</span></p></body></html>", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u869d\u6cb9</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">19.45</span></p></body></html>", None))
        self.label_69.setText("")
        self.label_67.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6d77\u9c9c\u7c89</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">30.00</span></p></body></html>", None))
        self.label_85.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6d77\u9c9c\u9171</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">28.50</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u751c\u8fa3\u9171</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">43.90</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u756a\u8304\u9171</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">10.00</span></p></body></html>", None))
        self.label_83.setText("")
        self.label_79.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9171\u6cb9</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">25.00</span></p></body></html>", None))
        self.label_75.setText("")
        self.label_81.setText("")
        self.label_73.setText("")
        self.label_71.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5473\u7cbe</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">15.50</span></p></body></html>", None))
        self.label_65.setText("")
        self.btn_twp.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5de7\u514b\u529b</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">14.00</span></p></body></html>", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5c71\u6942\u7247</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">49.30</span></p></body></html>", None))
        self.label_97.setText("")
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6842\u82b1\u7cd5</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">81.00</span></p></body></html>", None))
        self.label_164.setText("")
        self.label_95.setText("")
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u85af\u6761</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">20.00</span></p></body></html>", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u86cb\u7cd5</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u4e2a</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">9.50</span></p></body></html>", None))
        self.label_106.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u68c9\u82b1\u7cd6</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">31.23</span></p></body></html>", None))
        self.label_102.setText("")
        self.label_104.setText("")
        self.label_92.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u997c\u5e72</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">17.45</span></p></body></html>", None))
        self.label_94.setText("")
        self.label_100.setText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u7cd6\u679c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u76d2</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">9.20</span></p></body></html>", None))
        self.label_107.setText("")
        self.btn_dx.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_142.setText("")
        self.label_138.setText("")
        self.label_130.setText("")
        self.label_140.setText("")
        self.label_136.setText("")
        self.label_144.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5c0f\u7c73</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">19.50</span></p></body></html>", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u71d5\u9ea6</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">9.00</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u7cef\u7c73</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">21.00</span></p></body></html>", None))
        self.label_128.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u7389\u7c73\u7247</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">12.75</span></p></body></html>", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u767d\u7c73</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">38.00</span></p></body></html>", None))
        self.label_134.setText("")
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u4e09\u5408\u4e00\u9ea6\u7247</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">7.00</span></p></body></html>", None))
        self.label_145.setText("")
        self.label_126.setText("")
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9ec4\u8c46</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">33.25</span></p></body></html>", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u7389\u7c73\u997c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">16.25</span></p></body></html>", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u7cd9\u7c73</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">14.00</span></p></body></html>", None))
        self.label_132.setText("")
        self.btn_glmp.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_166.setText("")
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9cd5\u9c7c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">9.5</span></p></body></html>", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6d77\u53c2</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">13.25</span></p></body></html>", None))
        self.label_176.setText("")
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u867e\u7c73</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">18.40</span></p></body></html>", None))
        self.label_174.setText("")
        self.label_178.setText("")
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5e72\u8d1d</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">26.00</span></p></body></html>", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9f99\u867e</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b500\u514b</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">6.00</span></p></body></html>", None))
        self.label_170.setText("")
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u87f9</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b500\u514b</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">31.00</span></p></body></html>", None))
        self.label_186.setText("")
        self.label_180.setText("")
        self.label_172.setText("")
        self.label_168.setText("")
        self.label_190.setText("")
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u86b5</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">12.00</span></p></body></html>", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9c7f\u9c7c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">19.00</span></p></body></html>", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u867e\u5b50</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">9.65</span></p></body></html>", None))
        self.label_182.setText("")
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u58a8\u9c7c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b500\u514b</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">62.50</span></p></body></html>", None))
        self.label_189.setText("")
        self.label_188.setText("")
        self.label_185.setText("")
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9ec4\u9c7c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">25.89</span></p></body></html>", None))
        self.btn_hx.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5fb7\u56fd\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">38.00</span></p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u82b1\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">34.00</span></p></body></html>", None))
        self.label_122.setText("")
        self.label_120.setText("")
        self.label_123.setText("")
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5927\u4f17\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b6\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">21.00</span></p></body></html>", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6e29\u99a8\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">12.50</span></p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u767d\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">32.00</span></p></body></html>", None))
        self.label_114.setText("")
        self.label_118.setText("")
        self.label_112.setText("")
        self.label_124.setText("")
        self.label_116.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5149\u660e\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">55.00</span></p></body></html>", None))
        self.label_108.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6d6a\u82b1\u5976\u916a</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">2.50</span></p></body></html>", None))
        self.btn_ryp.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9e21\u8089</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">7.45</span></p></body></html>", None))
        self.label_160.setText("")
        self.label_157.setText("")
        self.label_162.setText("")
        self.label_158.setText("")
        self.label_163.setText("")
        self.label_146.setText("")
        self.label_151.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u732a\u8089\u5e72</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">53.00</span></p></body></html>", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u732a\u8089</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b500\u514b</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">39.00</span></p></body></html>", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u725b\u8089\u5e72</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">43.90</span></p></body></html>", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9e2d\u8089</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">123.79</span></p></body></html>", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u76d0\u6c34\u9e2d</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">32.80</span></p></body></html>", None))
        self.label_154.setText("")
        self.label_148.setText("")
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9e21</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b500\u514b</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">97.00</span></p></body></html>", None))
        self.label_152.setText("")
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u9e2d\u8089</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">24.00</span></p></body></html>", None))
        self.btn_rjq.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_202.setText("")
        self.label_197.setText("")
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6838\u6843</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b5\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">100.00</span></p></body></html>", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u82b1\u751f</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb130\u5305</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">10.00</span></p></body></html>", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u767d\u679c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b3\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">40.00</span></p></body></html>", None))
        self.label_205.setText("")
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u674f\u4ec1</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b1\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">18.00</span></p></body></html>", None))
        self.label_191.setText("")
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u74dc\u5b50</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u53055\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">30.00</span></p></body></html>", None))
        self.label_206.setText("")
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u8170\u679c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b1\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">30.00</span></p></body></html>", None))
        self.label_192.setText("")
        self.label_196.setText("")
        self.label_201.setText("")
        self.label_195.setText("")
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5f00\u5fc3\u679c</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u888b1\u516c\u65a4</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">10.00</span></p></body></html>", None))
        self.btn_tzp.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6c7d\u6c34</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">4.50</span></p></body></html>", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u725b\u5976</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">19.00</span></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u7eff\u8336</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">263.50</span></p></body></html>", None))
        self.label_110.setText("")
        self.label_60.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u871c\u6843\u6c41</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">18.00</span></p></body></html>", None))
        self.label_62.setText("")
        self.label_59.setText("")
        self.label.setText("")
        self.label_64.setText("")
        self.label_57.setText("")
        self.label_41.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u5564\u9152</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">14.00</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u82f9\u679c\u6c41</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">18.00</span></p></body></html>", None))
        self.label_39.setText("")
        self.label_18.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u6c99\u8336</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb112\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">23.25</span></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u8fd0\u52a8\u996e\u6599</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">18.00</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#c5c5c5;\">\u67f3\u6a59\u6c41</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6bcf\u7bb124\u74f6</span><br/></p><p><span style=\" color:#ff0000;\">\uffe5 </span><span style=\" font-size:20pt; color:#ff0000;\">46.00</span></p></body></html>", None))
        self.label_37.setText("")
        self.btn_yl.setText(QCoreApplication.translate("MainWindow", u"add to cart", None))
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", u"submit", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_213.setText("")
        self.label_216.setText("")
        self.label_215.setText("")
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Trade name", None))
        self.label_220.setText("")
        self.label_212.setText("")
        self.label_214.setText("")
        self.label_218.setText("")
        self.label_209.setText("")
        self.label_217.setText("")
        self.label_221.setText("")
        self.label_219.setText("")
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Cart Detail", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Order ID", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Delivery time", None))
        self.label_233.setText("")
        self.label_222.setText("")
        self.label_232.setText("")
        self.label_236.setText("")
        self.label_234.setText("")
        self.label_231.setText("")
        self.label_238.setText("")
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"Order time", None))
        self.label_235.setText("")
        self.label_229.setText("")
        self.label_237.setText("")
        self.label_27.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Welcome to our client software", None))
        self.label_28.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Click on the button in the upper left corner to log in/log on", None))
        self.label_26.setText("")
        self.label_29.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"city :", None))
        self.label_55.setText("")
        self.linecity.setText("")
        self.linecity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the city", None))
        self.label_56.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"position :", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"phone number :", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"password :", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"fax :", None))
        self.lineaddress.setText("")
        self.lineaddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the address", None))
        self.linephone.setText("")
        self.linephone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your phone number", None))
        self.Surebtn.setText(QCoreApplication.translate("MainWindow", u"Sure", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"address :", None))
        self.label_43.setText("")
        self.linename.setText("")
        self.linename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your name", None))
        self.lineposition.setText("")
        self.lineposition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your position", None))
        self.linecompany.setText("")
        self.linecompany.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your company name", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"region :", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"name :", None))
        self.linepostalcode.setText("")
        self.linepostalcode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the postal code", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u" Welcome to us \uff01", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"postal code :", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"country :", None))
        self.lineregion.setText("")
        self.lineregion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the region", None))
        self.linepassword.setInputMask("")
        self.linepassword.setText("")
        self.linepassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your password", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"company name :", None))
        self.lineensure.setText("")
        self.lineensure.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your password again", None))
        self.linefax.setText("")
        self.linefax.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the fax", None))
        self.linecountry.setText("")
        self.linecountry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the country", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"ensure :", None))
        self.label_33.setText("")
        self.linePassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your password", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"password :", None))
        self.label_32.setText("")
        self.surebtn.setText(QCoreApplication.translate("MainWindow", u"Sure", None))
        self.linePhone.setInputMask("")
        self.linePhone.setText("")
        self.linePhone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your phone number", None))
        self.label_3.setText("")
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_4.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"phone number :", None))
        self.label_8.setText("")
        self.label_2.setText("")
        self.label_22.setText("")
        self.btn_logon.setText(QCoreApplication.translate("MainWindow", u"Logon", None))
        self.label_21.setText("")
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_23.setText("")
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By : Group 21    Zhang Sa-ru  &  Ren Chen-wei  &  Li Ming-han", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Last update time : May 20, 2023", None))
    # retranslateUi

