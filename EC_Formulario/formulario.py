# trabalhando com spin_combo_boxes

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QFormLayout, QLineEdit, 
                                QTextEdit, QSpinBox, QComboBox, 
                                QHBoxLayout)
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

        self.setGeometry(100,100, 300, 400)
        self.setWindowTitle("Formulario")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """

        titl_lbl = QLabel("Formulario de Agendamento de Consulta")
        titl_lbl.setFont(QFont('Arial', 18))
        titl_lbl.setAlignment(Qt.AlignCenter)

        nome_edit = QLineEdit()
        nome_edit.resize(100, 100)
        ende_edit = QLineEdit()
        cel_edit = QLineEdit()
        cel_edit.setInputMask("00-00000-0000;")

        edad_lbl = QLabel("Edade")
        edad_sbx = QSpinBox()
        edad_sbx.setRange(1, 110)

        alt_lbl = QLabel("Altura")
        alt_edit = QLineEdit()
        alt_edit.setPlaceholderText("cm")
        peso_lbl = QLabel("Peso")
        peso_edit = QLineEdit()
        peso_edit.setPlaceholderText("kg")

        gen_cbx = QComboBox()
        gen_cbx.addItems(["Masculino", "Femenino"])

        cirur_edit = QTextEdit()
        cirur_edit.setPlaceholderText("separadas por ','")
        sang_cbx = QComboBox()
        sang_cbx.addItems(["A", "B", "AB", "O"])

        hora_sbx = QSpinBox()
        hora_sbx.setRange(8, 19)
        min_cbx = QComboBox()
        min_cbx.addItems([":00", ":15", ":30", ":45"])

        marc_btn = QPushButton("Marcar Consuta")
        marc_btn.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addSpacing(10)
        hbox.addWidget(edad_lbl)
        hbox.addWidget(edad_sbx)
        hbox.addWidget(alt_lbl)
        hbox.addWidget(alt_edit)
        hbox.addWidget(peso_lbl)
        hbox.addWidget(peso_edit)

        hora_hbox = QHBoxLayout()
        hora_hbox.addSpacing(10)
        hora_hbox.addWidget(hora_sbx)
        hora_hbox.addWidget(min_cbx)

        app_form = QFormLayout()

        app_form.addRow(titl_lbl)
        app_form.addRow("Nome Completo", nome_edit)
        app_form.addRow("Endereço", ende_edit)
        app_form.addRow("Telefone Celular", cel_edit)
        app_form.addRow(hbox)
        app_form.addRow("Gênero", gen_cbx)
        app_form.addRow("Cirurgias Anteriores ", cirur_edit)
        app_form.addRow("Tipo Sanguineo", sang_cbx)
        app_form.addRow("Horário Desejado", hora_hbox)
        app_form.addRow(marc_btn)

        self.setLayout(app_form)

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Formulario()
    sys.exit(app.exec_())
