import discord 
from discord.ext import commands

token = 'BOTTOKENHERE'

client = commands.Bot(command_prefix='!')

@client.command()  
async def raid(ctx):

   guild = client.get_guild(SERVERIDHERE)

   for channel in guild.channels:
     
      while True:
       
         await channel.send('@everyone ANARCHY! SYSTEM COMPROMISED!')
        
     
        

@client.command()
async def spam(ctx, amount: int, *, message):
   
   for i in range(amount):
     
      await ctx.send(message)
      
      
client.run(token)

