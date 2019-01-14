from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
import numpy as np
import cv2
import sys


class ScreenShot(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ScreenShot, self).__init__(parent)
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        self.took_screenshot = True
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('capture.png')
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        self.parent().showNormal()
        self.parent().setWindowOpacity(1)
        self.parent().setWindowFlag(QtCore.Qt.Window)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.ArrowCursor)
        )
        cv2.imshow('Captured Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ScreenShot()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())