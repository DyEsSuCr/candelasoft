from datetime import datetime


def simulate_email_notification(user, reason):
    return {
        'email_sent': True,
        'to': user.email,
        'subject': reason,
        'timestamp': datetime.now().isoformat(),
    }
