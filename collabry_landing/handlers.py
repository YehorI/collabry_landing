import fastapi

from pydantic import BaseModel
from email_statuses import EmailStatus
from enums import Enum, auto


class EmailStatus(Enum):
    EXISTS = auto()
    SAVED = auto()
    WRONG = auto()


class EmailRequest(BaseModel):
    email: str


async def post_email(request: fastapi.Request):
    email_data = await request.json()
    email_request = EmailRequest(**email_data)
    email = email_request.email

    database_service = request.app.service.database

    async with database_service.transaction() as session:
        try:
            email_status: EmailStatus = await database_service.save_email(
                email=email
            )
        except Exception as e:
            raise fastapi.HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to process the request."
            )

    if email_status == EmailStatus.EXISTS:
        return {"message": "Email already exists.", "status": "exists"}
    elif email_status == EmailStatus.SAVED:
        return {"message": "Email successfully saved.", "status": "saved"}
    elif email_status == EmailStatus.WRONG:
        return {"message": "Invalid email format.", "status": "wrong"}
    else:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Unknown error."
        )
