# 🤖 Groq Discord AI Assistant + Sistema de Presença

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.3.2+-blue)](https://discordpy.readthedocs.io/)
[![Groq API](https://img.shields.io/badge/Groq-API-green)](https://chat.groq.com/)

Um bot de Discord multifuncional que combina inteligência artificial avançada via Groq API com sistema de registro de presença em canais de voz. Desenvolvido em Python com recursos modernos de interação.

## ✨ Funcionalidades Principais

### 🧠 Núcleo de Inteligência Artificial
- **Conversação Contextual**: Mantém histórico completo das threads (usando `/chat`) 
- **Modelos Potentes**: Suporte para Mixtral 8x7B via Groq 
- **Personalização**: Respostas naturais em português

### ⏱ Sistema de Pontuação
- **Registro Automático**: Monitora entrada/saída em canais de voz
- **Relatórios Detalhados**: Gera relatórios de permanência com `/relatorio`
- **Histórico Armazenado**: Mantém dados para análise
- **Comandos Simples**: `/pontoin` e `/pontoout`

## 🚀 Instalação

### Pré-requisitos
- Python 3.10+
- Conta no [Groq Cloud](https://console.groq.com/)
- Bot criado no [Discord Developer Portal](https://discord.com/developers)

### Configuração
1. Clone o repositório:
```bash
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
GROQ_API_KEY=sua_chave_api
DISCORD_TOKEN=seu_token_bot
```

## ⚙ Comandos

| Comando | Descrição |
|---------|-----------|
| `/chat [texto]` | Conversa com a IA do Groq |
| `/pontoin` | Registra entrada no canal |
| `/pontoout` | Registra saída do canal |
| `/relatorio` | Gera relatório de presença |
| `/ajuda` | Mostra todos os comandos |

## 🔒 Permissões Necessárias
- `Gerenciar Mensagens`
- `Ver Histórico de Mensagens`
- `Conectar em Canal de Voz`
- `Intenção de Conteúdo de Mensagem`

## 🤝 Contribuição
Contribuições são bem-vindas! Siga estas etapas:
1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

Desenvolvido com ❤️ usando Python e Groq AI
