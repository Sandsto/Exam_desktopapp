from os import posix_fadvise
from PyQt5 import QtWidgets
from ui.exam import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import json
import random
 
 
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

        #peremennaya dlya buttona_9? kotoraya izmenyaet ee povedenie
        #v zavisimosti vvodyat otvet ili pokazivaut oshibku
        self.was_incorrect_answer = False

    def loadFile(self):
        filename, format_file = QtWidgets.QFileDialog.getOpenFileName(self, 
                        'Открыть файл', 
                        './', 
                        'JSON files (*.json)')
        if filename:
            with open(filename) as json_file:
                self.dict_question_and_answer = json.load(json_file)
            
            self.new_question()

    def new_question(self):
        
        # #очистить все поля ввода и убрать выбранные ячейки
        self.ui.textBrowser_9.clear()
        for textBrowser in self.answer_options:
            textBrowser.clear()
        #убрать все поставленные галочки с вопросов
        clear_check_box = list(self.check_answer.keys())
        for check_box in clear_check_box:
            check_box.setChecked(False)
        #поставить везде false в словаре для проверки ответов self.check_answer
        for key in self.check_answer.keys():   
            self.check_answer[key] = False
         
       
       



        #получаем индекс случайного вопроса и проверяем, чтобы его не было в списке пройденых вопросов
        i = random.randint(0, len(self.dict_question_and_answer)-1)
        while i in self.question_passed and len(self.dict_question_and_answer) != len(self.dict_question_and_answer):
            i = random.randint(0, len(self.dict_question_and_answer)-1)

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
           if len(self.question_passed) == len(self.dict_question_and_answer):
               pass#sdelat vizov okna zaversheniya
           else:
               
               #prodvinut' progress bar
                self.new_question()
        else:
            #uvelichit' indikator na 1
            answers = list(self.check_answer.values())
            for i in range(len(self.answer_options)):
                if answers[i] == True:
                    self.answer_options[i].#pomenyat' cvet fona na zeleni
            self.was_incorrect_answer = True




        
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())