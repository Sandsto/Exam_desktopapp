from PyQt5 import QtWidgets
from ui.welcome import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import teacher
import student


from PyQt5.QtCore import QCoreApplication
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.t = teacher.teach_mywindow()
        self.s = student.student_mywindow()

        self.ui.pushButton.clicked.connect(self.teach)
        self.ui.pushButton_2.clicked.connect(self.stud)

    def teach(self):
        self.t.show()
        self.close()
    
    def stud(self):
        self.s.show()
        self.close()


 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())