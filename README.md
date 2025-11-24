# 1. Project Title - 
Basic Python SIP Calculator
# 2. Overview of the Project-
  This project is a simple, command-line interface (CLI) application developed in Python. It functions as a Systematic Investment Plan (SIP) calculator, helping a user estimate the future   maturity value of an       investment made through regular, periodic installments. The calculator iteratively computes the future value by treating each monthly contribution as a separate compounded amount until the end of the tenure. It     handles user input validation to ensure the provided investment amount, rate of return, and time period are positive numerical values.
# 3. Features- 
.    User Input Collection: Accepts three required inputs from the user: Monthly Investment Amount,Expected Annual Rate of Return (in percentage),Investment Time Period (in years).
    Input Validation: Robust error handling using try-except blocks to ensure the user provides valid positive numerical input (floats for money/rate, integer for years).
    SIP Calculation Logic: Uses an iterative compounding loop to calculate the future value of an annuity, simulating monthly investments over the specified tenure.
    Detailed Output: Clearly displays the calculation results, including:Total Principal Amount Invested,Estimated Wealth Gained (Interest).
# 4.  Technologies/Tools Used-
.    Libraries/Modules: No external libraries are required. It uses built-in Python functions and data types (e.g., def, print, input, float, int, while True, try/except, for loop).
    Development Environment: Any standard IDE (like VS Code, PyCharm) or a simple text editor can be used to write and run the code.
# 5. Steps to Install & Run the Project-
  A. Installation -
    Install Python: Ensure you have Python 3 (preferably Python 3.6 or newer) installed on your operating system. You can download it from the official Python website.
    Save the Code: Save the provided code into a file named vithyarthiproject.py.
  B. Running the Project-
    Open Terminal: Navigate to the directory where you saved vithyarthiproject.py.
    Execute the File: Run the program using the Python interpreter commands.
    Follow Prompts: The program will launch and prompt you to enter the required investment details one by one.
# 6. Instructions for Testing - To test the functionality and accuracy of the calculator, use the following steps and test cases:
.    A. Functional Testing -Test the program's ability to handle incorrect inputs.
     B. Calculation Testing -Use standard SIP examples to verify the output.
     eg-INPUT -
               Enter the monthly investment amount: 5000
               Enter the expected annual return rate: 12
               Enter the investment time period: 5
       OUTPUT-
               Monthly Investment: 5,000.00
               Annual Rate: 12.0%
               Time Period: 5 years (60 months)
               Total Amount Invested: 300,000.00
               Estimated Wealth Gained: 112,431.83
               Estimated Future Value: 412,431.83
