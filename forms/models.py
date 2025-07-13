from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()

    
    fields = models.JSONField()

    def __str__(self):
        return self.formNumber
