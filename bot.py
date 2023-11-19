import discord
import responses


async def on_user_message(message, user_message, is_private):
    try:
        response = responses.handle_response(message.content)
        if is_private:
            await message.channel.send("Response sent to DMs")
            await message.author.send(response) 
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "token"
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username}: {user_message} ({channel})")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await on_user_message(message, user_message, is_private=True)
        else:
            await on_user_message(message, user_message, is_private=False)


    client.run(TOKEN)
