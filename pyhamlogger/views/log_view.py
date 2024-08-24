from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView


class LogView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)  # Adding an extra column for the timestamp
        self.table.setHorizontalHeaderLabels(
            ["Call Sign", "Frequency (kHz)", "Mode", "Rpt Rcvd", "Rpt Sent", "Notes", "Timestamp"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

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

    def format_timestamp(self, utc_timestamp):
        """Convert the UTC timestamp to local time and format it as a string, including the time zone."""
        # Convert the UTC datetime to local time
        local_time = utc_timestamp.astimezone()
        return local_time.strftime("%Y-%m-%d %H:%M:%S %z")  # Format as a string including time zone
