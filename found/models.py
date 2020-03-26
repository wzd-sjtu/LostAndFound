from django.db import models

# Create your models here.

from django.db import models
from django.template.defaultfilters import slugify

#   用户验证机制的引用包
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.  //已经存在，不用更改
class KindF(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0, unique=False)
    likes = models.IntegerField(default=0, unique=False)
    slug = models.SlugField(unique=True,default='')

    def save(self,*args,**kwargs):
            self.slug = slugify(self.name)
            super(KindF, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PageF(models.Model):
    kind = models.ForeignKey(KindF, on_delete=models.CASCADE,)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0, unique=False)
    likes = models.IntegerField(default=0, unique=False)
    #  进一步的内容在更加的里面存在的
    def __str__(self):
        return self.title
