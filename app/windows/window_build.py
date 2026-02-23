from PySide6 import QtCore, QtWidgets

from app.settings import SettingsList

def info_layout(widget, text):
    sublayout = QtWidgets.QHBoxLayout()
    info = QtWidgets.QLabel('ⓘ')
    info.setToolTip(text)
    sublayout.addWidget(widget, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
    sublayout.addWidget(info, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
    return sublayout

def world_history_widget():
    current_history = []
    for world in SettingsList("world_history"):
        current_history.append(world)
    current_history.reverse()

    widget = QtWidgets.QComboBox()
    widget.addItems(current_history)
    widget.setEditable(True)
    widget.setFixedWidth(200)
    return widget