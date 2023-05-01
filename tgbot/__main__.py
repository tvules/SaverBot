from aiogram import Bot, Dispatcher

from tgbot.config import get_settings
from tgbot.handlers import router


async def on_startup(bot: Bot) -> None:
    """On startup actions."""
    await bot.set_webhook("", drop_pending_updates=True)
    get_settings().downloads_dir.mkdir(parents=True, exist_ok=True)


def get_bot() -> Bot:
    """Get an instance of the bot."""
    return Bot(get_settings().bot_token.get_secret_value())


def get_dispatcher() -> Dispatcher:
    """Get an instance of the dispatcher."""
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    return dispatcher


def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    """Run the bot in the "long-polling" mode."""
    dispatcher.run_polling(bot)


def main() -> None:
    """Start the bot."""

    bot = get_bot()
    dispatcher = get_dispatcher()

    settings = get_settings()
    dispatcher["settings"] = settings
    dispatcher.startup.register(on_startup)

    run_polling(dispatcher, bot)


if __name__ == "__main__":
    main()
