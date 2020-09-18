
# Registro de um novo usuário

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QLineEdit, QMessageBox)
from PySide2.QtGui import QFont, QPixmap


class CriarNovoUsr(QWidget):
    """
    Inicializa a janela e mostra seu conteuda na tela
    """

    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 400)
        self.setWindowTitle("Criar Novo Usuário")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da janela
        """
        # Criando um label para uma imagem
        usr_img = "Imagens/pessoa.png"
        try:
            with open(usr_img):
                novo_usr = QLabel(self)
                pixmap = QPixmap(usr_img)
                pixmap = pixmap.scaled(100, 100)
                novo_usr.setPixmap(pixmap)
                novo_usr.move(150, 60)
        except FileNotFoundError:
            print("A imagem não esta disponível!")
        
        login_lbl = QLabel(self)
        login_lbl.setText("criar nova conta")
        login_lbl.move(110, 20)
        login_lbl.setFont(QFont('Arial', 20))

        # label e caixa de texto para nomes
        nome_lbl = QLabel("nome de usuário:", self)
        nome_lbl.move(30, 180)

        self.nome_edit = QLineEdit(self)
        self.nome_edit.move(150, 180)
        self.nome_edit.resize(200, 20)

        nomeC_usr_lbl = QLabel("nome completo:", self)
        nomeC_usr_lbl.move(30, 210)

        self.nomeC_edit = QLineEdit(self)
        self.nomeC_edit.move(150, 210)
        self.nomeC_edit.resize(200, 20)

        pswd_lbl = QLabel("senha:", self)
        pswd_lbl.move(30, 240)

        self.pswd_edit = QLineEdit(self)
        self.pswd_edit.setEchoMode(QLineEdit.Password)
        self.pswd_edit.move(130, 240)
        self.pswd_edit.resize(200, 20)

        conf_lbl = QLabel("confirmar:", self)
        conf_lbl.move(30, 270)

        self.conf_edit = QLineEdit(self)
        self.conf_edit.setEchoMode(QLineEdit.Password)
        self.conf_edit.move(130, 270)
        self.conf_edit.resize(200, 20)

        sigup_btn = QPushButton("Sign up", self)
        sigup_btn.move(100, 310)
        sigup_btn.resize(200,40)
        sigup_btn.clicked.connect(self.confirmarSignUp)

    def confirmarSignUp(self):
        """
        Quando o usuário preciona sign-up verifica se as senhas
        batem. Se confirmar então guarda o usuário e a senha no 
        arquivo usuarios.txt
        """

        pswd_text = self.pswd_edit.text()
        conf_text = self.conf_edit.text()

        if pswd_text != conf_text:
            QMessageBox.warning(self, "Mensagem de Erro", 
                                    "As senhas que vc digitou não estão batendo. Digite novamente!",  
                                    QMessageBox.Close, QMessageBox.Close)
        else:
            with open("usuarios.txt", "a+") as f:
                f.write(self.nome_edit.text() + " ")
                f.write(pswd_text + "\n")
            self.close()

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarNovoUsr()
    sys.exit(app.exec_())

