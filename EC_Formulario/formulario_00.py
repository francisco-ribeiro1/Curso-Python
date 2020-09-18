# trabalhando com spin_combo_boxes

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QComboBox, QSpinBox, QHBoxLayout, 
                                QVBoxLayout)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 300, 200)
        self.setWindowTitle("Formulario")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """

        info_lbl = QLabel("Selecione 2 itens que você almoçou e seus preços.")
        info_lbl.setFont(QFont('Arial', 16))
        info_lbl.setAlignment(Qt.AlignCenter)
        self.total_lbl = QLabel("Total: R$")
        self.total_lbl.setFont(QFont('Arial', 16))
        self.total_lbl.setAlignment(Qt.AlignRight)

        list_comida = ["ovos", "misto quente", "queijo quente", "queijo",
                        "homus", "iogurte", "maçã", "banana", "laranja", "pão de queijo", "cenouras",
                        "pão", "macarrão", "biscoitos", "tapioca", "batatas fritas",
                        "café", "refrigerante", "água"]

        alm1_cbx = QComboBox()
        alm1_cbx.addItems(list_comida)
        alm2_cbx = QComboBox()
        alm2_cbx.addItems(list_comida)

        self.pre1R_sbx = QSpinBox()
        self.pre1R_sbx.setRange(0,100)
        self.pre1R_sbx.setPrefix("R$ ")
        self.pre1R_sbx.valueChanged.connect(self.calculaTotal)
        self.pre1C_sbx = QSpinBox()
        self.pre1C_sbx.setRange(0,99)
        self.pre1C_sbx.setPrefix(".")
        self.pre1C_sbx.valueChanged.connect(self.calculaTotal)

        self.pre2R_sbx = QSpinBox()
        self.pre2R_sbx.setRange(0,100)
        self.pre2R_sbx.setPrefix("R$ ")
        self.pre2R_sbx.valueChanged.connect(self.calculaTotal)
        self.pre2C_sbx = QSpinBox()
        self.pre2C_sbx.setRange(0,99)
        self.pre2C_sbx.setPrefix(".")
        self.pre2C_sbx.valueChanged.connect(self.calculaTotal)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox1.addWidget(alm1_cbx)
        hbox1.addWidget(self.pre1R_sbx)
        hbox1.addWidget(self.pre1C_sbx)
        hbox2.addWidget(alm2_cbx)
        hbox2.addWidget(self.pre2R_sbx)
        hbox2.addWidget(self.pre2C_sbx)

        vbox = QVBoxLayout()
        vbox.addWidget(info_lbl)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.total_lbl)

        self.setLayout(vbox)

    def calculaTotal(self):
        """
        Calcular e exibir o preço total das spin boxes 
        e alterar o valor mostrado no QLabel
        """

        total = self.pre1R_sbx.value() + self.pre2R_sbx.value()
        total += (self.pre1C_sbx.value() / 100)
        total += (self.pre2C_sbx.value() / 100)
        self.total_lbl.setText("Total: R${}". format(str(total)))

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Formulario()
    sys.exit(app.exec_())
