from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup

from db import add_user


def start(update: Update, context: CallbackContext):
    if add_user(
        tg_id=update.message.from_user.id,
        full_name=update.message.from_user.full_name,
        username=update.message.from_user.username
    ):
        update.message.reply_text(
            text=f'salom {update.message.from_user.full_name}, botga xush kelibsiz.',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    ['Bosh Sahifa', 'Aloqa']
                ]
            )
        )
    else:
        update.message.reply_text(
            text=f'qaytganingiz bilan {update.message.from_user.full_name}.',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    ['🛍 Buyrtma berish'],
                    ['⚙️ Sozlamalar', '📦 Buyurtmalarim'],
                    ['ℹ️ Biz haqimizda', '✍️ Fikr qoldirish']
                ]
            )
        )

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=f'{update.message.from_user.full_name}, qanday yordam kerak?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ['button 1', 'button 2'],
                ['button 3', 'button 4', 'button 5']
            ]
        )
    )

def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        update.message.text
    )

def echo_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(
        update.message.photo[1]
    )
    
def echo_video(update: Update, context: CallbackContext):
    update.message.reply_video_note(
        update.message.video_note
    )

def send_products(update: Update, context: CallbackContext):
    update.message.reply_text('mana barcha mahsulotlar')

def main_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
                text=f'{update.message.from_user.full_name} bosh menyuga xush kelibsiz.',
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        ['🛍 Buyrtma berish'],
                        ['⚙️ Sozlamalar', '📦 Buyurtmalarim'],
                        ['ℹ️ Biz haqimizda', '✍️ Fikr qoldirish']
                    ]
                )
            )

def order(update: Update, context: CallbackContext):
    context.user_data["state"] = "order"
    update.message.reply_text(
        text=f"{update.message.from_user.full_name} sizda hali buyurtmalar yo'q.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["⬅️ Orqaga"]
            ]
        )
    )
    
def about_us(update: Update, context: CallbackContext):
    context.user_data["state"] = "about_us"
    update.message.reply_text(
        text="""shu yerda joylashganmiz
Elektron pochta: abror4work@gmail.com""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["⬅️ Orqaga"]
            ]
        )
    )

def coment(update: Update, context: CallbackContext):
    context.user_data["state"] = "coment"
    update.message.reply_text(
        text="✍️ Bizga o'z fikringizni qoldiring",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["⬅️ Orqaga"]
            ]
        )
    )
    
def settings(update: Update, context: CallbackContext):
    context.user_data["state"] = "settings" 
    update.message.reply_text(
        text=f"{update.message.from_user.full_name} nimani o'zgartirmoqchisiz",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["🌐 Tilni o'zgartirish"],
                ["📞 Telefon raqamingizni o'zgartiring"],
                ["⬅️ Orqaga"]
            ]
        )
    )
def lenguage(update: Update, context: CallbackContext):
    context.user_data["state"] = "language" 
    update.message.reply_text(
        text="🌐 Tilni tanlang",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["🇺🇸 English"], ["🇺🇿 O'zbekcha"],
                ["🇷🇺 Русский"],
                ["⬅️ Orqaga"]
            ]
        )
    )
def phone_number(update: Update, context: CallbackContext):
    context.user_data["state"] = "phone_number" 
    update.message.reply_text(
        text="📞 Telefon raqamingizni o'zgartiring",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["📞 Mening raqamim"],
                ["⬅️ Orqaga"]   
            ]
        )
    )

def back(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "⬅️ Orqaga":
        current_state = context.user_data.get("state")

        if current_state == "language":
            settings(update, context)

        elif current_state == "phone_number":
            settings(update, context)
        
        elif current_state == "settings":
            main_menu(update, context)
        
        elif current_state == "order":
            main_menu(update, context)
            
        elif current_state == "about_us":
            main_menu(update, context)
            
        elif current_state == "coment":
            main_menu(update, context)