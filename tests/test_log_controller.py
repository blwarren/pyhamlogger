import uuid
from unittest.mock import MagicMock

import pytest

from pyhamlogger.controllers.log_controller import LogController


@pytest.fixture
def mock_view():
    """Create a mock view object."""
    view = MagicMock()
    view.call_sign_input.text.return_value = "W5MYR"
    view.frequency_input.text.return_value = "14000"
    view.mode_input.text.return_value = "SSB"
    view.signal_report_received_input.text.return_value = "59"
    view.signal_report_sent_input.text.return_value = "59"
    view.notes_input.text.return_value = "Test entry"
    return view


def test_log_contact(mock_view):
    """Test logging a new contact using the LogController."""
    controller = LogController(mock_view)
    controller.db.add_log_entry = MagicMock()  # Mock the database interaction
    controller.log_contact()

    # Check that the add_log_entry method was called
    controller.db.add_log_entry.assert_called_once()


def test_edit_contact(mock_view):
    """Test editing an existing contact using the LogController."""
    controller = LogController(mock_view)
    controller.db.update_log_entry = MagicMock()  # Mock the database interaction
    entry_id = uuid.uuid4()
    controller.edit_contact(entry_id)

    # Check that the update_log_entry method was called
    controller.db.update_log_entry.assert_called_once()
