KNOWN_ROOMS = [
    "conference room a",
    "conference room b",
    "huddle room"
]

def extract_room_name(message: str):
    msg = message.lower()
    for room in KNOWN_ROOMS:
        if room in msg:
            return room.title()
    return None
