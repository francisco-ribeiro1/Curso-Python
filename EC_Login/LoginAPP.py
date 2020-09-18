# Login completo

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, 
                                QPushButton, QLineEdit, QCheckBox,
                                QMessageBox)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt
from Registration import CriarNovoUsr 

class JDaApp(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 230)
        self.setWindowTitle("Login")
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        
        login_lbl = QLabel(self)
        login_lbl.setText("login")
        login_lbl.move(180, 10) # localiza o label na tela
        login_lbl.setFont(QFont('Arial', 20))

        nome_lbl = QLabel("usuário:", self)
        nome_lbl.move(30, 60) # localiza o label na tela

        self.nome_edit = QLineEdit(self)
        self.nome_edit.setAlignment(Qt.AlignLeft) # Este é o padrão
        self.nome_edit.move(110, 60)
        self.nome_edit.resize(220, 20) # mudando o tamanho da caixa de texto
        
        pwd_lbl = QLabel("senha:", self)
        pwd_lbl.move(30, 90) # localiza o label na tela

        self.pwd_edit = QLineEdit(self)
        self.pwd_edit.setEchoMode(QLineEdit.Password)
        self.pwd_edit.setAlignment(Qt.AlignLeft) # Este é o padrão
        self.pwd_edit.move(110, 90)
        self.pwd_edit.resize(220, 20) # mudando o tamanho da caixa de texto

        sigin_btn = QPushButton('login', self)
        sigin_btn.clicked.connect(self.clickLogin)
        sigin_btn.move(100, 140) # localizando o botão na tela
        sigin_btn.resize(200, 40)

        show_pwd_cbx = QCheckBox("Mostrar a senha", self)
        show_pwd_cbx.move(110, 115)
        show_pwd_cbx.toggle()
        show_pwd_cbx.setChecked(False)
        show_pwd_cbx.stateChanged.connect(self.showPassword)

        out_lbl = QLabel("não é usuário?", self)
        out_lbl.move(50, 200) # localiza o label na tela

        sigup_btn = QPushButton('registrar', self)
        sigup_btn.clicked.connect(self.criarNovo)
        sigup_btn.move(160, 190) # localizando o botão na tela
        

    def clickLogin(self):
        """
        Quando o usuário acionar o botão de login, verifica se
        o usuário e o login conferem. Os registros estão no
        arquivo usuarios.txt.
        Se existe, apresenta uma mensagem e fecha o app
        Se não, mostra uma mensagem de erro
        """

        usuarios = {} 

        try:
            with open("usuarios.txt", 'r') as f:
                for line in f:
                    campos = line.split(" ")
                    username = campos[0]
                    senha = campos[1].strip('\n')
                    usuarios[username] = senha                
        except FileNotFoundError:
            print("O arquivo de usuários (usuarios.txt) não foi encontrado.")
            f = open("usuarios.txt", 'w')

        username = self.nome_edit.text()
        senha = self.pwd_edit.text()
        if (username, senha) in usuarios.items():
            QMessageBox.information(self, "Registro Ok", "Login realizado com sicesso", 
                                        QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else: 
            QMessageBox.warning(self, "Problemas!", "Senha o nome do usuário incorecto", 
                                    QMessageBox.Close, QMessageBox.Close)

    def showPassword(self, state):
        """
        Se o checkbox esta ativado,mostra a senha
        Caso contrario mascara a senha para ocultar 
        """

        if state == Qt.Checked:
            self.pwd_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_edit.setEchoMode(QLineEdit.Password)

    def criarNovo(self):
        """
        Quando o botão for acionado, abrir nova
        janela para registrar um novo usuário
        """
        self.criar_novo_usuario = CriarNovoUsr()
        self.criar_novo_usuario.show()
        

    def closeEvent(self, event):
        """
        Exiba um QMessageBox ao perguntar ao usuário
        se deseja sair do programa.
        """

        quit_msg = QMessageBox.question(self, "Sair da aplicação?", "Você tem certeza que quer sair?", 
                                            QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if quit_msg ==  QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())

