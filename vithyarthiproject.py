#   SIP  Calculator

def calculate_sip():
    """Calculates the estimated future value of a SIP."""
    
    print("Welcome to the Basic Python SIP Calculator!")
    
    while True:
        try:
            monthly_investment = float(input("Enter the monthly investment amount (in your currency, e.g., 5000): "))
            if monthly_investment <= 0:
                print("Investment must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    while True:
        try:
            annual_rate = float(input("Enter the expected annual return rate (in percentage, e.g., 12 for 12%): "))
            if annual_rate < 0:
                print("Rate cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            
    while True:
        try:
            time_period = int(input("Enter the investment time period (in years, e.g., 10): "))
            if time_period <= 0:
                print("Time period must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    monthly_rate = (annual_rate / 100) / 12
    
    total_months = time_period * 12
    
    future_value = 0.0
    
    for month in range(1, total_months + 1):
        
        remaining_periods = total_months - month + 1
        
        fv_this_month = monthly_investment * (1 + monthly_rate) ** remaining_periods
        
        future_value = future_value + fv_this_month
        
    total_invested = monthly_investment * total_months
    
    estimated_return = future_value - total_invested

    print("\n" + "="*40)
    print(" SIP Calculation Results ")
    print("="*40)
    
    print(f" Monthly Investment: {monthly_investment:,.2f}")
    print(f" Annual Rate: {annual_rate}%")
    print(f" Time Period: {time_period} years ({total_months} months)")
    print("-" * 40)
    print(f" Total Amount Invested (Principal): {total_invested:,.2f}")
    print(f" Estimated Wealth Gained (Interest): {estimated_return:,.2f}")
    print(f" **Estimated Future Value:** {future_value:,.2f}")
    print("="*40)

if __name__ == "__main__":
    calculate_sip()