import discord 
import random
from discord.ext import commands, tasks
from itertools import cycle

from discord.member import Member


client = commands.Bot(command_prefix='S!')

status = cycle(['eating', 'cooking','shooting'])



@client.event
async def on_ready():
    change_status.start()
    print('The Bot is online')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


    if not Member: #if not member isnt mentioned
        await ctx.send("User isnt mentioned")

        await member.kick(reason=reason)
    embed = discord.Embed(title=f"{ctx.author.name}  kicked:  {member.name}", color=0xea7938)
    embed.add_field(name="Reason", value=reason)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://media.giphy.com/media/xTcnTjeH5rtf6bdlwA/giphy.gif')
    embed.set_footer(text="Savage Bot")
    embed.add_field(name="Bot?", value=member.bot)
    
    await ctx.send(embed=embed) 

    

 
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



client.run('ODQ5Mjk3NDI1MjA1MTY2MTg3.YLZH3Q.ihFvZQttjPoZqBR3G9kqt8jZFac')