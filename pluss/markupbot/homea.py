from configs._def_main_ import *

@rexbt('home')
async def exit(client, msg):
    await msg.edit_message_text(cmds,reply_markup=mainstart)
    
