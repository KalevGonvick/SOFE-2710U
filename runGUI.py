import sys
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *
from GUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.state = False

        self.volSlider.valueChanged.connect(self.lcdNumber.display)
        self.pushButton.clicked.connect(self.on_shutdown_click)
        self.pushButton_2.clicked.connect(self.toggle_alarm_state)

        _translate = QCoreApplication.translate
        ls = [["hello", "world"], ["this is a date", "this is a time"], ["x", "y"], ["1", "2"]]

        for i in range(0,len(ls)):
            if self.tableWidget.item(i, 0) is None:
                # Increase table size
                self.tableWidget.setRowCount(i + 1)

                # Create new empty row
                item = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(i, item)
                item = self.tableWidget.verticalHeaderItem(i)
                item.setText(_translate("MainWindow", str(i + 1)))
                item = QTableWidgetItem()
                self.tableWidget.setItem(i, 0, item)
                item = QTableWidgetItem()
                self.tableWidget.setItem(i, 1, item)

            for j in range(0, 2):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("MainWindow", ls[i][j]))

    def toggle_alarm_state(self):
        _translate = QCoreApplication.translate
        if self.state is True:
            self.pushButton_2.setText(_translate("MainWindow", "Enable Alarm"))
            self.stateLabel.setStyleSheet("background:red;")
            self.stateLabel.setText(_translate("MainWindow", "Alarm Disabled"))
            self.state = False
        else:
            self.pushButton_2.setText(_translate("MainWindow", "Disable Alarm"))
            self.stateLabel.setStyleSheet("background:green;")
            self.stateLabel.setText(_translate("MainWindow", "Alarm Enabled"))
            self.state = True

    def on_shutdown_click(self):
        print "Shutting down..."
        self.close()


app = QApplication(sys.argv)
window = MainWindow()
# window = QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(window)

window.show()
sys.exit(app.exec_())
