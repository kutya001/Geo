# from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    deleted_date = models.DateTimeField(verbose_name="Дата удаления", null=True)

    class Meta:
        abstract = True


class Farmer(BaseModel):

    name_farmer = models.CharField("Фермер", max_length=200)

    class Meta:
        db_table = "appGeaDjango_" + "farmer"

    def __str__(self) -> str:
        return f"{self.name_farmer}"


class Culture(BaseModel):

    name_culture = models.CharField("Культура", max_length=200)

    class Meta:
        db_table = "appGeaDjango_" + "culture"

    def __str__(self) -> str:
        return f"{self.name_culture}"


class Season(BaseModel):

    name_season = models.CharField("Сезон", max_length=200)


    class Meta:
        db_table = "appGeaDjango_" + "season"

    def __str__(self) -> str:
        return f"{self.name_season}"


class Place(BaseModel):
    location = models.PointField("Местоположение")
    farmer = models.ForeignKey(Farmer, verbose_name="Фермер", on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, verbose_name="Культура", on_delete=models.CASCADE)
    season = models.ForeignKey(Season, verbose_name="Сезон", on_delete=models.CASCADE)

    class Meta:
        db_table = "appGeaDjango_" + "place"

    def __str__(self) -> str:
        return f"{self.location.wkt}"