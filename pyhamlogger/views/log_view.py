from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QHeaderView, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget)


class LogView(QWidget):
    entry_selected = pyqtSignal(int)  # Signal to indicate that a row has been selected

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(8)  # Increase column count to 8 for the UUID
        self.table.setHorizontalHeaderLabels(
            [
                "Call Sign",
                "Frequency (kHz)",
                "Mode",
                "Rpt Rcvd",
                "Rpt Sent",
                "Notes",
                "Timestamp",
                "UUID",
            ]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        # Hide the UUID column
        self.table.setColumnHidden(7, True)

        # Connect the cellDoubleClicked signal to our custom slot
        self.table.cellDoubleClicked.connect(self.on_cell_double_clicked)

    def add_log_entry(self, log_entry):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(log_entry.call_sign))
        self.table.setItem(row_position, 1, QTableWidgetItem(str(log_entry.frequency)))
        self.table.setItem(row_position, 2, QTableWidgetItem(log_entry.mode))
        self.table.setItem(row_position, 3, QTableWidgetItem(log_entry.signal_report_received))
        self.table.setItem(row_position, 4, QTableWidgetItem(log_entry.signal_report_sent))
        self.table.setItem(row_position, 5, QTableWidgetItem(log_entry.notes))
        self.table.setItem(
            row_position, 6, QTableWidgetItem(self.format_timestamp(log_entry.timestamp))
        )
        self.table.setItem(
            row_position, 7, QTableWidgetItem(str(log_entry.entry_id))
        )  # Add UUID to hidden column

    def format_timestamp(self, utc_timestamp):
        """Convert the UTC timestamp to local time and format it as a string, including the time zone."""
        local_time = utc_timestamp.astimezone()
        return local_time.strftime("%Y-%m-%d %H:%M:%S %z")

    def on_cell_double_clicked(self, row, column):
        """Emit a signal with the row index when a cell is double-clicked."""
        self.entry_selected.emit(row)
