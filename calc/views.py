# commission_calculator/views.py
from django.shortcuts import render
from .forms import CommissionForm
from .models import *

def commission_calculator(request):
    eligible_gross_profit = None  # Initialize to None initially

    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission = form.save(commit=False)
            eligible_gross_profit = commission.calculate_eligible_gross_profit()
    else:
        form = CommissionForm()

    commission_instance = Commission()

    return render(request, 'commission_calculator/form.html', {'form': form, 'eligible_gross_profit': eligible_gross_profit, 'commission_instance': commission_instance})