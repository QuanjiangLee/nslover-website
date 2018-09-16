from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

ACTIVE_CHIOCES = (
    ("active", "active"),
    ("deactive", "deactive"),
)


class Archives(models.Model):
    archive_name = models.CharField(max_length=128, verbose_name="归档名")
    archive_date = models.DateField(verbose_name="创建时间")
    archive_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建归类用户")
    class Meta:
        db_table = 'archives'
        verbose_name_plural="归档表"
        ordering = ["-archive_date"]

    def archive_articles(self):
        return Articles.objects.filter(article_archive=self).count()

    def __str__(self):
        return self.archive_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=128, verbose_name="标签名")
    tag_date = models.DateField(verbose_name="创建时间")
    tag_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建标签用户")
    class Meta:
        db_table = 'tags'
        verbose_name_plural="标签表"
        ordering = ["-tag_date"]

    def __str__(self):
        return self.tag_name


class Articles(models.Model):
    article_title = models.CharField(max_length=128, verbose_name="文章名")
    article_archive = models.ForeignKey(Archives, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="归类名")
    article_tags = models.ManyToManyField(
        Tags,
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        verbose_name = "文章标签",
        )
    article_content = models.TextField(verbose_name="文章内容")
    article_author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="文章作者")
    article_images = models.ImageField(upload_to='images/uploads/%Y/%m/%d/', blank=True, null=True, verbose_name="上传文章图片文件")
    article_likes = models.IntegerField(verbose_name="喜欢次数")
    article_created = models.DateTimeField(auto_now_add=True, verbose_name="文章撰写时间")
    article_updated = models.DateTimeField(auto_now=True, verbose_name="文章修改时间")
    artcle_status = models.CharField(max_length=20, choices=ACTIVE_CHIOCES, default="active", verbose_name="文章状态")
    
    class Meta:
        db_table = 'articles'
        verbose_name_plural="文章表"
        ordering = ["-article_created"]

    def __str__(self):
        return self.article_title

"""
class Menu(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True)
    status = models.BooleanField(default=True)
    lvl = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

    def get_children(self):
        return self.menu_set.all()

    def has_children(self):
        if self.get_children():
            return True
        return False
"""