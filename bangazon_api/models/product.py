from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from bangazon_api.models.rating import Rating


class Product(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(
        "Store", on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(validators=[
        MinValueValidator(0.00), MaxValueValidator(180000.00)])
    description = models.TextField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='products', height_field=None,
                                   width_field=None, max_length=None, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name='products')

    def save(self, *args, **kwargs):
        self.clean_fields()
        super().save(*args, **kwargs)

    @property
    def average_rating(self):
        """Average rating calculated attribute for each product
        Returns:
            number -- The average rating for the product
        """
        ratings = Rating.objects.filter(product_id=self.id)
        # TODO: Fix Divide by zero error
        # The below code returns a divide by zero error uncomment and fix

        total_rating = 0
        if ratings:
            for rating in ratings:
                total_rating += rating.score
            avg = total_rating / len(ratings)
        return avg

    def __str__(self):
        return self.name
