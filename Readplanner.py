# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Readplanner.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(766, 600)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(570, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(577, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(590, 0, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(widget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 252, 541, 341))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(390, 220, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_7 = QtWidgets.QTextEdit(widget)
        self.textEdit_7.setGeometry(QtCore.QRect(290, 110, 251, 91))
        self.textEdit_7.setObjectName("textEdit_7")
        self.progressBar = QtWidgets.QProgressBar(widget)
        self.progressBar.setGeometry(QtCore.QRect(287, 30, 241, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(widget)
        self.line.setGeometry(QtCore.QRect(0, 30, 251, 16))
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(widget)
        self.label_5.setGeometry(QtCore.QRect(280, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_8 = QtWidgets.QTextEdit(widget)
        self.textEdit_8.setGeometry(QtCore.QRect(370, 10, 181, 21))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_6 = QtWidgets.QLabel(widget)
        self.label_6.setGeometry(QtCore.QRect(340, 50, 121, 16))
        self.label_6.setObjectName("label_6")
        self.line_3 = QtWidgets.QFrame(widget)
        self.line_3.setGeometry(QtCore.QRect(290, 70, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.line_3.setFont(font)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_7 = QtWidgets.QLabel(widget)
        self.label_7.setGeometry(QtCore.QRect(370, 90, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(widget)
        self.line_2.setGeometry(QtCore.QRect(240, 0, 16, 41))
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(widget)
        self.line_4.setGeometry(QtCore.QRect(554, 0, 16, 161))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.listWidget = QtWidgets.QListWidget(widget)
        self.listWidget.setGeometry(QtCore.QRect(560, 160, 231, 431))
        self.listWidget.setObjectName("listWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 49, 271, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(widget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 200, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(widget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(widget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(570, 70, 192, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")

        self.retranslateUi(widget)
        self.commandLinkButton.clicked.connect(widget.link1)
        self.listWidget.clicked['QModelIndex'].connect(widget.select)
        self.pushButton.clicked.connect(widget.del_note)
        self.pushButton_2.clicked.connect(widget.add_note)
        self.pushButton_3.clicked.connect(widget.boost)
        self.commandLinkButton_2.clicked.connect(widget.link2)
        self.calendarWidget.clicked['QDate'].connect(widget.calspecial)
        self.textEdit_7.textChanged.connect(widget.note_for_date)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.commandLinkButton.setText(_translate("widget", "сайт Gutenberg"))
        self.label.setText(_translate("widget", "Топ 100 книг Gutenberg"))
        self.label_2.setText(_translate("widget", "Перейти до читання"))
        self.label_3.setText(_translate("widget", "Календарик"))
        self.label_4.setText(_translate("widget", "Плани, замітки, челленджі"))
        self.label_5.setText(_translate("widget", "челлендж: "))
        self.label_6.setText(_translate("widget", "Степінь виконаня"))
        self.label_7.setText(_translate("widget", "Для заміток"))
        self.pushButton.setText(_translate("widget", "Видалити виконані"))
        self.pushButton_2.setText(_translate("widget", "Додати новий"))
        self.pushButton_3.setText(_translate("widget", "+"))
        self.commandLinkButton_2.setText(_translate("widget", "сайт Букнет"))
