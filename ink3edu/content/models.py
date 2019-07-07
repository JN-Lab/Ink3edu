from django.db import models
from django.utils import timezone
from ink3edu.interactions.models import Group, Mentor
from ink3edu.trainings.models import Chapter

class ContentsInChapters(models.Model):
    """
    This class represents the contents per chapters
    This is an association table between Chapter and Content
    where we organize the content inside the chapter
    """
    
    chapter = models.ForeignKey(Chapter,
                                on_delete=models.CASCADE,
                                related_name='chapter_with_contents')
    content = models.ForeignKey('Content',
                                on_delete=models.CASCADE,
                                related_name='content_per_chapters')
    content_number = models.IntegerField()

    def __str__(self):
        return f"{self.chapter.title} - {self.content.title} - {self.content_number}"


class Content(models.Model):
    """
    This class represents the contents created
    """
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    mentor = models.ForeignKey(Mentor,
                               on_delete=models.CASCADE,
                              related_name='contents')
    groups = models.ManyToManyField(Group,
                                    related_name='contents')
    chapters = models.ManyToManyField(Chapter,
                                      through='ContentsInChapters',
                                      related_name='contents')
    url_content_readonly = models.URLField()
    url_content_modification_allowed = models.URLField()

    def __str__(self):
        return self.title