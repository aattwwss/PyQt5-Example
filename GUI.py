from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QWidget, QInputDialog, QLineEdit, QCompleter
from PyQt5.QtCore import QStringListModel
from mydesign import *
import sys
from constants import *
 
data = ['PyQt5','Is','Awesome']
 
class mywindow(QtWidgets.QMainWindow):
 
        def __init__(self):
            super().__init__() 
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

            #Fill comboBox
            self.ui.flat_Type_List.addItems(flat_Type_List)
            self.ui.flat_Model_List.addItems(flat_Model_List)
            
            #Linking button signals and actions
            self.ui.predictButton.clicked.connect(self.printAll)

        def printAll(self):
            (flatType,flatModel,storeyRange,lease,addr,floorArea,months) = self.getAll()
            print (flatType,flatModel,storeyRange,lease,addr,floorArea,months)

            flat_Type_Binary_copy = flat_Type_Binary.copy()
            flat_Model_Binary_copy = flat_Model_Binary.copy()

            for i, word in enumerate(flat_Type_List):
                if word == flatType:
                    flat_Type_Binary_copy[i] = 1
                    print (flat_Type_Binary_copy)
                    print (word)

            for i, word in enumerate(flat_Model_List):
                if word == flatModel:
                    flat_Model_Binary_copy[i] = 1
                    print (flat_Model_Binary_copy)
                    print (word)

            final_array = [floorArea,lease]
            final_array.extend(flat_Type_Binary_copy)
            final_array.extend(flat_Model_Binary_copy)
            final_array.append(addr)
            final_array.append(storeyRange)
            final_array.append(months)
  
            print (final_array)
            print(len(final_array))


        def getAll(self):
            flatType = self.ui.flat_Type_List.currentText()
            flatModel = self.ui.flat_Model_List.currentText()
            storeyRange = self.ui.storey_Range_Box.value()
            lease = self.ui.lease_Box.value()
            addr = self.ui.address_Box.text()
            floorArea = self.ui.horizontalSlider.value()
            months = self.ui.months_Box.value()
            return (flatType,flatModel,storeyRange,lease,addr,floorArea,months)

        def getLatLong(self,addr):
            return
            

 
app = QtWidgets.QApplication([])
#app.setStyle('Fusion')
win = mywindow()
win.show()
sys.exit(app.exec())