from configs._def_main_ import *

@rex('ip')
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        ips = msg.text[len('/ip '):]
        if not ips: return await msg.reply('<b><code>.ip 1.1.1.1</code> | Error ip.</b>')
        req = requests.get(f'https://ipwho.is/{ips}')
        if '"success":false' in req.text:
            return await msg.reply('<b>Invalid IP address ❌</b>')
        else:
            rr = req.json()
            ms = ip.format(ips=ips,country=rr['country'],country_code=rr['country_code'],emoji=rr['flag']['emoji'],lat=rr['latitude'],lon=rr['longitude'],city=rr['capital'],domi=rr['connection']['domain'],zip=rr['postal'],name=msg.from_user.first_name)
            await msg.reply(ms) 
    else:  return await msg.reply(controndb,reply_markup=dbre)
