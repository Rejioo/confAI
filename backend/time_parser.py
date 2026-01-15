from datetime import datetime, timedelta
import re

def extract_date_time(message: str):
    msg = message.lower()
    now = datetime.now()

    date = None
    start_time = None
    end_time = None

    if "tomorrow" in msg:
        date = (now + timedelta(days=1)).strftime("%Y-%m-%d")

    if "today" in msg:
        date = now.strftime("%Y-%m-%d")

    # time range: "2pm to 3pm"
    range_match = re.search(r"(\d{1,2})\s*(am|pm)\s*to\s*(\d{1,2})\s*(am|pm)", msg)
    if range_match:
        start_hour = int(range_match.group(1))
        end_hour = int(range_match.group(3))

        if range_match.group(2) == "pm" and start_hour != 12:
            start_hour += 12
        if range_match.group(4) == "pm" and end_hour != 12:
            end_hour += 12

        start_time = f"{start_hour:02d}:00"
        end_time = f"{end_hour:02d}:00"

        return date, start_time, end_time

    # single time: "4pm"
    single_match = re.search(r"(\d{1,2})\s*(am|pm)", msg)
    if single_match:
        hour = int(single_match.group(1))
        if single_match.group(2) == "pm" and hour != 12:
            hour += 12
        start_time = f"{hour:02d}:00"

    return date, start_time, end_time
