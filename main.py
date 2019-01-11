import tkinter as tk
import screenshot
from PyQt5 import QtWidgets
import sys
from google.cloud import vision
import io



def take_screenshot():
    app = QtWidgets.QApplication(sys.argv)
    window = screenshot.MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)

def analyze_screenshot():
    client = vision.ImageAnnotatorClient()
    with io.open('capture.png', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations



if __name__ == '__main__':
    m = tk.Tk()
    screenshot_button = tk.Button(m, text='screenshot', width=25, command=take_screenshot)
    screenshot_button.pack()
    analyze_screenshot_button = tk.Button(m, text='analyze screenshot', width=25, command=analyze_screenshot)
    analyze_screenshot_button.pack()
    m.mainloop()