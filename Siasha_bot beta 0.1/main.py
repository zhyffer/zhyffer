# Siasha
# Asche_Lillie_bot
# # # # # # # # hupper-m main.py

"""
Last Update : Agoust Random Day that can't remember 
good lucky , dammed 

"""



# Librerias de telegram ... !!!
from telegram import Update
from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes, \
MessageHandler , ConversationHandler , filters , CallbackQueryHandler 

# everything be for make her updateable and extensible 
# adds !!!!!

from Controllers.Handlers import littlehandlers as little
from Controllers.Todo_controllers import TodoController
from Controllers.Talking import Conversation as talk
from Controllers.Talking import ConverController
from Controllers.ProfileController import profile_creator_handler 
from Controllers.KeyboardInline import KeyboardInline

# comand for build the APP # Token , someone that see this are gay :) 
TOKEN = "here_is_where_need_put_the_token"
Siasha_Heart = ApplicationBuilder().token(TOKEN).build()

# The little things that you gimme away <3
Siasha_Heart.add_handler( CommandHandler ('start', little.hllo))
Siasha_Heart.add_handler( CommandHandler ('echo' , little.echo))
Siasha_Heart.add_handler( CommandHandler ('hi',    little.rice))

# Funcionalidad de Gestor de tareas 

Siasha_Heart.add_handler( CommandHandler ('add' ,  TodoController.add_todo))
Siasha_Heart.add_handler( CommandHandler ('list',  TodoController.todo_list))
Siasha_Heart.add_handler( CommandHandler ('check', TodoController.check_todo))
Siasha_Heart.add_handler( CommandHandler ('clear', TodoController.clear_todo))

# Talking with the usser
Siasha_Heart.add_handler( ConversationHandler ( filters.AUDIO & filters.PHOTO & ~filters.TEXT , talk.reply_non_text))
Siasha_Heart.add_handler( ConverController ) # en teoria debe haberse exportado bien ...
# exporta desde el talking lo que falta que solo el de arriba sabe como ...

# Creador de perfiles 
Siasha_Heart.add_handler( profile_creator_handler )

# Inline Keyboard 
## Beta de la Beta 
### high break chance

Siasha_Heart.add_handler( CommandHandler ('keyboard' , KeyboardInline.keyboard_inline))
Siasha_Heart.add_handler( CallbackQueryHandler ( KeyboardInline.keyboard_controller))



# sin esto no corre xdxdxd , venga , hasta el nombre te lo dice , gillipollas <3
Siasha_Heart.run_polling(allowed_updates = Update.ALL_TYPES) # Reacciona a todo lo que envie el usuario 



