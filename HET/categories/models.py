from django.db import models


class Categories(models.Model):
    RASHODY = 'Расходы'
    DOHODY = 'Доходы'
    SECTION_CHOICES = [
        (RASHODY, 'Расходы'),
        (DOHODY, 'Доходы'),
    ]

    section = models.CharField(max_length=10, choices=SECTION_CHOICES, default=RASHODY)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
