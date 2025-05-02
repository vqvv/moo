import discord
from discord.ext import commands
import json
import threading
from flask import Flask
import requests
import time

# === Load config ===
with open('config.json') as f:
    config = json.load(f)

TOKEN = config["token"]
MESSAGE = "moo"

# === Flask server for self-ping ===
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = threading.Thread(target=run_web)
    thread.start()

def ping_self():
    while True:
        try:
            requests.get("http://localhost:8080")
        except:
            pass
        time.sleep(280)  # Ping every ~5 minutes

# === Discord bot setup ===
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await message.channel.send("" + MESSAGE)
    await bot.process_commands(message)

# === Start web server and ping ===
keep_alive()
ping_thread = threading.Thread(target=ping_self)
ping_thread.start()

# === Run the bot ===
bot.run(TOKEN)
