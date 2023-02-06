
import os
import random, json, datetime, requests, io, discord, string, asyncio, os, ctypes, numpy, urllib.parse, urllib.request
from colorama import Fore
from asyncio import sleep

#import music, fun, crypto, admin

#cogs = ['cogs.music', 'cogs.fun', 'cogs.crypto', 'cogs.admin']

initial_extensions = []

for filename in os.listdir('./cogs/'):
   if filename.endswith('.py'):
         initial_extensions.append ("cogs." + filename [:-3])

intents = discord.Intents.default()
intents.members = True

from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

TOKEN = config.get('token')

with open('customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

def Clear():
    os.system('clear')
Clear()

prefix = config.get('prefix')

bot = commands.Bot(command_prefix=prefix, intents=intents)

if __name__ == '__main__':
     for extension in initial_extensions:
          bot.load_extension(extension)

bot.remove_command('help')

async def status():
    while True:
        await bot.wait_until_ready()
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f'Over {len(bot.guilds)} Servers | {prefix}help'))
        await sleep(10)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name=f'With {sum([len(guild.members) for guild in bot.guilds])} Users | {prefix}help'))
        await sleep(10)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f'Commands | {prefix}help'))
        await sleep(10)

@bot.event
async def on_ready():
    bot.loop.create_task(status())

#for ext in range(len(cogs)):
#    cogs[i].setup(bot)

@bot.event
async def on_connect():

    Clear()
    print(f'[Death Bot V1.1] | Logged in as {bot.user.name} | Prefix: {prefix}  | Total Servers: {len(bot.guilds)}')    
    print(f'''''')
    print(f'''{Fore.RED}██████╗ ███████╗ █████╗ ████████╗██╗  ██╗'''
    print(f'''{Fore.RED}██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║'''
    print(f'''{Fore.RED}██║  ██║█████╗  ███████║   ██║   ███████║'''
    print(f'''{Fore.RED}██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║'''
    print(f'''{Fore.RED}██████╔╝███████╗██║  ██║   ██║   ██║  ██║'''
    print(f'''{Fore.RED}╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝'''
    print(initial_extensions)

    print(f'''{Fore.WHITE}I've always been comfortable in chaos'''.center
    print(f'{Fore.LIGHTBLACK_EX}─' +Fore.RESET)           

commandsdone = 0

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.WHITE}Death is missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.WHITE}Missing arguments: {error}"+Fore.RESET)
        await ctx.send(f"Missing Arugments: {error}")
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.WHITE}Not a valid image"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.WHITE}Couldnt send a empty message"+Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.WHITE}{error_str}"+Fore.RESET)

@bot.event
async def on_guild_remove(guild):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict.pop(guild.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)

@bot.event
async def on_command(ctx):
        time = datetime.datetime.now().strftime("%H:%M %p")
        print(f"{Fore.RED}[{time}] {Fore.RESET} Command used | {Fore.RED}{ctx.command.name}{Fore.RESET}")
        global commandsdone

@bot.event
async def on_member_join(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    embed = discord.Embed(title="Welcome", description=f"Welcome To **{member.guild.name}** <@{member.id}>!\n We Now Have {member.guild.member_count} Users", color=embed_color)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/tFYJp8FzWsrnNS7qJJsSdVl2sMp9gzuh4sT-aOVTNwk/http/pm1.narvii.com/6871/dce35a106448dd7d89c258521305f37058e6ad38r1-384-216v2_00.jpg")

    channel_id = guilds_dict[str(member.guild.id)]
    await bot.get_channel(int(channel_id)).send(embed=embed)

@bot.event
async def on_member_remove(member):

    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    embed = discord.Embed(title="Goodbye", description=f"<@{member.id}> Left!\n We Now Have {member.guild.member_count} Users", color=embed_color)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/tFYJp8FzWsrnNS7qJJsSdVl2sMp9gzuh4sT-aOVTNwk/http/pm1.narvii.com/6871/dce35a106448dd7d89c258521305f37058e6ad38r1-384-216v2_00.jpg")

    channel_id = guilds_dict[str(member.guild.id)]

    await bot.get_channel(int(channel_id)).send(embed=embed)

@bot.command()
async def cogs(ctx):
  await ctx.message.delete()
  Sorted = 869032738588602418
  if ctx.message.author.id == Sorted:
    em = discord.Embed(title="Loaded Cogs", description=f"```{initial_extensions}```")
  await ctx.send(embed=em)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    Sorted = 869032738588602418
    if ctx.message.author.id == Sorted:
      bot.reload_extension(f"cogs.{extension}")
      embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=embed_color)
    await ctx.send(embed=embed)

@bot.command()
async def load(ctx, extension):
  Sorted = 869032738588602418
  if ctx.message.author.id == Sorted:
    bot.load_extension(f"cogs.{extension}")
    embed = discord.Embed(title='Load', description=f'{extension} successfully loaded', color=embed_color)
  await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Help", color=embed_color, description = f"**`{prefix}`fun** » Desplays The Fun Menu\n**`{prefix}`image** » Shows Image Menu\n**`{prefix}`tools** » Shows Tools Menu\n**`{prefix}`admin** » Shows Admin Menu\n**`{prefix}`info** » Shows Info Menu\n**`{prefix}`crypto** » Shows Crypto Menu\n**`{prefix}`music** » Shows Music Menu\n**`{prefix}`minecraft** » Shows Minecraft Menu\n**`{prefix}`nsfw** » Shows NSFW Menu\n**`{prefix}`credits** » Shows Credits Menu")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Info", color=embed_color, description = f"**`{prefix}`botinfo** » Sends Info About The Bot\n**`{prefix}`nasa** » Sends Nasa Fact Of The Day\n**`{prefix}`level** » Sends Hypixel Level Of User\n**`{prefix}`serverinfo** » Sends Information About Server")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def fun(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Fun", color=embed_color, description = f"**`{prefix}`shrug** » Sends A Custom Emoji\n**`{prefix}`tableflip** » Sends A Custom Emoji\n**`{prefix}`lenny** » Sends A Custom Emoji\n**`{prefix}`unflip** » Sends A Custom Emoji\n**`{prefix}`topic** » Suddenly Change The Topic")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def image(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Image", color=embed_color, description = f"**`{prefix}`clyde** » Have Clyde Say Somthing\n**`{prefix}`dog** » Send A Dog Picture\n**`{prefix}`meme** » Send A Random Meme\n**`{prefix}`hug** » Hug A User\n**`{prefix}`pfp** » Show Someones PFP\n**`{prefix}`tweet** » Make Someone Tweet Somthing\n**`{prefix}`kiss** » Kiss A User")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def crypto(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="Crypto", color=embed_color, description=f"**`{prefix}`btc** » Show btc Price\n**`{prefix}`xrp** » Shows XRP Price\n**`{prefix}`eth** » Shows ETH Price\n**`{prefix}`ltc** » Shows LTC Price\n**`{prefix}`xmr** » Shows XMR Price")
    em.set_author(name="Death")
    em.set_thumbnail(url=embed_thumbnail)
    em.set_footer(text=embed_footer)
    await ctx.send(embed=em)

@bot.command()
async def tools(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="Tools", color=embed_color, description=f"**`{prefix}`ascii** » Converts Normal Text To ascii text\n**`{prefix}`nitro** » Generates a random nitro code (Most likley wont work)\n**`{prefix}`invite** » Creates Invite For Server\n**`{prefix}`ranum** » Sends A Random Number")
    em.set_author(name="Death")
    em.set_thumbnail(url=embed_thumbnail)
    em.set_footer(text=embed_footer)
    await ctx.send(embed=em)

@bot.command()
async def admin(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="Admin", color=embed_color, description=f"**`{prefix}`kick** » Kicks a user\n**`{prefix}`ban** » Bans a user\n**`{prefix}`announce** » Make An Announcement\n**`{prefix}`setwelcome** » Set Welcome Channel\n**`{prefix}`clear** » Delete A Certain Number Of Messages")
    em.set_author(name="Death")
    em.set_thumbnail(url=embed_thumbnail)
    em.set_footer(text=embed_footer)
    await ctx.send(embed=em)

@bot.command()
async def nsfw(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="NSFW Menu", color=embed_color, description = f"**`{prefix}`hentai** » Shows Hentai\n**`{prefix}`feet** » Shows Some Feet\n**`{prefix}`boobs** » Shows Some Boobies\n**`{prefix}`anal** » Straight Up The Ass\n**`{prefix}`blowjob** » Well Its In The Name\n**`{prefix}`gonewild** » Random Pics\n**`{prefix}`pussy** » pussy")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def music(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Music", color=embed_color, description = f"**`{prefix}`join** » Makes Bit Join Channel\n**`{prefix}`leave** » Disconnects Bot\n**`{prefix}`play** » Plays Music\n**`{prefix}`pause** » Pauses Music\n**`{prefix}`resume** » Resume Music\n**`{prefix}`stop** » Stop Music")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def minecraft(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Minecraft", color=embed_color, description = f"**`{prefix}`level** » Shows Hypixel Level\n**`{prefix}`bedwars** » Shows Bedwars Stats\n**`{prefix}`classicduels** » Shows Classic Duels Stats\n**`{prefix}`skywars** » Shows SkyWars Stats\n**`{prefix}`uhc** » Shows UHC Stats\n**`{prefix}`sumo** » Shows Sumo Stats\n**`{prefix}`mc** » Shows User Info")
  embed.set_author(name="Death")
  embed.set_thumbnail(url=embed_thumbnail)
  embed.set_footer(text=embed_footer)
  await ctx.send(embed=embed)

@bot.command()
async def credits(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title="Death Development", color=embed_color)
    em.add_field(name = "Creator", value= "[Sorted#0010](https://taxevasion.xyz)", inline= True),
    em.add_field(name = "Discord Bot", value = "[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=908098992792027137&permissions=8&scope=bot)")
    em.set_footer(text=embed_footer)
    await ctx.send(embed=em)

import sys
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
  Sorted = 869032738588602418
  if ctx.message.author.id == Sorted:

    await ctx.send("Restarting bot...")
    restart_bot()

@bot.command()
async def pfp(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}")) 
        
bot.run(TOKEN)