from PyQt5 import QtWidgets
from ui.welcome import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from teacher import tapp, tapplication


from PyQt5.QtCore import QCoreApplication
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.teach)
        #self.ui.pushButton_2.clicked.connect(self.stud)

    def teach(self):
        
        QCoreApplication.instance().quit()
        self.teacher_app = tapp
        tapplication.show()
        #sys.exit(tapp.exec())

 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())