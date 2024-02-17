import asyncio
import os
import discord
from discord.ext import commands, tasks
from discord import app_commands
import datetime
import random

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())
current_mode = 'regular'


async def time_until_next_hour():
    now = datetime.datetime.now()
    next_hour = now.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1)
    return next_hour - now


# Event listener for when the bot has switched from offline to online.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('-'*20)
    await bot.get_channel(1204356188683247697).send(f'mogus bot has restarted in {current_mode} mode \nmogus')
    await bot.get_channel(1204356188683247697).send('https://tenor.com/view/amour-amongus-impostor-imposter-amog-gif-21848583')
    five_minute_mogus.start()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="mogus"))

    await start_hourly_task() # all code must go before this


@bot.event
async def on_message_delete(message):
    print(f"A message by {message.author.name} was deleted in {message.channel.name}: {message.content}")

    if message.author != bot.user:
        await message.channel.send(f"nah busta you aint delete this: \n{message.author.name}: \"{message.content}\"")
    else:
        await message.channel.send(message.content)


@tasks.loop(minutes=5)
async def five_minute_mogus():
    if str(bot.get_guild(1176130163268927539).name) != str('Mogus Ltd.'):
        await bot.get_guild(1176130163268927539).edit(name='Mogus Ltd.')


async def start_hourly_task():
    now = datetime.datetime.now()
    seconds_until_next_hour = (60 - now.minute) * 60 - now.second
    await asyncio.sleep(seconds_until_next_hour)
    hourly_ping.start()


@tasks.loop(hours=1)
async def hourly_ping():
    await bot.get_channel(1176318790712172626).send(f'{random.choice(bot.get_guild(1176130163268927539).members).mention} get pinged loser')


@bot.command(name='regular')
async def regular_mode(ctx):
    global current_mode
    current_mode = 'regular'
    await ctx.send('normie mode resuming, cutting off piss stream')


@bot.command(name='serious')
async def serious_mode(ctx):
    global current_mode
    current_mode = 'serious'
    await ctx.send('shitter mode enabled, activating piss stream')


def regular_mode():
    print()


conditions = ['mogus', 'amongus', 'impostor', 'sus', 'among', 'sussy', 'crewmate', 'amogus', 'vented', 'vent',
                  'amog', 'imposter', 'mog', 'gus', 'task', 'medbay', 'zka1']

serious_conditions = ['us']


@bot.event
async def on_message(message):
    print(message.content.lower())

    if message.author != bot.user \
            and any((x in message.content.lower()) for x in (conditions if regular_mode else conditions and serious_conditions)):
        await message.channel.send('https://tenor.com/view/amour-amongus-impostor-imposter-amog-gif-21848583')
        await message.add_reaction(bot.get_emoji(1203010439366320278))
        print('mogus')

    if message.author != bot.user and message.content.lower() == ('kys' or 'kill yourself'):
        await message.channel.send('no u')

    if message.author != bot.user and ('kill myself' in message.content.lower()
                                       or 'killing myself' in message.content.lower()):
        await message.channel.send('do it pussy you wont')

    if message.author != bot.user and ('james' in message.content.lower()
                                       or 'jamey' in message.content.lower()):
        await message.channel.send('jamey is mega cringe')
        await message.channel.send('so true! spit your fax brother')

    #if message.author != bot.user and '@everyone' in message.content.lower():
        #string = ""
        #for user in bot.get_guild(1176130163268927539).members:
            #string += (str(user.mention) + " ")
        #for i in range(5):
            #await message.channel.send(string)


with open('token.txt', 'r') as file:
    bot.run(file.read())
