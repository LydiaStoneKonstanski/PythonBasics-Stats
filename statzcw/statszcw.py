import statistics
from itertools import count
from math import sqrt
from typing import List


def zcount(data: List[float]) -> float:
    #with tools
    # return len(data)

    #full length logic
    counter = 0
    for i in data:
        counter += 1
    return counter


def zmean(data: List[float]) -> float:
    return sum(data) / zcount(data)


def zmode(data: List[float]) -> list[float]:
    #with tools
    #return statistics.mode(data)

    # full length logic
    high = 0
    mode: list[float] = []
    for i in data:
        count = data[i]
        if count > high:
            high = count
        if count == high:
            mode.append(i)
    return mode

    # Alternative Dictionary method with list comp
    # mode_dict = {}
    # for item in data:
    #     mode_dict[item] = mode_dict.get(item, 0) + 1
    # high_count = max(mode_dict.values())
    # mode = [key for key, value in mode_dict.items() if value == high_count]
    # return mode


def zmedian(data: List[float]) -> float:
    #with tools
    # return statistics.median(data)

    # full length logic
    a: int = zcount(data)
    for i in range(a):
        for j in range(i + 1, a):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    if a % 2 == 0:
        midL = data[a // 2 - 1]
        midR = data[a // 2]
        return(midL + midR) / 2
    else:
        return data[a // 2]


def zvariance(data: List[float]) -> float:
    #with tools
    #return statistics.variance(data)

    # full length logic
    n = zcount(data)
    deviations = [(x-n) **2 for x in data]
    s = sum(deviations)/n - 1
    return s


def zstddev(data: List[float]) -> float:
    std_dev = sqrt(zvariance(data))
    return std_dev


def zstderr(data: List[float]) -> float:
    s_error = zstddev(data)/ sqrt(zcount(data))
    return s_error


def cov(a, b):
    if zcount(a) != zcount(b):
        raise ValueError("lists a and b must be same length")
    count = zcount(a)
    add = 0
    mean_a = zmean(a)
    mean_b = zmean(b)

    for i in range(0, count):
        add += (a[i] - mean_a) * (b[i] - mean_b)
    c = add / (count - 1)
    return c


def zcorr(datax: List[float], datay: List[float]) -> float:
    if zcount(datax) != zcount(datay):
        raise ValueError("lists datax and datay must be same length")
    corr = cov(datax, datay)/(zstddev(datax) * zstddev(datay))
    return corr


def readDataFile(file):
    x, y = [], []
    with open(file) as f:
        first_line = f.readline()  # consume headers
        for l in f:
            row = l.split(',')
            # print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x, y)


def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data


# a = [9,5,6,3,8,2,4]
# b = []
# for num in a:
#     b.append(num + 5)
# print(b)

#OR

# a = [9, 5, 6, 3, 8, 2, 4]
# b = [num + 5 for num in a]
# print(b)

