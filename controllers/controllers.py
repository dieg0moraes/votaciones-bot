from bot import bot
from cogs import cogs
from settings import API_KEY

class Controller():

    def __init__(self):
        self.bot = bot.VotacionesBot()
        self.init_cogs()
        self.bot.run(API_KEY)


    def init_cogs(self):
        cog = cogs.ClubesCog(self.bot, self.bot.bot_client)
        self.bot.add_cog(cog)
