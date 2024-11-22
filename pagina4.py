from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem
from PyQt5.QtGui import QPalette, QColor

class PaginaQuatro(QWidget):
    def __init__(self, titulo, mensagem, litros):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, 400, 200)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()


        pag_apr= QLabel("pagamento aprovado")
        pag_apr.setStyleSheet("font-size: 24px; color: green; font-weight: bold;")
        layout.addWidget(pag_apr)

        layout.addSpacerItem(QSpacerItem(0, 0, 0, 200))

        label_mensagem = QLabel(mensagem)
        label_mensagem.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label_mensagem)

        label_litros = QLabel(f"Quantidade de litros abastecidos: {litros:.2f}")
        label_litros.setStyleSheet("font-size: 14px;")
        layout.addWidget(label_litros)

        botao_voltar = QPushButton("Voltar")
        botao_voltar.clicked.connect(self.close)  # Fecha a página
        layout.addWidget(botao_voltar)

        layout.setContentsMargins(200, 20, 200, 20)
        self.setLayout(layout)