from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, field_validator, model_validator


class LogEntry(BaseModel):
    call_sign: str = Field(
        ...,
        min_length=3,
        max_length=10,
        pattern=r"^[a-zA-Z0-9]{1,3}[0-9][a-zA-Z0-9]{0,3}[a-zA-Z]$",
    )
    frequency: int = Field(..., gt=0, description="Frequency in kHz")
    mode: str = Field(
        ...,
        min_length=2,
        max_length=10,
        description="Operating mode, e.g., SSB, CW, FM",
    )
    signal_report_received: Optional[str] = Field(
        None, pattern=r"^\d{2}$", description="Signal report received, two digits"
    )
    signal_report_sent: Optional[str] = Field(
        None, pattern=r"^\d{2}$", description="Signal report sent, two digits"
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Date and time of the contact",
    )
    notes: Optional[str] = Field(None, max_length=200)

    # Additional fields
    qth: Optional[str] = Field(None, description="Location of the contact")
    operator_name: Optional[str] = Field(None, description="Name of the operator")
    country: Optional[str] = Field(None, description="Country of the contact")
    power: Optional[int] = Field(None, gt=0, description="Power output in watts")
    band: Optional[str] = Field(None, description="Band used for the contact")
    grid_square: Optional[str] = Field(
        None,
        pattern=r"^[A-Ra-r]{2}[0-9]{2}[A-Xa-x]{0,2}[0-9]{0,2}$",
        description="Maidenhead Grid Square",
    )
    comments: Optional[str] = Field(
        None, max_length=300, description="Additional comments or notes"
    )

    @field_validator("call_sign")
    def validate_call_sign(cls, value):
        if not value.isalnum():
            raise ValueError("Call sign must be alphanumeric")
        return value.upper()

    @field_validator("signal_report_received", "signal_report_sent")
    def validate_signal_report(cls, value):
        if value and not (10 <= int(value) <= 59):
            raise ValueError("Signal report must be a two-digit number between 10 and 59")
        return value

    @model_validator(mode="before")
    def set_band(cls, values):
        frequency = values.get("frequency")
        if frequency:
            values["band"] = cls.identify_band(frequency)
        return values

    @staticmethod
    def identify_band(frequency: int) -> str:
        """Identify the amateur radio band based on the frequency in kHz."""
        if 1800 <= frequency < 2000:
            return "160m"
        elif 3500 <= frequency < 4000:
            return "80m"
        elif 7000 <= frequency < 7300:
            return "40m"
        elif 10100 <= frequency < 10150:
            return "30m"
        elif 14000 <= frequency < 14350:
            return "20m"
        elif 18068 <= frequency < 18168:
            return "17m"
        elif 21000 <= frequency < 21450:
            return "15m"
        elif 24890 <= frequency < 24990:
            return "12m"
        elif 28000 <= frequency < 29700:
            return "10m"
        elif 50000 <= frequency < 54000:
            return "6m"
        elif 144000 <= frequency < 148000:
            return "2m"
        elif 222000 <= frequency < 225000:
            return "1.25m"
        elif 420000 <= frequency < 450000:
            return "70cm"
        elif 902000 <= frequency < 928000:
            return "33cm"
        elif 1240000 <= frequency < 1300000:
            return "23cm"
        else:
            return "Unknown"


# Example usage
log_entry = LogEntry(
    call_sign="W5MYR",
    frequency=14070,  # Frequency in kHz
    mode="PSK31",
    signal_report_received="59",
    signal_report_sent="59",
    qth="Houston, TX",
    operator_name="John Doe",
    country="United States",
    power=100,
    grid_square="EM10",
    comments="First contact on 20m using new antenna",
)
print(log_entry)
