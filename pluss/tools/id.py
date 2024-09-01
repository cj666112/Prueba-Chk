from configs._def_main_ import *

@rex(['id','myid','mid','idk','idchat','chatid'])
async def start(client,msg):
    await msg.reply(f'<b>[•] id ⇾ <code>{msg.from_user.id}</code>\n[•] id chat ⇾ <code>{msg.chat.id}</code></b>')