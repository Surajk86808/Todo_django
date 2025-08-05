from app.db.config import  async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException

async def create_note(title:str,content:str):
    async with async_session() as session:
        note = Note(title=title, content=content)
        session.add(note)
        await session.commit()
        return note
    
async def get_note(note_id:int):
    async with async_session() as session:
        query = select(Note).where(Note.id == note_id)
        result = await session.execute(query)
        note = result.scalar_one_or_none()
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note
    
    
async def get_all_notes():
    async with async_session() as session:
        query = select(Note)
        result = await session.execute(query)
        notes = result.scalars().all()
        return notes 
    
async def update_note(note_id:int, title:str, content:str):
    async with async_session() as session:
        query = select(Note).where(Note.id == note_id)
        result = await session.execute(query)
        note = result.scalar_one_or_none()
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        
        note.title = title
        note.content = content
        await session.commit()
        return note
    
async def patch_note(note_id:int, title:str = None, content:str = None):
    async with async_session() as session:
        query = select(Note).where(Note.id == note_id)
        result = await session.execute(query)
        note = result.scalar_one_or_none()
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        
        if title is not None:
            note.title = title
        if content is not None:
            note.content = content
        
        await session.commit()
        return note
    
async def delete_note(note_id:int):
    async with async_session() as session:
        query = select(Note).where(Note.id == note_id)
        result = await session.execute(query)
        note = result.scalar_one_or_none()
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        
        await session.delete(note)
        await session.commit()
        return {"detail": "Note deleted successfully"}                    