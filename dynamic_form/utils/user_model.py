from django.contrib.auth import get_user_model

# Cache the user model and username field
UserModel = get_user_model()
USERNAME_FIELD = UserModel.USERNAME_FIELD
REQUIRED_FIELDS = UserModel.REQUIRED_FIELDS
