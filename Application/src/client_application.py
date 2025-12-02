#Cyber Clinic Standalone Application - Main entry point
#CS 425 Team 13 - Fall 2025

import sys
import os
from dotenv import load_dotenv
import permission_handler as perms
import Application.src.backend_handler as backend
import platform
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QDialog,
    QFormLayout,
    QPushButton,
    QWidget
)

class Form(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CyberClinic Authentication")

        layout = QFormLayout()

        self.l = QLabel("Please enter your CyberClinic Email and Password.")
        self.l.setMargin(10)

        self.e = QLineEdit()
        self.e.setPlaceholderText("Email")
        self.p = QLineEdit()
        self.p.setPlaceholderText("Password")
        self.p.setEchoMode(QLineEdit.EchoMode.Password)

        self.s = QPushButton("Submit")
        self.s.setDefault(1)
        self.s.clicked.connect(self.verify_user)

        widgets = [
            self.l,
            self.e,
            self.p,
            self.s
        ]

        for w in widgets:
            layout.addWidget(w)

        self.setLayout(layout)
        self.show()

    def verify_user(self):
        email = self.e.text()
        passwd = self.p.text()

        print(f"{email}: {passwd}")

        self.l.setText("Verifying...")


if __name__ == '__main__':
    load_dotenv()
    system = platform.system()
    if not(perms.is_admin(system)):
        perms.request_admin_privileges(system)
        if not(perms.is_admin(system)):
            sys.exit("Please re-run with administrative privleges!")

    app = QApplication(sys.argv)  
    w = Form()
    app.exec()
