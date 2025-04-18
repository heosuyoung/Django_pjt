from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):  # ⭐ 관심 종목 저장용
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class StockData(models.Model):  # 🧠 댓글 분석 저장용
    company_name = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=20)
    comments = models.TextField()
    analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
