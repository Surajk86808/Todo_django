from fastapi import FastAPI, HTTPException
from typing import List
from app.notes.services import (
    create_note,
    get_note,
    get_all_notes,
    update_note,
    patch_note,
    delete_note,
)
from app.notes.schemas import NoteCreate, NoteUpdate, NotePatch, NoteResponse

app = FastAPI()


@app.post("/notes/", response_model=NoteResponse)
async def create_note_route(new_note: NoteCreate):
    """Create a new note."""
    return await create_note(title=new_note.title, content=new_note.content)


@app.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note_route(note_id: int):
    """Get a note by ID."""
    note = await get_note(note_id=note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.get("/notes/", response_model=List[NoteResponse])
async def get_all_notes_route():
    """Get all notes."""
    return await get_all_notes()


@app.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note_route(note_id: int, updated_note: NoteUpdate):
    """Update a note by ID."""
    return await update_note(note_id=note_id, title=updated_note.title, content=updated_note.content)


@app.patch("/notes/{note_id}", response_model=NoteResponse)
async def patch_note_route(note_id: int, patch_data: NotePatch):
    """Patch a note by ID."""
    return await patch_note(note_id=note_id, title=patch_data.title, content=patch_data.content)


@app.delete("/notes/{note_id}")
async def delete_note_route(note_id: int):
    """Delete a note by ID."""
    return await delete_note(note_id=note_id)
