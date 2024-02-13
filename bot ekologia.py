import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def co_to_ekologia(ctx):
    print('Ekologia to nauka badająca wzajemne relacje między organizmami a ich środowiskiem, analizująca strukturę i funkcje ekosystemów oraz dynamikę populacji. Skupia się na zrozumieniu adaptacji organizmów do środowiska, interakcjach międzygatunkowych, cyklach biogeochemicznych i wpływie czynników abiotycznych. Ponadto, ekologia bada również wpływ ludzkiej działalności na środowisko naturalne. To interdyscyplinarna dziedzina obejmuje szeroki zakres zagadnień, mających na celu lepsze zrozumienie ekosystemów i przyczyniających się do zrównoważonego gospodarowania zasobami naturalnymi.{bot.user}')










bot.run("wpisz swój token")
