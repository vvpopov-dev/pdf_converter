from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from collections import defaultdict

class MediaGroupMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.album_data = defaultdict(list)

    async def on_process_message(self, message: types.Message, data: dict):
        if not message.media_group_id:
            return

        self.album_data[message.media_group_id].append(message)

        data["album"] = self.album_data[message.media_group_id]
        del self.album_data[message.media_group_id]
