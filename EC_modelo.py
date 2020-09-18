# trabalhando com spin_combo_boxes

import sys
from PySide2.QtWidgets import * #Colocar aqui os componentes a ser importados
from PySide2.QtGui import *     #Colocar aqui os componentes a ser importados
from PySide2.QtCore import *    #Colocar aqui os componentes a ser importados

#class NomeDaApp(QMainWindow):
class NomeDaApp(QWidget):     #Colocar aqui o nome da app
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 230)         #Modificar o tamanho da Janela
        self.setWindowTitle("Pesquisa de Opinião")  #Modificar o nome da Janela
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        pass



#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pesquisa()         #Colocar aqui o nome da app
    sys.exit(app.exec_())
