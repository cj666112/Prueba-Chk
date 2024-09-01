from configs._def_main_ import *

@rex(['start','ini','main','iniciar','star'])
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        await client.send_photo(msg.chat.id,'https://imgur.com/a/ZK1QxrJ', startx.format(adc=msg.from_user.id,ada=msg.from_user.first_name,abdc=msg.from_user.username,tt=dia()),reply_markup= mainstart)
    else:
        return await msg.reply(controndb,reply_markup=dbre)
    
