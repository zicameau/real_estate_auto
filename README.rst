This project is to help automate the process of identifying, analyzing and determining whether or not to make a purchase on a property or not. By utilizing different API's and different investment methodologies and barometers, the tool will be used to help to determine whether or not a property is a viable investment or not.

Project structure follows the advice as given by the Hitchhiker's Guide to Python which can be found here: https://docs.python-guide.org/writing/structure/

README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py


Phase I: Basics

We need to have all the basic functionalities that anybody needs when evalutating realestate deals. We need to have all of the below functionalities before starting anything else:

- Capitalization Rate Calculator
- Cashflow Calculator (Includes expenses calculation and income)
- Loan Rate Calculator
  Repeating Expenses Need to Calculate:
      1) Property Taxes Per Year
      2) Insurance Per Month
      3) Water Per Month
      4) Sewer Per Month
      5) Garbage Per Month
      6) Lawn and Snow
      7) Management Percentage
      8) Vacancy Percentage
      9) Maintenance Percentage
- Calculate Rental Incomes
    - Calculate the Current Rent per month for each unit
    - Calculate the Current Market Rent per month for each unit
- Calculate Monthly NOI, Annual NOI, and Cap Rate
- 
