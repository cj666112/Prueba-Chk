from configs._def_main_ import *

@rex('zip')
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        codep = msg.text[len('/zip '):]
        if not codep: return await msg.reply('<b><code>.zip 10010</code> | Error zip.</b>')
        zip_api = requests.get(f'https://zip.getziptastic.com/v2/US/{codep}')

        if 'Not Found' in zip_api.text:
            return await msg.reply('<b>Not Found | codigo postal erroneo. ❌</b>')
        else:
            ms = zip.format(pais=zip_api.json()['country'],cap=zip_api.json()['postal_code'],ciudad= zip_api.json()['city'],estado=zip_api.json()['state_short'],name=msg.from_user.first_name)
            await msg.reply(ms)    
    else:return await msg.reply(controndb,reply_markup=dbre)