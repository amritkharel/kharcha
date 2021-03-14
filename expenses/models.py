from django.db import models


class Budget(models.Model):
    total_budget = models.IntegerField()
    froms = models.DateTimeField(auto_now_add=True)
    to = models.DateTimeField()

    def __str__(self):
        return f"{self.total_budget}--from{self.froms}--expected_upto__{self.to}"


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    created = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"
