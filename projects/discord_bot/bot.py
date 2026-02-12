import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'🤖 {bot.user} is online and ready to hang out!')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Yo {ctx.author.name}! What's up, buddy? 🐍")

if __name__ == "__main__":
    print("Buddy, to run this for real, put your token in the code!")
