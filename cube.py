from discord.ext import commands
from time import sleep
from webserver import keep_alive


bot = commands.Bot(command_prefix="cb!", self_bot=True)

@bot.event
async def on_command_error():
  pass

@bot.event
async def on_connect():
  print(f"Logged in as {bot.user.name}#{bot.user.discriminator} (ID: {bot.user.id})")
  
@bot.command()
async def automsg(ctx, message):
    await ctx.message.delete()
    while True:
        await ctx.send(message)
        sleep(1260)
    


#cb!automsg $cube
keep_alive()    
bot.run("token-here", bot=False, reconnect=True)