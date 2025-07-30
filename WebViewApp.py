from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
import sys

class WebViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PalHandler Viewer")

        view = QWebEngineView(self)
        view.load(QUrl("https://palhandler123forwebview.free.nf/exp.html"))
        self.setCentralWidget(view)

        # 📺 Match screen resolution
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("🛑 Esc pressed — exiting viewer.")
            QApplication.quit()

if __name__ == "__main__":
    print("🚀 PalHandler Viewer adapting to your screen...")
    app = QApplication(sys.argv)
    window = WebViewApp()
    window.show()
    sys.exit(app.exec())
