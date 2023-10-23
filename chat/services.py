from .cipher import get_note_id
from .models import Message


def create_message_and_get_hash(form) -> str:
    """Создаёт записку в базе данных по заполненной форме. Возвращает hash записки."""
    secret_phrase = form.data['secret_phrase'].strip()
    text = form.data['text'].strip()
    note_hash = get_note_id(form.data['secret_phrase'][-1], form.data['text'][-1])

    Message.objects.create(text=text.strip(),
                        secret_phrase=secret_phrase.strip(),
                        note_hash=note_hash)
    
    return note_hash


def get_message_and_delete(form) -> dict:
    """Возвращает данные записки и удаляет её из БД."""
    secret_phrase = form.data['secret_phrase'].strip()
    note_hash = form.data['note_hash'].strip()
    try:
        message = Message.objects.get(note_hash=note_hash,
                                    secret_phrase=secret_phrase)
        data = {'text': message.text,
            'note_hash': message.note_hash,
            'secret_phrase': message.secret_phrase}
        
        message.delete()
    except:
        data = {'text': 'There is no one note by these ID and secret phrase.',
            'secret_phrase': 'Oops...'}

    return data
    
