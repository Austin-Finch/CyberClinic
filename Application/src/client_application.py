from PySide6 import QtWidgets
import dotenv
import sys
import permission_handler as perms
import platform

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CyberClinic Authentication")
        l = QtWidgets.QLabel("My simple app.")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()



if __name__ == '__main__':
    system = platform.system()
    if not(perms.is_admin(system)):
        perms.request_admin_privileges(system)
        if not(perms.is_admin(system)):
            sys.exit("Please re-run with administrative privleges!")
    
    app = QtWidgets.QApplication()  
    w = MainWindow()
    app.exec()
