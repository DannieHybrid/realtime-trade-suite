from django.contrib import admin
from .models import LeaderWallet, CopiedTrade


@admin.register(LeaderWallet)
class LeaderWalletAdmin(admin.ModelAdmin):
    list_display = ('alias', 'address', 'is_active', 'created_at')
    search_fields = ('alias', 'address')


@admin.register(CopiedTrade)
class CopiedTradeAdmin(admin.ModelAdmin):
    list_display = ('leader', 'token', 'amount', 'signature', 'copied', 'timestamp')
    search_fields = ('signature', 'token')
    list_filter = ('leader', 'copied', 'timestamp')
