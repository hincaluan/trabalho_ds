from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem
from PyQt5.QtGui import QPalette, QColor, QPainter, QBrush
from PyQt5.QtCore import Qt, QTimer
import random

class PaginaQuatro(QWidget):
    def __init__(self, titulo, mensagem, litros):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, 400, 300)

        # Configuração de cor do fundo
        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#ffede2"))
        self.setPalette(paleta)

        layout = QVBoxLayout()

        # Mensagem principal
        pag_apr = QLabel("Pagamento Aprovado")
        pag_apr.setStyleSheet("font-size: 24px; color: green; font-weight: bold;")
        layout.addWidget(pag_apr)

        layout.addSpacerItem(QSpacerItem(0, 0, 0, 200))

        # Mensagem personalizada
        label_mensagem = QLabel(mensagem)
        label_mensagem.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label_mensagem)

        # Quantidade de litros
        label_litros = QLabel(f"Quantidade de litros abastecidos: {litros:.2f}")
        label_litros.setStyleSheet("font-size: 14px;")
        layout.addWidget(label_litros)

        # Botão para voltar
        botao_voltar = QPushButton("encerrar")
        botao_voltar.clicked.connect(self.close)  # Fecha a página
        layout.addWidget(botao_voltar)

        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

        # Timer para fogos de artifício
        self.fogos = []  # Lista para armazenar as partículas dos fogos
        self.timer = QTimer()
        self.timer.timeout.connect(self.criar_fogos)
        self.timer.start(100)  # Fogos a cada 100ms

        # Timer para atualizar a tela (animação)
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update)
        self.update_timer.start(30)  # Atualiza a cada 30ms

    def criar_fogos(self):
        """Cria partículas de fogos em posições aleatórias."""
        for _ in range(10):  # Cria várias partículas de uma vez
            x = random.randint(50, self.width() - 50)
            y = random.randint(50, self.height() - 150)
            cor = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.fogos.append({"x": x, "y": y, "cor": cor, "raio": 5})

    def paintEvent(self, event):
        """Desenha os fogos na tela."""
        painter = QPainter(self)
        for fogo in self.fogos:
            painter.setBrush(QBrush(fogo["cor"]))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(fogo["x"], fogo["y"], fogo["raio"], fogo["raio"])

        # Atualiza as partículas (expansão e desaparecimento)
        for fogo in self.fogos:
            fogo["raio"] += 2  # Expande o fogo
            fogo["cor"].setAlpha(max(0, fogo["cor"].alpha() - 15))  # Reduz a opacidade

        # Remove fogos que desapareceram
        self.fogos = [fogo for fogo in self.fogos if fogo["cor"].alpha() > 0]
