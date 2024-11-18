from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.core.validators import MinLengthValidator

from user.data import DOCUMENT_TYPE_CHOICES

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = (
        'first_name',
        'last_name',
    )

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )    

    email = models.EmailField(
        unique=True,
        verbose_name='correo electrónico',
    )

    first_name = models.CharField(
        max_length=128,
        verbose_name='nombre(s)',
        validators=[MinLengthValidator(3, message='Debe tener por lo menos 3 caracteres')],
    )

    last_name = models.CharField(
        max_length=128,
        verbose_name='apellido(s)',
        validators=[MinLengthValidator(3, message='Debe tener por lo menos 3 caracteres')],
    )

    document_type = models.CharField(
        choices=DOCUMENT_TYPE_CHOICES,
        max_length=5,
        verbose_name='tipo de documento',
        blank=True,
    )

    document_number = models.CharField(
        max_length=12,
        verbose_name='número documento',
        blank=True,
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='staff',
        help_text='Indica si puede entrar al sitio de administración.',
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name='activo',
        help_text='Indica si el usuario puede ingresar a la plataforma.',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de registro',
    ) 
   
    class Meta:
        ordering = ('-id',)
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

