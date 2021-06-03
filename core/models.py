from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField(max_length=255)

    class Meta:
        abstract = True

    def ___str__(self):
        return self.title


class Virtualization(BaseModel):
    pass


class EnvironmentSettings(BaseModel):
    import_command = models.CharField(max_length=255)
