# Adicionando um lineedit

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QLineEdit)
from PySide2.QtCore import Qt

class JDaApp(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 200)
        self.setWindowTitle("Login")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        # Criando um label e um edit para o nome
        nome_label = QLabel("Nome:",self)
        nome_label.move(70, 50) # localiza o label na tela

        self.nome_edit = QLineEdit(self)
        self.nome_edit.setAlignment(Qt.AlignLeft)                           # Este é o padrão
        self.nome_edit.move(130, 50)
        self.nome_edit.resize(200, 20)                                      # mudando o tamanho da caixa de texto

        self.limpar_btn = QPushButton('Limpar', self)
        self.limpar_btn.clicked.connect(self.limparCxTxt)
        self.limpar_btn.move(160, 110)                                      # localizando o botão na tela

    def limparCxTxt(self):
        """
        Quando acionado o butão limpa a caixa de texto
        """

        sender = self.sender()
        if sender.text() == 'Limpar':
            self.nome_edit.clear()


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())
