from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from estilos import estilo_botao
from bomba_etanol import BombaEtanol
from bomba_gasolina import BombaGasolina


class PaginaTres(QWidget):
    def __init__(self, tipo_comb):
        super().__init__()
        self.tipo_comb = tipo_comb
        self.setWindowTitle("Página de Pagamento")
        self.setGeometry(100, 100, 400, 360)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()

        # Lixo
        self.label = QLabel()
        layout.addWidget(self.label)

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
        self.botao_calcular.clicked.connect(self.abastecer_por_litros)

    def mostrar_campo_litros_para_valor(self):
        self.opcao_selecionada = "litros_para_valor"
        self.campo_valor.show()
        self.botao_calcular.show()
        self.botao_calcular.clicked.connect(self.abastecer_por_valor)

    def abastecer_por_litros(self):
        litros = float(self.campo_valor.text())
        # Instanciar a bomba de combustível adequada
        if self.tipo_comb == "Etanol":
            self.bomba = BombaEtanol(2.00, 1000)
            litros = float(self.campo_valor.text())  # Converte a string para float
            total = self.bomba.abastecer_por_litros(litros)
            if total == -1:
                print("Quantidade de combustível insuficiente.")
            else:
                self.label.setText(f"Total a pagar: R$ {total:.2f}")  # Define o texto como string formatada
        elif self.tipo_comb == "Gasolina":
            self.bomba = BombaGasolina(5.00, 1000)
            litros = float(self.campo_valor.text())
            total = self.bomba.abastecer_por_litros(litros)
            if total == -1:
                print("Quantidade de combustível insuficiente.")
            else:
                self.label.setText(f"Total a pagar: R$ {total:.2f}") 
        elif self.tipo_comb == "Gasolina Aditivada":
            self.bomba = BombaGasolina(5.00, 1000)
            litros = float(self.campo_valor.text())
            total = self.bomba.abastecer_por_litros_com_adtivo(litros)
            if total == -1:
                print("Quantidade de combustível insuficiente.")
            else:
                self.label.setText(f"Total a pagar: R$ {total:.2f}")



    def abastecer_por_valor(self):
        litros = float(self.campo_valor.text())
        # Instanciar a bomba de combustível adequada
        if self.tipo_comb == "Etanol":
            self.bomba = BombaEtanol(2.00, 1000)
            litros = float(self.campo_valor.text())  # Converte a string para float
            total = self.bomba.abastecer_por_valor(litros)
            if total == -1:
                print("Quantidade de combustível insuficiente.")
            else:
                self.label.setText(f"valor abastecido: {total:.2f}")  # Define o texto como string formatada
        elif self.tipo_comb == "Gasolina":
            self.bomba = BombaGasolina(5.00, 1000)
            litros = float(self.campo_valor.text())
            total = self.bomba.abastecer_por_valor(litros)
            if total == -1:
                print("Quantidade de combustível insuficiente.")
            else:
                self.label.setText(f"valor abastecido: {total:.2f}") 
        elif self.tipo_comb == "Gasolina Aditivada":
            self.bomba = BombaGasolina(5.00, 1000)
            litros = float(self.campo_valor.text())
            total = self.bomba.abastecer_por_valor_com_aditivo(litros)
            if total == -1:
                print("Quantidade de combustível insuficiente.")
            else:
                self.label.setText(f"valor abastecido: {total:.2f}")
