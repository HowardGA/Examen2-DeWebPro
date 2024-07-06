from django import forms

CHOICES_LEVEL = (
    ("HIGH", "High"),
    ("MEDIUM", "Medium"),
    ("LOW", "Low"),
)

CHOICES_STATE = (
    ("PENDING", "Pending"),
    ("IN PROGRESS", "In Progress"),
    ("DONE", "Done"),
)

class CreateTaskForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Type the title of your task"})
    )
    description = forms.CharField(
        max_length=600,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Type a description for your task"})
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control", "placeholder": "Select Due Date"})
    )
    priority = forms.ChoiceField(
        choices=CHOICES_LEVEL,
        widget=forms.Select(attrs={"class": "form-select form-control"})
    )
    state = forms.ChoiceField(
        choices=CHOICES_STATE,
        widget=forms.Select(attrs={"class": "form-select form-control"})
    )
    user = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={"class": "form-select form-control"})
    )
    area = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={"class": "form-select form-control"})
    )
    
class AreaForm(forms.Form):
    area_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Area Name"}))
    description = forms.CharField(max_length=128, required=False, widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Area description"}))
