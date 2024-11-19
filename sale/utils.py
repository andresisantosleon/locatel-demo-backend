from django.db import transaction

from sale.models import Sale, SaleProduct
from decimal import Decimal

def create_sale_products(products, sale):
    subtotal = Decimal('0')
    iva = Decimal('0')

    for product_dict in products:
        product = product_dict["product"]
        iva_product = product.iva

        quantity = product_dict["quantity"]

        total_product = Decimal(str(product.price)) * Decimal(str(quantity))
        subtotal += total_product

        if iva_product:
            iva += total_product * (Decimal(str(iva_product)) / Decimal('100'))

        SaleProduct.objects.create(
            sale=sale,
            product=product,
            quantity=quantity,
            code=product.code,
            name=product.name,
            price=product.price,
            iva=product.iva,
        )

    subtotal = round(subtotal, 2)
    iva = round(iva, 2)

    return float(subtotal), float(iva)


@transaction.atomic
def create_sale(data):
    sale = Sale.objects.create(
        consecutive=data["consecutive"],
        date=data["date"],
        customer=data["customer"],
        subtotal=0,
        iva=0,
    )

    subtotal, iva = create_sale_products(data["products"], sale)

    sale.subtotal = subtotal
    sale.iva = iva

    sale.save(update_fields=("subtotal", "iva"))

    return sale
