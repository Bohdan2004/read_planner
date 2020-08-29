import json
import sys
import webbrowser

import requests
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QCheckBox, QWidget
from bs4 import BeautifulSoup

from Readplanner import *
from Readplanner import Ui_widget

app = QtWidgets.QApplication(sys.argv)
widget: QWidget = QtWidgets.QWidget()


def link1():
    webbrowser.open('https://www.gutenberg.org/')


def link2():
    webbrowser.open('https://booknet.com/uk')


def calspecial(date_v):
    s_date = str(date_v)
    with open('CDict.json') as fo_1:
        cdict = json.load(fo_1)
    for d_1, t_1 in cdict.items():
        if d_1 == s_date:
            ui.textEdit_7.setText(t_1)
            break
        else:
            ui.textEdit_7.setText('')


def note_for_date():
    with open('CDict.json') as fo_2:
        cdict = json.load(fo_2)

    s_date = str(ui.calendarWidget.selectedDate())
    cdict[s_date] = ui.textEdit_7.toPlainText()

    if ui.textEdit_7.toPlainText() == '':
        del cdict[s_date]

    with open('CDict.json', 'w') as fo_3:
        json.dump(cdict, fo_3)


widget.link1 = link1
widget.link2 = link2
widget.calspecial = calspecial
widget.note_for_date = note_for_date


def select(name):
    global books
    webbrowser.open(books[name.data()])


widget.select = select


def del_note():
    if ui.gridLayout.count() == 0:
        msg = QMessageBox()
        msg.setText('Виконаних планів нема')
        msg.setWindowTitle('Помилка')
        msg.setIcon(QMessageBox.Information)
        msg.exec()
        return
    n = 0
    while not ui.gridLayout.itemAtPosition(n, 1).widget().isChecked():
        n += 1
        if n == ui.gridLayout.count() // 2:
            msg = QMessageBox()
            msg.setText('Виконаних планів нема')
            msg.setWindowTitle('Помилка')
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            break
    for i in range(n, ui.gridLayout.count() // 2):
        ui.gridLayout.itemAtPosition(i, 0).widget().setParent(None)
        ui.gridLayout.itemAtPosition(i, 1).widget().setParent(None)


widget.del_note = del_note


def note_change():
    n = ui.gridLayout.count() // 2
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ui.gridLayout.itemAtPosition(j, 1).widget().isChecked():
                le = ui.gridLayout.itemAtPosition(j, 0)
                chb = ui.gridLayout.itemAtPosition(j, 1)
                ui.gridLayout.addWidget(ui.gridLayout.itemAtPosition(j + 1, 0).widget(), j, 0)
                ui.gridLayout.addWidget(ui.gridLayout.itemAtPosition(j + 1, 1).widget(), j, 1)
                ui.gridLayout.addWidget(le.widget(), j + 1, 0)
                ui.gridLayout.addWidget(chb.widget(), j + 1, 1)


def add_note():
    le = QLineEdit()
    chb = QCheckBox()
    chb.clicked.connect(note_change)
    if ui.gridLayout.count() < 10:
        chb.n = ui.gridLayout.count() // 2
        ui.gridLayout.addWidget(le, ui.gridLayout.count() // 2, 0)
        ui.gridLayout.addWidget(chb, ui.gridLayout.count() // 2, 1)
    else:
        ms = QMessageBox()
        ms.setText('Більше заміток не доступно')
        ms.setWindowTitle('Помилка')
        ms.setIcon(QMessageBox.Information)
        ms.exec()


widget.add_note = add_note


def boost():
    if ui.textEdit_8.toPlainText() != '':
        ui.progressBar.setValue(ui.progressBar.value() + 10)
        if ui.progressBar.value() >= 100:
            ui.progressBar.setValue(0)
            ui.textEdit_8.clear()
    else:
        msg = QMessageBox()
        msg.setText('Текст не введений')
        msg.setWindowTitle('Помилка')
        msg.setIcon(QMessageBox.Information)
        msg.exec()


widget.boost = boost

soup: BeautifulSoup = BeautifulSoup(requests.get('https://www.gutenberg.org/browse/scores/top').text, 'html.parser')
books: dict = {i.text: "https://www.gutenberg.org/" + BeautifulSoup(str(i), 'html.parser').find("a")["href"] for i in
               soup.findAll("ol")[4].findAll("li")}

ui: Ui_widget = Ui_widget()
ui.setupUi(widget)

for key in books:
    ui.listWidget.addItem(key)

with open('CDict.json') as fo:
    first_cdict = json.load(fo)

for d, t in first_cdict.items():
    if d == str(ui.calendarWidget.selectedDate()):
        ui.textEdit_7.setText(t)
        break

with open('Challenge.json', 'r') as fo_4:
    tmp = json.load(fo_4)

ui.textEdit_8.setText(tmp[0])
ui.progressBar.setValue(tmp[1])

widget.show()
sys.exit(app.exec_())
