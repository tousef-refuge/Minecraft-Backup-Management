import sys
from app import Application
from PySide6 import QtWidgets, QtCore, QtGui

def main():
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("@tousef_refuge")
    QtCore.QCoreApplication.setOrganizationDomain("MinecraftBackupManagement")
    app.setWindowIcon(QtGui.QIcon("textures/logo.svg"))

    application = Application()
    application.start()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()