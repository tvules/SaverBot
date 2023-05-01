from pathlib import Path
from typing import Type

import aiofiles
import pandas as pd
from aiogram import Bot
from aiogram.types import Document
from pandas import DataFrame
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db import Base
from tgbot.models import Resource


async def process_excel(
    document: Document, downloads_dir: Path, bot: Bot, session: AsyncSession
) -> DataFrame:
    """Process exel file from telegram document object."""
    file = await bot.download(document.file_id)

    df = pd.read_excel(file)
    await save_to_table(Resource, df, session)

    await save_file(file.read(), downloads_dir / document.file_name)
    return df


async def save_to_table(
    model: Type[Base], df: DataFrame, session: AsyncSession
) -> None:
    """Sync insert from pandas dataframe to db table."""
    conn = await session.connection()
    await conn.run_sync(
        lambda sync_conn: df.to_sql(
            model.__tablename__, sync_conn, if_exists="append", index=False
        )
    )


async def save_file(data: bytes, destination: str | Path) -> None:
    """Async file saving."""
    async with aiofiles.open(destination, "wb") as f:
        await f.write(data)
