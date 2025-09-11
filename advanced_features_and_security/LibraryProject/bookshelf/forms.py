# bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    q = forms.CharField(
        label="Search",
        required=False,
        max_length=200,
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "title or author"})
    )

    # Example of further validation: disallow suspicious characters if you want
    def clean_q(self):
        data = self.cleaned_data.get("q", "")
        # Optionally sanitize or reject certain input patterns. Keep it permissive but safe.
        # e.g., disallow control characters
        if any(ord(ch) < 32 for ch in data):
            raise forms.ValidationError("Invalid characters in search.")
        return data
