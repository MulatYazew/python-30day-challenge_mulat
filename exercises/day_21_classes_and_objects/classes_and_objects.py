# Exercises: Level 1
"""
Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, 
which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability 
(range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, 
and frequency distribution of the sample. You can create a class called Statistics and create all the functions 
that do statistical calculations as methods for the Statistics class. Check the output below.
"""

class Statistics:
    def __init__(self, list_variable:list):
        self.list_variable = list_variable
    
    def count(self):
        return len(self.list_variable)
    
    def sum_number(self):
        total = 0
        for i in range(len(self.list_variable)):
            total += self.list_variable[i]
        return total
    
    def maximum(self):
        high_value = None
        for i in range(len(self.list_variable)):
            if high_value == None or high_value<= self.list_variable[i]:
                high_value = self.list_variable[i]
            else:
                continue
        return high_value
    
    def minimum(self):
        low_value = None
        for i in range(len(self.list_variable)):
            if low_value == None or low_value >= self.list_variable[i]:
                low_value = self.list_variable[i]
            else: continue
        return low_value
    def mean(self):
        total_sum = self.sum_number()
        number_counts = self.count()
        return total_sum/number_counts
    
    def median(self):
        sorted_list = sorted(self.list_variable)
        n = len(sorted_list)
        if n % 2 == 0:
            middle = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            middle = sorted_list[n // 2]
        return middle
    def mode(self):
        sorted_list = sorted(self.list_variable)
        mode_dict = {}
        for i in sorted_list:
            mode_dict[i] = mode_dict.get(i, 0) + 1
        max_freq = max(mode_dict.values())
        modes = [(k, v) for k, v in mode_dict.items() if v == max_freq]
        return modes
    def range(self):
        highest = max(self.list_variable)
        lowest = min(self.list_variable)
        return highest-lowest
    def variance(self):
        sorted_list = sorted(self.list_variable)
        sum_nums = self.mean()
        variance_nums = sum((i-sum_nums)**2 for i in sorted_list)/len(sorted_list)
        return variance_nums
    def st_deviation(self):
        return self.variance()**0.5
    def frequency_distribution(self):
        sorted_list = sorted(self.list_variable)
        frequency_dict = {}
        freq_list = []
        for num in sorted_list:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        for key, value in frequency_dict.items():
            freq_list.append(((value*100)/len(sorted_list), key))
        return freq_list

# Exercises: Level 2
"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has 
total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.
"""


class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)
    
    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        print(f"Account Holder: {self.firstname} {self.lastname}")
        print("Incomes:")
        for amount, desc in self.incomes:
            print(f"  + {amount} ({desc})")
        print("Expenses:")
        for amount, desc in self.expenses:
            print(f"  - {amount} ({desc})")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expense: {self.total_expense()}")
        print(f"Account Balance: {self.account_balance()}")



if __name__ == "__main__":

    # Statistics
    stats = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
    print("Count:", stats.count())
    print("Sum:", stats.sum_number())
    print("Max:", stats.maximum())
    print("Min:", stats.minimum())
    print("Mean:", stats.mean())
    print("Median:", stats.median())
    print("Mode:", stats.mode())
    print("Range:", stats.range())
    print("Variance:", stats.variance())
    print("Standard Deviation:", stats.st_deviation())
    print("Frequency Distribution:", stats.frequency_distribution())

    #Person Account
    person_account = PersonAccount("John", "Doe", [], [])
    person_account.add_income(5000, "Salary")
    person_account.add_income(10000, "Shopping")
    person_account.add_expense(1500, "Rent")
    person_account.add_expense(200, "Utilities")
    person_account.account_info()
    