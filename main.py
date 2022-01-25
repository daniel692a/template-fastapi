from fastapi import FastAPI, status
from typing import List
from note import Note

app = FastAPI(title='Notas', version='0.0.1', description='API para gestionar notas')
notes: List[Note] = []

@app.get('/', response_model=List[Note])
def show_notes():
    return notes

@app.post('/new-note/', response_model=Note)
def new_note(note:Note):
    note.id = len(notes)
    notes.append(note)
    return note

@app.get('/note/{id}', response_model=Note)
def get_note(id:int):
    return notes[id] if id < len(notes) else {"detail": "Not found"}


@app.delete('/delete-note/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id:int):
    for note in notes:
        if note.id == id:
            notes.remove(note)
            return "Note deleted"
    return "Error"

@app.put('/update/{id}', response_model=Note)
def update_note(id: int, note_udt: Note):
    update_nt = notes[id]
    update_nt.title = note_udt.title
    update_nt.content = note_udt.content
    return update_nt
