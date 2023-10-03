from django import forms
from .models import Robot


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def get_serial(self):
        return f'{self.cleaned_data["model"].upper()}-{self.cleaned_data["version"].upper()}'
