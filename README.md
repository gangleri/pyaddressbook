# PyAddressBook

PyAddressBook is a simple address book application built using FastAPI and SQLAlchemy 
for the backend and sqlite as the database. It provides a RESTful API for managing 
contacts.

## Features

- Create, read, update and delete contacts
- List all contacts
- Retrieve a contact by ID
- Validation and error handling
- Exception logging 

## Installation

Clone this repository and install the required packages by running

```bash
poetry install
```

## Usage

To run the application, use the command

```bash 
poetry run pyphonebookapi
```

The application will be available at http://localhost:8000.

## API Endpoints

| Method | Endpoint                               | Description                      |
|--------|----------------------------------------|----------------------------------|
| GET    | /addressbook/v1/contacts               | Retrieve a list of all contacts  |
| GE     | /addressbook/v1/contacts/{contact_id}  | Retrieve a contact by ID         |
| POST   | 	/addressbook/v1/contacts              | Create a new contact             |
| PATCH  | 	/addressbook/v1/contacts/{contact_id} | Update an existing contact by ID |
| DELETE | 	/addressbook/v1/contacts/{contact_id} | Delete a contact by ID           |


## Testing

Tests can be run using the command

```bash
pytest
```

**Note:** this is a baisc app intended to learn/play with FastAPI and SQLAlchemy.
