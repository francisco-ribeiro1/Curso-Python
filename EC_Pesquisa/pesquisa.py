# pesquisa.py

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QPushButton, QCheckBox, 
                                QButtonGroup, QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QFont

class Pesquisa(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 230)
        self.setWindowTitle("Pesquisa de Opinião")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """

        titl_lbl = QLabel("Pizzaria Pinocchio")
        titl_lbl.setFont(QFont("Arial", 17))
        qust_lbl = QLabel("Como você classificaria o atendimento hoje?")

        titl_hbox = QHBoxLayout()
        titl_hbox.addStretch()
        titl_hbox.addWidget(titl_lbl)
        titl_hbox.addStretch()

        escala = ["Insatisfeito", "Médio", "Satisfeito"]

        escala_hbox = QHBoxLayout()
        escala_hbox.setSpacing(60)

        escala_hbox.addStretch()
        for eval in escala:
            eval_lbl = QLabel(eval, self)
            escala_hbox.addWidget(eval_lbl)
        escala_hbox.addStretch()

        btng_hbox = QHBoxLayout()
        btng_hbox.setSpacing(100)
        escala_bgrp = QButtonGroup(self)
        btng_hbox.addStretch()
        for btn in range(len(escala)):
            eval_chkb = QCheckBox(str(btn), self)
            btng_hbox.addWidget(eval_chkb)
            escala_bgrp.addButton(eval_chkb)
        btng_hbox.addStretch()

        escala_bgrp.buttonClicked.connect(self.checkboxClicked)

        close_btn = QPushButton("Fechar", self)
        close_btn.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addLayout(titl_hbox)
        vbox.addWidget(qust_lbl)
        vbox.addStretch(1)
        vbox.addLayout(escala_hbox)
        vbox.addLayout(btng_hbox)
        vbox.addStretch(2)
        vbox.addWidget(close_btn)

        self.setLayout(vbox)


    def checkboxClicked(self, chkb):
        """
        Imprime o texto do checkbox selecionado
        """

        print("{} Selecionado.",format(chkb.text()))

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pesquisa()
    sys.exit(app.exec_())

