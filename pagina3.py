from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from estilos import estilo_botao
from bomba_etanol import BombaEtanol
from bomba_gasolina import BombaGasolina
from pagina4 import PaginaQuatro  # Nova página para exibir resultados

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

        layout_voltar = QHBoxLayout()
        botao_para_pagina_dois = QPushButton('Voltar')
        botao_para_pagina_dois.setStyleSheet( "padding: 5px 10px;")
        botao_para_pagina_dois.clicked.connect(self.abrir_pagina_dois)
        layout_voltar.addWidget(botao_para_pagina_dois)
        layout_voltar.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(layout_voltar)

        self.label = QLabel()
        layout.addWidget(self.label)

        layout.addSpacerItem(QSpacerItem(40, 60, 40, 60))

        tipo_combs = QLabel("Abastecer por:")
        tipo_combs.setStyleSheet("font-size: 16px; font-weight: bold;")
        tipo_combs.setAlignment(Qt.AlignCenter)
        layout.addWidget(tipo_combs)

        layout.addSpacerItem(QSpacerItem(60, 100, 60, 100))

        self.botao_pagamento_por_litros = QPushButton('Litros')
        self.botao_pagamento_por_litros.setStyleSheet(estilo_botao)
        self.botao_pagamento_por_litros.clicked.connect(self.mostrar_campo_pagamento_por_litros)
        layout.addWidget(self.botao_pagamento_por_litros)

        layout.addSpacerItem(QSpacerItem(10, 30, 10, 30))

        self.botao_litros_para_valor = QPushButton('Valor')
        self.botao_litros_para_valor.setStyleSheet(estilo_botao)
        self.botao_litros_para_valor.clicked.connect(self.mostrar_campo_litros_para_valor)
        layout.addWidget(self.botao_litros_para_valor)

        self.campo_valor = QLineEdit()
        self.campo_valor.setPlaceholderText("Digite o valor desejado")
        self.campo_valor.hide()
        layout.addWidget(self.campo_valor)

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
     try:
        litros = float(self.campo_valor.text())
        if litros <= 0:
            raise ValueError("Quantidade inválida.")
    
        litros = float(self.campo_valor.text())
        if self.tipo_comb == "Etanol":
            self.bomba = BombaEtanol(2.00, 1000)
        elif self.tipo_comb == "Gasolina":
            self.bomba = BombaGasolina(5.00, 1000)
        elif self.tipo_comb == "Gasolina Aditivada":
            self.bomba = BombaGasolina(5.00, 1000)

        total = self.bomba.abastecer_por_litros(litros)
        if total == -1:
            self.abrir_pagina_resultado("Erro", "Quantidade de combustível insuficiente.", 0)
        else:
            self.abrir_pagina_resultado("Resultado", f"Total a pagar: R$ {total:.2f}", litros)
     except ValueError:
        self.abrir_pagina_resultado("Erro", "Por favor, insira um número válido.", 0)

    def abastecer_por_valor(self):
     try:
        litros = float(self.campo_valor.text())
        if litros <= 0:
            raise ValueError("Quantidade inválida.")
    
        valor = float(self.campo_valor.text())
        if self.tipo_comb == "Etanol":
            self.bomba = BombaEtanol(2.00, 1000)
        elif self.tipo_comb == "Gasolina":
            self.bomba = BombaGasolina(5.00, 1000)
        elif self.tipo_comb == "Gasolina Aditivada":
            self.bomba = BombaGasolina(5.00, 1000)

        litros = self.bomba.abastecer_por_valor(valor)
        if litros == -1:
            self.abrir_pagina_resultado("Erro", "Quantidade de combustível insuficiente.", 0)
        else:
            self.abrir_pagina_resultado("Resultado", f"Litros abastecidos: {litros:.2f}", litros)
     except ValueError:
         self.abrir_pagina_resultado("Erro", "Por favor, insira um número válido.", 0)
         
    def abrir_pagina_resultado(self, titulo, mensagem, litros):
        self.hide()
        self.pagina_resultado = PaginaQuatro(titulo, mensagem, litros)
        pagina_geometry = self.geometry()
        self.pagina_resultado.setGeometry(pagina_geometry)
        self.pagina_resultado.show()

    def abrir_pagina_dois(self):
        from pagina2 import PaginaDois  
        self.hide()
        self.pagina_dois = PaginaDois()
        self.pagina_dois.setGeometry(self.geometry())
        self.pagina_dois.show()