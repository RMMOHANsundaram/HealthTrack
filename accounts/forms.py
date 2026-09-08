from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    phone = forms.CharField(
        max_length=15,
        required=False
    )

    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        password = self.cleaned_data['password']

        user.set_password(password)

        if commit:
            user.save()

            UserProfile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                role=self.cleaned_data['role']
            )

        return user