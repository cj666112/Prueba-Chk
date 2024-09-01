from configs._def_main_ import *

@rex('gen')
async def start(client,msg):
    with open(file='db text/user.txt', mode='r+', encoding='utf-8') as archivo:
        dbx = archivo.readlines()
    if str(msg.from_user.id) + '\n' in dbx:
       
        ccbin = msg.text[len('/gen '):]
        if not ccbin: return await msg.reply('<b><code>.gen 123456</code> | error de bin.</b>')
        if len(str(ccbin)) < 6: return await msg.reply('<b>el bin es menos de 6 digitos | ingrese un bin.</b>')

        geneo = re.findall(r'[0-9]+',msg.text)
        if not geneo: return await msg.reply('<b>Ingrese el bin a generar | error de bin.</b>')
        
        binreq = requests.get(f'https://bins.antipublic.cc/bins/{ccbin}')
        
        if 'Invalid BIN' in binreq.text:
            return await msg.reply('<b>Status Dead ❌ | Invalid BIN.</b>')
        elif 'not found' in binreq.text:
            return await msg.reply('<b>Status Dead ❌ | Invalid BIN.</b>')
        else:
            if len(geneo) == 1:
                cc = geneo[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'
            elif len(geneo) ==2:
                cc = geneo[0]
                mes = geneo[1]
                ano = 'x'
                cvv = 'x'
            elif len(geneo) ==3:
                cc = geneo[0]
                mes = geneo[1]
                ano = geneo[2]
                cvv = 'x'
            elif len(geneo) ==4:
                cc = geneo[0]
                mes = geneo[1]
                ano = geneo[2]
                cvv = geneo[3]
            else:
                cc = geneo[0]
                mes = geneo[1]
                ano = geneo[2]
                cvv = geneo[3]

            cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)
    
            ms = gen.format(cc1=cc1,cc2=cc2,cc3=cc3,cc4=cc4,cc5=cc5,cc6=cc6,cc7=cc7,cc8=cc8,cc9=cc9,cc10=cc10,binif=binreq.json()['bin'],country = binreq.json()['country'],country_name = binreq.json()['country_name'],country_flag = binreq.json()['country_flag'],name=msg.from_user.first_name)
            await msg.reply(ms,reply_markup=regene)

    else:  return await msg.reply(controndb,reply_markup=dbre)
