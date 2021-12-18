from PyQt5 import QtWidgets
from ui.add_question import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import json

from PyQt5.Qt import QApplication, QClipboard, QFileDialog
from PyQt5.QtCore import QCoreApplication
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      
        #создаем словарь с будующими вопросами и правильными ответами
        #структура словаря {Вопрос_1:{ответ_1:false, ответ_2:true, ответ_3:false}, Вопрос_2:{ответ_1:true, ответ_2:false}}
        #ячеек под вопросы в программе 8, если ответов меньше, то их не будет в словаре 

        self.dict_question_and_answer ={}

        #создаем словарь с кнопкой вставки: текст
        self.dict_pushb_text = {self.ui.pushButton:self.ui.plainTextEdit, 
        self.ui.pushButton_2:self.ui.plainTextEdit_2,
        self.ui.pushButton_3:self.ui.plainTextEdit_3,
        self.ui.pushButton_4:self.ui.plainTextEdit_4,
        self.ui.pushButton_5:self.ui.plainTextEdit_5,
        self.ui.pushButton_6:self.ui.plainTextEdit_6,
        self.ui.pushButton_7:self.ui.plainTextEdit_7,
        self.ui.pushButton_8:self.ui.plainTextEdit_8}

        #создаем словарь вариант ответа(текст):кнопка выбора его как верный (checkbox)
        self.dict_text_checkb = {self.ui.plainTextEdit:self.ui.checkBox,
        self.ui.plainTextEdit_2:self.ui.checkBox_2,
        self.ui.plainTextEdit_3:self.ui.checkBox_3,
        self.ui.plainTextEdit_4:self.ui.checkBox_4,
        self.ui.plainTextEdit_5:self.ui.checkBox_5,
        self.ui.plainTextEdit_6:self.ui.checkBox_6,
        self.ui.plainTextEdit_7:self.ui.checkBox_7,
        self.ui.plainTextEdit_8:self.ui.checkBox_8}
        
        # Здесь прописываем событие нажатия на кнопку вставки текста     
        self.ui.pushButton.clicked.connect(self.ctrl_V)
        self.ui.pushButton_2.clicked.connect(self.ctrl_V)
        self.ui.pushButton_3.clicked.connect(self.ctrl_V)
        self.ui.pushButton_4.clicked.connect(self.ctrl_V)
        self.ui.pushButton_5.clicked.connect(self.ctrl_V)
        self.ui.pushButton_6.clicked.connect(self.ctrl_V)
        self.ui.pushButton_7.clicked.connect(self.ctrl_V)
        self.ui.pushButton_8.clicked.connect(self.ctrl_V)

        # сохранить и продолжить
        self.ui.pushButton_9.clicked.connect(self.saveForward)
        # сохранить и выйти, предложив как сохранить файл
        self.ui.pushButton_10.clicked.connect(self.saveFile)

        #self.ui.comboBox.currentIndexChanged.connect(self.ssssss)

    def ctrl_V(self):
        #получаем какая кнопка была нажата, используя метод sender
        sender = self.sender()
        #копируем содержимое буфера обмена
        past = QApplication.clipboard().text()
        #находим в какую ячейку надо вставить текст, используя словарь с кнопкой вставки: текст
        plain_text_edit = self.dict_pushb_text[sender]
        #добавляем текст в ячейку
        plain_text_edit.setPlainText(past)

    def saveForward(self):
        #получаем текст вопроса
        question = self.ui.plainTextEdit_9.toPlainText()
        #получаем ответы и помещаем в словарь
        answers = {}
        
        for answer_text in self.dict_text_checkb:
            #получаем нужный чекбокс
            check = self.dict_text_checkb[answer_text]
            #получаем выбран ли этот чекбокс
            x = check.isChecked()
            #присваевыем тексту ответа правильный он или нет true/false
            answers[answer_text.toPlainText()] = x
        
        #записываем вопрос и ответ в главный словарь dict_question_and_answer
        self.dict_question_and_answer[question] = answers

        #добавляем в comboBox вопрос для быстрой навигации
        #self.ui.comboBox.addItem(question[:15]) 
        #self.ui.comboBox.setCurrentText("Second item")

        #очистить все поля ввода и убрать выбранные ячейки
        self.ui.plainTextEdit_9.clear()
        for planText in self.dict_text_checkb:
            planText.clear()
            #убрать отметки выбранных ответов
            self.dict_text_checkb[planText].setChecked(False)

    #def ssssss(self):
    #    pass

    def saveFile(self):
        self.saveForward()
        #вызов диалогового окна для сохранения
        filename, format_file = QFileDialog.getSaveFileName(self,
                             "Сохранить файл",
                             ".",
                             "JSON files (*.json)")
        
        if filename: #проверяем задал ли пользователь имя для сохранения файла
            #запись данных в файл
            with open(filename+'.json', 'w') as outfile:
                json.dump(self.dict_question_and_answer, outfile)
            
            #закрываем приложение
            QCoreApplication.instance().quit()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())