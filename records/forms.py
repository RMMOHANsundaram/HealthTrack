from django import forms
from .models import HealthRecord, Prescription


class HealthRecordForm(forms.ModelForm):

    class Meta:
        model = HealthRecord

        fields = [
            'student',
            'appointment',
            'diagnosis',
            'symptoms',
            'treatment',
            'notes'
        ]

        widgets = {
            'diagnosis': forms.Textarea(
                attrs={'rows': 3}
            ),

            'symptoms': forms.Textarea(
                attrs={'rows': 3}
            ),

            'treatment': forms.Textarea(
                attrs={'rows': 3}
            ),

            'notes': forms.Textarea(
                attrs={'rows': 3}
            ),
        }


class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription

        fields = [
            'medicine_name',
            'dosage',
            'duration',
            'instructions'
        ]

        widgets = {
            'instructions': forms.Textarea(
                attrs={'rows': 3}
            ),
        }