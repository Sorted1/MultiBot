import discord
from discord.ext import commands
import requests, aiohttp, io, json
from bs4 import BeautifulSoup as bs4

with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shrug(self, ctx):
      await ctx.message.delete()
      shrug = r'¯\_(ツ)_/¯'
      await ctx.send(shrug)
    
    @commands.command()
    async def tableflip(self, ctx):
      await ctx.message.delete()
      tableflip = '(╯°□°）╯︵ ┻━┻'
      await ctx.send(tableflip)
    
    @commands.command()
    async def lenny(self, ctx):
      await ctx.message.delete()
      lenny = '( ͡° ͜ʖ ͡°)'
      await ctx.send(lenny)

    @commands.command()
    async def unflip(self, ctx):
      await ctx.message.delete()
      unflip = '┬─┬ ノ( ゜-゜ノ)'
      await ctx.send(unflip)
  
    @commands.command()
    async def topic(self, ctx):
        await ctx.message.delete()
        r = requests.get('https://www.conversationstarters.com/generator.php').content
        soup = bs4(r, 'html.parser')
        topic = soup.find(id="random").text
        await ctx.send(topic)

def setup(client):
    client.add_cog(fun(client))