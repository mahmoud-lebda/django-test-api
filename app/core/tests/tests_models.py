from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase
from core.models import Tag, Ingredient, Recipe,\
    recipe_image_file_path


def sample_user(
        email='test@test.com', password='Test@123'
):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating user with email"""
        email = 'test@gangawy.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizes(self):
        email = 'test@GANGAWY.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error"""
        # any thing run here and don't raise error this test is fail
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test@123')

    def test_create_new_super_user(self):
        """ test creating new super user """
        user = get_user_model().objects.create_superuser(
            'm@ml.com',
            'Test@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test the tag string representation"""
        tag = Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """test the ingredient string representation """
        ingredient = Ingredient.objects.create(
            user=sample_user(),
            name='test'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """test the recipe strings representation"""
        recipe = Recipe.objects.create(
            user=sample_user(),
            title='recipe1',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        filepath = recipe_image_file_path(None, 'mahmoud.jpg')
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(exp_path, filepath)
