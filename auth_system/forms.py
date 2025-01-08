from django.contrib.auth.forms import UserCreationForm
from auth_system.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        field = UserCreationForm.Meta.fields + ("phone_number", "first_name", "last_name",)
        
