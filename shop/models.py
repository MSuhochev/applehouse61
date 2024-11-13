from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from shop.utils import *


class Category(MPTTModel):
    """Модель категория товара"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey('self', related_name="children", on_delete=models.SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)


class Color(models.Model):
    """Модель для хранения цветов товара"""
    name = models.CharField(max_length=50, verbose_name="Цвет")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Product(models.Model):
    """Модель основного товара"""
    name = models.CharField(max_length=255, verbose_name="Название товара")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категория"
    )
    colors = models.ManyToManyField(Color, blank=True, related_name="products", verbose_name="Цвета")
    description = models.TextField(blank=True, verbose_name="Описание")
    configurations = models.ManyToManyField("Configuration", blank=True,
                                            related_name="products", verbose_name="Конфигурации")
    features = models.ManyToManyField("Feature", blank=True,
                                      related_name="products_with_feature", verbose_name="Особенности")
    package_contents = models.ManyToManyField("PackageContent", blank=True,
                                              related_name="products_with_package_content", verbose_name="Комплектация")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Configuration(models.Model):
    """Модель для конфигураций товара (разные варианты с разными ценами)"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="available_configurations", verbose_name="Товар")
    ram = models.CharField(max_length=50, blank=True, null=True, verbose_name="Оперативная память")
    cpu = models.CharField(max_length=50, blank=True, null=True, verbose_name="Процессор")
    cores = models.IntegerField(blank=True, null=True, verbose_name="Количество ядер")
    release_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Год выпуска")
    storage_type = models.CharField(max_length=50, blank=True, null=True, verbose_name="Тип жесткого диска")
    storage_size = models.CharField(max_length=50, blank=True, null=True, verbose_name="Объем жесткого диска")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Цена")
    is_price_on_request = models.BooleanField(default=False, verbose_name="Цена по запросу")

    def __str__(self):
        return f"{self.product.name} ({self.ram or ''} {self.cpu or ''})"

    class Meta:
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурации"


class Feature(models.Model):
    """Модель для описания особенностей товара (может включать фото и описание)"""
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_features',
                                verbose_name='Товар')
    name = models.CharField(max_length=100, verbose_name="Название особенности")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to=feature_image_upload_path, blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Особенность"
        verbose_name_plural = "Особенности"


class PackageContent(models.Model):
    """Модель для описания содержимого коробки (комплектации)"""
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_package_contents',
                                verbose_name='Товар')
    name = models.CharField(max_length=100, verbose_name="Название комплектации")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to=package_content_image_upload_path, blank=True, null=True,
                              verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комплектация"
        verbose_name_plural = "Комплектации"


class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Товар'
    )
    image = models.ImageField(upload_to=product_image_upload_path, verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Основное изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"Изображение {self.id} для {self.product.name}"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
