from telegram import Update
from telegram.ext import ContextTypes , MessageHandler , ConversationHandler , CommandHandler, filters

USSERNAME , PHOTOGRAPH , INFO = range(3)


class ProfileController:
    
    @staticmethod
    async def starting_getting_info(update : Update , context : ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("who in the fucking heart are you? \ngimme 'uor name , rice :3")
        return USSERNAME
    
    @staticmethod
    async def getting_name(update : Update , context : ContextTypes.DEFAULT_TYPE):
        context.user_data['ussername'] = update.message.text
        await update.message.reply_text("now send a photograph for your profile\n nudes run by your own responsability")
        return INFO
    
    @staticmethod
    async def getting_info(update : Update , context : ContextTypes.DEFAULT_TYPE):
        context.user_data['usserinfo'] = update.message.text
        await update.message.reply_text('Thank \'uo rice , your profile is done sussefully :D')
        await update.message.reply_photo
        return PHOTOGRAPH
    
    @staticmethod
    async def getting_photograph(update : Update , context : ContextTypes.DEFAULT_TYPE):
        message = update.effective_message
        
        if message.photo :
            # las fotos se guardan por peso , se guarda el ultimo elemento de la lista de fotos / el mas pesado
            context.user_data['usserphoto'] = message.photo[-1].file_id
            
            #asi se manda una foto con datos :: =>
            # returning the profile 
            await update.message.reply_photo(
                photo=context.user_data['usserphoto'],
                caption=
                f'{context.user_data['ussername']}\n{context.user_data['usserinfo']}'
            )
    
            
            
        else: 
            await update.message.reply_text('the cry baby was scared and for reveal itself??? pooooooor little hugly thing ')
        
        
        
        return ConversationHandler.END
    
    @staticmethod
    async def killing_conversation(update:Update , context : ContextTypes.DEFAULT_TYPE):
        
        await update.message.reply_text('This conversation is over /nBy Alessana')
        return ConversationHandler.END
    
    
profile_creator_handler = ConversationHandler(
    # comando que da entrada a la conversacion
    entry_points=[CommandHandler ('data',ProfileController.starting_getting_info)],
    
    states={
        # excluyendo los comandos para que no se carpee cuano matas la conversacion 
        # sigue siendo reutilizabre esta base ... xd
        
        USSERNAME  :MessageHandler  (filters.TEXT & ~filters.COMMAND,ProfileController.getting_name),
        INFO       :MessageHandler  (filters.TEXT & ~filters.COMMAND,ProfileController.getting_info),
        PHOTOGRAPH :MessageHandler  (filters.ALL & ~filters.COMMAND,ProfileController.getting_photograph),
    },
    # si algo se esto se cae retirar hasta dejar un solo comando # ignorar/borrar si no se cae 
    fallbacks=[MessageHandler('muerete','parate','tatequieto', ProfileController.killing_conversation)]
)