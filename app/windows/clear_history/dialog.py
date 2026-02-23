from PySide6 import QtWidgets

from app.logic import world_history

class Dialog(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirm")
        self.setText("Do you want to continue? This will\nclear your world history and is irreversible.")
        self.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No
        )

        response = self.exec_()
        if response == QtWidgets.QMessageBox.StandardButton.Yes:
            world_history.clear_history()
            QtWidgets.QMessageBox.information(
                self,
                "Success",
                "Your world history has been cleared."
            )

        self.close()