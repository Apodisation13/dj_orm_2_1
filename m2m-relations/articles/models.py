from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tag', through='TagThrough', related_name='tagsss')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']


class TagThrough(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тэг', related_name='t1')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='t1')
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-is_main', 'tag']
