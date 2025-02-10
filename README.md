git clone https://github.com/AmasaruMiyamoto/DiscordPonto.git
cd DiscordPonto
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
| `/chat [mensagem]` | Inicia uma conversa com a IA |
| `/pontoin` | Registra entrada no canal de voz |
| `/pontoout` | Registra saída do canal de voz |
| `/relatorio [@usuário]` | Mostra relatório de presença |
| `/ajuda` | Lista todos os comandos |
| `/ensinar` | Tutorial detalhado do bot |

## 🔒 Permissões Necessárias

O bot precisa das seguintes permissões no Discord:
- Enviar Mensagens
- Gerenciar Mensagens
- Ver Canais
- Conectar (Voz)
- Intenção de Conteúdo de Mensagem

## 🛠️ Desenvolvimento

### Estrutura do Projeto
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