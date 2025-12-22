from django.db import models


class Author(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    bio = models.TextField("Биография", null=True, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    
class Book(models.Model):
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", null=True, blank=True)
    published_date = models.DateField("Год издания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"