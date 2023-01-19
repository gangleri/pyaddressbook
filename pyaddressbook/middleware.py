import logging
from fastapi import HTTPException, Request

logger = logging.getLogger("addressbook")


def add_middleware(app):
    """
    Add middleware to the FastAPI addressbook application for:
        - handling exceptions.

    Parameters:
        - app (FastAPI): An instance of the FastAPI application.

    Returns:
        None
    """

    @app.middleware("http")
    async def handle_exception(request: Request, call_next):
        """
        Middleware function for handling exceptions.

        Parameters:
            - request (Request): The request object.
            - call_next: The next middleware function in the chain.

        Returns:
            - response (Union[JSONResponse, Exception]): The response object or an exception.
        """
        try:
            response = await call_next(request)
            return response
        except HTTPException as e:
            logger.error(e)
            return e
        except Exception as e:
            logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
