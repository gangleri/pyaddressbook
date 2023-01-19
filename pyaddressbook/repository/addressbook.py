from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from pyaddressbook.models import Contact as ContactModel

Base = declarative_base()


class Contact(Base):
    """
    A SQLAlchemy model representing a contact in the address book.
    """

    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    def to_model(self) -> ContactModel:
        """
        Convert the SQLAlchemy model to a plain Python model.

        Returns:
            - ContactModel: A plain Python representation of the contact.
        """
        return ContactModel(
            id=self.id, name=self.name, email=self.email, phone=self.phone
        )


class ContactRepository:
    """
    A repository for performing CRUD operations on contacts.
    """

    def __init__(self, session: Optional[Session] = None):
        """
        Initialize a new instance of the repository.

        Parameters:
            - session (Session, optional): An instance of SQLAlchemy's session. If not provided, a new session will be created.
        """
        self.session = session or Session()

    def create_contact(self, contact: ContactModel) -> ContactModel:
        """
        Create a new contact.

        Parameters:
            - contact (ContactModel): The contact details.

        Returns:
            - ContactModel: The contact details.
        """
        db_contact = Contact(
            name=contact.name, email=contact.email, phone=contact.phone
        )
        self.session.add(db_contact)
        self.session.commit()
        return db_contact.to_model()

    def get_contact(self, id: int) -> ContactModel:
        """
        Retrieve a single contact by ID.

        Parameters:
            - id (int): The ID of the contact.

        Returns:
            - ContactModel: The contact details.
        """
        db_contact = self.session.query(Contact).filter_by(id=id).first()
        return db_contact.to_model()

    def list_contacts(self) -> list[ContactModel]:
        """
        Retrieve a list of all contacts.

        Returns:
            - list[ContactModel]: A list of contact details.
        """
        db_contacts = self.session.query(Contact).all()
        return [db_contact.to_model() for db_contact in db_contacts]

    def update_contact(self, id: int, contact: ContactModel) -> ContactModel:
        """
        Update a contact by ID.

        Parameters:
            - contact_id (int): The ID of the contact.
            - contact (dict): The contact details to update.

        Returns:
            - dict: The updated contact details.
        """
        self.session.query(Contact).filter_by(id=id).update(
            contact.dict(exclude_unset=True)
        )
        self.session.commit()
        return self.get_contact(id)

    def delete_contact(self, contact_id: int) -> None:
        """
        Delete a contact by ID.

        Parameters:
            - contact_id (int): The ID of the contact.

        Returns:
            - None
        """
        db_contact = self.session.query(Contact).filter_by(id=contact_id).first()
        self.session.delete(db_contact)
        self.session.commit()
