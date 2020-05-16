


class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["name", "filepath"]
