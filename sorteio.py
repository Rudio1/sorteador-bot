import discord, asyncio
from discord.ext import commands


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)
participantes = []

class Menu(discord.ui.View):
  def init(self):
    super().init(timeout=None)

  @discord.ui.button(label='Participar do sorteio', style=discord.ButtonStyle.blurple)
  async def sorteio(self, interaction: discord.Interaction, Button: discord.ui.Button):
    user_id = interaction.user.id
    participantes.append(user_id)
    print(participantes)



@client.event
async def on_ready():
    print(f'{client.user.name}')

@client.command(name="sorteio") 
async def sortear(ctx):
    content = ctx.message.content.replace("!sorteio ", "")
    nick, time = content.split(" ")
    channel_id = 1154098170230493346 
    if ctx.channel.id == channel_id:
        guild = client.get_guild(1151924494789779596)
        role = discord.utils.get(guild.roles, id=1151925408925753394)
        embed = discord.Embed(title=f'Sorteio do Nick: {nick}', description=f'O nick: {nick}, será sorteado em {time} segundos')
        view = Menu()
        await ctx.send(embed=embed, view=view, content='\@everyone')
        await asyncio.sleep(int(time))  

client.run('MTE1MzQ5NjQzMzU5MzQyMTg2Nw.G9_Ky4.bDBieUtiu6HfUaDjOQ0bZwfOdt7A-hTbVzo1QA')
