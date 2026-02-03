from PySide6 import QtCore, QtWidgets

def info_layout(widget, text):
    sublayout = QtWidgets.QHBoxLayout()
    info = QtWidgets.QLabel('ⓘ')
    info.setToolTip(text)
    sublayout.addWidget(widget, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
    sublayout.addWidget(info, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
    return sublayout