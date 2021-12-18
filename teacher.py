from PyQt5 import QtWidgets
from ui.add_question import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

from PyQt5.Qt import QApplication, QClipboard
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      
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
        #self.ui.pushButton_10.clicked.connect(self.saveFinish)

    def ctrl_V(self):
        #получаем какая кнопка была нажата. Используем метод sender
        sender = self.sender()
        #копируем содержимое буфера обмена
        past = QApplication.clipboard().text()
        #находим в какую ячейку надо вставить текст, используя словарь с кнопкой вставки: текст
        plain_text_edit = self.dict_pushb_text[sender]
        #добавляем текст в ячейку
        plain_text_edit.setPlainText(past)
        

    def saveForward(self):
        pass

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())