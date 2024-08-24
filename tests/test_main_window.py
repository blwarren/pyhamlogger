import pytest
from PyQt6.QtCore import Qt

from pyhamlogger.ui.main_window import MainWindow


@pytest.fixture
def main_window(qtbot):
    """Fixture to create the main window."""
    window = MainWindow()
    qtbot.addWidget(window)
    return window


def test_initial_ui_state(main_window):
    """Test the initial state of the main window UI."""
    assert main_window.call_sign_input.text() == ""
    assert main_window.frequency_input.text() == ""
    assert main_window.mode_input.text() == ""
    assert main_window.submit_button.text() == "Log Contact"


def test_log_contact(main_window, qtbot):
    """Test logging a new contact through the UI."""
    # Ensure the table is initially empty
    main_window.log_view.table.setRowCount(0)

    main_window.call_sign_input.setText("W5MYR")
    main_window.frequency_input.setText("14000")
    main_window.mode_input.setText("SSB")
    main_window.signal_report_received_input.setText("59")
    main_window.signal_report_sent_input.setText("59")
    main_window.notes_input.setText("Testing contact")

    qtbot.mouseClick(main_window.submit_button, Qt.MouseButton.LeftButton)

    # Check if the log entry was added to the table
    assert main_window.log_view.table.rowCount() == 1
    assert main_window.log_view.table.item(0, 0).text() == "W5MYR"


def test_edit_contact(main_window, qtbot):
    """Test editing an existing contact through the UI."""
    # Ensure the table is initially empty
    main_window.log_view.table.setRowCount(0)

    main_window.call_sign_input.setText("W5MYR")
    main_window.frequency_input.setText("14000")
    main_window.mode_input.setText("SSB")
    main_window.signal_report_received_input.setText("59")
    main_window.signal_report_sent_input.setText("59")
    main_window.notes_input.setText("Testing contact")

    qtbot.mouseClick(main_window.submit_button, Qt.MouseButton.LeftButton)

    # Now edit the contact
    main_window.log_view.table.selectRow(0)
    qtbot.mouseDClick(main_window.log_view.table.viewport(), Qt.MouseButton.LeftButton)

    main_window.frequency_input.setText("14500")
    main_window.notes_input.setText("Edited contact")

    qtbot.mouseClick(main_window.submit_button, Qt.MouseButton.LeftButton)

    # Check if the log entry was updated
    assert main_window.log_view.table.item(0, 1).text() == "14500"
    assert main_window.log_view.table.item(0, 5).text() == "Edited contact"
