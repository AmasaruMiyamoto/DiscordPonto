git clone https://github.com/seu-usuario/groq-discord-bot.git
cd groq-discord-bot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env com:
GROQ_API_KEY=sua_chave_groq
DISCORD_TOKEN=seu_token_discord
```

## 🎮 Comandos

| Comando | Descrição |
|---------|-----------|
| `/chat [mensagem]` | Conversa com a IA |
| `/pontoin` | Registra entrada no canal de voz |
| `/pontoout` | Registra saída do canal de voz |
| `/relatorio [@usuário]` | Mostra relatório de presença |
| `/ajuda` | Lista todos os comandos |
| `/ensinar` | Tutorial detalhado |

## 🔒 Permissões Necessárias

O bot precisa das seguintes permissões:
- Enviar Mensagens
- Gerenciar Mensagens
- Ver Canais
- Conectar (Voz)
- Intenção de Conteúdo de Mensagem

## 📊 Logs e Diagnóstico

O bot inclui um sistema de logs detalhado para facilitar o diagnóstico:
- Logs de interação com a Groq API
- Registros detalhados de presença
- Mensagens de erro em português

Os logs são salvos em `bot.log` e podem ser consultados para diagnóstico.

## 🏗️ Estrutura do Projeto

```
DiscordPonto/
├── bot/
│   ├── cogs/
│   │   ├── attendance.py    # Sistema de presença
│   │   ├── chat.py         # Integração com Groq
│   │   └── help.py         # Comandos de ajuda
│   └── utils/
│       ├── attendance_tracker.py
│       ├── config.py
│       └── groq_client.py
└── main.py