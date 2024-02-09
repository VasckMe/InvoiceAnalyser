# Invoice Analyser

A useful Python program that will help you calculate the difference between exchange rates, save the results and check the data

# Tasks

- The program provides information whether the invoice has been paid in full, how much is missing or how much is overpaid
- Program allow to configure accessable rates (EUR, USD, GBP, ...) with help of environment property or the parameter
- The program allows you to configure available currencies (EUR, USD, GBP) using an environment variable or call parameter
- The user enters the payment date and amount, which can be in PLN or foreign currency, for the full or partial amount of the invoice
- The program downloads exchange rates with appropriate dates
- The program calculates exchange rate differences between the invoice date and the payment date
- The program saves the entered data and calculation results to a file
- The program verifies the correctness of the entered data and handles errors, e.g. incorrect currency
