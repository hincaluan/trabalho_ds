from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout
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

        # Layout principal
        layout = QVBoxLayout()

        # Layout para o botão de voltar no canto superior esquerdo
        layout_voltar = QHBoxLayout()
        botao_para_pagina_dois = QPushButton('Voltar')
        botao_para_pagina_dois.setStyleSheet( "padding: 5px 10px;")
        botao_para_pagina_dois.clicked.connect(self.abrir_pagina_um)
        layout_voltar.addWidget(botao_para_pagina_dois)
        layout_voltar.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Preenche o espaço restante
        layout.addLayout(layout_voltar)

        # Mensagem no topo
        tipo_combs = QLabel("Escolha o tipo de combustível:")
        tipo_combs.setStyleSheet("font-size: 16px; font-weight: bold;")
        tipo_combs.setAlignment(Qt.AlignCenter)
        layout.addWidget(tipo_combs)

        # Ajustar espaçamento entre os botões
        layout.setSpacing(40)

        # Adiciona três botões para tipos de combustível
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

        # Adiciona um espaçamento na parte inferior
        layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Define margens para o layout (esquerda, cima, direita, baixo)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(layout)

    # Função para abrir a página em branco
    def abrir_pagina_em_branco(self, tipo_comb):
        self.hide()
        self.pagina_em_branco = PaginaTres(tipo_comb)
        pagina_2_geometry = self.geometry()
        self.pagina_em_branco.setGeometry(pagina_2_geometry)
        self.pagina_em_branco.show()

    def abrir_pagina_um(self):
        from pagina1 import PaginaInicial  # Importação movida para dentro do método
        self.hide()
        self.pagina_dois = PaginaInicial()
        self.pagina_dois.setGeometry(self.geometry())
        self.pagina_dois.show()
