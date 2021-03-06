from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

from .models import Subscription, Mail


class MailAdmin(MarkdownxModelAdmin):
    list_display = ('subject', 'sender_name', 'sender_email', 'date_created')


admin.site.register(Subscription)
admin.site.register(Mail, MailAdmin)
