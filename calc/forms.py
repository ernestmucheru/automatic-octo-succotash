# commission_calculator/forms.py
from django import forms
from .models import Commission

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['persona', 'sales_group', 'gross_profit', 'target_profit']
