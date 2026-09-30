from django.db import models

class Product(models.Model):
    # Node representation in the network
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    isActive = models.BooleanField(default=True)
    imageUrl = models.URLField(blank=True)

    def __str__(self):
        return self.name

class PurchaseRelationship(models.Model):
    # Edge representation (Undirected Graph)
    source_product = models.ForeignKey(Product, related_name='source_relations', on_delete=models.CASCADE)
    target_product = models.ForeignKey(Product, related_name='target_relations', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=1) 

    class Meta:
        # Prevent identical database rows
        unique_together = ('source_product', 'target_product')

    def __str__(self):
        return f"{self.source_product.name} <-> {self.target_product.name} (Weight: {self.weight})"
    
    def incrementRelationshipWeight(self, amount=1):
        # Increases the strength of the connection
        self.weight += amount
        self.save()
