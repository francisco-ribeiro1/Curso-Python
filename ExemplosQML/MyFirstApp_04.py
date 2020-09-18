from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
    
    def contextMenuEvent(self, event):
       print("Context menu event|")
       super(MainWindow, self).contextMenuEvent(event)

    



app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
