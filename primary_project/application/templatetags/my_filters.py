from django import template
from django.utils.timezone import localtime, now


register = template.Library()

@register.filter
def facebook_timestamp(value):
    now_utc = now()
    value_local = localtime(value)

    diff = now_utc - value_local

    if diff.days == 0 and diff.seconds < 60:
        return 'just now'
    elif diff.days == 0 and 60 <= diff.seconds < 3600:
        minutes = diff.seconds // 60
        return f'{minutes} mins ago'
    elif value_local.date() == now_utc.date():
        return f'today at {value_local.strftime("%H:%M")}'
    elif now_utc.day - value_local.day == 1:    
        return f'yesterday at {value_local.strftime("%H:%M")}'
    else:
        return value_local.strftime("%A at %H:%M")