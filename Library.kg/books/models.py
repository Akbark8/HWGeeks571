from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги")
    image = models.ImageField(upload_to='books/', verbose_name="Обложка")
    quatity_page = models.PositiveIntegerField(verbose_name="Количество страниц")
    author = models.CharField(max_length=255, verbose_name="Автор")
    book_audio = models.URLField(verbose_name="Ссылка на аудиокнигу", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
