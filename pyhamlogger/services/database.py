import sqlite3
from pathlib import Path
from models.log_entry import LogEntry


class Database:
    def __init__(self, db_name="pyhamlogger.db"):
        self.db_path = self.get_database_path(db_name)
        self.connection = None
        self.connect()

    def get_database_path(self, db_name):
        """Determine the path to store the database in the 'data' directory."""
        # Assuming the 'data' folder is at the same level as 'models', 'controllers', etc.
        db_dir = Path(__file__).resolve().parent.parent / "data"
        db_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
        return db_dir / db_name

    def connect(self):
        """Establish a connection to the SQLite database."""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        """Create the log_entries table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS log_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    call_sign TEXT NOT NULL,
                    frequency INTEGER NOT NULL,
                    mode TEXT NOT NULL,
                    signal_report_received TEXT,
                    signal_report_sent TEXT,
                    notes TEXT,
                    timestamp TEXT NOT NULL
                )
            """)

    def add_log_entry(self, log_entry: LogEntry):
        """Insert a new log entry into the database."""
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO log_entries (call_sign, frequency, mode, signal_report_received, signal_report_sent, notes, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    log_entry.call_sign,
                    log_entry.frequency,
                    log_entry.mode,
                    log_entry.signal_report_received,
                    log_entry.signal_report_sent,
                    log_entry.notes,
                    log_entry.timestamp.isoformat(),
                ),
            )

    def get_all_log_entries(self):
        """Retrieve all log entries from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM log_entries")
        rows = cursor.fetchall()
        return [self.row_to_log_entry(row) for row in rows]

    def row_to_log_entry(self, row):
        """Convert a database row to a LogEntry object."""
        return LogEntry(
            call_sign=row["call_sign"],
            frequency=row["frequency"],
            mode=row["mode"],
            signal_report_received=row["signal_report_received"],
            signal_report_sent=row["signal_report_sent"],
            notes=row["notes"],
            timestamp=row["timestamp"],
        )

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
