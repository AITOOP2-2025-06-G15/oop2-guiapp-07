from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QImage
import cv2
import numpy as np

class PreviewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("画像プレビュー")
        self.resize(600, 400)

        # QLabel に画像を表示
        self.label = QLabel()
        self.label.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def set_image(self, img: np.ndarray):
        """NumPy(OpenCV)画像をQt画像に変換して表示"""
        if img is None:
            print("画像がありません")
            return
        
        # OpenCV(BGR) → RGB に変換
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w

        # NumPy → QImage
        qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # QPixmap化
        pixmap = QPixmap.fromImage(qimg)

        # QLabel に設定
        self.label.setPixmap(pixmap)
        self.label.repaint()
