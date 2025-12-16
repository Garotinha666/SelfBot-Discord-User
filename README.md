# 🤖 Selfbot Interativo para Discord

Um selfbot completo e interativo para Discord que permite controlar sua conta através de comandos digitados no próprio Discord.

## ⚠️ AVISO IMPORTANTE

**O uso de selfbots VIOLA os Termos de Serviço do Discord e pode resultar em:**
- ❌ Banimento permanente da sua conta
- ❌ Suspensão de IP
- ❌ Perda de acesso ao Discord

**USE POR SUA CONTA E RISCO!** Este projeto é apenas para fins educacionais.

---

## 📋 Índice

- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Comandos Disponíveis](#comandos-disponíveis)
- [Solução de Problemas](#solução-de-problemas)

---

## ✨ Funcionalidades

### 💬 Gerenciamento de DMs
- ✅ Listar todas as DMs abertas
- ✅ Deletar suas mensagens de DMs específicas
- ✅ Deletar mensagens que contenham texto específico
- ✅ Fechar DMs individuais ou todas de uma vez

### 🧹 Limpeza de Mensagens
- ✅ Limpar suas últimas N mensagens de qualquer chat
- ✅ Deletar mensagens com conteúdo sensível
- ✅ Limpeza automática com delays para evitar rate limit

### 👥 Gerenciamento de Amigos (Limitado)
- ⚠️ Listar amigos (pode ter limitações na API)
- ✅ Remover amigos por ID
- ⚠️ Funcionalidades de amigos dependem da versão do discord.py-self

### ⚡ Utilidades
- ✅ Teste de latência (ping)
- ✅ Sistema de ajuda integrado
- ✅ Comandos executados por edição de mensagem (mais discreto)

---

## 📦 Instalação

### Pré-requisitos

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)

### Passo 1: Desinstalar Versões Conflitantes

Antes de instalar, remova versões antigas que podem causar conflitos:

```bash
pip uninstall discord discord.py discord.py-self py-cord -y
pip cache purge
```

### Passo 2: Instalar Dependências

**Opção A - Usando requirements.txt (Recomendado):**
```bash
pip install -r requirements.txt
```

**Opção B - Instalação Manual:**
```bash
pip install discord.py-self aiohttp
```

**Opção C - Se houver problemas:**
```bash
pip install git+https://github.com/dolfies/discord.py-self.git
```

### Passo 3: Verificar Instalação

```bash
python -c "import discord; print(f'✓ Discord.py-self {discord.__version__} instalado!')"
```

Se não houver erros, a instalação foi bem-sucedida! ✅

---

## 🔑 Configuração

### Obter Seu Token do Discord

⚠️ **NUNCA compartilhe seu token com ninguém!**

#### Método 1: Console do Navegador (Mais Fácil)

1. Abra o Discord no navegador: https://discord.com/app
2. Pressione `F12` para abrir o DevTools
3. Vá para a aba **Console**
4. Cole e execute este código:

```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

5. Copie o token que aparecer (sem as aspas)

#### Método 2: Arquivos do Discord (Windows)

1. Pressione `Win + R`
2. Digite: `%appdata%\discord\Local Storage\leveldb`
3. Abra os arquivos `.ldb` com Notepad++
4. Procure por: `"token":"`
5. Copie o token que vem após

#### Método 3: Arquivos do Discord (Linux/Mac)

**Linux:**
```bash
~/.config/discord/Local Storage/leveldb/
```

**Mac:**
```bash
~/Library/Application Support/discord/Local Storage/leveldb/
```

### Configurar o Token no Script

1. Abra o arquivo `selfbot_interativo.py`
2. Localize a linha:
   ```python
   TOKEN = "SEU_TOKEN_AQUI"
   ```
3. Substitua por seu token real:
   ```python
   TOKEN = "MTIzNDU2Nzg5MDEyMzQ1Njc4OQ.GaBcDe.FgHiJkLmNoPqRsTuVwXyZ"
   ```
4. Salve o arquivo (`Ctrl + S`)

### Personalizar Prefixo (Opcional)

Você pode mudar o prefixo dos comandos:

```python
PREFIX = "!"  # Mude para qualquer símbolo: !, ., -, etc.
```

---

## 🚀 Como Usar

### Iniciar o Selfbot

1. Abra o terminal/PowerShell na pasta do projeto
2. Execute:
   ```bash
   python selfbot_interativo.py
   ```
3. Aguarde a mensagem de confirmação:
   ```
   ✅ SELFBOT CONECTADO!
   👤 Usuário: SeuNome
   🆔 ID: 123456789
   ⚡ Prefixo: !
   ```

### Usar Comandos no Discord

1. Abra o Discord (aplicativo ou navegador)
2. Digite comandos em **qualquer canal** ou **DM**
3. Os comandos começam com `!` (ou seu prefixo personalizado)
4. O selfbot irá **editar sua mensagem** com a resposta

---

## 📖 Comandos Disponíveis

### 📋 Comandos Gerais

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `!ajuda` | Mostra lista completa de comandos | `!ajuda` |
| `!ping` | Testa a latência do bot | `!ping` |

### 💬 Comandos de Mensagens DM

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `!dms` | Lista todas as suas DMs abertas | `!dms` |
| `!limpardm <ID> [qtd]` | Deleta suas mensagens de uma DM | `!limpardm 123456789 50` |
| `!deletartexto <ID> <texto>` | Deleta mensagens com texto específico | `!deletartexto 123456789 senha` |
| `!fechardm <ID>` | Fecha uma conversa DM | `!fechardm 123456789` |
| `!fechartodas` | Fecha todas as DMs abertas | `!fechartodas` |

### 👥 Comandos de Amigos

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `!amigos` | Lista seus amigos (limitado) | `!amigos` |
| `!removeramigo <ID>` | Remove um amigo pelo ID | `!removeramigo 123456789` |
| `!limparamigos [dias]` | ⚠️ Não disponível na API atual | - |

### 🧹 Comandos de Limpeza

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `!limpar [qtd]` | Apaga suas últimas N mensagens do chat | `!limpar 10` |

---

## 💡 Exemplos de Uso

### Exemplo 1: Ver suas DMs e limpar uma conversa

```
Você digita: !dms
[Selfbot mostra lista de DMs com IDs]

Você digita: !limpardm 987654321 100
[Selfbot deleta suas últimas 100 mensagens daquela DM]
```

### Exemplo 2: Deletar mensagens com informações sensíveis

```
Você digita: !deletartexto 987654321 senha
[Selfbot busca e deleta todas as mensagens que contêm "senha"]
```

### Exemplo 3: Limpar suas mensagens de um canal

```
Você digita: !limpar 20
[Selfbot deleta suas últimas 20 mensagens do canal atual]
```

### Exemplo 4: Como obter IDs de usuários

1. Ative o **Modo Desenvolvedor** no Discord:
   - `Configurações` → `Avançado` → `Modo Desenvolvedor` ✅
2. Clique com botão direito em um usuário
3. Selecione **"Copiar ID"**
4. Use esse ID nos comandos

---

## 🔒 Dicas de Segurança

### ✅ Boas Práticas

1. **Nunca compartilhe seu token** com ninguém
2. **Use apenas quando necessário** - não deixe rodando 24/7
3. **Aguarde entre ações** - o script já tem delays, não force
4. **Não execute em servidores grandes** - alto risco de detecção
5. **Use em DMs e servidores privados** - mais discreto

### ⚠️ Sinais de Rate Limit

Se você vir:
- Erros `429 Too Many Requests`
- Mensagens não deletando
- Comandos demorando muito

**PARE IMEDIATAMENTE** e aguarde 15-30 minutos.

### 🛡️ Como Minimizar Riscos

- ✅ Use com **moderação**
- ✅ **Não spam** comandos
- ✅ Aguarde alguns **segundos entre comandos**
- ✅ Evite usar em **horários de pico**
- ❌ **NÃO** use para spam ou harassment
- ❌ **NÃO** compartilhe que está usando selfbot

---

## 🐛 Solução de Problemas

### Erro: `discord.py-self não encontrado`

**Solução:**
```bash
pip uninstall discord discord.py discord.py-self -y
pip install discord.py-self
```

### Erro: `Invalid token`

**Causas possíveis:**
- Token copiado incorretamente (faltando partes)
- Espaços antes/depois do token
- Token expirado

**Solução:**
1. Gere um novo token usando o método do navegador
2. Copie TODO o token (incluindo pontos e hífens)
3. Cole entre as aspas sem espaços

### Erro: `'ClientUser' object has no attribute 'relationships'`

**Solução:** Já corrigido na versão atual do script. Se ainda ocorrer:
- Alguns comandos de amigos têm limitações na API
- Use `!removeramigo <ID>` para remover manualmente

### Selfbot não responde aos comandos

**Verificações:**
1. ✅ O selfbot está conectado? (veja mensagem no terminal)
2. ✅ Você está usando o prefixo correto? (padrão: `!`)
3. ✅ O comando está escrito corretamente?
4. ✅ Você tem internet?

### Mensagens não deletam

**Possíveis causas:**
- Mensagens muito antigas (>14 dias)
- Você não é o autor
- Rate limit atingido

**Solução:**
- Aguarde alguns minutos
- Use quantidades menores: `!limpardm <ID> 10`

---

## 📊 Estrutura do Projeto

```
selfbot-discord/
│
├── selfbot_interativo.py    # Script principal
├── requirements.txt          # Dependências
└── README.md                 # Este arquivo
```

---

## 🔄 Atualizações

Para atualizar o discord.py-self:

```bash
pip install --upgrade discord.py-self
```

---

## ⚖️ Isenção de Responsabilidade

Este projeto é fornecido **"como está"**, apenas para fins **educacionais**. 

**O desenvolvedor NÃO se responsabiliza por:**
- ❌ Banimentos de conta
- ❌ Perda de dados
- ❌ Violações dos Termos de Serviço
- ❌ Problemas legais
- ❌ Qualquer dano resultante do uso

**AO USAR ESTE SCRIPT, VOCÊ CONCORDA QUE:**
- Está ciente dos riscos
- Usa por sua própria conta e risco
- Não responsabilizará o desenvolvedor por problemas

---

## 📝 Notas Finais

### Limitações Conhecidas

- ⚠️ Comandos de amigos têm funcionalidade limitada
- ⚠️ Rate limits do Discord são rigorosos
- ⚠️ Mensagens antigas (>14 dias) não podem ser deletadas
- ⚠️ API de relacionamentos pode variar entre versões

### Comandos Mais Usados

1. `!dms` - Ver conversas
2. `!limpardm <ID> 50` - Limpar mensagens
3. `!limpar 10` - Apagar suas mensagens
4. `!deletartexto <ID> senha` - Remover info sensível

### Performance

- ⚡ Delays automáticos entre ações
- ⚡ Otimizado para evitar rate limits
- ⚡ Respostas rápidas (edição de mensagens)

---

## 🆘 Suporte

Se encontrar problemas:

1. ✅ Leia a seção [Solução de Problemas](#solução-de-problemas)
2. ✅ Verifique se seguiu todos os passos de instalação
3. ✅ Confira se seu token está correto
4. ✅ Teste com o comando `!ping` primeiro

---

## 📜 Licença

Este projeto é fornecido sem nenhuma garantia. Use por sua conta e risco.

---

**⚠️ LEMBRE-SE: Use selfbots com responsabilidade e moderação!**

**❤️ Desenvolvido para fins educacionais**
