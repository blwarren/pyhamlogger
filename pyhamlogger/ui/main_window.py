from controllers.log_controller import LogController
from PyQt6.QtWidgets import (
    QFormLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from services.database import Database
from views.log_view import LogView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyHamLogger")
        self.setGeometry(100, 100, 800, 600)

        self.editing_entry_id = None  # To keep track of the UUID of the contact being edited

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
        self.submit_button.clicked.connect(self.on_submit)

        # Connect the LogView's entry_selected signal to our slot
        self.log_view.entry_selected.connect(self.on_entry_selected)

        # Load the log entries from the database and display them
        self.load_log_entries()

    def on_entry_selected(self, row):
        """Populate the form with the selected entry's details."""
        print(self.log_view.table)
        item = self.log_view.table.item(row, 7)  # Column 7 corresponds to the UUID
        if item:
            entry_id = item.text()
            log_entry = self.controller.get_log_entry(entry_id)

            if log_entry:
                self.editing_entry_id = log_entry.entry_id  # Keep track of the UUID
                self.call_sign_input.setText(log_entry.call_sign)
                self.frequency_input.setText(str(log_entry.frequency))
                self.mode_input.setText(log_entry.mode)
                self.signal_report_received_input.setText(log_entry.signal_report_received or "")
                self.signal_report_sent_input.setText(log_entry.signal_report_sent or "")
                self.notes_input.setText(log_entry.notes or "")
                self.submit_button.setText("Save Contact")
        else:
            self.view.show_error("Failed to retrieve the UUID for the selected entry.")

    def on_submit(self):
        """Handle the submission of a new or edited contact."""
        if self.editing_entry_id:
            # Edit existing contact
            self.controller.edit_contact(self.editing_entry_id)
            self.editing_entry_id = None  # Reset after editing
            self.submit_button.setText("Log Contact")
        else:
            # Log new contact
            self.controller.log_contact()

        self.clear_form()

    def clear_form(self):
        """Clear the form after submission."""
        self.call_sign_input.clear()
        self.frequency_input.clear()
        self.mode_input.clear()
        self.signal_report_received_input.clear()
        self.signal_report_sent_input.clear()
        self.notes_input.clear()

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
