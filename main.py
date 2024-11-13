from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QPalette, QColor, QPixmap, QFont

from PyQt5.QtCore import *

# Classe para a terceira página (em branco)
class paginaTres(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página de Pagamento")
        self.setGeometry(100, 100, 400, 360)

        layout = QVBoxLayout()

        # Cria o botão para "Pagamento por Litros"
        self.botao_pagamento_por_litros = QPushButton('Pagamento por Litros')
        self.botao_pagamento_por_litros.clicked.connect(self.mostrar_campo_pagamento_por_litros)
        layout.addWidget(self.botao_pagamento_por_litros)

        # Cria o botão para "Litros para Valor"
        self.botao_litros_para_valor = QPushButton('Litros para Valor')
        self.botao_litros_para_valor.clicked.connect(self.mostrar_campo_litros_para_valor)
        layout.addWidget(self.botao_litros_para_valor)

        # Campo de entrada para o valor
        self.campo_valor = QLineEdit()
        self.campo_valor.setPlaceholderText("Digite o valor desejado")
        self.campo_valor.hide()  # Esconde o campo inicialmente
        layout.addWidget(self.campo_valor)

        # Botão para realizar o cálculo
        self.botao_calcular = QPushButton('Calcular')
        self.botao_calcular.hide()  # Esconde o botão inicialmente
        layout.addWidget(self.botao_calcular)
        
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

# Classe para a segunda página
class PaginaDois(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página Dois")
        self.setGeometry(100, 100, 300, 360)

        layout = QVBoxLayout()

        # Adiciona três botões que levam para a página em branco
        botao1 = QPushButton('Gasolina')
        botao1.clicked.connect(self.abrir_pagina_em_branco)
        layout.addWidget(botao1)

        botao2 = QPushButton('Etanol')
        botao2.clicked.connect(self.abrir_pagina_em_branco)
        layout.addWidget(botao2)

        botao3 = QPushButton('Gasolina Adtivada')
        botao3.clicked.connect(self.abrir_pagina_em_branco)
        layout.addWidget(botao3)

        self.setLayout(layout)

    # Função para abrir a página em branco
    def abrir_pagina_em_branco(self):
        self.hide( )
        self.pagina_em_branco = paginaTres()
        pagina_2_geometry = self.geometry()
        self.pagina_em_branco.setGeometry(pagina_2_geometry)
        self.pagina_em_branco.show()



# Classe para a página inicial
class PaginaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página Inicial")
        self.setGeometry(100, 100, 300, 360)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#007c84"))
        self.setPalette(paleta)

        layout = QVBoxLayout()


        # Nome do aplicativo
        titulo_app = QLabel("έλαιο")
        titulo_app.setAlignment(Qt.AlignCenter)
        titulo_app.setStyleSheet("font-size: 60px; font-weight: calibri;")
        layout.addWidget(titulo_app)

        # Mensagem de boas-vindas
        mensagem_boas_vindas = QLabel("Bem-vindo")
        mensagem_boas_vindas.setStyleSheet("font-size: 20px; font-weight: bold;")
        mensagem_boas_vindas.setAlignment(Qt.AlignCenter)
        layout.addWidget(mensagem_boas_vindas)


        self.imagem_label = QLabel()
        pixmap = QPixmap("imagem.png")  # Substitua "imagem_inicial.png" pelo caminho da sua imagem
        self.imagem_label.setPixmap(pixmap)
        self.imagem_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.imagem_label)
    
        # Botão que leva à segunda página
        botao_para_pagina_dois = QPushButton('start')
        botao_para_pagina_dois.clicked.connect(self.abrir_pagina_dois)
        layout.addWidget(botao_para_pagina_dois)


        self.setLayout(layout)

    # Função para abrir a segunda página
    def abrir_pagina_dois(self):
        self.hide( )
        self.pagina_dois = PaginaDois()
        pagina_1_geometry = self.geometry()
        self.pagina_dois.setGeometry(pagina_1_geometry)
        self.pagina_dois.show()

# Cria a aplicação
app = QApplication([])

# Cria e exibe a página inicial
pagina_inicial = PaginaInicial()
pagina_inicial.show()

# Executa a aplicação
app.exec()
