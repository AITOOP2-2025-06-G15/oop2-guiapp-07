import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from src.lecture05_01 import capture_image,change_image,save_image,preview_image

class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("画像処理アプリケーション")
        self.setMinimumSize(400, 200)

        self.preview_window = None


        ##ボタンの定義
        self.btn_capture = QPushButton("画像取得")
        self.btn_change = QPushButton("画像置換")
        self.btn_save = QPushButton("画像保存")

        # レイアウト
        layout = QVBoxLayout()

        self.btn_capture.clicked.connect(self.capture_image)
        self.btn_change.clicked.connect(self.change_image)
        self.btn_save.clicked.connect(self.save_image)

        layout.addWidget(self.btn_capture)
        layout.addWidget(self.btn_change)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

        # 保存用に画像データを保持
        self.captured_image = None
        self.changed_image = None

    ##ボタンから関数呼び出し
    def capture_image(self):
        self.captured_image = capture_image()
        self.show_preview(self.captured_image)

    def change_image(self):
        if self.captured_image is None:
            print("先に画像を保存してください")
            return
        self.changed_image = change_image(self.captured_image)
        self.show_preview(self.changed_image)
    
    def save_image(self):
        if self.captured_image is None:
            print("保存するための画像がありません")
            return
        save_image(self.changed_image)
        print("保存が完了しました。")

    def show_preview(self, img):
        self.preview_window.set_image(img)
        self.preview_window.show()

class PreviewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("プレビュー")
        self.resize(600, 400)

        self.label = QLabel()
        self.label.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def set_image(self, img):
        """
        img は numpy 配列(OpenCV画像)を想定
        """
        if img is None:
            return

        # OpenCV(BGR) → RGB変換
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w

        qimage = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)

        self.label.setPixmap(pixmap)
        self.label.repaint()






