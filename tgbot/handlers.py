from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.config import Settings
from tgbot.db import AsyncSession_
from tgbot.enums import Answer, MIMEType, ProcessErrorDesc
from tgbot.middlewares import DBSessionMiddleware
from tgbot.services import process_excel

router = Router()
router.message.middleware(DBSessionMiddleware(AsyncSession_))


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Handler of the /start command."""
    await message.answer(Answer.GREETING.format(message.from_user.first_name))
    await help_handler(message)


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    """Handler of the /help command."""
    await message.answer(Answer.HELP)


@router.message(F.document & F.document.mime_type == MIMEType.XLSX)
async def receive_excel_handler(
    message: Message, bot: Bot, settings: Settings, session: AsyncSession
) -> None:
    """Handler of received excel documents."""
    try:
        df = await process_excel(
            message.document, settings.downloads_dir, bot, session
        )
    except (IntegrityError, OperationalError) as exc:
        await message.answer(
            Answer.ERROR.format(
                ProcessErrorDesc[type(exc).__name__.upper()].value
            )
        )
    else:
        await session.commit()
        await message.answer(
            Answer.SUCCESS.format("\n".join(map(str, list(df.values))))
        )


router.message.register(help_handler)
