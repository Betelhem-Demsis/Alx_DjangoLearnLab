from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, help_text="Enter the title of the book.")
    author = forms.CharField(max_length=100, help_text="Enter the author of the book.")
    description = forms.CharField(widget=forms.Textarea, help_text="Enter a brief description of the book.")
    published_date = forms.DateField(help_text="Enter the published date (YYYY-MM-DD).")
