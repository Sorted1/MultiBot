import discord
from discord.ext import commands
import youtube_dl, json
with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def join(self, ctx):
      await ctx.message.delete()
      
      if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel. Please connect to a channel for me to join.")

      if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

      await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
      await ctx.message.delete()

      if ctx.voice_client is not None:
          return await ctx.voice_client.disconnect()
    
      await ctx.send("I am not connected to a voice channel.")

    @commands.command()
    async def play(self,ctx,url):
      await ctx.message.delete()
      await ctx.send("Downloading Music")
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      
      YDL_OPTIONS = {
        'format':"bestaudio",
        'noplaylist': False,
      }
      vc = ctx.voice_client
      try:

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        await ctx.send('Now playing: Music')
        vc.play(source)
      except:
          await ctx.send("[Error] Could Not Play Music")
    
    @commands.command()
    async def pause(self,ctx):
      await ctx.message.delete()

      await ctx.voice_client.pause()
      return await ctx.send("Paused ⏸️")

    @commands.command()
    async def resume(self,ctx):
      await ctx.message.delete()

      await ctx.voice_client.resume()
      return await ctx.send("Resumed ▶️")
    
    @commands.command()
    async def stop(self,ctx):
      await ctx.message.delete()

      await ctx.voice_client.stop()
      return await ctx.send("Stoped ⏹")

def setup(client):
    client.add_cog(music(client))