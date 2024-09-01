from configs._def_main_ import *

@rexbt('es')
async def exit(client, msg):
    with open('db text/user.txt', 'a', encoding='utf-8') as archivo:
        dbdd = f'{msg.from_user.id}\n' 
        archivo.write(dbdd)
        await msg.edit_message_text("<b>Registro completado correctamente. ✅</b>",reply_markup=homedb)

    await client.send_message(chat_id=-1001630559377, text=f"""<b>[•] ⇾ <a>New users register [ 👨🏿 ]</a>
                              
[•] ⇾ Id: <code>{msg.from_user.id}</code>
[•] ⇾ Alias: @{msg.from_user.username}
[•] ⇾ Name: <code>{msg.from_user.first_name}</code>
[•] ⇾ su Idioma (siglas):{msg.from_user.language_code}
[•] ⇾ Telegram premium : {msg.from_user.is_premium}

[•] ⇾ Esto es un control de registro no el un scamm.
━━━━━━━━━
[•] ⇾ M1000
[•] ⇾ @MyDrugs_M1000
━━━━━━━━━
</b>""")