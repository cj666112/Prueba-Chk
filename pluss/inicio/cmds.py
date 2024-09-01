from configs._def_main_ import *

@rex(['cm','cmd','cmds','comandos','command','help','ayuda'])
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        await msg.reply(cmds,reply_markup=mainstart)
    else:return await msg.reply(controndb,reply_markup=dbre)
    
    
    
    