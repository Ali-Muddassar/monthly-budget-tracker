# Python Expense Tracker

## Description
A Python program that helps users track their monthly income and expenses. The program takes user input for various expense categories, calculates total spending and remaining balance, and provides intelligent feedback on spending habits. Created as part of my learning journey with **@Codanics**.

## Features
- Input monthly income
- Track expenses across multiple categories:
  - Rent
  - Food
  - Transportation
  - Entertainment
- Calculate total expenses automatically
- Display remaining balance
- Smart budget analysis:
  - Warns if total expenses exceed income
  - Alerts if savings are below 20% of income
  - Flags any category exceeding 30% of income as "too high"

## How to Run
1. Ensure Python 3 is installed on your system
2. Clone or download this repository
3. Open terminal/command prompt in the project folder
4. Run the script:
5. 5. Enter values when prompted

## Example Output
enter the monthly salary 50000
enter the monthly rent 15000
enter the monthly food expens 10000
enter the transporation 5000
enter the monthly expenses of enterainment 3000
Total Expenses: 33000
Remaining: 17000

monthly income 50000
expenses: rent 15000, entertainment 3000, food 10000, transporation 5000
remaining 17000

Good job, you're within budget
Try to save more!
Rent is reasonable
food is reasonable
transport is reasonable
entertainment is reasonable

## Budget Rules Applied
| Rule | Threshold | Message |
| :--- | :--- | :--- |
| Overspending Check | Expenses > Income | "You're overspending!" |
| Savings Check | Savings < 20% of Income | "Try to save more!" |
| Category Analysis | Any category > 30% of Income | "[Category] is too high" |

## Technologies Used
- Python 3
- Basic input/output operations
- Conditional statements (`if-elif-else`)
- Arithmetic operations
- F-strings for formatted output

## What I Learned
- Taking and converting user input with `int(input())`
- Performing calculations with multiple variables
- Using conditional logic for budget analysis
- Formatting output with f-strings
- Building a practical, real-world application
- Implementing multiple validation rules

## Potential Enhancements
- Store expenses in a file for historical tracking
- Add more expense categories
- Create visual charts of spending
- Build a GUI version with Tkinter
- Add monthly comparison feature

## About Me
**Ali Muddassar**
- [GitHub](https://github.com/Ali-Muddassar)
- [LinkedIn](https://www.linkedin.com/in/ali-muddassar-17466a3b7)


