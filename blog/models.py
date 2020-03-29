from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    verbose_name = '分类'
    verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('标题', max_length=70)  #标题
    body = models.TextField('正文')  # 内容
    created_time = models.DateTimeField('创建时间')  # 创建时间
    modified_time = models.DateTimeField('修改时间')   # 修改时间
    excerpt = models.CharField('摘要', max_length=200, blank=True)   #文章摘要
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

