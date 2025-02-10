import discord
from discord import app_commands
from discord.ext import commands
import logging
from ..utils.groq_client import GroqClient
from ..utils.config import load_config

logger = logging.getLogger(__name__)

class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.groq_client = GroqClient()
        self.chat_histories = {}

    @app_commands.command(name="chat", description="Conversar com a IA do Groq")
    async def chat(self, interaction: discord.Interaction, message: str):
        """Gerenciar comando de chat"""
        await interaction.response.defer()

        try:
            # Get chat history for this channel
            channel_id = str(interaction.channel_id)
            if channel_id not in self.chat_histories:
                self.chat_histories[channel_id] = []

            # Add user message to history
            self.chat_histories[channel_id].append({
                "role": "user",
                "content": message
            })

            # Get AI response
            response = await self.groq_client.get_completion(
                self.chat_histories[channel_id]
            )

            # Add AI response to history
            self.chat_histories[channel_id].append({
                "role": "assistant",
                "content": response
            })

            # Send response
            await interaction.followup.send(response)

        except Exception as e:
            logger.error(f"Erro no comando de chat: {e}")
            await interaction.followup.send("Desculpe, encontrei um erro ao processar sua solicitação.")

async def setup(bot):
    await bot.add_cog(ChatCog(bot))