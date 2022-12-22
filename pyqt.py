import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем три кнопки
        self.button1 = QPushButton('Кнопка 1')
        self.button2 = QPushButton('Кнопка 2')
        self.button3 = QPushButton('Кнопка 3')

        # Создаем вертикальный слой для размещения кнопок
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)

        # Связываем кнопки с функциями
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)

    def on_button1_clicked(self):
        QMessageBox.information(self, 'Кнопка 1', 'Кнопка 1 нажата')

    def on_button2_clicked(self):
        QMessageBox.information(self, 'Кнопка 2', 'Кнопка 2 нажата')

    def on_button3_clicked(self):
        QMessageBox.information(self, 'Кнопка 3', 'Кнопка 3 нажата')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
