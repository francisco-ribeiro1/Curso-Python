
# Criando uma janela básica

# Importando os modulos

import sys
from PySide2.QtWidgets import QApplication, QWidget

class JDaApp(QWidget):

    def __init__(self):
        super().__init__() # chamada ao construtor padrão da superclasse
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 300)
        self.setWindowTitle("Crachá")
        self.show()

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())

