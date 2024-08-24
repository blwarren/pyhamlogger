from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
from controllers.log_controller import LogController
from views.log_view import LogView
from services.database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyHamLogger")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        form_layout = QFormLayout()

        self.call_sign_input = QLineEdit()
        form_layout.addRow("Call Sign:", self.call_sign_input)

        self.frequency_input = QLineEdit()
        form_layout.addRow("Frequency (kHz):", self.frequency_input)

        self.mode_input = QLineEdit()
        form_layout.addRow("Mode:", self.mode_input)

        self.signal_report_received_input = QLineEdit()
        form_layout.addRow("Signal Report Received:", self.signal_report_received_input)

        self.signal_report_sent_input = QLineEdit()
        form_layout.addRow("Signal Report Sent:", self.signal_report_sent_input)

        self.notes_input = QLineEdit()
        form_layout.addRow("Notes:", self.notes_input)

        layout.addLayout(form_layout)

        self.submit_button = QPushButton("Log Contact")
        layout.addWidget(self.submit_button)

        # Create the LogView and add it to the layout
        self.log_view = LogView(self)
        layout.addWidget(self.log_view)

        # Initialize the controller with this view
        self.controller = LogController(self)
        self.submit_button.clicked.connect(self.controller.log_contact)

        # Load the log entries from the database and display them
        self.load_log_entries()

    def load_log_entries(self):
        """Load log entries from the database and display them in the LogView."""
        db = Database()  # Initialize the database connection
        log_entries = db.get_all_log_entries()  # Fetch all log entries

        for entry in log_entries:
            self.log_view.add_log_entry(entry)  # Add each entry to the LogView

        db.close()  # Close the database connection

    def show_error(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Warning)
        error_box.setText(message)
        error_box.setWindowTitle("Error")
        error_box.exec()
