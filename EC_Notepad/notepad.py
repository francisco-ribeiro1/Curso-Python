# notepad.py

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, 
                                QMessageBox, QTextEdit, QFileDialog)

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 300, 400)
        self.setWindowTitle("Notepad GUI")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """

        novo_btn = QPushButton("Novo", self)
        novo_btn.move(10, 20)
        novo_btn.clicked.connect(self.limpaTxt)

        grav_btn = QPushButton("Salvar", self)
        grav_btn.move(80, 20)
        grav_btn.clicked.connect(self.salvaTxt)

        self.texto = QTextEdit(self)
        self.texto.resize(280, 330)
        self.texto.move(10, 60)

    def limpaTxt(self):
        """
        Se o botão novo for clicado, exibe a caixa de diálogo 
        perguntando ao usuário se deseja limpar o campo de 
        edição de texto ou não.
        """

        resp = QMessageBox.question(self, "Limpar Texto", "Deseja limpar a tela?",
                                    QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if resp == QMessageBox.Yes:
            self.texto.clear()
        else:
            pass

    def salvaTxt(self):
        """
        Se o botão salvar for clicado, exibe a caixa de diálogo 
        para salvar o texto, no campo de edição, em um arquivo.
        """

        opção = QFileDialog.Options()
        notepad_text = self.texto.toPlainText()

        arquivo, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", 
                                                    "Todos os Arquivos (*);; Arquivos de texto (*.txt)", 
                                                    options=opção)

        if arquivo:
            with open(arquivo, 'w') as f:
                f.write(notepad_text)

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())
