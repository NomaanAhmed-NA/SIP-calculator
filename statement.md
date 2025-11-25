# 1. Problem Statement-
   The need for an easy-to-use tool to assist users in estimating the financial results of their regular, periodic investments (also known as Systematic Investment Plans, or SIPs) is the main issue this project attempts to solve.
    Understanding the possible return on investment is necessary for financial planning.  The program provides an essential forecast for financial goal-setting and decision-making by precisely applying the time-value-of-money principle (future value of an annuity, compounded monthly) to user-defined investment parameters.
# 2. Scope of the Project-
  accepting the monthly investment, annual return rate, and time in years as the three necessary numerical inputs.
   Strong input validation for positive numbers and appropriate data types (int for years, float for money/rate).
   An iterative compounding loop that simulates the effect of compound interest on each monthly installment is used to calculate the final maturity value.

# 3. Target Users-
 Financial Novices: Individuals who are new to investing and require a simple tool to comprehend compounding's power.
   Small Investors: People who are preparing or carrying out a SIP in stocks, mutual funds, or other financial products.
   Students/Learners: Students studying Python programming or financial concepts who require a straightforward, useful application to illustrate fundamental computation concepts.
   DIY Financial Planners: People who don't want to use complicated or feature-rich web applications in favour of fast, on-demand computations.
# 4. High-Level Features-
Interactive Input Handling: To guarantee the gathering of accurate, positive, numerical data for investment parameters, input() is used within while loops and try/except blocks.
 Monthly Compounding Logic: Treats each month's contribution as a principal that accrues interest, simulating monthly compounding over the whole tenure using an explicit for loop.
 Three important financial metrics are calculated and presented by Comprehensive Output Generation: Total Invested Principal, Estimated Interest (Wealth Gained), and Estimated Future Value (Maturity Amount).
