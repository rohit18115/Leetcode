def average(salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    avg = 0
    n = len(salary)
    salary = sorted(salary)
    avg = sum(salary[1:-1]) / len(salary[1:-1])
    return avg


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

print(average(salary))
