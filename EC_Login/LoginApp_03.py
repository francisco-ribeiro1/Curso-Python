# Adicionando um MessageBox

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QLineEdit, QCheckBox,
                                QMessageBox)
from PySide2.QtGui import QFont
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
        
        info_lbl = QLabel(self)
        info_lbl.setText("Lista de Funcionarios")
        info_lbl.move(20, 20) # localiza o label na tela
        info_lbl.setFont(QFont('Arial', 20))

        quest_lbl = QLabel(self)
        quest_lbl.setText("Entre o nome do funcionarioa que procura:")
        quest_lbl.move(40, 60) # localiza o label na tela

        nome_lbl = QLabel("Nome:", self)
        nome_lbl.move(50, 90) # localiza o label na tela

        self.nome_edit = QLineEdit(self)
        self.nome_edit.setAlignment(Qt.AlignLeft) # Este é o padrão
        self.nome_edit.move(95, 90)
        self.nome_edit.resize(240, 20) # mudando o tamanho da caixa de texto
        self.nome_edit.setPlaceholderText("nome sobrenome")

        self.pesq_btn = QPushButton('Procurar', self)
        self.pesq_btn.clicked.connect(self.displayMessageBox)
        self.pesq_btn.move(125, 130) # localizando o botão na tela
        self.pesq_btn.resize(150, 40)


    def displayMessageBox(self):
        """
        Quando o butão for acionado procurar na lista de
        funcionarios. Se o funcionario for localizado o app
        mostra uma mensagem de Funcionario localizado. Caso
        contrario mostra a mensagem Funcionario não localizado
        """

        try:
            with open("funcionarios.txt", 'r') as f:
                funcionarios = [line.rstrip('\n') for line in f]
        except FileNotFoundError:
            print("O arquivo com a lista de funcionarios (funcionarios.txt) não foi encontrado.")

        # Procurando o funcionario na lista
        msg_no_encontrado = QMessageBox()

        if self.nome_edit.text() in funcionarios:
            QMessageBox().information(self, "Funcionario Localizado", "Funcionario localizado na lista!", 
                                        QMessageBox.Ok, QMessageBox.Ok)
        else: 
            msg_no_encontrado = QMessageBox().question(self, "Funcionario Não Localizado", 
                                        "Funcionario não consta na lista!\nDeseja continuar?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if msg_no_encontrado == QMessageBox.No:
            print("Closing application.")
            self.close()
        else:
            pass


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())
