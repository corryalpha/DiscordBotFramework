from discord.ext import commands
import time
import config

class colors: # class to make color print possible
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def debug(text, color:""):
    if not config.silent: # if silent mode is off
        print(color + text + colors.ENDC) # print the text, styled


bot = commands.Bot("<COMMAND PREFIX>") # replace this with anything you want 

debug("Bot is starting.", colors.WARNING) # write "Bot is starting." in yellow

start_time = time.time() # save the start time to a variable

@bot.event
async def on_ready(): # when bot goes online
    end_time = time.time() # get the end time
    time_taken = round(end_time - start_time, 3) # calculate the time taken
    debug(f"Bot started. Time taken: {time_taken} seconds.", colors.OKGREEN) # write time taken to console

@bot.command()
async def somecommand(ctx, args): # command template, feel free to delete, copy, or replace this with anything you want
    debug("Command executed!", colors.WARNING)

bot.run(config.token) # run bot
