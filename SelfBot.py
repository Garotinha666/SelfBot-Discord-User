import discord
import asyncio
from typing import Optional
from datetime import datetime, timezone

class InteractiveSelfbot(discord.Client):
    """
    Selfbot interativo - Execute comandos digitando no Discord
    
    ⚠️ AVISO: Uso de selfbots viola os Termos de Serviço do Discord
    Use com moderação e por sua conta e risco!
    """
    
    def __init__(self, prefix: str = "!"):
        super().__init__()
        self.prefix = prefix
        print(f"🤖 Prefixo dos comandos: {prefix}")
        print(f"   Exemplo: {prefix}ajuda")
    
    async def on_ready(self):
        print('='*60)
        print(f'✅ SELFBOT CONECTADO!')
        print(f'👤 Usuário: {self.user.name}')
        print(f'🆔 ID: {self.user.id}')
        print(f'⚡ Prefixo: {self.prefix}')
        print('='*60)
        print(f'\n💡 Digite "{self.prefix}ajuda" em qualquer canal para ver comandos!')
        print('🔴 Pressione Ctrl+C para desligar\n')
    
    async def on_message(self, message):
        # Ignora mensagens de outros usuários
        if message.author.id != self.user.id:
            return
        
        # Verifica se a mensagem começa com o prefixo
        if not message.content.startswith(self.prefix):
            return
        
        # Separa comando e argumentos
        parts = message.content[len(self.prefix):].strip().split()
        if not parts:
            return
        
        comando = parts[0].lower()
        args = parts[1:]
        
        # ==================== COMANDOS ====================
        
        try:
            # AJUDA
            if comando == "ajuda" or comando == "help" or comando == "comandos":
                await self.cmd_ajuda(message)
            
            # PING
            elif comando == "ping":
                await self.cmd_ping(message)
            
            # LISTAR AMIGOS
            elif comando == "amigos" or comando == "listaramigos":
                await self.cmd_listar_amigos(message)
            
            # REMOVER AMIGO
            elif comando == "removeramigo":
                if not args:
                    await message.edit(content="❌ Use: `!removeramigo <ID>`")
                    return
                await self.cmd_remover_amigo(message, args[0])
            
            # REMOVER AMIGOS INATIVOS
            elif comando == "limparamigos":
                dias = int(args[0]) if args else 60
                await self.cmd_limpar_amigos(message, dias)
            
            # LISTAR DMS
            elif comando == "dms" or comando == "listardms":
                await self.cmd_listar_dms(message)
            
            # DELETAR MENSAGENS DM
            elif comando == "limpardm":
                if len(args) < 1:
                    await message.edit(content="❌ Use: `!limpardm <ID_usuario> [quantidade]`")
                    return
                user_id = int(args[0])
                limite = int(args[1]) if len(args) > 1 else 100
                await self.cmd_limpar_dm(message, user_id, limite)
            
            # DELETAR POR CONTEÚDO
            elif comando == "deletartexto":
                if len(args) < 2:
                    await message.edit(content="❌ Use: `!deletartexto <ID_usuario> <texto>`")
                    return
                user_id = int(args[0])
                texto = " ".join(args[1:])
                await self.cmd_deletar_por_texto(message, user_id, texto)
            
            # FECHAR DM
            elif comando == "fechardm":
                if not args:
                    await message.edit(content="❌ Use: `!fechardm <ID_usuario>`")
                    return
                await self.cmd_fechar_dm(message, int(args[0]))
            
            # FECHAR TODAS DMS
            elif comando == "fechartodas":
                await self.cmd_fechar_todas_dms(message)
            
            # LIMPAR CHAT (deleta suas últimas mensagens)
            elif comando == "limpar" or comando == "clear":
                quantidade = int(args[0]) if args else 10
                await self.cmd_limpar_chat(message, quantidade)
            
            # COMANDO NÃO RECONHECIDO
            else:
                await message.edit(content=f"❌ Comando `{comando}` não encontrado. Use `{self.prefix}ajuda`")
                await asyncio.sleep(3)
                await message.delete()
        
        except Exception as e:
            await message.edit(content=f"❌ Erro: {str(e)}")
            await asyncio.sleep(5)
            await message.delete()
    
    # ==================== IMPLEMENTAÇÃO DOS COMANDOS ====================
    
    async def cmd_ajuda(self, message):
        """Mostra lista de comandos"""
        ajuda = f"""
**🤖 COMANDOS DO SELFBOT**

**📋 Geral:**
`{self.prefix}ajuda` - Mostra esta mensagem
`{self.prefix}ping` - Testa latência

**👥 Amigos:**
`{self.prefix}amigos` - Lista todos os amigos
`{self.prefix}removeramigo <ID>` - Remove um amigo
`{self.prefix}limparamigos [dias]` - Remove inativos (padrão: 60 dias)

**💬 Mensagens DM:**
`{self.prefix}dms` - Lista DMs abertas
`{self.prefix}limpardm <ID> [qtd]` - Deleta suas msgs (padrão: 100)
`{self.prefix}deletartexto <ID> <texto>` - Deleta msgs com texto
`{self.prefix}fechardm <ID>` - Fecha uma DM
`{self.prefix}fechartodas` - Fecha todas as DMs

**🧹 Utilidades:**
`{self.prefix}limpar [qtd]` - Limpa suas mensagens (padrão: 10)

**⚠️ Use com moderação para evitar banimento!**
        """
        await message.edit(content=ajuda)
    
    async def cmd_ping(self, message):
        """Testa latência"""
        latencia = round(self.latency * 1000)
        await message.edit(content=f"🏓 Pong! Latência: {latencia}ms")
    
    async def cmd_listar_amigos(self, message):
        """Lista todos os amigos"""
        await message.edit(content="🔍 Buscando amigos...")
        
        try:
            # Busca os relacionamentos do usuário
            amigos = []
            async for relationship in self.user.mutual_friends():
                amigos.append(relationship)
            
            # Se mutual_friends não funcionar, tenta outra forma
            if not amigos:
                # Tenta pegar do cache de usuários
                for user_id, user in self.users.items():
                    if hasattr(user, 'relationship') and user.relationship:
                        if user.relationship.type == discord.RelationshipType.friend:
                            amigos.append(user)
            
            if not amigos:
                await message.edit(content="❌ Nenhum amigo encontrado ou método não suportado.")
                return
            
            # Cria lista formatada
            lista = "**📋 SEUS AMIGOS:**\n\n"
            for idx, friend in enumerate(amigos[:20], 1):  # Mostra até 20
                nome = friend.name if hasattr(friend, 'name') else str(friend)
                user_id = friend.id if hasattr(friend, 'id') else 'N/A'
                lista += f"`{idx}.` {nome} - `{user_id}`\n"
            
            if len(amigos) > 20:
                lista += f"\n*...e mais {len(amigos) - 20} amigos*"
            
            lista += f"\n\n**Total: {len(amigos)} amigos**"
            
            await message.edit(content=lista)
            
        except Exception as e:
            await message.edit(content=f"❌ Erro ao listar amigos: {str(e)}\n\n⚠️ Esta função pode não estar disponível no discord.py-self atual.")
    
    async def cmd_remover_amigo(self, message, user_id):
        """Remove um amigo pelo ID"""
        await message.edit(content=f"🗑️ Removendo amigo ID: {user_id}...")
        
        try:
            user = await self.fetch_user(int(user_id))
            await user.remove_friend()
            await message.edit(content=f"✅ Amigo removido: **{user.name}**")
        except Exception as e:
            await message.edit(content=f"❌ Erro ao remover: {e}")
    
    async def cmd_limpar_amigos(self, message, dias):
        """Remove amigos inativos"""
        await message.edit(content=f"⚠️ Função de limpar amigos não disponível no discord.py-self atual.\n\nUse `!removeramigo <ID>` para remover manualmente.")
    
    async def cmd_listar_dms(self, message):
        """Lista DMs abertas"""
        await message.edit(content="🔍 Buscando DMs...")
        
        dms = [ch for ch in self.private_channels if isinstance(ch, discord.DMChannel)]
        
        if not dms:
            await message.edit(content="❌ Nenhuma DM aberta.")
            return
        
        lista = "**💬 SUAS DMs ABERTAS:**\n\n"
        for idx, dm in enumerate(dms[:15], 1):
            lista += f"`{idx}.` {dm.recipient.name} - `{dm.recipient.id}`\n"
        
        if len(dms) > 15:
            lista += f"\n*...e mais {len(dms) - 15} DMs*"
        
        lista += f"\n\n**Total: {len(dms)} DMs**"
        
        await message.edit(content=lista)
    
    async def cmd_limpar_dm(self, message, user_id, limite):
        """Deleta mensagens de uma DM"""
        await message.edit(content=f"🗑️ Deletando {limite} mensagens...")
        
        try:
            user = await self.fetch_user(user_id)
            dm = await user.create_dm()
            
            deletadas = 0
            async for msg in dm.history(limit=limite):
                if msg.author.id == self.user.id:
                    try:
                        await msg.delete()
                        deletadas += 1
                        await asyncio.sleep(0.8)
                    except:
                        pass
            
            await message.edit(content=f"✅ **{deletadas}** mensagens deletadas de **{user.name}**!")
        except Exception as e:
            await message.edit(content=f"❌ Erro: {e}")
    
    async def cmd_deletar_por_texto(self, message, user_id, texto):
        """Deleta mensagens que contenham um texto"""
        await message.edit(content=f"🔍 Buscando mensagens com '{texto}'...")
        
        try:
            user = await self.fetch_user(user_id)
            dm = await user.create_dm()
            
            deletadas = 0
            async for msg in dm.history(limit=1000):
                if msg.author.id == self.user.id and texto.lower() in msg.content.lower():
                    try:
                        await msg.delete()
                        deletadas += 1
                        await asyncio.sleep(0.8)
                    except:
                        pass
            
            await message.edit(content=f"✅ **{deletadas}** mensagens com '{texto}' deletadas!")
        except Exception as e:
            await message.edit(content=f"❌ Erro: {e}")
    
    async def cmd_fechar_dm(self, message, user_id):
        """Fecha uma DM"""
        await message.edit(content=f"🚪 Fechando DM...")
        
        try:
            user = await self.fetch_user(user_id)
            dm = await user.create_dm()
            await dm.close()
            await message.edit(content=f"✅ DM fechada com **{user.name}**!")
        except Exception as e:
            await message.edit(content=f"❌ Erro: {e}")
    
    async def cmd_fechar_todas_dms(self, message):
        """Fecha todas as DMs"""
        await message.edit(content="🚪 Fechando todas as DMs...")
        
        fechadas = 0
        for channel in list(self.private_channels):
            if isinstance(channel, discord.DMChannel):
                try:
                    await channel.close()
                    fechadas += 1
                except:
                    pass
        
        await message.edit(content=f"✅ **{fechadas}** DMs fechadas!")
    
    async def cmd_limpar_chat(self, message, quantidade):
        """Limpa suas últimas mensagens do chat"""
        canal = message.channel
        deletadas = 0
        
        async for msg in canal.history(limit=quantidade + 1):
            if msg.author.id == self.user.id:
                try:
                    await msg.delete()
                    deletadas += 1
                    await asyncio.sleep(0.5)
                except:
                    pass
        
        # Não precisa editar a mensagem pois ela já foi deletada


# ==================== MAIN ====================

def main():
    """Inicializa o selfbot"""
    
    print("="*60)
    print("🤖 SELFBOT INTERATIVO - DISCORD")
    print("="*60)
    
    # ⚠️ COLE SEU TOKEN AQUI
    TOKEN = "SEU_TOKEN_AQUI"
    
    # Prefixo dos comandos (você pode mudar)
    PREFIX = "!"
    
    if TOKEN == "SEU_TOKEN_AQUI":
        print("\n❌ ERRO: Configure seu token no script!")
        print("   Edite a linha: TOKEN = 'SEU_TOKEN_AQUI'\n")
        input("Pressione Enter para sair...")
        return
    
    # Inicia o selfbot
    client = InteractiveSelfbot(prefix=PREFIX)
    
    try:
        client.run(TOKEN)
    except KeyboardInterrupt:
        print("\n\n✅ Selfbot desligado pelo usuário!")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        input("\nPressione Enter para sair...")


if __name__ == "__main__":
    main()
