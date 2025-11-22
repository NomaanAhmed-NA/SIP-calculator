1. Problem Statement-
   The core problem this project addresses is the need for a simple, accessible tool to help users estimate the financial outcome of their regular, periodic investments (Systematic Investment Plans or SIPs).
   Financial planning requires knowing the potential return on investment. The program solves this by accurately applying the time-value-of-money principle (future value of an annuity, compounded monthly) to
   user-defined investment parameters, providing a crucial projection for financial goal setting and decision-making.

2. Scope of the Project-
  Accepting the three required numerical inputs: monthly investment, annual return rate, and time in years.
  Robust input validation for positive numbers and correct data types (float for money/rate, int for years).
  Calculating the final maturity value using an iterative compounding loop, which models the impact of compounding interest on each monthly installment.

3. Target Users-
  Financial Beginners: Those who are new to investing and need a straightforward tool to understand the power of compounding.
  Small Investors: Individuals planning or currently executing a SIP in mutual funds, stocks, or other financial instruments.
  Students/Learners: Those studying financial concepts or programming (Python) who need a simple, practical application to demonstrate core calculation principles.
  DIY Financial Planners: Users who prefer quick, on-demand calculations without using complex or feature-heavy web applications.
4. High-Level Features-
Interactive Input Handling: Uses input() within while loops and try/except blocks to ensure the collection of valid, positive, numerical data for investment parameters.
Monthly Compounding Logic: Implements the core financial formula by simulating monthly compounding over the entire tenure using an explicit for loop, treating each month's contribution as a principal that
accrues interest.
Comprehensive Output Generation: Calculates and presents three key financial metrics: Total Invested Principal,,Estimated Interest (Wealth Gained),Estimated Future Value (Maturity Amount).
