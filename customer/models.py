from django.db import models
from django.core.validators import MinLengthValidator

from user.data import DOCUMENT_TYPE_CHOICES


class Customer(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name="correo electrónico",
    )

    first_name = models.CharField(
        max_length=128,
        verbose_name="nombre(s)",
        validators=[
            MinLengthValidator(3, message="Debe tener por lo menos 3 caracteres")
        ],
    )

    last_name = models.CharField(
        max_length=128,
        verbose_name="apellido(s)",
        validators=[
            MinLengthValidator(3, message="Debe tener por lo menos 3 caracteres")
        ],
    )

    document_type = models.CharField(
        choices=DOCUMENT_TYPE_CHOICES,
        max_length=5,
        verbose_name="tipo de documento",
        blank=True,
    )

    document_number = models.CharField(
        max_length=12,
        verbose_name="número documento",
        blank=True,
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
