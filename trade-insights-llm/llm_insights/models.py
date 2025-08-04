from django.db import models


class TradeInsight(models.Model):
    leader_address = models.CharField(max_length=100)
    summary = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Aggressive Buying"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.leader_address} — {self.category or 'Insight'} @ {self.created_at.strftime('%Y-%m-%d %H:%M')}"
