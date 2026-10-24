from telegram import Update
from telegram.ext import CommandHandler , ConversationHandler , ContextTypes , filters , MessageHandler

NICK , OTHER , ID = range(3) # constantes 

class Conversation:
    
    @staticmethod
    async def reply_non_text(update : Update , context : ContextTypes.DEFAULT_TYPE):
        
        await update.message.reply_text("Don't send nudes , rice .../insertar mas excusas genericas ")
        
    @staticmethod
    async def gimme_data(update : Update , context : ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("who in the heart are you?")
        return NICK
    
    @staticmethod
    async def obtaining_data(update : Update , context : ContextTypes.DEFAULT_TYPE):
        context.user_data['name'] = update.message.text 
        await update.message.reply_text('gimme your id')
        return ID
    
    @staticmethod
    async def get_id(update : Update , context : ContextTypes.DEFAULT_TYPE):
        
        context.user_data['id'] = update.message.text
        await update.message.reply_text('')
        await update.message.reply_text('somtihing more?')
        return OTHER
        
        
    @staticmethod
    async def ending_obtaining(update : Update , context : ContextTypes.DEFAULT_TYPE):
        context.user_data['some'] = update.message.text
        await update.message.reply_text('saving data ... don\'t tunr of the pc ...')
        await update.message.reply_text(
            f'Data saved, Nickname is {context.user_data["name"]}\nID is {context.user_data['id']}\n{context.user_data['some']}')
        return ConversationHandler.END
    
    @staticmethod
    async def killing_conversation(update:Update , context : ContextTypes.DEFAULT_TYPE):
        
        await update.message.reply_text('This conversation is over /nBy Alessana')
        return ConversationHandler.END
    
    
    
# ahora a ver como re mil porongas accedo a esto desde el main ...
# PD , ya pude accederle desde el main , i'll pray to the Fool

ConverController = ConversationHandler(
    # comando que da entrada a la conversacion
    entry_points=[CommandHandler ('data',Conversation.gimme_data)],
    
    states={
        # excluyendo los comandos para que no se carpee cuano matas la conversacion 
        
        NICK:MessageHandler (filters.TEXT & ~filters.COMMAND,Conversation.obtaining_data),
        OTHER:MessageHandler(filters.TEXT & ~filters.COMMAND,Conversation.ending_obtaining),
        ID :MessageHandler  (filters.TEXT & ~filters.COMMAND,Conversation.get_id),
    },
    
    fallbacks=[MessageHandler('muerete', Conversation.killing_conversation)]
)

