from pydantic import EmailStr

from facet import ServiceMixin


class SaveEmailMixin:
    async def save_email(
        self,
        session: AsyncSession,
        email: str
    ):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return EmailStatus.WRONG

        result = await session.execute(select(Email).filter(Email.email == email))
        existing_email = result.scalars().first()
        if existing_email:
            return EmailStatus.EXISTS

        new_email = Email(email=email)
        session.add(new_email)
        await session.commit()
        return EmailStatus.SAVED
