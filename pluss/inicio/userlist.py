from configs._def_main_ import *

@rex(['userlist','list','lista','listausuario','listausuarios'])
async def start(client,msg):
    if msg.from_user.id == 1062237452:
        with open('db text/user.txt', mode='r+', encoding='utf-8') as archivo:
            x = archivo.readlines()
        ass = await msg.reply('<b>Hi señor Max. </b>')
        time.sleep(1.5)
        ss = ""
        ss += ' <b>Users id access bot :\n\n</b>'
        for s in x:
            ss += f'<b>[•] <code>{s} </code></b>'
            await ass.edit(ss)
        mm = len(x)
        ss += f'''<b>\n[•] Monton ⇾ <code>{mm}</code>
━━━━━━━━━
[•] ⇾ M1000
[•] ⇾ @MyDrugs_M1000
━━━━━━━━━</b>'''
        await ass.edit(ss)

    else: return await msg.reply('<b> Losiento solo le respondo a mi creador <code>RexAwait (max)</code></b>')

