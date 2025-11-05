#1
class Statistics:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list cannot be empty")
        self.data = sorted(data)


    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

    def mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]
        if len(modes) == len(freq):
            return None  
        return modes

  
    def data_range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean_val = self.mean()
        return sum((x - mean_val) ** 2 for x in self.data) / (len(self.data) - 1)

    def std_dev(self):
        return self.variance() ** 0.5

   
    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

    def count(self):
        return len(self.data)

    def percentile(self, p):
        """p: percentile between 0 and 100"""
        if not 0 <= p <= 100:
            raise ValueError("Percentile must be between 0 and 100")
        k = (len(self.data) - 1) * (p / 100)
        f = int(k)
        c = min(f + 1, len(self.data) - 1)
        return self.data[f] + (self.data[c] - self.data[f]) * (k - f)

    def frequency_distribution(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        return dict(sorted(freq.items()))


    def summary(self):
        return {
            "count": self.count(),
            "min": self.minimum(),
            "max": self.maximum(),
            "mean": round(self.mean(), 2),
            "median": self.median(),
            "mode": self.mode(),
            "range": self.data_range(),
            "variance": round(self.variance(), 2),
            "std_dev": round(self.std_dev(), 2),
            "25th percentile": round(self.percentile(25), 2),
            "50th percentile": round(self.percentile(50), 2),
            "75th percentile": round(self.percentile(75), 2),
            "frequency distribution": self.frequency_distribution(),
        }


if __name__ == "__main__":
    sample = [4, 7, 2, 9, 10, 4, 5, 8, 4, 6]
    stats = Statistics(sample)
    for k, v in stats.summary().items():
        print(f"{k:25}: {v}")


#2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}   # {description: amount}
        self.expenses = {}  # {description: amount}

    # ---------- Add new items ----------
    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    # ---------- Totals ----------
    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    # ---------- Balance ----------
    def account_balance(self):
        return self.total_income() - self.total_expense()

    # ---------- Info ----------
    def account_info(self):
        print(f"Account Holder: {self.firstname} {self.lastname}")
        print(f"Total Income : ${self.total_income():,.2f}")
        print(f"Total Expense: ${self.total_expense():,.2f}")
        print(f"Balance      : ${self.account_balance():,.2f}\n")

        print("Incomes:")
        for desc, amt in self.incomes.items():
            print(f"  {desc:20s} +${amt:,.2f}")

        print("\nExpenses:")
        for desc, amt in self.expenses.items():
            print(f"  {desc:20s} -${amt:,.2f}")



if __name__ == "__main__":
    person = PersonAccount("John", "Doe")

    person.add_income("Salary", 5000)
    person.add_income("Freelance", 1200)

    person.add_expense("Rent", 1500)
    person.add_expense("Groceries", 600)
    person.add_expense("Internet", 150)

    person.account_info()
