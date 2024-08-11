from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class man(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = "People"

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year", )

class Grade(models.Model):
    man = models.ForeignKey(man, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Grade(models.Model):
    # ...

    def __str__(self):
        return f"{self.grade}, {self.man}, {self.course}"