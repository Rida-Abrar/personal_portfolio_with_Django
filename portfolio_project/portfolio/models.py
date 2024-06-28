from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_completed = models.IntegerField()

    def __str__(self):
        return f"{self.degree} at {self.institution} ({self.year_completed})"

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company} ({self.start_date} - {self.end_date})"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completion_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.completion_date})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
