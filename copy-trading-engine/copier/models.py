from django.db import models

class LeaderWallet(models.Model):
    address = models.CharField(max_length=64, unique=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alias or self.address


class CopiedTrade(models.Model):
    leader = models.ForeignKey(LeaderWallet, on_delete=models.CASCADE, related_name='trades')
    signature = models.CharField(max_length=100, unique=True)
    token = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    copied = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.token} - {self.amount} from {self.leader}"
