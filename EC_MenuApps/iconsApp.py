# trabalhando com icones 

import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QVBoxLayout)
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
import random

#class NomeDaApp(QMainWindow):
class IconApp(QWidget): 
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 200, 200)
        self.setWindowTitle("Exemplo com Icones")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        
        info_lbl = QLabel("Clique no botão e selecione uma fruta.")

        self.imgs = [
            "Imagens/apple.png",
            "Imagens/pineapple.png",
            "Imagens/watermelon.png",
            "Imagens/banana.jpg"
        ]

        self.icon_btn = QPushButton(self)
        self.fruta = random.choice(self.imgs)
        self.icon_btn.setIcon(QIcon(self.fruta))
        self.icon_btn.setIconSize(QSize(60, 60))
        self.icon_btn.clicked.connect(self.changeButtonIcon)

        vbox = QVBoxLayout()
        vbox.addWidget(info_lbl)
        vbox.addWidget(self.icon_btn)

        self.setLayout(vbox)

    def changeButtonIcon(self):
        """
        Quando o botão for clicado, altera o ícone 
        para uma das imagens da lista.
        """
        fruta = random.choice(self.imgs)
        while fruta == self.fruta:
            fruta = random.choice(self.imgs)
        self.fruta = fruta
        self.icon_btn.setIcon(QIcon(self.fruta))
        self.icon_btn.setIconSize(QSize(60, 60))

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IconApp()
    sys.exit(app.exec_())
