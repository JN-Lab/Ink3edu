from django.db import models

class Training(models.Model):
    """
    This class represents the trainings created
    """


    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, 
                                decimal_places=2)
    status = models.ForeignKey('Status', 
                               on_delete=models.CASCADE)
    category = models.ForeignKey('Category', 
                                on_delete=models.CASCADE)
    sections = models.ManyToManyField('Section', 
                                      through='SectionsInTrainings',
                                      related_name='trainings')

    def __str__(self):
        return self.title

class Section(models.Model):
    """
    This class represents the sections created
    """
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    chapters = models.ManyToManyField('Chapter',
                                      through='ChaptersInSections',
                                      related_name='sections')

    def __str__(self):
        return self.title

class SectionsInTrainings(models.Model):
    """
    This class represents the sections per trainings
    This is an association table between Training and Section
    where we organize the sections inside the trainings
    """


    training = models.ForeignKey('Training',
                                on_delete=models.CASCADE,
                                related_name='training_with_sections')
    section = models.ForeignKey('Section',
                                on_delete=models.CASCADE,
                                related_name='section_per_trainings')
    section_number = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.training.title, self.section.title, self.movement_number)

class Chapter(models.Model):
    """
    This class represents the chapters created
    """

    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class ChaptersInSections(models.Model):
    """
    This class represents the chapters per sections
    This is an association tables between Sections and Chapters
    where we organize the chapters inside the sections
    """
    
    section = models.ForeignKey('Section',
                                on_delete=models.CASCADE,
                                related_name='section_with_chapters')
    chapter = models.ForeignKey('Chapter',
                                 on_delete=models.CASCADE,
                                 related_name='chapters_per_section')
    chapter_number = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.section.title, self.chapter.title, self.chapter_number)

class Status(models.Model):
    """
    This class represents the training's status
    """
    PRIVATE = 'PRIVATE'
    PUBLIC = 'PUBLIC'
    TRAINING_STATUS = (
        (PRIVATE, 'PRIVATE'),
        (PUBLIC, 'PUBLIC')
    )

    name = models.CharField(max_length=10,
                              choices=TRAINING_STATUS)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    This class represents the categories created
    """

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
