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
        modes = [k for k, v in mode_dict.items() if v == max_freq]
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
        freq_list = []
        

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

    def total_income(self):
        pass
    def total_expense(self):
        pass
    def account_info(self):
        pass
    def add_income(self):
        pass
    def add_expense(self):
        pass
    def account_balance(self):
        pass



    if __name__ == "__main__":
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