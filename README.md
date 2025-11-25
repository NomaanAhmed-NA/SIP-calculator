# 1. Project Title - 
Basic Python SIP Calculator
# 2. Overview of the Project-
 This project is a straightforward Python command-line interface (CLI) application.  It assists a user in estimating the future maturity value of an investment made through regular, periodic installments by acting as a Systematic Investment Plan (SIP) calculator.  By treating each monthly contribution as a distinct compounded amount until the end of the tenure, the calculator iteratively determines the future value.  It manages user input validation to guarantee that the time period, rate of return, and investment amount entered are all positive numbers.
# 3. Features- 
Three necessary inputs are collected from the user: Monthly Investment Amount, Expected Annual Rate of Return (in percentage), and Investment Time Period (in years).
    Validation of Input: Try-except blocks are used in robust error handling to guarantee that the user enters valid positive numbers (integer for years, floats for money/rate).
    SIP Calculation Logic: This method simulates monthly investments over a given period of time by using an iterative compounding loop to determine an annuity's future value.
    Detailed Output: The computation results, such as the total principal amount invested and the estimated wealth gained (interest), are clearly displayed.
# 4.  Technologies/Tools Used-
Libraries/Modules: No external libraries are needed.  It makes use of built-in Python data types and functions, such as def, print, input, float, int, while True, try/except, and for loop.
     Environment of Development:  The code can be written and executed using a basic text editor or any standard IDE (such as VS Code or PyCharm).
# 5. Steps to Install & Run the Project-
 A. Installation: Make sure your operating system has Python 3 (ideally Python 3.6 or later) installed. It is available for download on the official Python website.
    Keep the code safe: The supplied code should be saved in a file called vithyarthiproject.py.
  B. Launching the Project: Open Terminal Go to the directory in which vithyarthiproject.py was saved.
    Run the File: Use the Python interpreter commands to launch the program.
    Observe Prompts: When the program launches, it will ask you to enter each of the necessary investment details.

# 6. Instructions for Testing -Use the following procedures and test scenarios to evaluate the calculator's accuracy and functionality.    
  A. Functional Testing: Examine how well the program manages erroneous inputs.
      B. Calculation Testing: To confirm the results, use common SIP examples'
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
