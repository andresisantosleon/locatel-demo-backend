from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    code = models.CharField(max_length=128, verbose_name='codigo',unique=True)
    
    name = models.CharField(max_length=128, verbose_name='nombre')
    
    price = models.FloatField(verbose_name='precio', validators=[MinValueValidator(0)])
    
    iva = models.FloatField(verbose_name='porcentaje IVA',default=0,blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])

    has_iva= models.BooleanField(verbose_name='tiene IVA')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

class Sale(models.Model):
    consecutive = models.CharField(max_length=128, verbose_name='consecutivo',unique=True)

    date= models.DateField(verbose_name='fecha')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha y hora de creación')
    
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT, verbose_name='cliente')

    subtotal = models.FloatField(verbose_name='subtotal', validators=[MinValueValidator(0)])

    iva= models.FloatField(verbose_name='iva', validators=[MinValueValidator(0)])

    class Meta:
        ordering = ('-id',)
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'

class SaleProduct(models.Model):
    sale= models.ForeignKey('sale.Sale', on_delete=models.CASCADE, verbose_name='venta')

    product= models.ForeignKey('sale.Product', on_delete=models.SET_NULL, null=True, verbose_name='producto')

    quantity= models.PositiveIntegerField(verbose_name='cantidad', validators=[MinValueValidator(1)])
    
    code = models.CharField(max_length=128, verbose_name='codigo')
    
    name = models.CharField(max_length=128, verbose_name='nombre')
    
    price = models.FloatField(verbose_name='precio', validators=[MinValueValidator(0)])
    
    iva = models.FloatField(verbose_name='porcentaje IVA',default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-id',)
        verbose_name = 'producto vendido'
        verbose_name_plural = 'productos vendidos'