# trabalhando com menu

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QAction)

class MenuApp(QMainWindow):     
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 350, 350)
        self.setWindowTitle("Menu Simples")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        
        sair_act = QAction('Sair', self)
        sair_act.setShortcut('Ctrl+Q')
        sair_act.triggered.connect(self.close)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        file_menu = menu_bar.addMenu('Arquivo')
        file_menu.addAction(sair_act)

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuApp()         
    sys.exit(app.exec_())
