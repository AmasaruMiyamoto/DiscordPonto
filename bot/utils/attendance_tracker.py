from datetime import datetime, timedelta
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class AttendanceRecord:
    def __init__(self, user_id: int, channel_id: int, entry_time: datetime):
        self.user_id = user_id
        self.channel_id = channel_id
        self.entry_time = entry_time
        self.exit_time: Optional[datetime] = None
        self.duration: Optional[timedelta] = None

class AttendanceTracker:
    def __init__(self):
        self.active_sessions: Dict[int, AttendanceRecord] = {}
        self.session_history: Dict[int, list[AttendanceRecord]] = {}
        logger.info("AttendanceTracker inicializado")

    def register_entry(self, user_id: int, channel_id: int, timestamp: datetime):
        """Registrar entrada no canal de voz"""
        logger.info(f"Tentando registrar entrada - Usuário: {user_id}, Canal: {channel_id}")

        if user_id in self.active_sessions:
            logger.warning(f"Usuário {user_id} já possui uma sessão ativa no canal {self.active_sessions[user_id].channel_id}")
            return

        record = AttendanceRecord(user_id, channel_id, timestamp)
        self.active_sessions[user_id] = record
        logger.info(f"Entrada registrada com sucesso para usuário {user_id}")

        if user_id not in self.session_history:
            self.session_history[user_id] = []

    def register_exit(self, user_id: int, timestamp: datetime) -> Optional[timedelta]:
        """Registrar saída do canal de voz"""
        logger.info(f"Tentando registrar saída - Usuário: {user_id}")

        if user_id not in self.active_sessions:
            logger.warning(f"Nenhuma sessão ativa encontrada para o usuário {user_id}")
            return None

        record = self.active_sessions[user_id]
        record.exit_time = timestamp
        record.duration = timestamp - record.entry_time

        logger.info(f"Saída registrada - Usuário: {user_id}, Duração: {record.duration}")

        # Move to history
        self.session_history[user_id].append(record)
        del self.active_sessions[user_id]

        return record.duration

    def generate_report(self, user_id: int) -> str:
        """Gerar relatório de presença"""
        logger.info(f"Gerando relatório para usuário {user_id}")

        if user_id not in self.session_history:
            logger.info(f"Nenhum registro encontrado para usuário {user_id}")
            return "Nenhum registro de presença encontrado."

        records = self.session_history[user_id]

        # Calculate total time
        total_duration = timedelta()
        for record in records:
            if record.duration:
                total_duration += record.duration

        # Format report
        report = f"Total de Sessões: {len(records)}\n"
        report += f"Tempo Total: {str(total_duration)}\n\n"
        report += "Sessões Recentes:\n"

        # Show last 5 sessions
        for record in records[-5:]:
            report += f"Entrada: {record.entry_time.strftime('%d/%m/%Y %H:%M:%S')}\n"
            if record.exit_time:
                report += f"Saída: {record.exit_time.strftime('%d/%m/%Y %H:%M:%S')}\n"
                report += f"Duração: {str(record.duration)}\n"
            report += "---\n"

        logger.info(f"Relatório gerado com sucesso para usuário {user_id}")
        return report