from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from estilos import estilo_botao
from pagina3 import *

class PaginaResultado(QWidget):
    def __init__(self, aprovado, valor, preco_por_litro, voltar_inicio_callback):
        super().__init__()
        self.setWindowTitle("Resultado do Pagamento")
        self.setGeometry(100, 100, 400, 360)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()

        # Mensagem de resultado
        if aprovado:
            mensagem = QLabel("Pagamento Aprovado!")
            mensagem.setStyleSheet("font-size: 24px; color: green; font-weight: bold;")
            
            valor_float = float(valor)
            litros = valor_float / preco_por_litro
            
            valor_label = QLabel(f"Valor Pago: R$ {valor_float:.2f}")
            valor_label.setStyleSheet("font-size: 18px; color: black; font-weight: bold;")
            
            litros_label = QLabel(f"Quantidade de Litros: {litros:.2f} L")
            litros_label.setStyleSheet("font-size: 18px; color: black; font-weight: bold;")
        else:
            mensagem = QLabel("Pagamento Recusado!")
            mensagem.setStyleSheet("font-size: 24px; color: red; font-weight: bold;")
            valor_label = QLabel("")
            litros_label = QLabel("")

        mensagem.setAlignment(Qt.AlignCenter)
        valor_label.setAlignment(Qt.AlignCenter)
        litros_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(mensagem)
        layout.addWidget(valor_label)
        layout.addWidget(litros_label)

        layout.addSpacerItem(QSpacerItem(60, 100, 60, 100))

        # Botão para voltar à página inicial
        botao_voltar = QPushButton('Voltar ao Início')
        botao_voltar.setStyleSheet(estilo_botao)
        botao_voltar.clicked.connect(voltar_inicio_callback)
        layout.addWidget(botao_voltar)

        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)