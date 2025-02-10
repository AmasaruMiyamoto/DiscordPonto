import discord
from discord import app_commands
from discord.ext import commands
import logging

logger = logging.getLogger(__name__)

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ajuda", description="Mostra todos os comandos disponíveis e suas funções")
    async def help(self, interaction: discord.Interaction):
        """Mostra lista de comandos e suas funções"""
        try:
            help_embed = discord.Embed(
                title="📚 Ajuda - Lista de Comandos",
                description="Aqui estão todos os comandos disponíveis:",
                color=discord.Color.blue()
            )

            help_embed.add_field(
                name="🎯 Comandos de Presença",
                value=(
                    "`/pontoin` - Registra sua entrada no canal de voz\n"
                    "`/pontoout` - Registra sua saída do canal de voz\n"
                    "`/relatorio` - Gera um relatório detalhado da sua presença"
                ),
                inline=False
            )

            help_embed.add_field(
                name="💬 Comandos de Chat",
                value=(
                    "`/chat [mensagem]` - Conversa com a IA do Groq\n"
                    "A IA mantém o contexto da conversa no canal atual"
                ),
                inline=False
            )

            help_embed.add_field(
                name="❓ Ajuda",
                value=(
                    "`/ajuda` - Mostra esta mensagem de ajuda\n"
                    "`/ensinar` - Tutorial detalhado de como usar o bot"
                ),
                inline=False
            )

            help_embed.set_footer(text="Bot desenvolvido com Groq AI e Sistema de Presença")

            await interaction.response.send_message(embed=help_embed)

        except Exception as e:
            logger.error(f"Erro ao mostrar ajuda: {e}")
            await interaction.response.send_message(
                "Desculpe, encontrei um erro ao mostrar a ajuda.",
                ephemeral=True
            )

    @app_commands.command(name="ensinar", description="Tutorial detalhado de como usar o bot")
    async def teach(self, interaction: discord.Interaction):
        """Tutorial detalhado sobre todas as funções do bot"""
        try:
            tutorial_embed = discord.Embed(
                title="🎓 Tutorial - Como usar o Bot",
                description="Guia completo de todas as funcionalidades!",
                color=discord.Color.green()
            )

            # Sistema de Presença
            tutorial_embed.add_field(
                name="⏱️ Sistema de Presença",
                value=(
                    "**Como Registrar Presença:**\n"
                    "1. Entre em um canal de voz\n"
                    "2. Use `/pontoin` para registrar entrada\n"
                    "3. Ao sair, use `/pontoout`\n"
                    "4. Para ver seu histórico: `/relatorio`\n\n"
                    "**Dicas:**\n"
                    "• O bot registra o tempo exato\n"
                    "• Você pode ver relatórios de outros usuários mencionando-os\n"
                    "• O histórico mostra as últimas 5 sessões"
                ),
                inline=False
            )

            # Sistema de Chat
            tutorial_embed.add_field(
                name="🤖 Chat com IA",
                value=(
                    "**Como Conversar com a IA:**\n"
                    "1. Use `/chat [sua mensagem]`\n"
                    "2. A IA mantém contexto da conversa\n"
                    "3. Pode fazer perguntas complexas\n\n"
                    "**Dicas:**\n"
                    "• A IA usa Groq (Mixtral 8x7B)\n"
                    "• Respostas são em português\n"
                    "• Cada canal tem seu próprio histórico"
                ),
                inline=False
            )

            # Exemplos Práticos
            tutorial_embed.add_field(
                name="📝 Exemplos Práticos",
                value=(
                    "**Registro de Presença:**\n"
                    "`/pontoin` - Ao entrar na call\n"
                    "`/pontoout` - Ao sair da call\n"
                    "`/relatorio @usuário` - Ver relatório\n\n"
                    "**Chat com IA:**\n"
                    "`/chat olá` - Iniciar conversa\n"
                    "`/chat me explique X` - Fazer perguntas"
                ),
                inline=False
            )

            tutorial_embed.set_footer(text="Use /ajuda para ver a lista rápida de comandos")

            await interaction.response.send_message(embed=tutorial_embed)

        except Exception as e:
            logger.error(f"Erro ao mostrar tutorial: {e}")
            await interaction.response.send_message(
                "Desculpe, encontrei um erro ao mostrar o tutorial.",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(HelpCog(bot))