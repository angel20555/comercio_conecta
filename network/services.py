from django.core.exceptions import ValidationError
from .models import Product, PurchaseRelationship

class NetworkManagerService:
    """
    Handles business logic for the commercial graph.
    Ensures undirected graph rules.
    """

    @staticmethod
    def createCoPurchaseRelationship(productIdA, productIdB, initialWeight=1):
        # Rule: Product cannot be related to itself
        if productIdA == productIdB:
            raise ValidationError("A product cannot be related to itself.")

        # Rule: Reject invalid weights
        if initialWeight < 1:
            raise ValidationError("Relationship weight must be positive.")

        # Enforce undirected graph (Always store smaller ID as source)
        sourceId, targetId = sorted([productIdA, productIdB])

        # Verify existence implicitly (will fail if IDs don't exist)
        try:
            relationship, created = PurchaseRelationship.objects.get_or_create(
                source_product_id=sourceId,
                target_product_id=targetId,
                defaults={'weight': initialWeight}
            )

            # If it already exists, just strengthen the bond
            if not created:
                relationship.incrementRelationshipWeight(initialWeight)

            return relationship

        except Exception as error:
            raise ValidationError(f"Invalid products provided: {str(error)}")