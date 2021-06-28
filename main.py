import discord
from discord.ext import commands
import logging
from bot import bot
from cogs import cogs
from controllers import controllers

token = 'ODU4ODM1MDcxNzMyNjc4Njc3.YNj6fQ.9xuN9DnCTXUJ2UaMdXZoSjkvf8Y'

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

controller = controllers.Controller()

"""

v_bot = bot.VotacionesBot()
@v_bot.bot_client.event
async def on_message(message):
    if message.content.startswith('/greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await v_bot.bot_client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

v_bot.bot_client.add_cog(cogs.ClubesCog(v_bot))
v_bot.run()
"""

