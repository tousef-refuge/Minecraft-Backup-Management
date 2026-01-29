import sys
from app import Application
from PySide6 import QtWidgets, QtCore

def main():
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("@tousef_refuge")
    QtCore.QCoreApplication.setOrganizationDomain("MinecraftBackupManagement")

    application = Application()
    application.start()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()