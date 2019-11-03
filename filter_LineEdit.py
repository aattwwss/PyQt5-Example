import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QCompleter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QStringListModel
import constants

print (len(constants.FLAT_LOCATION))

def get_data(model):
    #model.setStringList(["1 ROOM","3 ROOM","4 ROOM","5 ROOM","2 ROOM","EXECUTIVE","MULTI GENERATION"])
    model.setStringList(constants.FLAT_LOCATION)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    edit = QLineEdit()
    completer = QCompleter()
    edit.setCompleter(completer)

    model = QStringListModel()
    completer.setModel(model)
    get_data(model)

    edit.show()
    sys.exit(app.exec_())