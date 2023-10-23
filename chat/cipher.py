import hashlib
import datetime
def get_note_id(text: str, salt: str) -> str:
    return hashlib.sha256(
        text.encode('UTF-8') + salt.encode('UTF-8') + str(datetime.datetime.now()).encode('UTF-8')
    ).hexdigest()