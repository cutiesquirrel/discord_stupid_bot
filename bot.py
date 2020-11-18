import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CLID =int(os.getenv('CHANNEL_ID'))
MSG = os.getenv('MSG')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def send_msg():
    print(MSG)
    MSG_i=""
    while MSG_i != '/quit':
        MSG_i = input('Type ur msg here --> ')
        await channel.send(MSG_i)
        print(f'{MSG_i}  is send')
        

@client.event
async def on_ready():
    global channel
    channel = client.get_channel(CLID)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n' 
        f'{guild.name} (id: {guild.id}) \n'
        f'{CLID}'    )
    await send_msg()


client.run(TOKEN)