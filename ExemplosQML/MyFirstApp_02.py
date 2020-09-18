
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt

import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Change the title of our main window
        self.setWindowTitle("My Awesome App") 

        # add our first widget — a QLabel — to the middle of the window
        label = QLabel("THIS IS AWESOME!!!")

        # We set the alignment of the widget to the centre
        label.setAlignment(Qt.AlignCenter)
        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec_()
