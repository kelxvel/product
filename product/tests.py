from django.test import TestCase
from product.models import Category, Product

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name = "Test Category", description = "")
 
    def test_category_slug(self):
        category = Category.objects.get(name = "Test Category")
        self.assertEqual(category.slug, "test-category")


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name = "Test Product", description = "", price = 451.3, 
                               category = Category.objects.create(name = "Test Category", description = ""))

    def test_product_price(self):
        product = Product.objects.get(name = "Test Product")
        self.assertEqual(product.price, 451.3)
