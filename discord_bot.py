# Criar o bot em https://discord.com/developers/
# TUTORIAL: https://www.freecodecamp.org/portuguese/news/tutorial-de-criacao-de-bot-para-o-discord-em-python/
# EXEMPLO: https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot



from random import randint

import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!comandos'):
        await message.channel.send(
            '''
            Comandos:
            !d4 - lança um dado de 4 lados

            !d6 - lança um dado de 6 lados

            !d8 - lança um dado de 8 lados

            !d10 - lança um dado de 10 lados

            !d12 - lança um dado de 12 lados

            !d20 - lança um dado de 20 lados

            !d100 - lança um dado de 100 lados

            !flip - lança uma moeda (cara ou coroa)
            '''
        )

    if msg.startswith('hello'):
        await message.channel.send('Hello!')

    if msg.startswith('!d4'):
        roll = randint(1, 4)
        await message.channel.send(f'Você rolou um d4')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!d6'):
        roll = randint(1, 6)
        await message.channel.send(f'Você rolou um d6')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!d8'):
        roll = randint(1, 8)
        await message.channel.send(f'Você rolou um d8')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!d10'):
        roll = randint(1, 10)
        await message.channel.send(f'Você rolou um d10')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!d12'):
        roll = randint(1, 12)
        await message.channel.send(f'Você rolou um d12')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!d20'):
        roll = randint(1, 20)
        await message.channel.send(f'Você rolou um d20')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!d100'):
        roll = randint(1, 100)
        await message.channel.send(f'Você rolou um d100')
        await message.channel.send(f'o resultado é {roll}.')

    if msg.startswith('!flip'):
        roll = randint(1, 2)
        await message.channel.send(f'Você lançou uma moeda')
        if roll == 1:
            await message.channel.send(f'o resultado é "cara".')
        else:
            await message.channel.send(f'o resultado é "coroa".')


client.run('COLOQUE_A_CHAVE_DO_SEU_BOT_AQUI')
