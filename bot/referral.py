from bot.database import get_user, update_balance

def generate_referral_link(telegram_id):
    user = get_user(telegram_id)
    if user:
        user.referral_link = f'https://t.me/Mysr_test_bot?start={telegram_id}'
        return user.referral_link
    return None

def track_referrals(invited_telegram_id):
    inviter = get_user(invited_telegram_id)
    if inviter:
        inviter.invited_count += 1
        if inviter.invited_count >= 5:
            inviter.status = 'privileged'
        update_balance(inviter.telegram_id, 0.2 * amount)  # 20% от подписки
