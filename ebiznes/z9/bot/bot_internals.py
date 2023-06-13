import discord
import text_processing

async def handle_message(chat, message, message_innards, is_private):
    try:
        response = chat.process_message(message_innards)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def start_bot():
    discord_token = ""
    with open("credentials/discord.txt", mode="r") as token_file:
        discord_token = token_file.read()
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)

    chat = text_processing.ChatInstance()

    @client.event
    async def on_ready():
        print("I'm awake!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        caller = str(message.author)
        message_innards = str(message.content)
        where = str(message.channel)
        if len(message_innards) < 8:
            return

        if message_innards[:8] == "!r_chat ":
            message_innards = message_innards[8:]
            await handle_message(chat, message, message_innards, False)
        if message_innards[:8] == "?r_chat ":
            message_innards = message_innards[8:]
            await handle_message(chat, message, message_innards, True)

    client.run(discord_token)


