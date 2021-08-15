# -*- coding: utf-8 -*-

import random

import discord
from discord.ext import commands


class Actions_setup:
    def __init__(self):
        self.folder = "Actions/"
        self.blush_list = open(self.folder+"blush.txt", "r").readlines()
        self.cry_list = open(self.folder + "cry.txt", "r").readlines()
        self.dance_list = open(self.folder + "dance.txt").readlines()
        self.die_list = open(self.folder + "die.txt").readlines()
        self.facepalm_list = open(self.folder + "facepalm.txt", "r").readlines()
        self.panic_list = open(self.folder + "panic.txt", "r").readlines()
        self.pout_list = open(self.folder + "pout.txt", "r").readlines()
        self.run_list = open(self.folder + "run.txt", "r").readlines()
        self.scared_list = open(self.folder + "scared.txt", "r").readlines()
        self.shrug_list = open(self.folder + "shrug.txt", "r").readlines()
        self.sip_list = open(self.folder + "sip.txt", "r").readlines()
        self.sleep_list = open(self.folder + "sleepy.txt", "r").readlines()
        self.smile_list = open(self.folder + "smile.txt", "r").readlines()
        self.smug_list = open(self.folder+"smug.txt", "r").readlines()
        self.stare_list = open(self.folder + "stare.txt", "r").readlines()
        self.thumbsup_list = open(self.folder + "thumbsup.txt", "r").readlines()
        self.wave_list = open(self.folder + "wave.txt", "r").readlines()

    def blush(self):
        return random.choice(self.blush_list)

    def cry(self):
        return random.choice(self.cry_list)

    def dance(self):
        return random.choice(self.dance_list)

    def die(self):
        return random.choice(self.die_list)

    def facepalm(self):
        return random.choice(self.facepalm_list)

    def panic(self):
        return random.choice(self.panic_list)

    def pout(self):
        return random.choice(self.pout_list)

    def run(self):
        return random.choice(self.run_list)

    def scared(self):
        return random.choice(self.scared_list)

    def shrug(self):
        return random.choice(self.shrug_list)

    def sip(self):
        return random.choice(self.sip_list)

    def sleep(self):
        return random.choice(self.sleep_list)

    def smile(self):
        return random.choice(self.smile_list)

    def smug(self):
        return random.choice(self.smug_list)

    def stare(self):
        return random.choice(self.stare_list)

    def thumbsup(self):
        return random.choice(self.thumbsup_list)

    def wave(self):
        return random.choice(self.wave_list)


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.acts = Actions_setup()

    def usage_example(self):
        command = random.choice(self.bot.get_cog('Actions').get_commands())
        while command.hidden:
            command = random.choice(self.bot.get_cog('Actions').get_commands())

        return f"{command.name}`"

    @commands.command(aliases=["Blush", "shy", "Shy"])
    async def blush(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** blushes"

        if ctx.message.mentions:
            description += " at"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.blush())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Cry", "sad", "Sad"])
    async def cry(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** cries"

        if ctx.message.mentions:
            description += " from"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.cry())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Dance", "danse", "Danse"])
    async def dance(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** is dancing yay !"

        if ctx.message.mentions:
            description += " with"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.dance())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Die", "dies", "Dies"])
    async def die(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** dies"

        if ctx.message.mentions:
            description += " from"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.die())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Facepalm", "uhh", "Uhh"])
    async def facepalm(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** facepalms..."

        if ctx.message.mentions:
            description += " of"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.facepalm())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Panic", "panics", "Panics"])
    async def panic(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** panics"

        if ctx.message.mentions:
            description += " from"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.panic())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Pout", "pouts", "Pouts"])
    async def pout(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** pouts"

        if ctx.message.mentions:
            description += " about"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.pout())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Run", "runs", "Runs"])
    async def run(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** is running away"

        if ctx.message.mentions:
            description += " from"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.run())
        await ctx.send(embed=embed)

    @commands.command(alases=["Scared", "scare", "Scare"])
    async def scared(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** is scared"

        if ctx.message.mentions:
            description += " of"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.scared())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Shrug"])
    async def shrug(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** shrugs"

        if ctx.message.mentions:
            description += " at"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.shrug())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Sip", "Sips", "sips"])
    async def sip(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** sips"

        if ctx.message.mentions:
            description += " with"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.sip())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Sleep", "Slep", "slep", "sleeps", "Sleeps"])
    async def sleep(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** is feeling sleepy"

        if ctx.message.mentions:
            description += " with"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.sleep())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Smile", "Happy", "happy"])
    async def smile(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** is smiling"

        if ctx.message.mentions:
            description += " at"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.smile())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Smug"])
    async def smug(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** wears their smug face"

        if ctx.message.mentions:
            description += " at"
            for member in ctx.message.mentionss:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.smug())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Stare", "sugoi", "Sugoi", "Waa", "waa"])
    async def stare(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** is impressed"

        if ctx.message.mentions:
            description += " by"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.stare())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Thumbsup", "thumbs up", "Thumbs up", "thumbup", "Thumbup"])
    async def thumbsup(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** gives a thumbs up"

        if ctx.message.mentions:
            description += " to"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.thumbsup())
        await ctx.send(embed=embed)

    @commands.command(aliases=["Wave", "waves", "Waves", "greet", "Greet", "Greets", "greets", "welcome", "Welcome"])
    async def wave(self, ctx, *, bullshit=None):
        description = f"**{ctx.author.display_name}** waves"

        if ctx.message.mentions:
            description += " at"
            for member in ctx.message.mentions:
                description += f" {member.mention}"

        embed = discord.Embed(color=0xffd1f3, description=description)
        embed.set_image(url=self.acts.wave())
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def actions_reload(self, ctx):
        self.acts = Actions_setup()
        await ctx.message.add_reaction("\u2705")
