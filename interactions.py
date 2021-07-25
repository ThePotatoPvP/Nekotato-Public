# -*- coding: utf-8 -*-
import random

import discord
from discord.ext import commands


class Interactions_setup:
    def __init__(self):
        self.folder = "Interactions/"

        self.bonk_list = open(self.folder + "bonk.txt", "r").readlines()
        self.chase_list = open(self.folder + "chase.txt", "r").readlines()
        self.cuddle_list = open(self.folder + "cuddle.txt", "r").readlines()
        self.glomp_list = open(self.folder + "glomp.txt", "r").readlines()
        self.handhold_list = open(self.folder + "handhold.txt", "r").readlines()
        self.hate_list = open(self.folder + "hate.txt", "r").readlines()
        self.highfive_list = open(self.folder + "highfive.txt", "r").readlines()
        self.hug_list = open(self.folder + "hug.txt", "r").readlines()
        self.kill_list = open(self.folder + "kill.txt", "r").readlines()
        self.kiss_list = open(self.folder + "kiss.txt", "r").readlines()
        self.lick_list = open(self.folder + "lick.txt", "r").readlines()
        self.nom_list = open(self.folder + "nom.txt", "r").readlines()
        self.pat_list = open(self.folder + "pat.txt", "r").readlines()
        self.poke_list = open(self.folder + "poke.txt", "r").readlines()
        self.punch_list = open(self.folder + "punch.txt", "r").readlines()
        self.shoot_list = open(self.folder + "shoot.txt", "r").readlines()
        self.slap_list = open(self.folder + "slap.txt", "r").readlines()
        self.stab_list = open(self.folder + "stab.txt", "r").readlines()
        self.tease_list = open(self.folder + "tease.txt", "r").readlines()
        self.tickle_list = open(self.folder + "tickle.txt", "r").readlines()

        self.self_lick = "https://media1.tenor.com/images/2834a92a3631f54354c49ec0bf7b7c1d/tenor.gif?itemid=16012106"
        self.clap = "https://uploads.disquscdn.com/images/62f9a6b729349cd0ae75706e7011f44fb05d779ded4c587428ea1ef4ca67177e.gif"

    def bonk(self):
        return random.choice(self.bonk_list)

    def chase(self):
        return random.choice(self.chase_list)

    def cuddle(self):
        return random.choice(self.cuddle_list)

    def glomp(self):
        return random.choice(self.glomp_list)

    def hate(self):
        return random.choice(self.hate_list)

    def handhold(self):
        return random.choice(self.handhold_list)

    def highfive(self):
        return random.choice(self.highfive_list)

    def hug(self):
        return random.choice(self.hug_list)

    def kill(self):
        return random.choice(self.kill_list + self.stab_list + self.shoot_list + self.punch_list)

    def kiss(self):
        return random.choice(self.kiss_list)

    def lick(self):
        return random.choice(self.lick_list)

    def nom(self):
        return random.choice(self.nom_list)

    def pat(self):
        return random.choice(self.pat_list)

    def poke(self):
        return random.choice(self.poke_list)

    def punch(self):
        return random.choice(self.punch_list)

    def shoot(self):
        return random.choice(self.shoot_list)

    def slap(self):
        return random.choice(self.slap_list)

    def stab(self):
        return random.choice(self.stab_list)

    def tickle(self):
        return random.choice(self.tickle_list)

    def tease(self):
        return random.choice(self.tease_list)


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ints = Interactions_setup()

    def usage_example(self):
        command = random.choice(self.bot.get_cog('Interactions').get_commands())
        while command.hidden:
            command = random.choice(self.bot.get_cog('Interactions').get_commands())

        return f"{command.name}` {self.bot.user.mention}"

    @commands.command(aliases=["Nom", "Bite", "nom", "Bit", "bit"])
    async def bite(self, ctx, *, bullshit=None):
        """To bite people like a weirdo"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Biting yourself ? that gotta hurt ●﹏●)", color=0xffd1f3)
                embed.set_image(url=self.ints.nom())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is biting"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.nom())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Thanks I guess (´・ω・｀)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Biting the air ? How do you have friends acting like that ?")

    @commands.command(aliases=["Bonk", "bok", "Bok"])
    async def bonk(self, ctx, *, bullshit=None):
        """To bonk weirdos"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Bonking yourself ? good, stay pure", color=0xffd1f3)
                embed.set_image(url=self.ints.bonk())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** bonks"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.bonk())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="I'll try to stay pure")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Bonking the air ? How do you have friends acting like that ?")

    @commands.command(aliases=["Chase", "chases", "Chases"])
    async def chase(self, ctx, *, bullshit=None):
        """To chase people like a weirdo"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="If you're chasing yourself you should run faster.", color=0xffd1f3)
                embed.set_image(url=self.ints.cuddle())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is chasing"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.cuddle())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="(‘ - ’* ) Please stop I'm scared")
                await ctx.send(embed=embed)

        else:
            await ctx.send("You chase nobody, seems like you just wanna run.")

    @commands.command(aliases=["Cuddle", "cuddles", "Cuddles"])
    async def cuddle(self, ctx, *, bullshit=None):
        """To cuddle cuties"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Trying to cuddle yourself, how sad... Let me help you.", color=0xffd1f3)
                embed.set_image(url=self.ints.cuddle())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is cuddling"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.cuddle())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi thanks (〃ﾉωﾉ)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Giving cuddles away ? May I catch some ?")

    @commands.command(aliases=["Glomp", "pounce", "Pounce", "glomps", "Glomps", "Pounces", "pounces", "pounce on", "Pounce on"])
    async def glomp(self, ctx, *, bullshit=None):
        """To pounce on cuties"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="I don't know how you do that but yeah why not", color=0xffd1f3)
                embed.set_image(url=self.ints.glomp())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** pounces on"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.glomp())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Yay \( ﾟヮﾟ)/")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to pounce on, seems like you need friends.")

    @commands.command(aliases=["Hate", "hates", "Hates", "dislike", "Dislike"])
    async def hate(self, ctx, *, bullshit=None):
        """To hate people"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Hating on yourself...here, get some headpats", color=0xffd1f3)
                embed.set_image(url=self.ints.pat())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is hating on"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.hate())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Not cool T.T")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to hold your hand, seems like people are too far for your short arms.")

    @commands.command(aliases=["Handhold", "handholding", "Handholding", "hold hand", "Hold hand"])
    async def handhold(self, ctx, *, bullshit=None):
        """To hold cuties' hands"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Holding your own hand, how sad... Let me help you.", color=0xffd1f3)
                embed.set_image(url=self.ints.handhold())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is holding the hand of"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.handhold())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi thanks (′ꈍᴗꈍ‵)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to hold your hand, seems like people are too far for your short arms.")

    @commands.command(aliases=["Highfive", "highfives", "Highfives", "high five", "High five"])
    async def highfive(self, ctx, *, bullshit=None):
        """To highfive people"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Giving a highfive to yourself, this sounds like clapping...", color=0xffd1f3)
                embed.set_image(url=self.ints.clap)
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** gives a highfive to"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.highfive())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Yay \( ﾟヮﾟ)/")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to give a highfive to, seems like people are too far for your short arms.")

    @commands.command(aliases=["Hug", "hugs", "Hugs"])
    async def hug(self, ctx, *, bullshit=None):
        """To hug cuties"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Trying to hug yourself, how sad... Let me help you.", color=0xffd1f3)
                embed.set_image(url=self.ints.hug())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is hugging"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.hug())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi thanks (′ꈍᴗꈍ‵)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Giving hugs away ? May I catch one ?")

    @commands.command(aliases=["Kill", "kills", "Kills"])
    async def kill(self, ctx, *, bullshit=None):
        """To kill weirdos"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Wait... isn't it suicide ?", color=0xffd1f3)
                embed.set_image(url=self.ints.kill())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** killed"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.kill())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Not cool T.T")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Seems like you need aim, I've no idea who you tried to kill.")

    @commands.command(aliases=["Kiss", "Smooch", "smooch"])
    async def kiss(self, ctx, *, bullshit=None):
        """To give a smooch"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Trying to kiss yourself, how sad...", color=0xffd1f3)
                embed.set_image(url=self.ints.pat())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is kissing"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.kiss())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi thanks (〃ﾉωﾉ)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Oh you poor, no one to kiss here")

    @commands.command(aliases=["Lick", "Licc", "licc"])
    async def lick(self, ctx, *, bullshit=None):
        """To lick like a weirdo"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Licking yourself ? Aww what a cute kitty !", color=0xffd1f3)
                embed.set_image(url=self.ints.self_lick)
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is licking"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description + "(〃ﾉωﾉ)")
                embed.set_image(url=self.ints.lick())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Thanks I guess ( 〃．．)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Licking the air ? You might want to look up at the same time :slight_smile:")

    @commands.command(aliases=["Pat", "Pet", "pet", "headpat", "Headpat"])
    async def pat(self, ctx, *, bullshit=None):
        """To give headpats"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Petting yourself ? How sad... Let me help you", color=0xffd1f3)
                embed.set_image(url=self.ints.pat())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is giving headpats to"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.pat())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi thanks (′ꈍᴗꈍ‵)")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Petting nobody ? pet me next time (〃ﾉωﾉ)")

    @commands.command(aliases=["Poke", "Pokes", "pokes"])
    async def poke(self, ctx, *, bullshit=None):
        """To poke people"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Poking yourself ? You must be pretty bored...", color=0xffd1f3)
                embed.set_image(url=self.ints.poke())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is poking"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.poke())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="(‘ - ’* ) I'm literally here 24/7")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to poke, seems like people are too far for your short arms.")

    @commands.command(aliases=["Punch", "punches", "Punches"])
    async def punch(self, ctx, *, bullshit=None):
        """To punch people"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Punching yourself ? You must be pretty bored...", color=0xffd1f3)
                embed.set_image(url=self.ints.punch())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is punching"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.punch())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Not cool T.T")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to poke, seems like people are too far for your short arms.")

    @commands.command(aliases=["Shoot", "shot", "Shot", "Shoots", "shoots", "shots", "Shots"])
    async def shoot(self, ctx, *, bullshit=None):
        """To shoot weirdos"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Wait... isn't it suicide ?", color=0xffd1f3)
                embed.set_image(url=self.ints.shoot())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** shot"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.shoot())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Not cool T.T")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Seems like you need aim, I've no idea who you tried to shoot.")

    @commands.command(aliases=["Slap", "slaps", "Slaps"])
    async def slap(self, ctx, *, bullshit=None):
        """To slap weirdos"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Slapping yourself ? You must be pretty bored...", color=0xffd1f3)
                embed.set_image(url=self.ints.slap())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** slapped"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.slap())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Not cool T.T")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to slap, seems like people are too far for your short arms.")

    @commands.command(aliases=["Stab", "Stabs", "stabs"])
    async def stab(self, ctx, *, bullshit=None):
        """To slap weirdos"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Stabbing yourself ? You must be pretty bored...", color=0xffd1f3)
                embed.set_image(url=self.ints.stab())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** stabbed"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.stab())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Not cool T.T")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to stab, seems like people are too far for your short arms.")

    @commands.command(aliases=["Tease", "Teases", "teases"])
    async def tease(self, ctx, *, bullshit=None):
        """To tease like a weirdo"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Teasing yourself ? You must be pretty horny...", color=0xffd1f3)
                embed.set_image(url=self.ints.tease())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is teasing"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.tease())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi stop uwu")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to tease, seems like you're just awkward.")

    @commands.command(aliases=["Tickle", "Tickles", "tickles"])
    async def tickle(self, ctx, *, bullshit=None):
        """To tickle weirdos like a weirdo"""
        if ctx.message.mentions:

            if len(ctx.message.mentions) == 1 and ctx.message.mentions[0] == ctx.author:
                embed = discord.Embed(description="Tickling yourself ? You must be pretty bored...", color=0xffd1f3)
                embed.set_image(url=self.ints.tickle())
                await ctx.send(embed=embed)

            else:
                description = f"**{ctx.author.display_name}** is tickling"
                for member in ctx.message.mentions:
                    description += f" {member.mention}"
                embed = discord.Embed(color=0xffd1f3, description=description)
                embed.set_image(url=self.ints.tickle())
                if self.bot.user.mentioned_in(ctx.message): embed.set_footer(text="Hihi stop uwu")
                await ctx.send(embed=embed)

        else:
            await ctx.send("Nobody to tickle, seems like people are too far for your short arms.")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def interactions_reload(self, ctx):
        self.ints = Interactions_setup()
        await ctx.message.add_reaction("\u2705")
