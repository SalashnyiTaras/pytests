from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """
    title = models.CharField(
        verbose_name=("title"),
        help_text=("Required"),
        max_length=255,
    )
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    description = models.TextField(verbose_name=("description"), help_text=("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=("Regular price"),
        help_text=("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=("Discount price"),
        help_text=("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=("Product visibility"),
        help_text=("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    def __str__(self):
        return self.title
