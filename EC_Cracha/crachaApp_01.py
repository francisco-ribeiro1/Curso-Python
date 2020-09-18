
# Adicionando um "label" na janela

# Importando os modulos

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPixmap

class JDaApp(QWidget):

    def __init__(self):
        super().__init__() # chamada ao construtor padrão da superclasse
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 250, 250)
        self.setWindowTitle("Crachá")
        self.displayLabels()

        self.show()

    def displayLabels(self):
        """
        Apresentando texto e imagens com QLabels.

        Verifica se o arquivo de imagem está disponível,
        caso contrario gera uma exception.
        """

        text = QLabel(self)
        text.setText("Saudações")
        text.move(95, 15)

        img = "Imagens/pessoa.png"
        try:
            with open(img):
                foto = QLabel(self)
                pixmap = QPixmap(img)
                pixmap = pixmap.scaled(160, 160)
                foto.setPixmap(pixmap)
                foto.move(45, 45)
        except FileNotFoundError:
            print("Não tem foto para o cracha!")

        

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())

