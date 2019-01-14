from screenshot import ScreenShot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from google.cloud import vision
import io


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'LOL Champ Select App'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        button = QPushButton('Screenshot', self)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        self.setWindowOpacity(0.3)
        self.showMaximized()
        self.showFullScreen()
        screenshot_window = ScreenShot(self)
        screenshot_window.show()

    def analyze_screenshot(self):
        client = vision.ImageAnnotatorClient()
        with io.open('capture.png', 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        for text in texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
