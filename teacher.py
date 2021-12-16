from PyQt5 import QtWidgets
from ui.add_question import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

from PyQt5.Qt import QApplication, QClipboard
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        

        

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.ctrl_V)

    def ctrl_V(self):
        #копируем содержимое буфера обмена
        past = QApplication.clipboard().text()
        #добавляем текст в ячейку
        self.ui.plainTextEdit.setPlainText(past)
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())