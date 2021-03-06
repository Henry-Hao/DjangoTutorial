from django.db import models
from django.contrib.auth.models import User
import markdown,pygments
from django.utils.html import strip_tags

# Create your models here.
'''
    Table:Category
    Fields:
        id --- primary key
        name(char(100)) --- name of the category(Eg. Django, Python)
'''
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

'''
    Table:Tag
    Fields:
        id --- primary key
        name(char(100)) --- name of the tag(Eg. DjangoLearning, PythonLearning)
'''
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

'''
    Table: Article
    Fields:
        id --- primary key
        title(char(70)) --- title of the article
        text(text()) --- text of the article
        created_time(DateTimeField()) -- time of the creation
        modified_time(DateTimeField()) -- time of the latest modification
        excerpt(char(200)) --- abstract of the article
        tag(Tag) --- tag of this article
        category(Category) --- category of the article
        author(User) --- author of the article
'''

class Article(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True, null=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog:detail', kwargs={'pk': self.pk})
    
    def save(self, *args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=['extra','codehilite','toc'])
            self.excerpt = strip_tags(md.convert(self.text))[:54]
        super(Article,self).save(*args,**kwargs)



    class Meta:
        ordering = ['-created_time', 'title']
