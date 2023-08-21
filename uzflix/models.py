from django.db import models
from django.utils import timezone

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_CHOICES = (
    ("jangari", "JANGARI"),
    ("fantastika", "FANTASTIKA"),
    ("oilaviy", "OILAVIY"),
)


class Janr(models.Model):
    """Janrlar"""

    name = models.CharField(
        "Nomi", choices=CATEGORY_CHOICES, max_length=100, unique=True
    )
    # slug = models.SlugField(blank=True, max_length=283)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"


class Aktyor(models.Model):
    """Aktyorlar va rejissorlar"""

    ism = models.CharField("Ism", max_length=100)
    yosh = models.PositiveSmallIntegerField("Yoshi", default=0)
    batafsil = models.TextField("Batafsil")
    # image = models.FileField("Rasmi", upload_to="actors/")

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Aktyor yoki rejissor"
        verbose_name_plural = "Aktyorlar va rejissorlar"


class Film(models.Model):
    """Film"""

    nomi = models.CharField("Nomi", max_length=100)
    haqida = models.TextField("Film haqida")
    # rasmi = models.FileField("Rasmi", upload_to="movies/")
    yili = models.PositiveSmallIntegerField("Olingan yili", default=2019)
    mamlakat = models.CharField(max_length=100)
    aktyorlar = models.ManyToManyField(
        Aktyor, verbose_name="aktiyor", related_name="film_actor"
    )
    rejissorlar = models.ManyToManyField(
        Aktyor, verbose_name="rejissor", related_name="film_director"
    )
    genres = models.ManyToManyField(Janr, verbose_name="janrlar")
    # slug = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("sayitga_joylangan", default=False)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.nomi)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Filim"
        verbose_name_plural = "Filimlar"


class Baho(models.Model):
    """Baho"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="film")

    class Meta:
        verbose_name = "Reting"
        verbose_name_plural = "Ratinglar"


class Izoh(models.Model):
    """Izoh"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    matn = models.TextField("Matn", max_length=1000)
    film = models.ForeignKey(Film, verbose_name="film", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izoh"

