import asyncio
from telethon import events


class BotController:
    def __init__(self, client, model, view):
        self.client = client
        self.model = model
        self.view = view

    async def handle_group_join(self, event):
        group_id = event.chat_id
        if not self.model.get_origin():
            self.model.set_origin(group_id)
            print(f"Te has unido al grupo de origen: {group_id}")

            await self.copy_historic_messages()

            await self.view.notify_start(self.model.get_destination())
        else:
            print(f"Ya se definió un grupo de origen: {self.model.get_origin()}")

    async def copy_historic_messages(self):
        origin_id = self.model.get_origin()
        destination_id = self.model.get_destination()

        print(f"Copiando mensajes históricos de {origin_id} a {destination_id}...")

        async for message in self.client.iter_messages(origin_id, reverse=True):
            await self.view.forward_message(message, destination_id)
            await asyncio.sleep(1)
        print("Mensajes históricos copiados.")

    async def handle_new_message(self, event):
        if event.chat_id == self.model.get_origin():
            await self.view.forward_message(event.message, self.model.get_destination())

    def register_handlers(self):
        self.client.add_event_handler(self.handle_group_join, events.ChatAction)
        self.client.add_event_handler(self.handle_new_message, events.NewMessage)
