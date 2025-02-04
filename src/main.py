import sys
from PyQt5.QtWidgets import QApplication
from gui.app import MainApp
import tkinter as tk

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()