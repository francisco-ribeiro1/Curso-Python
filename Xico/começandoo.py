# Fuçando Qt

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QLineEdit, QMessageBox, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QFont, QPixmap


class VotacaoAlbumRet(QWidget):
    """
    Inicializa a janela e mostra o conteudo na tela
    """

    def __init__(self):
        super().__init__()
        self.inicialUI()

    def inicialUI(self):
        """
        Inicializa a janela e mostra o conteudo na tela
        """

        self.setGeometry(500, 500, 500, 500)
        self.setWindownTitle("Pesquisa")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da janela
        """
        title_lbl = QLabel("Albuns Filipe Ret")
        title_lbl.setfont(QFont("Arial", 17))
        qust_lbl = QLabel("Qual é o melhor album do rapper?")

        title_hbox = QHBoxlayout()
        title_hbox.addStretch()
        title_hbox.addWidget(title_lbl)
        title_hbox.addStretch()

        # Criando Labels para 3 imagens
        vivaz_img = "Imagens/vivaz.png"
        revel_img = "Imagens/revel.png"
        audaz_img = "Imagens/audaz.png"
        try:
            with open(vivaz_img):
                vivaz1_img = QLabel(self)
                pixmap = QPixmap(vivaz_img)
                pixmap = pixmap.scaled(33, 33)
                vivaz1_img.SetPixmap(pixmap)
                vivaz1_img.Move(150, 60)
        except FileNotFoundError:
            print("A imagem não está disponível!")

        try:
            with open(revel_img):
                revel1_img = QLabel(self)
                pixmap = QPixmap(revel_img)
                pixmap = pixmap.scaled(66, 66)
                revel1_img.SetPixmap(pixmap)
                revel1_img.Move(150, 60)
        except FileNotFoundError:
            print("A imagem não está disponível!")

        try:
            with open(audaz_img):
                audaz1_img = QLabel(self)
                pixmap = QPixmap(audaz_img)
                pixmap = pixmap.scaled(99, 99)
                audaz1_img.SetPixmap(pixmap)
                audaz1_img.Move(150, 60)
        except FileNotFoundError:
            print("A imagem não está disponível!")
            

        escala = ["Vivaz", "Revel", "Audaz"]

        escala_hbox =  QHBoxLayout()
        escala_hbox.setSpacing(33)

        escala_hbox.addStrech()
        for eval in escala:
            eval_lbl = QLabel(eval, self)
            escala_hbox.addWidget(eval_lbl)
        escala_hbox.addStrech()

        btng_hbox = QHBoxLayout()
        btng_hbox.setSpacing(55)
        escala_bgrp = QButtonGroup(self)
        btg_hbox.addStretch()
        for btn in range(len(escala)):
            eval_chkb = QCheckBox(str(btn), self)
            btng_hbox.addWidget(eval_chkb)
            escala_bgrp.addButton(eval_chkb)
        btng_hbox.addStretch()

        escala_bgrp.buttonClicked.connect(self.checkBoxClicked)

        close_btn = QPushButton("Fechar", self)
        close_btn.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addLayout(title_hbox)
        vbox.addWidget(qust_lbl)
        vbox.addStretch(1)
        vbox.addLayout(escala_hbox)
        vbox.addLayout(btng_hbox)
        vbox.addStretch(2)
        vbox.addWidget(close_btn)

        self.setLayout(vbox)


    def CheckBoxClicked(self,chkb):
        """
        Imprime o texto do checkbox selecionado
        """

        print("{} Selecionado.", format(chkb.text()))

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VotacaoAlbumRet()
    sys.exit(app.exec_())


        
