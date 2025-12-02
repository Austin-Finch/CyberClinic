from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget
)

import dotenv
import sys
import permission_handler as perms
import platform

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CyberClinic Authentication")

        layout = QVBoxLayout()

        l = QLabel("Please enter your CyberClinic Email and Password.")
        l.setMargin(10)

        e = QLineEdit()
        p = QLineEdit()
        p.setEchoMode(QLineEdit.EchoMode.Password)

        s = QPushButton("Submit")

        widgets = [
            l,
            e,
            p,
            s
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()



if __name__ == '__main__':
    system = platform.system()
    if not(perms.is_admin(system)):
        perms.request_admin_privileges(system)
        if not(perms.is_admin(system)):
            sys.exit("Please re-run with administrative privleges!")
    
    app = QApplication(sys.argv)  
    w = MainWindow()
    app.exec()
