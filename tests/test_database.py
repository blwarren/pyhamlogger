import pytest
from pyhamlogger.services.database import Database
from pyhamlogger.models.log_entry import LogEntry
import uuid
from datetime import datetime, timezone


@pytest.fixture
def db(tmp_path):
    """Fixture to provide a temporary database for testing."""
    db_path = tmp_path / "test_pyhamlogger.db"
    return Database(db_name=str(db_path))


def test_add_log_entry(db):
    """Test adding a log entry to the database."""
    entry_id = uuid.uuid4()
    log_entry = LogEntry(
        entry_id=entry_id,
        call_sign="W5MYR",
        frequency=14000,
        mode="SSB",
        signal_report_received="59",
        signal_report_sent="59",
        notes="Test entry",
        timestamp=datetime.now(timezone.utc),
    )

    db.add_log_entry(log_entry)
    retrieved_entry = db.get_log_entry_by_id(str(entry_id))

    assert retrieved_entry.call_sign == "W5MYR"
    assert retrieved_entry.frequency == 14000
    assert retrieved_entry.mode == "SSB"
    assert retrieved_entry.signal_report_received == "59"
    assert retrieved_entry.signal_report_sent == "59"
    assert retrieved_entry.notes == "Test entry"


def test_update_log_entry(db):
    """Test updating a log entry in the database."""
    entry_id = uuid.uuid4()
    log_entry = LogEntry(
        entry_id=entry_id,
        call_sign="W5MYR",
        frequency=14000,
        mode="SSB",
        signal_report_received="59",
        signal_report_sent="59",
        notes="Test entry",
        timestamp=datetime.now(timezone.utc),
    )

    db.add_log_entry(log_entry)

    # Modify the log entry
    log_entry.frequency = 14500
    log_entry.notes = "Updated entry"
    db.update_log_entry(log_entry)

    updated_entry = db.get_log_entry_by_id(str(entry_id))

    assert updated_entry.frequency == 14500
    assert updated_entry.notes == "Updated entry"
