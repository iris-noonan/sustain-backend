from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True) # not required
    photo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add will update the first time the record is created
    updated_at = models.DateTimeField(auto_now=True) # auto_now will update every time we update the record
    owner = models.ForeignKey(
        to='users.User', # the table the relationship is with - syntax: appname.ModelName
        related_name='owned_products', # the name for this relationship on the foreign object
        on_delete=models.CASCADE # This selection will ensure this propert is deleted if the owner is deleted, therefore not leaving orphans
    )
    # seasonality = models.ManyToManyField(
    #     to='seasonality.Season',
    #     related_name='products',
    #     blank=True # Allows us to not specify this field on creation of a Product
    # )
    # badges = models.ManyToManyField(
    #     to='badges.Badge',
    #     related_name='products',
    #     blank=True # Allows us to not specify this field on creation of a Product
    # )
    # categories = models.ManyToManyField(
    #     to='categories.Category',
    #     related_name='products',
    #     blank=True # Allows us to not specify this field on creation of a Product
    # )

    def __str__(self):
        return self.name