from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField("Название", max_length=255)
    image = FilerImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="slider_images",
    )
    is_active = models.BooleanField("Активно", default=True)
    order = models.PositiveIntegerField("Порядок", default=0, db_index=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "элемент слайдера"
        verbose_name_plural = "элементы слайдера"
        ordering = ["order", "-created_at"]

    def __str__(self) -> str:
        return self.title

from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Название"),
    )
    image = FilerImageField(
        verbose_name=_("Изображение"),
        related_name="slider_items",
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Показывать на сайте"),
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Порядок"),
        help_text=_("Используется для сортировки слайдов drag&drop в админке."),
    )

    class Meta:
        verbose_name = _("элемент слайдера")
        verbose_name_plural = _("элементы слайдера")
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title

