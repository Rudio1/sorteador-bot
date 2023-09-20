import discord
import asyncio
import random
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

sorteio = []
total_participants = 0

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Participar do sorteio', style=discord.ButtonStyle.blurple)
    async def sorteio(self, interaction: discord.Interaction, Button: discord.ui.Button):
        global total_participants
        try:
            userid = interaction.user.id
            if userid not in sorteio:
                sorteio.append(userid)
                total_participants += 1
                await interaction.response.send_message(f"> Boa sorte, você foi cadastrado no sorteio", ephemeral=True)
            else:
                await interaction.response.send_message(f"> Você já se inscreveu no sorteio", ephemeral=True)
            
        except Exception as e:
            print(e)

@client.event
async def on_ready():
    print(f'{client.user.name}')

@client.command(name="nick") 
async def sortearnick(ctx):
    global total_participants
    global sorteio
    if ctx.channel.id == 1154178318757797888:
        guild = client.get_guild(1151924494789779596)
        rolemod = discord.utils.get(guild.roles, id=1151925408925753394)
        if rolemod in ctx.author.roles:  
            try:
                content = ctx.message.content
                content = content.replace('!nick ', "")
                nick, n = content.split(',')
            except:
                await ctx.send(embed=(embed:= discord.Embed(title=f"Faltam argumentos.",description=f'Exemplo de uso:```!nick Karthus,30\n\nnick: Karthus\ninicio do sorteio: 30 segundos```')), ephemeral=True)
                return

            message = await ctx.send(embed=(embed := discord.Embed(title=f'Sorteio do Nick **{nick}**', description=f'Clique no botão para se registrar no sorteio!\nTotal de Participantes: {total_participants}\nO sorteio será realizado em {n} segundos.')), view=(view := Menu()))

            while int(n) > 0:
                await message.edit(embed=discord.Embed(title=f'Sorteio do Nick **{nick}**', description=f'Clique no botão para se registrar no sorteio!\nTotal de Participantes: {total_participants}\nO sorteio será realizado em {n} segundos.'))
                await asyncio.sleep(1) 
                n = str(int(n) - 1)

            sorteado = client.get_user((sorteadoid := random.choice(sorteio)))
            await ctx.send(embed=(embed := discord.Embed(title=f"Parabéns!", description=f"{sorteado.mention} venceu o sorteio e faturou o nick {nick}!")))
            await message.delete()
            total_participants = 0
            sorteio = []
            try:
                await sorteado.send(embed=(embed := discord.Embed(title=f"Ganhou!",description=f"Você se inscreveu e ganhou o sorteio do nick {nick} no servidor da NinjaCorps.\nResgate com:```@rudio1\n@brenoprates\n@gopzera\n@gentlemantrollface```")))
            except:
                pass
        else:
            await ctx.send(embed=(embed := discord.Embed(title=f'Ops...', description=f'Você não tem autorização para isso.\nPeça para um dos {(roledonos := discord.utils.get(guild.roles, id=1151925408925753394)).mention} para iniciar um sorteio.')), view=(view := Menu()))
    


@client.command(name="conta") 
async def sortearconta(ctx):
    global total_participants
    global sorteio
    if ctx.channel.id == 1154178318757797888:
        guild = client.get_guild(1151924494789779596)
        rolemod = discord.utils.get(guild.roles, id=1151925408925753394)
        if rolemod in ctx.author.roles:  
            try:
                content = ctx.message.content
                content = content.replace('!conta ', "")
                nick, n = content.split(',')
            except:
                await ctx.send(embed=(embed:= discord.Embed(title=f"Faltam argumentos.",description=f'Exemplo de uso:```!conta HANDLEVEL/UPADA BOT ,30\n\nconta: HANDLEVEL\ninicio do sorteio: 30 segundos```')), ephemeral=True)
                return

            message = await ctx.send(embed=(embed := discord.Embed(title=f'Sorteio de contas', description=f'Clique no botão para se registrar no sorteio!\nTotal de Participantes: {total_participants}\nO sorteio será realizado em {n} segundos.')), view=(view := Menu()))

            while int(n) > 0:
                await message.edit(embed=discord.Embed(title=f'Sorteio de contas', description=f'Clique no botão para se registrar no sorteio!\nTotal de Participantes: {total_participants}\nO sorteio será realizado em {n} segundos.'))
                await asyncio.sleep(1) 
                n = str(int(n) - 1)
            
            global sorteio
            sorteado = client.get_user((sorteadoid := random.choice(sorteio)))
            await ctx.send(embed=(embed := discord.Embed(title=f"Parabéns!", description=f"{sorteado.mention} venceu o sorteio e ganhou a conta!")))
            await message.delete()
            total_participants = 0
            sorteio = []
            try:
                await sorteado.send(embed=(embed := discord.Embed(title=f"Ganhou!",description=f"Você se inscreveu e ganhou o Sorteio de contas no servidor da NinjaCorps.\nResgate com:```@rudio1\n@brenoprates\n@gopzera\n@gentlemantrollface```")))
            except:
                pass
        else:
            await ctx.send(embed=(embed := discord.Embed(title=f'Ops...', description=f'Você não tem autorização para isso.\nPeça para um dos {(roledonos := discord.utils.get(guild.roles, id=1151925408925753394)).mention} para iniciar um sorteio.')), view=(view := Menu()))
          
client.run('MTE1MzQ5NjQzMzU5MzQyMTg2Nw.G9_Ky4.bDBieUtiu6HfUaDjOQ0bZwfOdt7A-hTbVzo1QA')
