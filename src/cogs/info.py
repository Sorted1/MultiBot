import discord
from discord.ext import commands
import requests, aiohttp, io, json, os
from aiohttp import ClientSession

with open('./config.json') as f:
    config = json.load(f)

with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

prefix = config.get('prefix')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        verilevel = str(ctx.guild.verification_level)
        afkchan = str(ctx.guild.afk_channel)
        mfalevel = str(ctx.guild.mfa_level)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color(0x00000)
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name= "AFK Channel", value=afkchan, inline=True)
        embed.add_field(name= "Verification Level", value=verilevel, inline=True)
        embed.add_field(name= "MFA Level", value=mfalevel, inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def botinfo(self, ctx): # b'\xfc'
        await ctx.message.delete()
        em = discord.Embed(title="Sorted Development", color=embed_color)
        em.add_field(name = "Version", value= "1.7", inline= True),
        em.add_field(name = "Library", value= "discord.py", inline= True),
        em.add_field(name = "Creator", value= "Sorted#0010", inline= True),
        em.add_field(name = "Servers", value= f"{len(bot.guilds)}", inline= True),
        em.add_field(name = "Users", value= f"{sum([len(guild.members) for guild in bot.guilds])}", inline= True)
        em.set_footer(text=embed_footer)
        await ctx.send(embed=em)

    @commands.command()
    async def nasa(self, ctx):
        await ctx.message.delete()
        url = f'https://api.nasa.gov/planetary/apod?api_key=k4jg3cagKhLDxz92J6SZV4ThRqeF0RguPGmVepTv'

        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                title = f"{r['title']}"
                date = f"{r['date']}"
                explanation = f"{r['explanation']}"
                image = f"{r['url']}"

        embed = discord.Embed(color=embed_color, title=title, description=explanation)
        embed.add_field(name="Date", value=date)
        embed.set_image(url=image)

        await ctx.send(embed=embed)
  

def setup(client):
    client.add_cog(info(client))