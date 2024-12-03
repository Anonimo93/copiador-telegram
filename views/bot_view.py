from telethon import TelegramClient, events

class BotView:
    def __init__(self, client: TelegramClient):
        self.client = client

    async def send_message(self, chat_id, text):
        await self.client.send_message(chat_id, text)

    async def forward_message(self, message, destination_id):
        await message.forward_to(destination_id)

    async def notify_start(self, destination_id):
        await self.send_message(destination_id, "Copia de mensajes iniciada!")
