from aiogram import executor

from core.app import dp, bot
from core.settings import settings
from src.middleware.media_group import MediaGroupMiddleware
from src.handlers.pdf.merge import merge_pdf_handler
import src.handlers


async def on_startup(dp):
    dp.middleware.setup(MediaGroupMiddleware())
    print(f"Бот {settings.BOT_USERNAME} запущен")


async def on_shutdown(dp):
    print(f"Бот {settings.BOT_USERNAME} остановлен")


def main():
    executor.start_polling(dp, skip_updates=True,
                            on_startup=on_startup,
                            on_shutdown=on_shutdown)


if __name__ == "__main__":
    main()
