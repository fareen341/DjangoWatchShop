from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'myclass'}), 'password':
        forms.PasswordInput(attrs={'class':'myclass'})}

        def save(self, commit=True):
            password = self.cleaned_data.get('password')
            user = super().save(commit=commit)
            if password:
                user.reset_password(password)
            else:
                pass
            return user

# class UserProfileForm(models.Model):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

class UserProfileForm(forms.ModelForm):
    # role1=[('customer','customer'),('admin','admin')]
    # role=forms.ChoiceField(widget=forms.RadioSelect(),choices=role1)
    class Meta:
        model = UserProfile
        fields=['location','contact']
