from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper



class NewUserForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create User"))

    # @database_sync_to_async
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        # Normalize email using the custom user model
        User = get_user_model()
        email = User.objects.normalize_email(email)

        cleaned_data["email"] = email

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    class Meta:
        model = get_user_model()  # Set the model to your custom user model
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Login"))
