import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import Main_window 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()

    sys.exit(app.exec())