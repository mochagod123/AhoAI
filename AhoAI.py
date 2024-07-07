import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

def AhoChat(word: str):
    a = word
    response = requests.get(f"https://www.google.com/search?q={a}")
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
    if links:
        linksa = soup.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})[1]
        return f"「{a}」は\n「{linksa.get_text()}」です。"
    else:
        return f"うーん、、よくわからないな、、"

class AhoAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, type=commands.BucketType.user)
    async def ahoai(self, ctx, a: str):
        await ctx.reply(AhoChat(a))

async def setup(bot):
    await bot.add_cog(AhoAI(bot))