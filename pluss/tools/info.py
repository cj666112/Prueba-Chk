from configs._def_main_ import *

@rex(['info','me','user','status','yo','perfil'])
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        ms = info.format(id =msg.from_user.id,name=msg.from_user.first_name,alias=msg.from_user.username,idchat=msg.chat.id)
        await msg.reply(ms)
    else:  return await msg.reply(controndb,reply_markup=dbre)