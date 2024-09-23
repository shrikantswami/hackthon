from django import forms


class UploadFileForm(forms.Form):
    """
    This is file upload form
    """
    title = forms.CharField(max_length=255)
    file = forms.FileField()
