from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, PurchaseRelationship
from .serializers import ProductSerializer, PurchaseRelationshipSerializer
from .services import NetworkManagerService
from django.core.exceptions import ValidationError

class ProductViewSet(viewsets.ModelViewSet):
    # Standard CRUD for nodes
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RelationshipViewSet(viewsets.ModelViewSet):
    # Standard CRUD for edges
    queryset = PurchaseRelationship.objects.all()
    serializer_class = PurchaseRelationshipSerializer
    
    def create(self, request, *args, **kwargs):
        # Override creation to use our custom graph rules
        productA = request.data.get('source_product')
        productB = request.data.get('target_product')
        weight = request.data.get('weight', 1)
        
        try:
            newRelation = NetworkManagerService.createCoPurchaseRelationship(productA, productB, weight)
            responseSerializer = self.get_serializer(newRelation)
            return Response(responseSerializer.data, status=status.HTTP_201_CREATED)
            
        except ValidationError as validationError:
            return Response({"error": str(validationError)}, status=status.HTTP_400_BAD_REQUEST)
        
    