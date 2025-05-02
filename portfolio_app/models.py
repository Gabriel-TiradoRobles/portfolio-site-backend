from django.db import models

# Create your models here.
class Courses(models.Model):
    courseCode = models.CharField(max_length=15)
    courseName = models.CharField(max_length=100)

    def __str__(self):
        return '%d: %s' % (self.id, self.courseCode)
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    

class Languages(models.Model):
    langName = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.langName)


class PapersAndPresentations(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    courseCode = models.ForeignKey(Courses, related_name='papers', on_delete=models.CASCADE)
    courseGrade = models.CharField(max_length=3)
    fileLink = models.CharField(max_length=100)

    def __str__(self):
        return '%d: %s' % (self.id, self.title)
    
    class Meta:
        verbose_name = 'Paper or Presentation'
        verbose_name_plural = 'Papers and Presentations'


class Projects(models.Model):
    projTitle = models.CharField(max_length=100)
    projectType = models.CharField(max_length=30)
    courseCode = models.ForeignKey(Courses, related_name='projects', on_delete=models.CASCADE)
    courseGrade = models.CharField(max_length=3)
    sourceCodeRepo = models.CharField(max_length=200)
    projThumbnail = models.CharField(max_length=200)
    projLanguages = models.ManyToManyField(Languages)

    def __str__(self):
        return '%d: %s' % (self.id, self.projTitle)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectInfo(models.Model):
    projectID = models.ForeignKey(Projects, related_name='project_info', on_delete=models.CASCADE)
    projDescription = models.TextField()
    projCompileInfo = models.TextField()

    # Headers surround with <h2></h2> Images reference with <fig#> (# == img figure number)
    projUiInfo = models.TextField()
    projAddConsiderations = models.TextField()


class ProjectUIImages(models.Model):
    projectInfoID = models.ForeignKey(ProjectInfo, related_name='ui_images', on_delete=models.CASCADE)
    imgHeader = models.CharField(max_length=100)
    imgLink = models.CharField(max_length=100)
    figureNum = models.IntegerField(default=1)

    def __str__(self):
        return '%d: %s -- %s' % (self.id, self.projectInfoID, self.projectInfoID)
    
    class Meta:
        unique_together = ['projectInfoID', 'figureNum']
        ordering = ['projectInfoID']
        verbose_name = 'Project UI Image'
        verbose_name_plural = 'Project UI Images'