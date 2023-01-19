from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pyaddressbook.models import ContactIn, ContactPatch


def get_routes(repo) -> APIRouter:
    """
    Create and return an instance of APIRouter with routes for the contact endpoints.

    Parameters:
        - repo (Repository): An instance of the Repository for performing CRUD operations on the contact resource.

    Returns:
        - router (APIRouter): An instance of APIRouter with the contact routes.
    """
    router = APIRouter(prefix="/addressbook")

    @router.options("/v1/contacts")
    async def contact_options():
        return JSONResponse(content={}, headers={"Access-Control-Allow-Methods": "GET"})

    @router.options("/v1/contacts/{contact_id}")
    async def contact_options():
        return JSONResponse(content={}, headers={"Access-Control-Allow-Methods": "GET,POST,PATCH,DELETE"})

    @router.get("/v1/contacts")
    async def list_contacts():
        """
        Endpoint for listing all contacts.

        Returns:
            - list: A list of contacts.
        """
        return repo.list_contacts()

    @router.get("/v1/contacts/{contact_id}")
    async def get_contact(contact_id: int):
        """
        Endpoint for retrieving a single contact by ID.

        Parameters:
            - contact_id (int): The ID of the contact to retrieve.

        Returns:
            - dict: The contact details.
        """
        return repo.get_contact(contact_id)

    @router.post("/v1/contacts", status_code=status.HTTP_201_CREATED)
    async def create_contact(contact: ContactIn):
        """
        Endpoint for creating a new contact.

        Parameters:
            - contact (ContactIn): The contact details.

        Returns:
            - dict: The contact details.
        """
        return repo.create_contact(contact)

    @router.patch("/v1/contacts/{contact_id}")
    async def update_contact(contact_id: int, contact: ContactPatch):
        """
        Endpoint for updating a contact by ID.

        Parameters:
            - contact_id (int): The ID of the contact to update.
            - contact (ContactPatch): The contact details to update.

        Returns:
            - dict: The contact details.
        """
        return repo.update_contact(contact_id, contact)

    @router.delete("/v1/contacts/{contact_id}")
    async def delete_contact(contact_id: int):
        """
        Endpoint for deleting a contact by ID.

        Parameters:
            - contact_id (int): The ID of the contact to delete.

        Returns:
            - bool: True if the contact was deleted, False otherwise.
        """
        return repo.delete_contact(contact_id)

    return router
