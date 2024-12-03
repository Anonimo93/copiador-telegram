import asyncio
from telethon import TelegramClient
from models.group_model import GroupModel
from views.bot_view import BotView
from controllers.bot_controller import BotController
from config.Config import API_ID, API_HASH, DESTINATION_ID, SESSION_NAME

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

model = GroupModel()
view = BotView(client)
controller = BotController(client, model, view)


async def main():
    print("Iniciando bot...")
    await client.start()

    model.set_destination(DESTINATION_ID)

    controller.register_handlers()

    print("Esperando eventos...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
