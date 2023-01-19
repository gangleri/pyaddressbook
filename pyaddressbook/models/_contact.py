from typing import Optional
from pydantic import BaseModel


class ContactIn(BaseModel):
    name: str
    email: str
    phone: str


class ContactPatch(ContactIn):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class ContactOut(ContactIn):
    id: int


class Contact(ContactIn):
    id: int
