from discord.ext import commands
from discord.ext.commands import Bot

class VotacionesBot():

    def __init__(self):
        self.bot_client = Bot(command_prefix='/')

    def run(self, token):
        self.bot_client.run(token)

    def add_cog(self, cog):
        self.bot_client.add_cog(cog)

