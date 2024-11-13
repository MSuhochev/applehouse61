import os
from django.utils.text import slugify


def product_image_upload_path(instance, filename):
    """Функция для сохранения изображений товара в папку с наименованием товара"""
    # Используем slugify для создания корректного пути на основе названия продукта
    product_name_slug = slugify(instance.product.name)
    # Сохраняем в папку media/products_images/<product_name_slug>/
    return os.path.join('media/products_images', product_name_slug, filename)


def feature_image_upload_path(instance, filename):
    """Функция для сохранения изображений особенностей товара в папку с наименованием товара"""
    product_name_slug = slugify(instance.product.name)  # Предполагаем, что Feature связана с Product
    return os.path.join('media/products_images', product_name_slug, 'features', filename)


def package_content_image_upload_path(instance, filename):
    """Функция для сохранения изображений содержимого коробки в папку с наименованием товара"""
    product_name_slug = slugify(instance.product.name)  # Предполагаем, что PackageContent связана с Product
    return os.path.join('media/products_images', product_name_slug, 'package_contents', filename)