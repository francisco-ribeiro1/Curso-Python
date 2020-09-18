# Adicionando um checkbox

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QLineEdit, QCheckBox)
from PySide2.QtCore import Qt

class JDaApp(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 250, 250)
        self.setWindowTitle("Login")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        # Criando um label e um edit para o nome
        quest_lbl = QLabel(self)
        quest_lbl.setText("Em quais turnos você pode trabalhar? (Verifque antes de confirmar)")
        quest_lbl.setWordWrap(True)
        quest_lbl.move(10, 10) # localiza o label na tela
        quest_lbl.resize(230, 60)

        # definindo os checkboxes
        manha_cbx = QCheckBox("Matutino [8:00 - 14:00]", self)
        manha_cbx.move(20, 80)
        manha_cbx.toggle()
        manha_cbx.stateChanged.connect(self.printToTerminal)

        tarde_cbx = QCheckBox("Vespertino [14:00 - 20:00]", self)
        tarde_cbx.move(20, 100)
        #tarde_cbx.toggle()
        tarde_cbx.stateChanged.connect(self.printToTerminal)

        noite_cbx = QCheckBox("Noturno [20:00 - 2:00]", self)
        noite_cbx.move(20, 120)
        #noite_cbx.toggle()
        noite_cbx.stateChanged.connect(self.printToTerminal)



    def printToTerminal(self, state):
        """
        Mostra como determinar o estado de um checkbox
        Imprime no terminal o texto do widget que mandou
        o sinal
        """

        sender = self.sender()
        if state == Qt.Checked:
            print("{} Selecionado.".format(sender.text()))
        else:
            print("{} Recusado.".format(sender.text()))


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())
