import sys
from app.windows import MainWindow
from PySide6 import QtWidgets, QtCore, QtGui

def main():
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("@tousef_refuge")
    QtCore.QCoreApplication.setOrganizationDomain("MinecraftBackupManagement")
    app.setWindowIcon(QtGui.QIcon("textures/logo.svg"))

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()