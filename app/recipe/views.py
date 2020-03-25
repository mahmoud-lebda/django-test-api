from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipe.serializers import TagSerializer, IngredientSerializer


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin
                 ):
    """manage tag in the database"""

    # check that the user is authenticated to use the API
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # when define a list model mixin in the generic view set
    # need to add queryset
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create new tag"""
        serializer.save(user=self.request.user)


class IngredientViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    """manage Ingredient in database"""

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        """return objects for the current user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create new ingredient"""
        serializer.save(user=self.request.user)
