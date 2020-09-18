# Notepad com Rich text

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QAction,
                                QMessageBox, QTextEdit, QFileDialog, 
                                QInputDialog, QFontDialog, QColorDialog)
from PySide2.QtGui import QIcon, QTextCursor, QColor
from PySide2.QtCore import Qt

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 400, 500)
        self.setWindowTitle("Notepad")
        self.displayWidgets()
        self.notepadMenu()

        self.show()

    def displayWidgets(self):
        """
        Configura os widgets da app
        """
        
        self.tedit = QTextEdit()
        self.setCentralWidget(self.tedit)


    def notepadMenu(self):
        """
        Criando o menu para o Notepad
        """

        novo_act = QAction(QIcon('Imagens/new_file.png'), 'Novo', self)
        novo_act.setShortcut('Ctrl+N')
        novo_act.triggered.connect(self.clearText)

        abre_act = QAction(QIcon('Imagens/open_file.png'), 'Abrir', self)
        abre_act.setShortcut('Ctrl+O')
        abre_act.triggered.connect(self.openFile)

        salv_act = QAction(QIcon('Imagens/save_file.png'), 'Salvar', self)
        salv_act.setShortcut('Ctrl+S')
        salv_act.triggered.connect(self.saveToFile)

        sair_act = QAction(QIcon('Imagens/exit.png'), 'Sair', self)
        sair_act.setShortcut('Ctrl+Q')
        sair_act.triggered.connect(self.close)

        dsfz_act = QAction(QIcon('Imagens/undo.png'),'Desfazer', self)
        dsfz_act.setShortcut('Ctrl+Z')
        dsfz_act.triggered.connect(self.tedit.undo)

        rfaz_act = QAction(QIcon('Imagens/redo.png'),'Refazer', self)
        rfaz_act.setShortcut('Ctrl+Shift+Z')
        rfaz_act.triggered.connect(self.tedit.redo)

        rcrt_act = QAction(QIcon('Imagens/cut.png'),'Recortar', self)
        rcrt_act.setShortcut('Ctrl+X')
        rcrt_act.triggered.connect(self.tedit.cut)

        copr_act = QAction(QIcon('Imagens/copy.png'),'Copiar', self)
        copr_act.setShortcut('Ctrl+C')
        copr_act.triggered.connect(self.tedit.copy)

        colr_act = QAction(QIcon('Imagens/paste.png'),'Colar', self)
        colr_act.setShortcut('Ctrl+V')
        colr_act.triggered.connect(self.tedit.paste)

        proc_act = QAction(QIcon('Imagens/find.png'), 'Encontrar', self)
        proc_act.setShortcut('Ctrl+F')
        proc_act.triggered.connect(self.findTextDialog)

        font_act = QAction(QIcon('Imagens/font.png'), 'Fonte', self)
        font_act.setShortcut('Ctrl+T')
        font_act.triggered.connect(self.chooseFont)

        cor_act = QAction(QIcon('Imagens/color.png'), 'Cor', self)
        cor_act.setShortcut('Ctrl+Shift+C')
        cor_act.triggered.connect(self.chooseFontColor)

        hilh_act = QAction(QIcon('Imagens/highlight.png'), 'Destaque', self)
        hilh_act.setShortcut('Ctrl+Shift+H')
        hilh_act.triggered.connect(self.chooseFontBackgroundColor)

        sobr_act = QAction('Sobre', self)
        sobr_act.triggered.connect(self.aboutDialog)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        arqv_menu = menu_bar.addMenu('Arquivo')
        arqv_menu.addAction(novo_act)
        arqv_menu.addSeparator()
        arqv_menu.addAction(abre_act)
        arqv_menu.addAction(salv_act)
        arqv_menu.addSeparator()
        arqv_menu.addAction(sair_act)

        edit_menu = menu_bar.addMenu('Editar')
        edit_menu.addAction(dsfz_act)
        edit_menu.addAction(rfaz_act)
        edit_menu.addSeparator()
        edit_menu.addAction(rcrt_act)
        edit_menu.addAction(copr_act)
        edit_menu.addAction(colr_act)
        edit_menu.addSeparator()
        edit_menu.addAction(proc_act)

        tool_menu = menu_bar.addMenu('Ferramentas')
        tool_menu.addAction(font_act)
        tool_menu.addAction(cor_act)
        tool_menu.addAction(hilh_act)

        help_menu = menu_bar.addMenu('Ajuda')
        help_menu.addAction(sobr_act)


    def clearText(self):
        """
        Se o botão novo for clicado, exibe a caixa de diálogo perguntando 
        ao usuário se deseja limpar o campo de edição de texto ou não.
        """
        resp = QMessageBox.question(self, "Limpar texto",
                "Você deseja limpar o texto?", QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes)
        
        if resp == QMessageBox.Yes:
            self.tedit.clear()
        else:
            pass

    def openFile(self):
        """
        Abrir um arquivo de texto ou html e exiba seu 
        conteúdo no campo de edição de texto.
        """

        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo",
                        "", "Arquivos HTML (*.html);;Arquivos de Texto (*.txt)")

        if file_name:
            with open(file_name, 'r') as f:
                notepad_text = f.read()
            self.tedit.setText(notepad_text)
        else:
            QMessageBox.information(self, "Erro", "Impossível abrir o arquivo.", 
                                        QMessageBox.Ok)

    def findTextDialog(self):
        """
        Pesquisar texto no widget QTextEdit
        """
        find_text, ok = QInputDialog.getText(self, "Encontrar Texto", "Procurar:")

        extra = []

        if ok and not self.tedit.isReadOnly():
            self.tedit.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)

            while(self.tedit.find(find_text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                selection.cursor = self.tedit.textCursor()
                extra.append(selection)
            
            for i in extra_selections:
                self.tedit.setExtraSelections(extra)

    def saveToFile(self):
        """
        Se o botão salvar for clicado, exibe a caixa de diálogo perguntando ao usuário 
        se deseja salvar o texto em um arquivo.
        """

        file_name, _ = QFileDialog.getSaveFileName(self, 'Salvar Aqrquivo',
                        "","Arquivos HTML (*.html);;Arquivos de Texto (*.txt)")
        
        if file_name.endswith('.txt'):
            notepad_text = self.tedit.toPlainText()
            with open(file_name, 'w') as f:
                f.write(notepad_text)
        elif file_name.endswith('.html'):
            notepad_richtext = self.text_field.toHtml()
            with open(file_name, 'w') as f:
                f.write(notepad_richtext)
        else:
            QMessageBox.information(self, "Erro", "Impossível salvar o arquivo.", 
                                    QMessageBox.Ok)

    def chooseFont(self):
        """
        Selecione a fonte do texto
        """
        
        atual = self.tedit.currentFont()
        font, ok = QFontDialog.getFont(atual, self, 
                    options=QFontDialog.DontUseNativeDialog)
        
        if ok:
            self.tedit.setCurrentFont(font)



    def chooseFontColor(self):
        """
        Selecione a cor do texto
        """
        cor = QColorDialog.getColor()
        if cor.isValid():
            self.tedit.setTextColor(cor)

    def chooseFontBackgroundColor(self):
        """
        Selecione a cor de fundo do texto
        """
        cor = QColorDialog.getColor()
        if cor.isValid():
            self.tedit.setTextBackgroundColor(cor)

    def aboutDialog(self):
        """
        Exibir informações sobre o programa
        """
        QMessageBox.about(self, "Sobre Notepad", 
            "Bloco de notas adaptado do Guia prático para iniciantes no PyQt")

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())
