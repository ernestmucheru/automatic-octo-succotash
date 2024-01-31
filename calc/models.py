from django.db import models

# Create your models here.
class Commission(models.Model):
    persona_choices = [('manager', 'Manager'), ('sales', 'Sales')]
    sales_group_choices = [('checkout', 'Checkout'), ('payouts', 'Payouts'), ('banking', 'Banking')]

    persona = models.CharField(max_length=10, choices=persona_choices)
    sales_group = models.CharField(max_length=10, choices=sales_group_choices)
    target_profit = models.FloatField()
    gross_profit = models.FloatField()

    def calculate_eligible_gross_profit(self):
        # Manager Commission Scale for checkout/payouts
        manager_threshold = 0.75
        manager_rate = 0.025
        manager_over_100_rate = 0.025
        # Sales/Account Owner Commission Scale for checkout/payouts
        sales_threshold = 0.75
        sales_rate = 0.1
        sales_over_100_rate = 0.15
        # Manager/Sales Owner Commission Scale for Banking
        banking_threshold = 0.9
        banking_rate = 0.1
        banking_over_100_rate = 0.15

    

        # Gross Profit % Calculation
        # Ensure that the target_profit is not zero to avoid division by zero
        gross_profit_percentage = self.gross_profit / self.target_profit  # Calculate gross profit percentage

        if self.persona == 'manager':
            if self.sales_group in ['checkout', 'payouts'] and gross_profit_percentage >= manager_threshold:
                if gross_profit_percentage <= 1.0:
                    return round(((gross_profit_percentage - manager_threshold) * manager_rate)* self.target_profit ,2)
                else:
                    return ((1.0 - manager_threshold) * manager_rate + (gross_profit_percentage - 1.0) * manager_over_100_rate)* self.target_profit
            elif self.sales_group == 'banking' and gross_profit_percentage >= banking_threshold:
                if gross_profit_percentage <= 1.0:
                    return round(((gross_profit_percentage - banking_threshold) * banking_rate)* self.target_profit,2)
                else:
                    return round(((1.0 - banking_threshold) * banking_rate + (gross_profit_percentage - 1.0) * banking_over_100_rate)* self.target_profit,2)
            else:
                return 0
        else:  # persona is 'sales'
            if self.sales_group in ['checkout', 'payouts'] and gross_profit_percentage >= sales_threshold:
                if gross_profit_percentage <= 1.0:
                    return round(((gross_profit_percentage - sales_threshold) * sales_rate)* self.target_profit,2)
                else:
                    return round(((1.0 - sales_threshold) * sales_rate + (gross_profit_percentage - 1.0) * sales_over_100_rate)* self.target_profit,2)
            elif self.sales_group == 'banking' and gross_profit_percentage >= banking_threshold:
                if gross_profit_percentage <= 1.0:
                    return round(((gross_profit_percentage - banking_threshold) * banking_rate)* self.target_profit,2)
                else:
                    return round(((1.0 - banking_threshold) * banking_rate + (gross_profit_percentage - 1.0) * banking_over_100_rate)* self.target_profit,2)
            else:
                return 0