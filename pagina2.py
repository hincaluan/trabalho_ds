# Arquivo: pagina_dois.py

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from estilos import estilo_botao
from pagina3 import PaginaTres



class PaginaDois(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página Dois")
        self.setGeometry(100, 100, 300, 360)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()

        layout.addSpacerItem(QSpacerItem(20, 50, 20, 50))  # Espaço após o botão

        # Cria uma mensagem no topo
        tipo_combs = QLabel("Escolha o tipo de combustível:")
        tipo_combs.setStyleSheet("font-size: 16px; font-weight: bold;")
        tipo_combs.setAlignment(Qt.AlignCenter)
        layout.addWidget(tipo_combs)

        layout.addSpacerItem(QSpacerItem(40, 140, 40, 140))  # Espaço após o botão

        # Ajustar espaçamento entre os botões
        layout.setSpacing(40)  # Define o espaço entre os botões

        # Adiciona três botões que levam para a página em branco
        botao1 = QPushButton('Gasolina')
        botao1.setStyleSheet(estilo_botao)
        botao1.clicked.connect(lambda: self.abrir_pagina_em_branco('Gasolina'))
        layout.addWidget(botao1)

        botao2 = QPushButton('Etanol')
        botao2.setStyleSheet(estilo_botao)
        botao2.clicked.connect(lambda: self.abrir_pagina_em_branco('Etanol'))
        layout.addWidget(botao2)

        botao3 = QPushButton('Gasolina Aditivada')
        botao3.setStyleSheet(estilo_botao)
        botao3.clicked.connect(lambda: self.abrir_pagina_em_branco('Gasolina Aditivada'))
        layout.addWidget(botao3)

        # Adiciona um espaçamento na parte inferior (caso precise de mais espaço após os botões)
        layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Define margens para o layout (esquerda, cima, direita, baixo)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(layout)

    # Função para abrir a página em branco
    def abrir_pagina_em_branco(self, tipo_comb):
        self.hide()
        self.pagina_em_branco = PaginaTres(tipo_comb)  # Correção aqui (PáginaTres com P maiúsculo)
        pagina_2_geometry = self.geometry()
        self.pagina_em_branco.setGeometry(pagina_2_geometry)
        self.pagina_em_branco.show()
