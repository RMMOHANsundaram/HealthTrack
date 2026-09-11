from django import forms
from django.contrib.auth.models import User
# pyrefly: ignore [missing-import]
from .models import UserProfile
from appointments.models import Doctor


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    phone = forms.CharField(
        max_length=15,
        required=False
    )

    role = forms.ChoiceField(
        choices=[
            ('student', 'Student'),
            ('doctor', 'Doctor'),
        ]
    )

    specialization = forms.CharField(
        max_length=100,
        required=False,
        help_text="Required if you are registering as a Doctor"
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

            role = self.cleaned_data['role']

            UserProfile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                role=role
            )

            if role == 'doctor':
                Doctor.objects.create(
                    user=user,
                    specialization=self.cleaned_data.get('specialization', 'General')
                )

        return user