import discord
from discord.ext import commands

import sqlite3
import json
import os
import aiohttp

from io import BytesIO


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # First we set the prefix
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "-"
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

        await self.help(guild.system_channel)        

        sql_add(guild)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        greet_channel = sql_get(member.guild, "greet_channel")
        default_role = sql_get(member.guild, "default_role")

        if not (greet_channel is None or greet_channel == "None"):
            channel = self.bot.get_channel(int(greet_channel))
            await channel.send(sql_get(member.guild, 'greet_with').replace('@', f'{member.mention}'))

        if not (default_role is None or default_role == "None"):
            role = member.guild.get_role(int(default_role))
            await member.add_roles(role)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def addgif(self, ctx, file, link):
        interactions = os.listdir("Interactions")
        actions = os.listdir("Actions")

        for filename in interactions:
            if file in filename:
                add_link("Interactions/" + filename, link)
                break

        else:
            for filename in actions:
                if file in filename:
                    add_link("Actions/" + filename, link)
                    break

            else:
                ctx.send("I can't seem to find what command is that gif for")

    @commands.command(aliases=["createemoji", "Createemoji", "Addemote", "createemote", "addemoji", "Addemoji"], brief="addemote <url/emote> <name> to add an emote to your server")
    @commands.has_permissions()
    async def addemote(self, ctx, emote=None, *, name=None):
        if emote is None:
            await ctx.send("Use `addemote <url/emote> <name>` to add an emote in this server !")

        elif name is None or len(name)<2:
            await ctx.send("Emote must have a name at least 2 letters long !")

        else:
            #Grab the emote id to have the link to the image
            if emote.startswith("<") and emote.endswith(">"):
                count = 0
                animated = False
                if emote[1] == "a": animated = True
                while count<2:
                    if emote[0] == ":":
                        count+=1
                    emote=emote[1:]
                emote_id = emote[:-1]
                emote = f"https://cdn.discordapp.com/emojis/{emote_id}.png?size=128"
                if animated:
                    emote = emote.replace("png", "gif")
            else:

                if "gif" in emote: animated = True
                else: animated = False
            url = emote

            async with aiohttp.ClientSession() as ses:

                	async with ses.get(url) as r:
                		try:

                			img_or_gif = BytesIO(await r.read())
                			b_value = img_or_gif.getvalue()
                			if r.status in range(200, 299):

                				emoji = await ctx.guild.create_custom_emoji(image=b_value, name=name.replace(" ", ""))
                				if animated :await ctx.send(f'Done, I just added <a:{name}:{emoji.id}> to the server !')
                				else:await ctx.send(f'Done, I just added <:{name}:{emoji.id}> to the server !')
                				await ses.close()

                			else:
                				await ctx.send(f'Error when making request | {r.status} response. !')
                				await ses.close()

                		except discord.HTTPException:
                 		    await ctx.send('An error occured while adding the emoji \n \
                                Please make sure your image is 256*256 or smaller \n \
                                To avoid bugs like this, use the image link directly')

    @commands.command(aliases=["giverole"], brief="Gives the requested role(s) to the requested user(s)")
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx):
        if ctx.message.member_mentions:
            
            if ctx.message.role_mentions:

                for member in ctx.message.mentions:
                    
                    for role in ctx.message.role_mentions:
                        
                        try:
                            await member.add_roles(role, reason=f"{ctx.author.name} asked me to")
                        except discord.Forbidden:
                            await ctx.send(f"I do not have permissions to give {role.mention} role to {member.mention}")
                        except:
                            await ctx.send(f"An error occured while giving `{role.name}` role to {member.mention}")
                
                await ctx.message.add_reaction("\u2705")

            else:
                await ctx.send("Please use `addrole <@member mention> <@role mention>`")

        else:
            await ctx.send(f"Please use `addrole <@member mention> <@role mention>`")
      
    @commands.command(brief="Deletes the requested number of messages, 5 by default.")
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, number="5"):
        try:
            assert int(number) < 100
            assert int(number) > 0
            await ctx.channel.purge(limit=int(number)+1)
        except:
            pass

    @commands.command(aliases=["h", "Help", "H"], brief="Shows the help menu, which I guess you already saw")
    async def help(self, ctx, *, input=""):
        """Show to help page of the bot"""
        # First of all, we grab the prefix if the command is issued in a server
        # And put the default prefix in case it's not
        a_prefix = "-"

        if ctx.guild:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)
                a_prefix = prefixes[str(ctx.guild.id)]
            description = f"My prefix here is `{a_prefix}`\n \n **Have fun playing with me~ ! \n**"

        else:
            description = f"Meow, I like it when you slide in my dms"
        # Now that we have description according to the context, we can start

        # Adapt to include more ways to write the page you want
        if input.lower() in ["n", "neko", "nekotato", "main", "m", "moderation"]:
            input = "main_help"
        elif input.lower() in ["a", "act", "acts", "action"]:
            input = "actions"
        elif input.lower() in ["i", "int", "ints", "interact", "interacts", "interaction"]:
            input = "interactions"

        # If the user is looking for help about a category other than the main one
        # Because the main one has another format
        for cog in self.bot.cogs:

            if input.lower() == cog.lower():
                # We create the embed according to the category
                embed = discord.Embed(title=f"Here's all the {input.lower()} commands I know", color=0xf8e3e1,
                                      description=description)
                commands_list = ""
                # Fill the list of commands in this category
                for command in self.bot.get_cog(cog).get_commands():
                    if not command.hidden:
                        commands_list += f"`{command.name}` | "
                embed.add_field(name="???", value=commands_list[:-3])
                embed.add_field(name="Usage", value=f"`{a_prefix}{self.bot.get_cog(cog).usage_example()}", inline=False)
                break

        else:

            if input == "main_help":
                embed = discord.Embed(title=f"Here are my main commands", color=0xf8e3e1, description=description)
                commands_list = ""
                # Fill the list of commands in the main category
                for command in self.bot.get_cog("Moderation").get_commands():
                    if not command.hidden:
                        commands_list += f"`{command.name}`"
                        commands_list += "???" * (8 - len(command.name))
                        commands_list += f"| {command.brief} \n \n"
                embed.add_field(name="???", value=commands_list[:-2])

            else:
                embed = discord.Embed(color=0xf8e3e1, description=description)

                for cog in self.bot.cogs:
                    commands_list = ""

                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            commands_list += f"`{command.name}` | "
                    embed.add_field(name=f"????{cog}", value=commands_list[:-3], inline=False)

                embed.add_field(name="???",
                                value=f"**Use** `{a_prefix}help <Category>` **for more information about a category.**",
                                inline=False)

        embed.add_field(name="???",
                        value="[Invite me](https://discord.com/api/oauth2/authorize?client_id=862433335833002045&permissions=85056&scope=bot) \
                            | [Support server](https://discord.gg/MBjkNqaSGW) \
                            | [Vote for me](https://top.gg/bot/862433335833002045/vote)",
                        inline=False)

        embed.set_author(name=f"{self.bot.user.display_name}'s help page", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["inv", "Invite", "Inv"], brief="Gives you a link to invite the bot to your own server")
    async def invite(self, ctx):
        embed = discord.Embed(title="Click this to add me to your server !",
                              url="https://discord.com/api/oauth2/authorize?client_id=862433335833002045&permissions=85056&scope=bot",
                              color=0xf8e3e1)
        
        embed.set_author(name="Nekotato's invite link", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(brief="Enables you to change the prefix of the bot on the server")
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, new_prefix=""):
        """To change the prefix of the bot in a server"""
        if (new_prefix.startswith("<:") or new_prefix.startswith("<a:")) and new_prefix.endswith(">") and len(
                new_prefix) > 5:
            await ctx.send("Sorry, to avoid bugs I don't work with that kind of prefix")

        elif new_prefix == "":
            await ctx.send("Sorry, you need to provide me a prefix.")

        else:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = new_prefix.lower()
            with open("prefixes.json", "w") as f:
                json.dump(prefixes, f)

            await ctx.send(f"Understood, my new prefix here is `{new_prefix}` ~")

    @commands.command(aliases=["takerole"], brief="Removes the requested role(s) away from the requested user(s)")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx):
        if ctx.message.member_mentions:
            
            if ctx.message.role_mentions:

                for member in ctx.message.mentions:
                    
                    for role in ctx.message.role_mentions:
                        
                        try:
                            await member.remove_roles(role, reason=f"{ctx.author.name} asked me to")
                        except discord.Forbidden:
                            await ctx.send(f"I do not have permissions to remove {role.mention} role from {member.mention}")
                        except:
                            await ctx.send(f"An error occured while removing `{role.name}` role from {member.mention}")
                
                await ctx.message.add_reaction("\u2705")

            else:
                await ctx.send("Please use `removerole <@member mention> <@role mention>`")

        else:
            await ctx.send("Please use `removerole <@member mention> <@role mention>`")     

    @commands.command(brief="To see and modify my settings in here")
    async def settings(self, ctx):
        embed = discord.Embed(color=0xf8e3e1)

        # First of all, we grab the prefix
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
            cur_prefix = prefixes[str(ctx.guild.id)]
            
            
        greet_channel = sql_get(ctx.guild, "greet_channel")
        # If the server doesn't have enabled the greetings
        if greet_channel is None or greet_channel == "None":
            value = f"This server didn't enable greetings \n \n" \
                    f"Use `{cur_prefix}greet_here` in any channel and I will send my welcomes there. \n" \
                    f"Use `{cur_prefix}greet_with` <welcome sentence> to set this server's welcome sentence \n Use `@` where you want to mention the user.\n"

        else:
            value = f"My greetings channel here is <#{greet_channel}> \n " \
                    f"Use `{cur_prefix}greet_here` in any channel I can write in to make it the new greetings channel."

            value += "\n \n"

            value += f"My greetings sentence is : \n \n {sql_get(ctx.guild, 'greet_with').replace('@', f'{self.bot.user.mention}')} \n \n" \
                     f"To change it use `{cur_prefix}greet_with` <welcome sentence>, use `@` where you want to mention the user."

        embed.add_field(name="Greetings", value=value, inline=False)

        # Default role part
        default_role = sql_get(ctx.guild, "default_role")
        if default_role is None or default_role == "None":
            value = f"This server doesn't have a default role. \n " \
                    f"Use `{cur_prefix}autorole` to set a role to give people when they join the server."

        else:
            value = f"The current default role in this server is <@&{default_role}> .\n " \
                    f"Use `{cur_prefix}autorole` to set a new role to give people when they join the server."

        embed.add_field(name="Default role", value=value, inline=False)

        embed.add_field(name="???", value="[Invite me](https://discord.com/api/oauth2/authorize?client_id=862433335833002045&permissions=85056&scope=bot) \
                        | [Support server](https://discord.gg/MBjkNqaSGW) \
                        | [Vote for me](https://top.gg/bot/862433335833002045/vote)", inline=False)
        embed.set_author(name="Here are my settings for this server.", icon_url=self.bot.user.avatar_url)
        await ctx.channel.send(embed=embed)

    @commands.command(brief="Gives you an invite to my support server")
    async def support(self, ctx):
        """Sends the author an invite link to the support server in dms"""
        await ctx.author.send("Hey, here's the invite to my support server, I hope you'll find the help you need \n "
                              "https://discord.gg/MBjkNqaSGW")  

    @commands.command(aliases=["vot", "Vote", "votes"], brief="Gives you a link to vote for me on top.gg")
    async def vote(self, ctx):
        embed = discord.Embed(title="Click this to vote for me !",
                              url="https://top.gg/bot/862433335833002045/vote",
                              color=0xf8e3e1)
        
        embed.set_author(name="Nekotato's vote link", icon_url=self.bot.user.avatar_url)
        await ctx.author.send(embed=embed)

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def greet_here(self, ctx):
        cur = base.cursor()
        cur.execute('update settings set greet_channel = ? where server_id = ?', (str(ctx.channel.id), str(ctx.guild.id)))
        cur.close()

        await ctx.message.add_reaction("\u2705")

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def greet_with(self, ctx, *greetings):
        cur = base.cursor()
        cur.execute('update settings set greet_with = ? where server_id = ?', (greetings, str(ctx.guild.id)))
        cur.close()

        await ctx.message.add_reaction("\u2705")

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def autorole(self, ctx):
        if ctx.message.role_mentions and len(ctx.message.role_mentions) == 1:
            cur = base.cursor()
            cur.execute('update settings set default_role = ? where server_id = ?', (ctx.message.role_mentions[0].id, str(ctx.guild.id)))
            cur.close()

            await ctx.message.add_reaction("\u2705")

        else:
            await ctx.send("Please provide the role you want as default")


def add_link(filename, link):
    with open(filename, "a") as f:
        f.write("\n" + link)


def sql_get(server, request):
    cur = base.cursor()

    cur.execute(f"select {request} from settings where server_id = ?", (str(server.id),))
    base.commit()
    result = cur.fetchall()[0][0] 

    cur.close()
    return result


def sql_add(server):
    cur = base.cursor()

    my_tuple = (str(server.id), "None", "Welcome @ I hope you'll find here everything you need ~", "None")
    cur.execute("insert into settings(server_id, greet_channel, greet_with, default_role) values(?,?,?,?)", my_tuple)
    base.commit()

    cur.close()


def sql_set(server, request, new):
    cur = base.cursor()

    try:
        cur.execute(f"update settings set {request} = ? where server_id = ?", (new, str(server.id)))
        base.commit()
    except:
        print("Can't set new settings")

    cur.close()

base = sqlite3.connect("nekotato_settings.db")
