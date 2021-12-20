from os import posix_fadvise
from PyQt5 import QtWidgets
from ui.exam import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import json
import random
from PyQt5.QtCore import QCoreApplication

 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        #словарь с вопросами и ответами
        self.dict_question_and_answer = {}
        
        #массив с пройденными вопросами
        self.question_passed =[]

        #загрузка файла с вопросами
        self.ui.pushButton_10.clicked.connect(self.loadFile)

        #создаем список текстовых окон под ответы
        self.answer_options  = [self.ui.textBrowser, self.ui.textBrowser_2, self.ui.textBrowser_3, self.ui.textBrowser_4,
        self.ui.textBrowser_5, self.ui.textBrowser_6, self.ui.textBrowser_7, self.ui.textBrowser_8]

        #создаем словарь {checkBox:правильный/неправильный вариант ответа} по умолчанию все неправильные
        self.check_answer = {self.ui.checkBox:False, self.ui.checkBox_2:False, self.ui.checkBox_3:False, self.ui.checkBox_4:False,
        self.ui.checkBox_5:False, self.ui.checkBox_6:False, self.ui.checkBox_7:False, self.ui.checkBox_8:False} 

        #Переменная для ф-ции show_question котороая изменяет ее поведение
        #в зависимости что сейчас отображется- правильные варианты ответов или 
        #экран для ввода ответа
        self.was_incorrect_answer = False
        self.ui.pushButton_9.clicked.connect(self.next_question)

        self.ui.progressBar.setValue(0)
        #подсчет количества ошибок
        self.num_errors = 0

    def loadFile(self):
        filename, format_file = QtWidgets.QFileDialog.getOpenFileName(self, 
                        'Открыть файл', 
                        './', 
                        'JSON files (*.json)')
        if filename:
            with open(filename) as json_file:
                self.dict_question_and_answer = json.load(json_file)
            #зададим progressBar максимальное значение
            self.ui.progressBar.setMaximum(len(self.dict_question_and_answer))
            self.show_question()

    def clean_all(self):
         # #очистить все поля ввода и убрать выбранные ячейки
        #убрать зеленую окраску границ 
        self.ui.textBrowser_9.clear()
        for textBrowser in self.answer_options:
            textBrowser.clear()
            textBrowser.setStyleSheet('')
        #убрать все поставленные галочки с вопросов
        clear_check_box = list(self.check_answer.keys())
        for check_box in clear_check_box:
            check_box.setChecked(False)
        #поставить везде false в словаре для проверки ответов self.check_answer
        for key in self.check_answer.keys():   
            self.check_answer[key] = False

    def next_question(self):
        
        if self.was_incorrect_answer:
            self.clean_all()
            self.was_incorrect_answer = False
            self.show_question()
        else:
            self.check_answer_func()

    def show_question(self):
        #получаем индекс случайного вопроса и проверяем, чтобы его не было в списке пройденых вопросов
        self.i = random.randint(0, len(self.dict_question_and_answer)-1)
        while self.i in self.question_passed:
            self.i = random.randint(0, len(self.dict_question_and_answer)-1)

        i = self.i

        #Возвращает пару (название, описание) из словаря
        items = list(self.dict_question_and_answer.items())
        
        #получаем вопрос
        question = items[i][0]
        #получаем словарь ответов
        dict_answers = items[i][1]
        #выводим вопрос на экран 
        self.ui.textBrowser_9.setText(question)
        
        #выводим ответы  на экран        
        for num in range(len(dict_answers)):
            textBrowser = self.answer_options[num]
            answers = list(dict_answers.keys())
            answer = answers[num]
            textBrowser.setText(answer)

            #записываем в словарь self.check_answer какие варианты правильные
            #сначал получаем элемент checkBox по индексу
            checkBoxs = list(self.check_answer.keys())
            checkBox = checkBoxs[num]
            #затем меняем значение у данного чек бокса на True или оставляем False, самое значение True/False берем из словаря
            # dict_answers по соответсвенному вопросу 
            self.check_answer[checkBox] = dict_answers[answer]
        


       
    def check_answer_func(self):
        answer_correct = True
        
        for answer in self.check_answer:
            if answer.isChecked() !=self.check_answer[answer]:
                answer_correct = False
        if answer_correct:
            self.question_passed.append(self.i)
            #передаем в progress bar длину списка пройденных вопросов
            self.ui.progressBar.setValue(len(self.question_passed))

            if len(self.question_passed) == len(self.dict_question_and_answer):
               print('finish')#sdelat vizov okna zaversheniya

               msg = QtWidgets.QMessageBox()
               msg.setWindowTitle("Экзамен завершен!")
               msg.setText(f"""Количество вопросов {len(self.dict_question_and_answer)}\nКоличество ошибок {self.num_errors}""")
               msg.setIcon(QtWidgets.QMessageBox.Information)
               msg.exec_()
               #закрываем приложение
               QCoreApplication.instance().quit()

            else:
               self.clean_all()
               self.show_question()
        else:
            #увеличим значение индикатора на 1
            self.num_errors += 1
            self.ui.label_3.setText("Ошибок "+ str(self.num_errors))
            #сделал чтобы рамка текста с Ошибка растягивалась в зависимости от количества ошибок
            self.ui.label_3.adjustSize()
            answers = list(self.check_answer.values())
            for i in range(len(self.answer_options)):
                if answers[i] == True:
                    self.answer_options[i].setStyleSheet("""
                    border-width:3px;
                    border-style:solid;
                    border-color: rgb(0, 255, 0);
                    """)
            self.was_incorrect_answer = True




        
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())