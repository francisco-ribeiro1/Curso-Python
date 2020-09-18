# Trabalhando com button

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class JDaApp(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 200, 150)
        self.setWindowTitle("Login")
        self.displayButton()

        self.show()

    def displayButton(self):
        """
        Configura o button 
        """

        nome_label = QLabel(self)
        nome_label.setText("Não aperte o botão!!!")
        nome_label.move(30, 30) # localiza o label na tela

        botao = QPushButton('Aperte aqui!', self)
        botao.clicked.connect(self.buttonClicked)
        botao.move(50, 70) # localizando o botão na tela

    def buttonClicked(self):
        """
        Imprime uma msg no terminal e fecha
        o app quando o botão for acionado 
        """

        print("A janela vai ser fechada!!!!")
        self.close()


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())
