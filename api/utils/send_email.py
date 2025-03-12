from datetime import datetime


def simulate_email_notification(user, reason):
    return {
        'email_sent': True,
        'to': user.email,
        'subject': 'Notificación importante sobre tu cuenta',
        'timestamp': datetime.now().isoformat(),
    }
