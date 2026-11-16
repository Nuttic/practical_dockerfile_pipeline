from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя котика")
    breed = models.CharField(max_length=100, default="Дворовый", blank=True, verbose_name="Порода")
    age = models.PositiveIntegerField(default=1, verbose_name="Возраст (лет)")
    is_cute = models.BooleanField(default=True, verbose_name="Милый ли котик?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Котик"
        verbose_name_plural = "Котики"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.breed})"
