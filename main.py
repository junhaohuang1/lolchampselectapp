import tkinter as tk
import screenshot
from PyQt5 import QtWidgets
import sys

def take_screenshot():
    app = QtWidgets.QApplication(sys.argv)
    window = screenshot.MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())


if __name__ == '__main__':
    m = tk.Tk()
    button = tk.Button(m, text='screenshot', width=25, command=take_screenshot)
    button.pack()
    m.mainloop()