import discord
import os

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 1 # Inicializa o contador como um atributo da classe

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('$kort'):
            await message.channel.send(f'O Kort falou merda {self.count} vezes.')
            self.count += 1
        elif message.content.startswith('$autor'):
            await message.channel.send(f'Feito por sowisz.')
        elif message.content.startswith('$altura'):
            await message.channel.send(f'Kort tem 1,46cm.')
        elif message.content.startswith('$idade'):
            await message.channel.send(f'Kort tem 14 anos.')
        elif message.content.startswith('$qi'):
            await message.channel.send(f'Kort tem 2 de qi.')
        elif message.content.startswith('$help'):
            await message.author.send(f'{message.author.name} os comando disponiveis no bot são: {os.linesep}$autor{os.linesep}$altura{os.linesep}$idade{os.linesep}$qi{os.linesep}$help')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTI1NTE5OTU2MzkwODkxMTE5NQ.GHy1O4.VPESylBtfgejD_RKGqWOM434ACRtS4FSFtGGSs')