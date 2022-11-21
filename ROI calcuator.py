class ROI:
    def __init__(self, name, income, expense, annual_cashflow):
        self.name = name
        self.income = income
        self.expense = expense
        self.annual_cashflow = annual_cashflow

    def gross_income(self):
        salary = input('What is your monthly gross income amount: $')
        other = input('Is there any other income you would like to include? If yes how much? If no please input 0: $')
        salary_int = int(salary)
        other_int = int(other)
        total_income = salary_int + other_int
        self.income = total_income
        print(f'The amount of your gross income is equivilent to: ${total_income}')
        print(f'The following amount has been saved: ${self.income} ')

    def expenses(self):
        expense = input('What is your monthly expenss?: $')
        expense_int = int(expense)
        self.expense = expense_int
        print(f'Your total expenses come out to: ${expense_int}')
    
    def net_income(self):
        print(f'Your monthly gross income is equivalent to ${self.income}.')
        print(f'Your monthly expenses is equivalent to ${self.expense}')
        monthly_cash_flow = self.income - self.expense
        self.annual_cashflow = monthly_cash_flow * 12
        print(f'Your total monthly cash flow is equivalent to: ${monthly_cash_flow}')
        print(f'Your annual cash flow is equivalent to: ${self.annual_cashflow} ')
    
    def return_on_investment(self):
        down_payment = input('How much do you spend a on a downpayment?: $')
        closing_costs = input('What were the closing costs?: $')
        refurbishment_budget = input('Did you spend any money on refurbishments for the property? If you have none please enter 0: $')
        misc = input('Please enter any other misc expenses. If you have none please enter 0: $')
        down_payment_int  = int(down_payment)
        closing_costs_int = int(closing_costs)
        refurbishment_budget_int = int(refurbishment_budget)
        misc_int = int(misc)
        total_investment = down_payment_int + closing_costs_int + refurbishment_budget_int + misc_int
        Return_on_investment = self.annual_cashflow / total_investment
        Return_on_investment_percentage = Return_on_investment * 100
        print(f'Your Return on Investment: {Return_on_investment_percentage}%')






User = ROI('Jake','tbd', 'tbd', 'tbd')

User.gross_income()
User.expenses()
User.net_income()
User.return_on_investment()

