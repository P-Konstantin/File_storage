from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('storage:file_list_by_category', args=[self.slug])


class File(models.Model):
    category = models.ForeignKey(Category, related_name='files',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='file_images/%Y/%m/%d', blank=True)
    upload_file = models.FileField(upload_to = 'upload_files/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('storage:file_detail', args=[self.id, self.slug])


# Create your models here.

