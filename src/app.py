import sys
from PyQt6.QtWidgets import QApplication, QDialog
from vista.ui_main import Ui_Dialog
from logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar selección del ComboBox
        self.ui.comboBox.currentIndexChanged.connect(self.mostrar_pagina)
        self.ui.btnCalcular.clicked.connect(self.calcular_area)
        self.ui.actionSalir.clicked.connect(self.close)

    def mostrar_pagina(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        self.ui.lineResultado.clear()


    def calcular_area(self):
        figura = self.ui.comboBox.currentText()
        try:
            if figura == "CIRCULO":
                radio = self.ui.spinRadio.value()
                if radio <= 0:
                    raise ValueError("El radio debe ser positivo.")
                area = Circulo(radio).calcular_area()

            elif figura == "TRIANGULO":
                base = self.ui.spinBaseT.value()
                altura = self.ui.spinAlturaT.value()
                if base <= 0 or altura <= 0:
                    raise ValueError("Base y altura deben ser positivos.")
                area = Triangulo(base, altura).calcular_area()

            elif figura == "RECTANGULO":
                base = self.ui.spinBaseR.value()
                altura = self.ui.spinAlturaR.value()
                if base <= 0 or altura <= 0:
                    raise ValueError("Base y altura deben ser positivos.")
                area = Rectangulo(base, altura).calcular_area()

            elif figura == "CUADRADO":
                lado = self.ui.spinBaseR_2.value()
                if lado <= 0:
                    raise ValueError("El lado debe ser positivo.")
                area = Cuadrado(lado).calcular_area()

            else:
                self.ui.lineResultado.setText("Figura no válida.")
                return

            self.ui.lineResultado.setText(f"{area:.2f}")

        except ValueError as e:
            self.ui.lineResultado.setText(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MainDialog()
    dialogo.show()
    sys.exit(app.exec())