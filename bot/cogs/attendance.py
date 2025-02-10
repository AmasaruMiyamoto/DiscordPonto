import discord
from discord import app_commands
from discord.ext import commands
import logging
from ..utils.attendance_tracker import AttendanceTracker
from datetime import datetime

logger = logging.getLogger(__name__)

class AttendanceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tracker = AttendanceTracker()

    @app_commands.command(name="pontoin", description="Registrar entrada no canal de voz")
    async def ponto_in(self, interaction: discord.Interaction):
        """Registrar entrada manual"""
        if not interaction.user.voice:
            await interaction.response.send_message("Você precisa estar em um canal de voz para registrar entrada!")
            return

        try:
            self.tracker.register_entry(
                user_id=interaction.user.id,
                channel_id=interaction.user.voice.channel.id,
                timestamp=datetime.now()
            )
            await interaction.response.send_message("Entrada registrada com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao registrar entrada: {e}")
            await interaction.response.send_message("Falha ao registrar entrada.")

    @app_commands.command(name="pontoout", description="Registrar saída do canal de voz")
    async def ponto_out(self, interaction: discord.Interaction):
        """Registrar saída manual"""
        try:
            duration = self.tracker.register_exit(
                user_id=interaction.user.id,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(f"Saída registrada. Duração da sessão: {duration}")
        except Exception as e:
            logger.error(f"Erro ao registrar saída: {e}")
            await interaction.response.send_message("Falha ao registrar saída.")

    @app_commands.command(name="relatorio", description="Gerar relatório de presença")
    async def report(self, interaction: discord.Interaction, user: discord.User = None):
        """Gerar relatório de presença"""
        target_user = user or interaction.user

        try:
            report = self.tracker.generate_report(target_user.id)
            await interaction.response.send_message(f"Relatório de Presença para {target_user.name}:\n{report}")
        except Exception as e:
            logger.error(f"Erro ao gerar relatório: {e}")
            await interaction.response.send_message("Falha ao gerar relatório de presença.")

async def setup(bot):
    await bot.add_cog(AttendanceCog(bot))