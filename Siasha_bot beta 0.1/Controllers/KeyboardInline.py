### Buttons controllers

from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ContextTypes , CallbackContext, CommandHandler , CallbackQueryHandler # handler de los botones

class KeyboardInline:
    
    @staticmethod
    async def keyboard_inline(update : Update , context : ContextTypes.DEFAULT_TYPE):
        
        # array of arrays , each array represent one line in the keyboard 
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton( text='Generic A' , callback_data='A' ),
                InlineKeyboardButton( text='Generic B' , callback_data='B' ),
                InlineKeyboardButton( text='Generic C' , callback_data='C' ),
                ],
            [
                InlineKeyboardButton( text='Obiton AA' , callback_data='AA' ),
                InlineKeyboardButton( text='Obtion AB' , callback_data='AB' ),
                ],
            [
                InlineKeyboardButton( text='Backspace' , callback_data='Backspace')
                ],
        ])
        
        # esto brikea , revisa con Liora ...
    @staticmethod
    async def keyboard_controller (update : Update , context : CallbackContext):
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(update.callback_query.data)# revisar esto en la documentacion , puede que brickee
        
        await update.callback_query.answer('none')
        
        