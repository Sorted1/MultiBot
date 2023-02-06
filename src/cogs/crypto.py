import discord
from discord.ext import commands
import requests, json


with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

class crypto(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def btc(self, ctx):
      await ctx.message.delete()
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(color=embed_color, description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='Bitcoin', icon_url='https://s2.coinmarketcap.com/static/img/coins/64x64/1.png')
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)

    @commands.command()
    async def xrp(self, ctx): # b'\xfc'
      await ctx.message.delete()
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(color=embed_color, description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='XRP', icon_url='https://s2.coinmarketcap.com/static/img/coins/32x32/52.png')
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)

    @commands.command()
    async def eth(self, ctx): # b'\xfc'
      await ctx.message.delete()
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(color=embed_color, description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='ETH', icon_url='https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png')
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)    

    @commands.command()
    async def xmr(self, ctx): # b'\xfc'
      await ctx.message.delete()
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(color=embed_color, description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='XMR', icon_url='https://s2.coinmarketcap.com/static/img/coins/64x64/328.png')
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)
    
    @commands.command()
    async def ltc(self, ctx): # b'\xfc'
      await ctx.message.delete()
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(color=embed_color, description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='LTC', icon_url='https://s2.coinmarketcap.com/static/img/coins/64x64/2.png')
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)

def setup(client):
    client.add_cog(crypto(client))