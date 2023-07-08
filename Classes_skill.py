class Name:
    def __init__(self, first, last):
        self.First = first
        self.Last = last

    def __str__(self):
        return self.First + ' ' + self.Last

n = Name('Sumit', 'Sindhu')

print(str(n))