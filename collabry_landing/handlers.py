import fastapi

from pydantic import BaseModel

from collabry_landing.database import db_save_email
from collabry_landing.enums import EmailStatus





class EmailRequest(BaseModel):
    email: str


async def post_email(email_data: EmailRequest):
    email = email_data.email


    email_status: EmailStatus = await db_save_email(
        email=email
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
