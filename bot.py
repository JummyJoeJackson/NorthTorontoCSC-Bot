import discord
from discord.ext import commands

# Intents are required for the bot to work properly (DONT DELETE)
intents = discord.Intents.all()

# Includes the intents for the bot to work properly as well as the command prefix (DONT DELETE)
client = commands.Bot(command_prefix = '?', intents=intents)

#Start up code, for when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")

'''
To add a command use the following template:

@client.command() <-- This is the command decorator, needed for the bot to recognize the command
async def <command name>(ctx, parameters): <-- This is the command name, this is what you type in discord to use the command, and the parameters are what you have to pass into the command. You will probably need to put ctx as a parameter in order to send messages. 
    await ctx.send(<message>) <-- This is the code that runs when the command is used, ctx.send sends a message to the channel the command was used in, and the message is what is sent
'''


#Command to test if the bot is working
#Command can be used by doing ?ping in the discord server
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


#Command to add two numbers together
#Command can be used by doing ?add (number1) (number2) in the discord server
@client.command()
async def add(ctx, number1, number2):
    await ctx.send(int(number1) + int(number2))


#Command to calculate grade from given grade and weight
#Command can be used by doing ?calculate_grade (grade1) (weight1) ... in the discord server
@client.command()
async def calculate_grade(ctx, *args): #*args allows the user to enter any number of arguments
    try:
        grades = [float(arg) for arg in args[::2]]
        weights = [float(arg) for arg in args[1::2]]
        
        if len(grades) != len(weights):
            raise ValueError("Number of grades and weights must be the same.")
        
        weighted_sum = sum(g * w for g, w in zip(grades, weights))
        total_weight = sum(weights)
        final_grade = (weighted_sum / total_weight)
        await ctx.send(f"Your calculated grade is: {final_grade:.2f}")
        
    except (ValueError, ZeroDivisionError, IndexError):
        await ctx.send("Invalid Input. Please provide grades and weights in the format: '?calculate_grade grade1 weight1 grade2 weight2 ...'")
        

#Enter the bot token here, in " " (DONT DELETE)
client.run("Token")
