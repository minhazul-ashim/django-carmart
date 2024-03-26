from django import forms;
from . import models;

class CommentForm(forms.ModelForm) :
    class Meta :
        model = models.CommentModel;
        fields = "__all__"
        widgets = {
            "comment": forms.Textarea(attrs={"row": 3})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Add a ModelChoiceField for the ForeignKey relation
            self.fields['car'] = forms.ModelChoiceField(queryset=models.CarModel.objects.all())