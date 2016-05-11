citation = {
        'journal'      : 'The Mathematical Intelligencer',
        'volume'       : 38,
        'number'       : 1,
        'season'       : 'Spring',
        'year'         : 2016,
        'title'        : 'Prague Clocks',
        'first_author' : 'Chan Bae',
    }


def triangular_num_list(n):
    """
    finds the first n triangular numbers
    """
    num_list = []
    cumulative = 0
    for num in range(n):
        cumulative = cumulative + num
        num_list.append(cumulative)
    return num_list


def modulo_list(m, num_list=None, append_m=True):
    """
    reduces the first m-1 triangular numbers mod m
    """
    if num_list is None:
        num_list = triangular_num_list(m)
    num_list = sorted(set(num % m for num in num_list))
    if append_m:
        num_list.append(m)
    return num_list


def sorted_list_diff(num_list):
    """
    sorts and calculates differences given a modulo
    """
    num_list = sorted(num_list)
    diff_list = []
    for i in range(1, len(num_list)):
        diff_list.append(num_list[i] - num_list[i - 1])
    return diff_list
    
        