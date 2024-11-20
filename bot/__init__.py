# bot/__init__.py

# Пример инициализации
from .handlers import start, help_command, register, donate, referral_link, balance, withdraw
from .admin import admin_stats, admin_manage_access
from .database import get_user, create_user, update_balance
from .payment import process_payment
from .referral import generate_referral_link
