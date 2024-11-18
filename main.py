# Arquivo: main.py

import sys
from PyQt5.QtWidgets import QApplication
from pagina1 import PaginaInicial

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pagina_inicial = PaginaInicial()
    pagina_inicial.show()
    sys.exit(app.exec())
