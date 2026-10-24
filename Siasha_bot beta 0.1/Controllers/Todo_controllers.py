# Aca vienen todos los modificadores de To_do :)
from telegram import Update
from telegram.ext import ContextTypes

from Models.Todo import Todo
from Models.Todo_list import todo_list  

class TodoController:
    
    @staticmethod
    async def add_todo(update : Update , context : ContextTypes.DEFAULT_TYPE):
        
        # guardando el nombre del todo
        # el split sin parametros por defaul separa por espacios
        comand = update.message.text.split()[0]  # separa el string y toma solo el nombre del comando ( when split queda "/comando + text + text ...")
        # el split separa todo el texto entre comando + nombre del todo 
        # guardandose el nombre del todo en el tittle 
        
        title = ''.join( update.message.text.split(comand)[1])
        # print(comand) descomentar para ver desde la terminal como funca 
        # print(title)
        
        # add el nuevo to_do a la lista de Todo
        todo_list.append(Todo(title))
        await update.message.reply_text("Your new Mission was added sussefully  :) ")
        
        
    # showing the Todoes    
    @staticmethod
    async def todo_list( update : Update , context : ContextTypes.DEFAULT_TYPE):
        # si no hay To_dos se sale
        if (len(todo_list)==0):
            await update.message.reply_text("Don't have nothing to do ...\n ") 
            return # 
        
        reply = ''
        for i , todo in enumerate(todo_list):
            reply = reply + f"{i+1} - {" ❎ " if todo.is_completed else " ⚠️ "} \n"
            
        await update.message.reply_text(reply)
        
    # completing todoes
    @staticmethod
    async def check_todo( update:Update , context : ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if (index.len(todo_list) or index <= 0):
            await update.message.reply_text("Unexist Quest \nInsertar excusa generica...")
            return
        
        todo_list[index-1].set_completed()
        await update.message.reply_text(f'Quest {index} was sussefully completed ')
        # listarlos luego de completarlos # optionals
        # se pueden encadenar controladores asi tipo el Meta de Yugi
        await TodoController.todo_list(update , context)
        
    @staticmethod
    async def clear_todo(update : Update , context : ContextTypes.DEFAULT_TYPE):
        todo_list.clear()
        await update.message.reply_text("All Quest going to the hell ... \nRice <3")
        
        
         
        
        
    