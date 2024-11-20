from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from bot.handlers import start, help_command, register, donate, referral_link, balance, withdraw, handle_message, view_transactions, settings, feedback
from bot.admin import admin_stats, admin_manage_access, admin_view_transactions, admin_schedule_post, admin_weekly_report
from config import TOKEN

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("register", register))
    application.add_handler(CommandHandler("donate", donate))
    application.add_handler(CommandHandler("referral", referral_link))
    application.add_handler(CommandHandler("balance", balance))
    application.add_handler(CommandHandler("withdraw", withdraw))
    application.add_handler(CommandHandler("transactions", view_transactions))
    application.add_handler(CommandHandler("settings", settings))
    application.add_handler(CommandHandler("feedback", feedback))
    application.add_handler(CommandHandler("admin_stats", admin_stats))
    application.add_handler(CommandHandler("admin_manage_access", admin_manage_access))
    application.add_handler(CommandHandler("admin_view_transactions", admin_view_transactions))
    application.add_handler(CommandHandler("admin_schedule_post", admin_schedule_post))
    application.add_handler(CommandHandler("admin_weekly_report", admin_weekly_report))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "main_menu":
        await start(update, context)
    elif query.data == "help":
        await help_command(update, context)
    elif query.data == "register":
        await register(update, context)
    elif query.data == "donate":
        await donate(update, context)
    elif query.data == "referral":
        await referral_link(update, context)
    elif query.data == "balance":
        await balance(update, context)
    elif query.data == "withdraw":
        await withdraw(update, context)
    elif query.data == "transactions":
        await view_transactions(update, context)
    elif query.data == "settings":
        await settings(update, context)
    elif query.data == "feedback":
        await feedback(update, context)

if __name__ == '__main__':
    main()
