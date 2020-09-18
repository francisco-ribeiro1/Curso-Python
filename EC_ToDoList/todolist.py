# todolist.py
# trabalhando com spin_combo_boxes

import sys
from PySide2.QtWidgets import  (QApplication, QWidget, QLabel, 
                                QTextEdit, QLineEdit, QPushButton, 
                                QCheckBox, QGridLayout, QVBoxLayout)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt


class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 500, 350)
        self.setWindowTitle("ToDo List")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        grid = QGridLayout()

        titl_lbl = QLabel("To Do List")
        titl_lbl.setFont(QFont('Arial', 24))
        titl_lbl.setAlignment(Qt.AlignCenter)

        close_btn = QPushButton("Fechar")
        close_btn.clicked.connect(self.close)

        pend_lbl = QLabel("Tarefas")
        pend_lbl.setFont(QFont('Arial', 20))
        pend_lbl.setAlignment(Qt.AlignCenter)
        comp_lbl = QLabel("Compromissos")
        comp_lbl.setFont(QFont('Arial', 20))
        comp_lbl.setAlignment(Qt.AlignCenter)

        pend_grd = QGridLayout()
        pend_grd.setContentsMargins(5, 5, 5, 5)

        pend_grd.addWidget(pend_lbl, 0, 0, 1, 2)

        for pos in range(1, 15):
            cbox = QCheckBox()
            cbox.setChecked(False)
            ledit = QLineEdit()
            ledit.setMinimumWidth(200)
            pend_grd.addWidget(cbox, pos, 0)
            pend_grd.addWidget(ledit, pos, 1)

        mat_lbl = QLabel("Manhã")
        mat_lbl.setFont(QFont('Arial', 16))
        mat_tedit = QTextEdit()
        ves_lbl = QLabel("Tarde")
        ves_lbl.setFont(QFont('Arial', 16))
        ves_tedit = QTextEdit()
        not_lbl = QLabel("Noite")
        not_lbl.setFont(QFont('Arial', 16))
        not_tedit = QTextEdit()

        vbox = QVBoxLayout()
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.addWidget(comp_lbl)
        vbox.addWidget(mat_lbl)
        vbox.addWidget(mat_tedit)
        vbox.addWidget(ves_lbl)
        vbox.addWidget(ves_tedit)
        vbox.addWidget(not_lbl)
        vbox.addWidget(not_tedit)

        grid.addWidget(titl_lbl, 0, 0, 1, 2)
        grid.addLayout(pend_grd, 1, 0)
        grid.addLayout(vbox, 1, 1)
        grid.addWidget(close_btn, 2, 0, 1, 2)

        self.setLayout(grid)

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())
