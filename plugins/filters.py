import pyrogram
from pyrogram.types import (
InlineKeyboardButton, 
InlineKeyboardMarkup, 
Message,
CallbackQuery
)

from bot import Bot

from pyrogram import (
filters,
Client
)
from config import LOGCHANNEL_ID

 

@Client.on_message(filters.group & filters.text & ~filters.command(["start","help","about","upgrade","donate","add","deletechannel","currentchannel"]))
async def dmca(client: Bot, message: Message):

      buttons = []
      
      async for msg in client.USER.search_messages(LOGCHANNEL_ID,query=message.text,filter='document',limit=50):
                         file_name = msg.document.file_name
                         msg_id = msg.message_id                     
                         link = msg.link
                         buttons.append([InlineKeyboardButton(text=f"{file_name}",url=f"{link}")])
      if not buttons:
         return
      
      buttons.append([InlineKeyboardButton(text=f"⏭️",callback_data="next")])
      await message.reply_text(f"<b> here is the result for {message.text}</b>",reply_markup=InlineKeyboardMarkup(buttons))



@Client.on_callback_query()
async def cb_handler(client: Bot, query:CallbackQuery):

    if "next" in query.data:
        try:
            buttons = []
            async for msg in client.USER.search_messages("@uc_movies",query=query.message.reply_to_message.text,filter='document',limit=20,offset=50):
                  name = msg.document.file_name
                  link = msg.link
                  buttons.append([InlineKeyboardButton(text=f"{name}",url=link")])
            await query.edit_message_reply_markup( 
                reply_markup=InlineKeyboardMarkup(buttons)
           
               )
        except:
              await query.answer("no more result found",show_alert=True)

