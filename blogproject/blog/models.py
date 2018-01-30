from django.db import models
from django.contrib.auth.models import User

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
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return "title:%s, author:%s, time of last modification:%s" % (self.title, self.author.username, self.modified_time)
