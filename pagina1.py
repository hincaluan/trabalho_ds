# Arquivo: pagina_inicial.py

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
from estilos import estilo_botao1
from pagina2 import PaginaDois


class PaginaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página Inicial")
        self.setGeometry(100, 100, 300, 360)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()

        titulo_app = QLabel("      𝔈́𝔩𝔞𝔦𝔬       ")
        titulo_app.setStyleSheet("font-size: 100px; font-weight: bold;")
        titulo_app.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo_app)

        mensagem_boas_vindas = QLabel("𝚂𝚎𝚞 𝚊𝚙𝚕𝚒𝚌𝚊𝚝𝚒𝚟𝚘 𝚍𝚎 𝚊𝚋𝚊𝚜𝚝𝚎𝚌𝚒𝚖𝚎𝚗𝚝𝚘 𝚘𝚗𝚕𝚒𝚗𝚎!")
        mensagem_boas_vindas.setStyleSheet("font-size: 12px; font-weight: bold;")
        mensagem_boas_vindas.setAlignment(Qt.AlignCenter)
        layout.addWidget(mensagem_boas_vindas)

        self.imagem_label = QLabel()
        pixmap = QPixmap("imagem.png")  # Substitua "imagem.png" pelo caminho da sua imagem
        self.imagem_label.setPixmap(pixmap)
        self.imagem_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.imagem_label)

        botao_para_pagina_dois = QPushButton('Entrar')
        botao_para_pagina_dois.setStyleSheet(estilo_botao1)
        botao_para_pagina_dois.clicked.connect(self.abrir_pagina_dois)
        layout.addWidget(botao_para_pagina_dois)

        layout.addSpacerItem(QSpacerItem(20, 70, 20, 50))
        self.setLayout(layout)

    def abrir_pagina_dois(self):
        self.hide()
        self.pagina_dois = PaginaDois()
        self.pagina_dois.setGeometry(self.geometry())
        self.pagina_dois.show()
