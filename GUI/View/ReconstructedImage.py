from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel

from GUI.View.Module import Module
from Parameters import input_path, image_name


class ReconstructedImage(Module):
    def __init__(self, main_window):
        super().__init__(main_window, "Reconstructed Image")
        self.img = QLabel(self)
        pixmap = QPixmap(input_path+image_name)
        pixmap = pixmap.scaled(480, 270)
        self.img.setPixmap(pixmap)
        self.layout.addWidget(self.img)

    def set_image(self, imgQt):
        QtImage2 = QImage(imgQt)
        print(QtImage2.colorCount())
        pixmap = QPixmap.fromImage(QtImage2)
        pixmap = pixmap.scaled(480, 270)
        self.img.setPixmap(pixmap)


