KNOWN_USERS = {"rajit", "adam", "julie"}

def extract_participants_from_text(message: str):
    msg = message.lower()
    found = []

    for name in KNOWN_USERS:
        if name in msg:
            found.append(name)

    return found
