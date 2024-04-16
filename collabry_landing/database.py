import aiosqlite
import re

from collabry_landing.enums import EmailStatus


async def db_save_email(
    email: str
):
    async with aiosqlite.connect('database.db') as db:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return EmailStatus.WRONG

        result = await db.execute(
            "SELECT email FROM emails WHERE email = ?", (email,)
        )
        existing_email = await result.fetchone()
        if existing_email:
            return EmailStatus.EXISTS

        await db.execute(
            "INSERT INTO emails (email) VALUES (?)", (email,)
        )

        await db.commit()
        return EmailStatus.SAVED


async def db_create_email_table():
    async with aiosqlite.connect('database.db') as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL
            );
        """)

        await db.commit()
