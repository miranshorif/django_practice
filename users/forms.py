from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class meta:
        model = CustomUser
        fields = ('email',)
        
        
        
class CustomUserChangeForm(UserChangeForm):
    
    class meta:
        model = CustomUser
        fields = ('email',)