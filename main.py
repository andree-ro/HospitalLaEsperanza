import sys
from PyQt5.QtWidgets import QApplication
from views import VentanaPrincipal

app = QApplication(sys.argv)
mi_app = VentanaPrincipal()
mi_app.show()
sys.exit(app.exec())