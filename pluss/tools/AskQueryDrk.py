from configs._def_main_ import *

@rex('Query')
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        dorks = msg.text[len('/Query '):]
        if not dorks: return await msg.reply('<b><code>.query dorks</code> | error de dorks.</b>')
        msg1 = await msg.reply('<b>Scrappeando Dorks..</b>')
        newreq = AskQuery(dorks).req()
        messag = ""
        messag += f"<b>[•] Hunts Dorks ASK QUERY ✅\n\n[•] Id user : <code>{msg.from_user.id}</code>\n[•] UserName: <code>{msg.from_user.username}</code>\n[•]Dorks: <code>{dorks}</code>\n[•]   ━━ Resultado  ━━ [•]</b>"
        for inputurl in urlsave(newreq):
            messag += f"<b>\n\n[•] Url : <code>{inputurl} </code></b>"
            time.sleep(1.5)
            await msg1.edit(messag)

        monton = len(urlsave(newreq))

        messag += f'''<b>\n\n[•] Monton ⇾ <code>{monton}</code>
━━━━━━━━━
[•] ⇾ M1000
[•] ⇾ @MyDrugs_M1000
━━━━━━━━━</b>'''
        await msg1.edit(messag)
    else: return await msg.reply(controndb,reply_markup=dbre)