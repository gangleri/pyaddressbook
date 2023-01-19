import click
import signal
import uvicorn
from fastapi import FastAPI
from pyaddressbook.api.addressbook import get_routes
from pyaddressbook.middleware import add_middleware
from pyaddressbook.repository.addressbook import ContactRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@click.command()
@click.option(
    "--host",
    "-h",
    help="host IP address that the server should listen on",
    type=str,
    default="0.0.0.0",
)
@click.option(
    "--port", "-p", help="Port to run API on, defaults to 8000", type=int, default=8000
)
def main(host: str, port: int):
    engine = create_engine("sqlite:///db.sqlite")
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = session_local()
    repo = ContactRepository(session)

    def close_db_session():
        session.close()
        exit(0)

    signal.signal(signal.SIGINT, close_db_session)
    signal.signal(signal.SIGTERM, close_db_session)

    app = FastAPI()
    add_middleware(app)
    app.include_router(get_routes(repo), prefix="/api")

    uvicorn.run(app, host=host, port=port)
