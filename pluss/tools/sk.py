from configs._def_main_ import *

@rex('sk')
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
        
        ccskey = msg.text[len('/sk '):]
        if not ccskey: return await msg.reply('<b><code>.sk sk_****</code> | Error Sk.</b>')

        headers={
        "Content-Type": "application/x-www-form-urlencoded"
        }

        data={
        "card[number]": 4543218722787334,
        "card[cvc]": 780,
        "card[exp_month]": 7,
        "card[exp_year]": 2026
        }

        pos = requests.post(f"https://api.stripe.com/v1/tokens",data=data, headers=headers, auth=(ccskey, ""))


        if 'Invalid API Key provided' in pos.text:
            resp = sk.format(res= 'Dead ❌',
                            message='Invalid API Key provided',
                            name=msg.from_user.first_name)
            await msg.reply(resp)
        elif 'api_key_expired' in pos.text:
            resp = sk.format(res= 'Dead ❌',
                                message='api_key_expired',
                                name=msg.from_user.first_name)
            await msg.reply(resp)
        elif 'testmode_charges_only' in pos.text:
            resp = sk.format(res= 'Dead ❌',
                                message='testmode_charges_only',
                                name=msg.from_user.first_name)
            await msg.reply(resp)
            
        elif 'test_mode_live_card' in pos.text:
            resp = sk.format(res= 'Live ✅',
                                message='test_mode_live_card',
                                name=msg.from_user.first_name)
            await msg.reply(resp)
        else:
            resp = sk.format(res= 'Live ✅',
                    message='Aprovado',
                    name=msg.from_user.first_name)
            await msg.reply(resp)
    else:return await msg.reply(controndb,reply_markup=dbre)
