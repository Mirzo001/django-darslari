from django.conf import settings
from django.db import models
from django.urls import reverse


class Card(models.Model):
    bank_name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    card_number = models.IntegerField(blank=False, null=False)
    password = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.bank_name

    # def get_absolute_url(self):
    #     return reverse("article_detail", kwargs={"pk": self.pk})
