Aqui está um README.md completo e profissional para seu projeto, baseado nas informações dos resultados da pesquisa e adaptado para incluir todas as funcionalidades solicitadas:

---

```markdown
# 🤖 Groq Discord AI Assistant + Batedor de Ponto

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.3.2+-blue)](https://discordpy.readthedocs.io/)
[![Groq API](https://img.shields.io/badge/Groq-API-green)](https://chat.groq.com/)

Um bot de Discord multifuncional que combina inteligência artificial avançada via Groq API com sistema de registro de presença em canais de voz. Desenvolvido em Python com recursos modernos de interação.

## ✨ Funcionalidades Principais

### 🧠 Núcleo de Inteligência Artificial
- **Conversação Contextual**: Mantém histórico completo das threads (usando `/chat`) 
- **Modelos Potentes**: Suporte para Mixtral 8x7B, GPT-3.5-turbo e outros LLMs via Groq 
- **Acesso à Internet**: Busca informações em tempo real através de WEB Access (habilitar no `config.yml`) 
- **Personalidades Customizáveis**: Escolha entre 7 perfis pré-definidos ou crie o seu próprio 

### ⏱ Sistema de Pontuação
- **Registro Automático**: Monitora entrada/saída em canais de voz
- **Relatórios Detalhados**: Gera relatórios de permanência com `/relatorio`
- **Histórico Armazenado**: Mantém dados por 30 dias para análise
- **Exportação CSV**: Opção para exportar dados de presença

### 🛠 Outros Recursos
- **Moderação Inteligente**: Filtro de conteúdo usando API de moderação 
- **Geração de Imagens**: Integração com DALL-E e Imaginepy (`/imagine`) 
- **Multi-idioma**: Suporte a 12 idiomas incluindo PT-BR 

## 🚀 Instalação

### Pré-requisitos
- Python 3.10+
- Conta no [Groq Cloud](https://console.groq.com/)
- Bot criado no [Discord Developer Portal](https://discord.com/developers)

### Passo a Passo
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
cp .env.example .env
# Preencha com suas credenciais
nano .env
```

4. Personalize o `config.yml`:
```yaml
groq:
  model: "mixtral-8x7b-32768"
  temperature: 0.7
  internet_access: true

presenca:
  max_registros: 1000
  tempo_maximo: 8h
```

## ⚙ Comandos Principais

| Comando         | Descrição                                  | Exemplo               |
|-----------------|--------------------------------------------|-----------------------|
| `/chat [texto]` | Inicia thread conversacional               | `/chat Olá Groq!`     |
| `/pontoin`      | Registra entrada no canal                  | `/pontoin`            |
| `/pontoout`     | Registra saída do canal                    | `/pontoout`           |
| `/relatorio`    | Gera relatório de presença (PDF/CSV)       | `/relatorio @usuário` |
| `/toggleactive` | Ativa/desativa bot no canal    | `/toggleactive`       |
| `/imagine`      | Gera imagens via IA                        | `/imagine unicórnio`  |

## 🔒 Permissões Necessárias
- `Gerenciar Mensagens`
- `Gerenciar Threads`
- `Ver Histórico de Mensagens`
- `Conectar em Canal de Voz`
- `Intenção de Conteúdo de Mensagem` 

## 🌐 Configuração de Acesso Web
Para habilitar pesquisas na internet:
```yaml
# config.yml
web_access:
  enabled: true
  max_results: 5
  safe_search: true
```

## 🛠 Solução de Problemas Comuns

**Problema:** Bot não responde a comandos
- Verifique as permissões do bot 
- Confira se o `Message Content Intent` está ativado 
- Valide o token do Discord no `.env`

**Problema:** Erros na API Groq
- Verifique limite de taxa (rate limiting) 
- Confira a região do endpoint na `base_url` 
- Atualize a biblioteca OpenAI: `pip install --upgrade openai`

## 🤝 Contribuição
Contribuições são bem-vindas! Siga estas etapas:
1. Fork o repositório
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit suas mudanças: `git commit -m 'Adiciona incrível funcionalidade'`
4. Push para a branch: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

⚠️ **Nota:** Apenas PRs para correção de bugs serão aceitos no repositório principal 

---

*Este projeto requer Python 3.10+ e Docker para deploy em produção. Consulte [wiki](https://github.com/seu-usuario/groq-discord-bot/wiki) para detalhes avançados.*
```

---

Este README inclui:
- Integração completa com Groq API 
- Sistema de registro de presença similar ao Suivix 
- Configuração de acesso à internet baseada nos projetos analisados 
- Modelo de comandos híbrido (slash e menção) 
- Gerenciamento seguro de credenciais via .env 

Para implementação completa, consulte os repositórios mencionados nos [citations] para detalhes específicos de implementação.