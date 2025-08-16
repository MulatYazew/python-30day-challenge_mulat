class Statistics:
    def __init__(self, list_variable:list):
        self.list_variable = list_variable
    
    def count(self):
        return len(self.list_variable)
    
    def sum_number(self):
        for i in range(len(self.list_variable)):
            total += self.list_variable[i]
        return total
    
    def maximum(self):
        high_value = None
        for i in range(len(self.list_variable)):
            if high_value <= self.list_variable[i]:
                high_value = self.list_variable[i]
            else:
                continue
        return high_value
    
    def minimum(self):
        low_value = None
        for i in range(len(self.list_variable)):
            if low_value >= self.list_variable[i]:
                low_value = self.list_variable[i]
            else: continue
        return low_value
    def mean(self):
        total_sum = self.sum_number()
        number_counts = self.count()
        return total_sum/number_counts
    
    def median(self):
        new_list = self.list_variable.sort()
        if len(new_list) % 2 == 0:
            middle = (new_list[len(new_list)//2] + new_list[(len(new_list)//2) + 1])/2
        else:
            middle = new_list[len(new_list)//2]
        return middle
    def mode(self):
        pass
    def range(self):
        pass
    def variance(self):
        pass
    def st_deviation(self):
        pass


