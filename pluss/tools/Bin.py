from configs._def_main_ import *

@rex('bin')
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        ccbin = msg.text[len('/bin '):]
        if not ccbin: return await msg.reply('<b><code>.bin 123456</code> | ingrese un bin.</b>')
        
        if len(str(ccbin)) < 6: return await msg.reply('<b>el bin es menos de 6 digitos | ingrese un bin.</b>')

        binreq = requests.get(f'https://bins.antipublic.cc/bins/{ccbin}')
        
        if 'Invalid BIN' in binreq.text:
            return await msg.reply('<b>Status Dead ❌ | Invalid BIN.</b>')
        elif 'not found' in binreq.text:
            return await msg.reply('<b>Status Dead ❌ | Invalid BIN.</b>')
        else:
            msg1 = bin.format(binif=ccbin,
                            brand=binreq.json()['brand'],
                            country = binreq.json()['country'],
                            country_name = binreq.json()['country_name'],
                            country_flag = binreq.json()['country_flag'],
                            bank = binreq.json()['bank'],
                            level = binreq.json()['level'],
                            type = binreq.json()['type'],
                            name = msg.from_user.first_name)
            await msg.reply(msg1)
    else:return await msg.reply(controndb,reply_markup=dbre)