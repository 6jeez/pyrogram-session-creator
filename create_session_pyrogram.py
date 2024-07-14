from pyrogram import Client
import asyncio


async def get_user_id():
    api_id = input("Введите API_ID: ")
    api_hash = input("Введите API_HASH: ")

    while True:
        session_name = input("Введите имя сессии: ")

        async with Client(session_name, api_id, api_hash) as client:
            me = await client.get_me()

            print("Ваш user_id:", me.id)

asyncio.run(get_user_id())
