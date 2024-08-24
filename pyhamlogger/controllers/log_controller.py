from pydantic import ValidationError
from services.database import Database
from models.log_entry import LogEntry


class LogController:
    def __init__(self, view):
        self.view = view
        self.db = Database()  # Initialize the database connection

    def log_contact(self):
        try:
            # Create a LogEntry instance with the form data
            log_entry = LogEntry(
                call_sign=self.view.call_sign_input.text(),
                frequency=int(self.view.frequency_input.text()),  # Convert frequency to int
                mode=self.view.mode_input.text(),
                signal_report_received=self.view.signal_report_received_input.text(),
                signal_report_sent=self.view.signal_report_sent_input.text(),
                notes=self.view.notes_input.text(),
            )

            # Save the log entry to the database
            self.db.add_log_entry(log_entry)

            # Update the view to display the new log entry
            self.view.log_view.add_log_entry(log_entry)

        except ValidationError as e:
            # Handle validation errors
            self.view.show_error(f"Validation Error: {e}")

    def close(self):
        """Close the database connection."""
        self.db.close()
