from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QWidget, QBoxLayout, QPushButton, QLineEdit, QLabel
import sys

class Conculyator(QWidget):
    def btn_0_a(self):
        self.action("0")

    def btn_1_a(self):
        self.action("1")

    def btn_2_a(self):
        self.action("2")

    def btn_3_a(self):
        self.action("3")

    def btn_4_a(self):
        self.action("4")

    def btn_5_a(self):
        self.action("5")

    def btn_6_a(self):
        self.action("6")

    def btn_7_a(self):
        self.action("7")

    def btn_8_a(self):
        self.action("8")

    def btn_9_a(self):
        self.action("9")

    def btn_comma_a(self):
        self.action(".")

    def btn_size_a(self):
        self.action("=")

    def btn_bolinma_a(self):
        self.action("÷")

    def btn_kopaytma_a(self):
        self.action("×")

    def btn_qosh_a(self):
        self.action("+")

    def btn_ayirma_a(self):
        self.action("-")

    def btn_foyz_a(self):
        self.action("%")

    def btn_manfi_a(self):
        text = self.label.text()
        self.label.setText("-" + text)

    def btn_clear_a(self):
        self.label.setText("")


    def action(self, i):
        self.i = i
        text = self.label.text()
        if self.i != "=":
            self.label.setText(text + f'{self.i}')
        else:
            self.label.setText(f"{eval(text)}")

    def qoshish(self, a, b, c, d, e):
        a.addWidget(b)
        a.addWidget(c)
        a.addWidget(d)
        a.addWidget(e)

    def  __init__(self):

        super().__init__()

        self.label = QLabel()

        self.v_box = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()

        self.btn_0 = QPushButton("0")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_comma = QPushButton(",")
        self.btn_size = QPushButton("=")
        self.btn_bolinma = QPushButton("÷")
        self.btn_kopaytma = QPushButton("×")
        self.btn_qosh = QPushButton("+")
        self.btn_ayirma = QPushButton("-")
        self.btn_foyz = QPushButton("%")
        self.btn_clear = QPushButton("AC")
        self.btn_manfi = QPushButton("+/-")


        self.qoshish(self.h_box5, self.btn_clear, self.btn_manfi, self.btn_foyz, self.btn_bolinma)
        self.qoshish(self.h_box4, self.btn_7, self.btn_8, self.btn_9, self.btn_kopaytma)
        self.qoshish(self.h_box3, self.btn_4, self.btn_5, self.btn_6, self.btn_ayirma)
        self.qoshish(self.h_box2, self.btn_1, self.btn_2, self.btn_3, self.btn_qosh)

        self.h_box1.addWidget(self.btn_0)
        self.h_box1.addWidget(self.btn_comma)
        self.h_box1.addWidget(self.btn_size)

        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box1)

        self.btn_0.clicked.connect(self.btn_0_a)
        self.btn_1.clicked.connect(self.btn_1_a)
        self.btn_2.clicked.connect(self.btn_2_a)
        self.btn_3.clicked.connect(self.btn_3_a)
        self.btn_4.clicked.connect(self.btn_4_a)
        self.btn_5.clicked.connect(self.btn_5_a)
        self.btn_6.clicked.connect(self.btn_6_a)
        self.btn_7.clicked.connect(self.btn_7_a)
        self.btn_8.clicked.connect(self.btn_8_a)
        self.btn_9.clicked.connect(self.btn_9_a)
        self.btn_comma.clicked.connect(self.btn_comma_a)
        self.btn_size.clicked.connect(self.btn_size_a)
        self.btn_bolinma.clicked.connect(self.btn_bolinma_a)
        self.btn_kopaytma.clicked.connect(self.btn_kopaytma_a)
        self.btn_qosh.clicked.connect(self.btn_qosh_a)
        self.btn_ayirma.clicked.connect(self.btn_ayirma_a)
        self.btn_foyz.clicked.connect(self.btn_foyz_a)
        self.btn_clear.clicked.connect(self.btn_clear_a)
        self.btn_manfi.clicked.connect(self.btn_manfi_a)

        self.setLayout(self.v_box)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    win = Conculyator()
    sys.exit(app.exec_())
