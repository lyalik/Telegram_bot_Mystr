from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.database import session, User, Transaction, Post
from config import ADMIN_ID

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:
        total_users = session.query(User).count()
        privileged_users = session.query(User).filter_by(status='privileged').count()
        total_transactions = session.query(Transaction).count()
        await update.message.reply_text(f'Статистика:\nОбщее количество пользователей: {total_users}\nПривилегированных пользователей: {privileged_users}\nОбщее количество транзакций: {total_transactions}')
    else:
        await update.message.reply_text('У вас нет доступа к этой команде.')

async def admin_manage_access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:
        # Логика управления доступами
        await update.message.reply_text('Введите Telegram ID пользователя для изменения статуса:')
    else:
        await update.message.reply_text('У вас нет доступа к этой команде.')

async def admin_view_transactions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:
        transactions = session.query(Transaction).all()
        message = "История транзакций:\n"
        for transaction in transactions:
            message += f"{transaction.date}: {transaction.amount} TON ({transaction.type}) для пользователя {transaction.user_id}\n"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text('У вас нет доступа к этой команде.')

async def admin_schedule_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:
        # Логика запланирования поста
        await update.message.reply_text('Введите текст поста:')
    else:
        await update.message.reply_text('У вас нет доступа к этой команде.')

async def admin_weekly_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:
        total_users = session.query(User).count()
        privileged_users = session.query(User).filter_by(status='privileged').count()
        total_transactions = session.query(Transaction).count()
        await update.message.reply_text(f'Еженедельный отчёт:\nОбщее количество пользователей: {total_users}\nПривилегированных пользователей: {privileged_users}\nОбщее количество транзакций: {total_transactions}')
    else:
        await update.message.reply_text('У вас нет доступа к этой команде.')
