import os
import asyncio
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
from bot.utils.logging_config import setup_logging
from bot.utils.config import load_config

# Load environment variables from .env file
load_dotenv()

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Load configuration
config = load_config()

# Initialize bot with all intents
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def load_extensions():
    """Load all cogs"""
    await bot.load_extension('bot.cogs.chat')
    await bot.load_extension('bot.cogs.attendance')
    await bot.load_extension('bot.cogs.help')  # Add new help cog

@bot.event
async def on_ready():
    """Called when bot is ready"""
    logger.info(f'Logged in as {bot.user.name}')

    # Generate and log invite link
    permissions = discord.Permissions(
        send_messages=True,
        manage_messages=True,
        read_message_history=True,
        connect=True
    )
    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=permissions
    )
    logger.info(f'Invite Link: {invite_link}')

    # Log servers the bot is in
    for guild in bot.guilds:
        logger.info(f'Connected to server: {guild.name} (ID: {guild.id})')

    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")

def main():
    """Main entry point"""
    try:
        asyncio.run(load_extensions())
        bot.run(os.getenv('DISCORD_TOKEN'))
    except discord.errors.PrivilegedIntentsRequired:
        logger.error(
            "Failed to start bot: Privileged intents are not enabled. "
            "Please enable MESSAGE CONTENT INTENT, SERVER MEMBERS INTENT, "
            "and PRESENCE INTENT in the Discord Developer Portal under "
            "your application's Bot settings."
        )
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    main()