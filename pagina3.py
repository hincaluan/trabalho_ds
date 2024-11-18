# Arquivo: pagina_tres.py

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt

from estilos import estilo_botao


class PaginaTres(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página de Pagamento")
        self.setGeometry(100, 100, 400, 360)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()

        layout.addSpacerItem(QSpacerItem(40, 60, 40, 60))

        tipo_combs = QLabel("Abastecer por:")
        tipo_combs.setStyleSheet("font-size: 16px; font-weight: bold;")
        tipo_combs.setAlignment(Qt.AlignCenter)
        layout.addWidget(tipo_combs)

        layout.addSpacerItem(QSpacerItem(60, 100, 60, 100))

        # Botão para "Pagamento por Litros"
        self.botao_pagamento_por_litros = QPushButton('Litros')
        self.botao_pagamento_por_litros.setStyleSheet(estilo_botao)
        self.botao_pagamento_por_litros.clicked.connect(self.mostrar_campo_pagamento_por_litros)
        layout.addWidget(self.botao_pagamento_por_litros)

        layout.addSpacerItem(QSpacerItem(10, 30, 10, 30))

        # Botão para "Litros para Valor"
        self.botao_litros_para_valor = QPushButton('Valor')
        self.botao_litros_para_valor.setStyleSheet(estilo_botao)
        self.botao_litros_para_valor.clicked.connect(self.mostrar_campo_litros_para_valor)
        layout.addWidget(self.botao_litros_para_valor)

        # Campo de entrada para o valor
        self.campo_valor = QLineEdit()
        self.campo_valor.setPlaceholderText("Digite o valor desejado")
        self.campo_valor.hide()
        layout.addWidget(self.campo_valor)

        # Botão para realizar o cálculo
        self.botao_calcular = QPushButton('Calcular')
        self.botao_calcular.setStyleSheet(estilo_botao)
        self.botao_calcular.hide()
        layout.addWidget(self.botao_calcular)

        layout.addSpacerItem(QSpacerItem(30, 70, QSizePolicy.Minimum, QSizePolicy.Expanding))

        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

        self.opcao_selecionada = None

    def mostrar_campo_pagamento_por_litros(self):
        self.opcao_selecionada = "pagamento_por_litros"
        self.campo_valor.show()
        self.botao_calcular.show()

    def mostrar_campo_litros_para_valor(self):
        self.opcao_selecionada = "litros_para_valor"
        self.campo_valor.show()
        self.botao_calcular.show()
