from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.database import get_user, create_user, update_balance, get_transactions
from bot.payment import process_payment
from bot.referral import generate_referral_link

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Register", callback_data="register")],
        [InlineKeyboardButton("Donate", callback_data="donate")],
        [InlineKeyboardButton("Referral", callback_data="referral")],
        [InlineKeyboardButton("Balance", callback_data="balance")],
        [InlineKeyboardButton("Withdraw", callback_data="withdraw")],
        [InlineKeyboardButton("Transactions", callback_data="transactions")],
        [InlineKeyboardButton("Settings", callback_data="settings")],
        [InlineKeyboardButton("Feedback", callback_data="feedback")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Я бот с подпиской и реферальной системой.', reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text('Список команд:\n/start - Начало\n/help - Помощь\n/register - Регистрация\n/donate - Донат\n/referral - Реферальная ссылка\n/balance - Баланс\n/withdraw - Вывод средств\n/transactions - История транзакций\n/settings - Настройки\n/feedback - Обратная связь')

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.callback_query.from_user.id)
    if not user:
        create_user(update.callback_query.from_user.id, update.callback_query.from_user.username)
        await update.callback_query.message.reply_text('Вы успешно зарегистрировались!')
    else:
        await update.callback_query.message.reply_text('Вы уже зарегистрированы.')

async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text('Спасибо за донат!')
    # Логика доната

async def referral_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = generate_referral_link(update.callback_query.from_user.id)
    await update.callback_query.message.reply_text(f'Ваша реферальная ссылка: {link}')

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.callback_query.from_user.id)
    if user:
        await update.callback_query.message.reply_text(f'Ваш баланс: {user.balance} TON')
    else:
        await update.callback_query.message.reply_text('Вы не зарегистрированы.')

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.callback_query.from_user.id)
    if user and user.balance > 0:
        await update.callback_query.message.reply_text('Вывод средств...')
        # Логика вывода средств
    else:
        await update.callback_query.message.reply_text('Нет средств для вывода.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Я не понимаю эту команду.')

async def view_transactions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.callback_query.from_user.id)
    if user:
        transactions = get_transactions(user.id)
        message = "История транзакций:\n"
        for transaction in transactions:
            message += f"{transaction.date}: {transaction.amount} TON ({transaction.type})\n"
        await update.callback_query.message.reply_text(message)
    else:
        await update.callback_query.message.reply_text('Вы не зарегистрированы.')

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text('Настройки:\n1. Изменить язык интерфейса (пока не реализовано)')

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text('Пожалуйста, напишите ваше сообщение для администратора:')
    # Логика обратной связи
