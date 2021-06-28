from bot import bot
from cogs import cogs

class Controller():

    def __init__(self):
        self.bot = bot.VotacionesBot()
        self.init_cogs()
        self.bot.run('ODU4ODM1MDcxNzMyNjc4Njc3.YNj6fQ.9xuN9DnCTXUJ2UaMdXZoSjkvf8Y')


    def init_cogs(self):
        cog = cogs.ClubesCog(self.bot, self.bot.bot_client)
        self.bot.add_cog(cog)
