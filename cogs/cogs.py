import discord
from discord.ext import commands

class ClubesCog(commands.Cog):

    def __init__(self, bot, client):
        self.client = client
        self.bot = bot


    @commands.command()
    async def add_club(self, ctx):
        member = ctx.author
        dmChannel = await ctx.author.send(
            "Agregar un nuevo club"
        )


        def check(message):
            return message.author == ctx.author and message.channel == dmChannel.channel


        async def ask_question(question):
            await ctx.author.send(question)
            userReply = await self.client.wait_for('message', check=check)
            print("User replied")
            return userReply.content

        questions = ['Nombre dele club', 'Distrito']
        userName = await ask_question(questions[0])
        userAge = await ask_question(questions[1])
        e = discord.Embed(title=str(userName) + "'s Profile", description=f"""
            Age: `{str(userAge)}`
            """)

        await ctx.author.send(embed=e)

