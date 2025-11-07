from config import BOT_TOKEN

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters, 
)
from handlers import (
    start, help, echo_text, 
    echo_photo, send_products,
    main_menu, settings,
    lenguage, back, order,
    phone_number, about_us,
    coment
)


updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher

# command hendlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))

# message handlers
dispatcher.add_handler(MessageHandler(Filters.text('Mahsulotlar'), send_products))
dispatcher.add_handler(MessageHandler(Filters.text('Bosh Sahifa'), main_menu))
dispatcher.add_handler(MessageHandler(Filters.text('⚙️ Sozlamalar'),settings))
dispatcher.add_handler(MessageHandler(Filters.text("🌐 Tilni o'zgartirish"),lenguage))
dispatcher.add_handler(MessageHandler(Filters.text("📞 Telefon raqamingizni o'zgartiring"),phone_number))
dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Orqaga"),back))
dispatcher.add_handler(MessageHandler(Filters.text("📦 Buyurtmalarim"),order))
dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ Biz haqimizda"),about_us))
dispatcher.add_handler(MessageHandler(Filters.text("✍️ Fikr qoldirish"),coment))
dispatcher.add_handler(MessageHandler(Filters.text, echo_text))
dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))

# botni ishga tushurish
updater.start_polling()
updater.idle()
