def average(salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    return sum(sorted(salary)[1:-1]) / len(salary[1:-1])


salary = [
    48000,
    59000,
    99000,
    13000,
    78000,
    45000,
    31000,
    17000,
    39000,
    37000,
    93000,
    77000,
    33000,
    28000,
    4000,
    54000,
    67000,
    6000,
    1000,
    11000,
]
salary = [int(i) for i in salary]
print(average(salary))
