from pydantic import BaseModel, Field

#shared base fields
class NoteBase(BaseModel):
    title: str = Field(..., max_length=100, description="Title of the note")
    content: str = Field(..., description="Content of the note")
    # tags: list[str] = Field(default_factory=list, description="List of tags associated with the note")
    
#schemas for creating and updating notes
class NoteCreate(NoteBase):
    """Schema for creating a new note."""
    pass    

#for full update
class NoteUpdate(NoteBase):
    """Schema for updating an existing note."""
    pass

#for partial update
class NotePatch(BaseModel):
    """Schema for partially updating a note."""
    title: str = Field(None, max_length=100, description="Title of the note")
    content: str = Field(None, description="Content of the note")
    # tags: list[str] = Field(None, description="List of tags associated with the note")
    
#for response seriliazation
class NoteResponse(NoteBase):
    """Schema for note response."""
    id: int = Field(..., description="ID of the note")
    
    class Config:
        orm_mode = True  # Enable ORM mode to read data from SQLAlchemy models    