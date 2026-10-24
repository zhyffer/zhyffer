# Main Handlers
# reaccionan a disintos tipos de eventos en la app
# la data de la actualizacion viene en el update , la del usuario en el context !!!

from telegram import Update
from telegram.ext import ContextTypes 

class littlehandlers:
    
    @staticmethod
    async def hllo(update : Update , context : ContextTypes.DEFAULT_TYPE) :
        await update.message.reply_text("Welcome to this death Parade , enjoy you instance \n Select one of the following options , rice <3")
    
    @staticmethod
    async def echo (update : Update , context : ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(update.message.text)
        await update.message.reply_text("Iu'll say anything more??? rice \n \t\t\t\t <3")
        
    @staticmethod
    async def rice (update : Update , context : ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('zorra <3')
        
    @staticmethod
    async def spam (update : Update , context : ContextTypes.DEFAULT_TYPE):
        for i in range (10):
            await update.message.reply_text(
                'sorra\nsorra\nsorra\nsorrasorra\nsorra\nsorra\nsorrasorra\nsorra\nsorra\nsorrasorra\nsorra\nsorra\nsorrasorra\nsorra\nsorra'
                                            )
            
    #@staticmethod
    #async def tamare():
    #pass