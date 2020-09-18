
# Versão completa do Crachá

# Importando os modulos

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPixmap, QFont

class JDaApp(QWidget):

    def __init__(self):
        super().__init__() # chamada ao construtor padrão da superclasse
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(50,50, 250, 400)
        self.setWindowTitle("Crachá")
        self.displayImag()
        self.displayInfo()

        self.show()

    def displayImag(self):
        """
        Modifica a imagem de fundo e mostra imagem 
        do funcionario no crachá

        Verifica se os arquivos de imagens estão disponível,
        caso contrario gera uma exception.
        """

        text = QLabel(self)
        text.setText("Saudações")
        text.move(105, 15)

        bckImg = "Imagens/modelo.png"
        usrImg = "Imagens/pessoa.png"

        try:
            with open(bckImg):
                bck = QLabel(self)
                pixmap = QPixmap(bckImg)
                pixmap = pixmap.scaled(250, 400)
                bck.setPixmap(pixmap)
        except FileNotFoundError:
            print("Não tem imagem de fundo!")

        try:
            with open(usrImg):
                foto = QLabel(self)
                pixmap = QPixmap(usrImg)
                pixmap = pixmap.scaled(130, 130)
                foto.setPixmap(pixmap)
                foto.move(120-65,122-65)
        except FileNotFoundError:
            print("Não tem foto para o cracha!")

        
    def displayInfo(self):
        """
        Cria labels para apresentar as informações do funcionario
        """

        nomeFun = QLabel(self)
        nomeFun.setText("Francisco Silva Oliveira")
        nomeFun.move(40, 240)
        nomeFun.setFont(QFont('Arial', 14))

        cargFun = QLabel(self)
        cargFun.setText("Programador")
        cargFun.move(40, 280)
        nomeFun.setFont(QFont('Arial', 12))


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())

