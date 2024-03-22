import statistics
from itertools import count
from math import sqrt
from typing import List


def zcount(data: List[float]) -> float:
    #with tools
    return len(data)

    #showing logic
    # counter = 0
    # for i in data:
    #     counter = counter + 1
    # return counter


def zmean(data: List[float]) -> float:
    #with tools
    return sum(data) / len(data)

    # #showing logic
    # counter = zcount(data)
    # val = sum(data)
    # total = val / counter
    # return total


def zmode(data: List[float]) -> float:
    #with tools
    return statistics.mode(data)

    #showing logic
    # data.sort(reverse=True)
    # return data.index(0)


def zmedian(data: List[float]) -> float:
    #with tools
    return statistics.median(data)

    #showing logic
    # tmp = sorted(data)
    # mid = len(tmp)
    # return (tmp[mid] + tmp[-mid - 1])/2


def zvariance(data: List[float]) -> float:
    #with tools
    return statistics.variance(data)

    #showing logic
    # n = zcount(data)
    # m = zcount(data)
    # deviations = [(x-m) **2 for x in data]
    # s = sum(deviations)/n - 1
    # return s


def zstddev(data: List[float]) -> float:
    variance = zvariance(data)
    std_dev = sqrt(variance)
    return std_dev


def zstderr(data: List[float]) -> float:
    s_error = zstddev(data)/ sqrt.zcount(data)
    return s_error


def cov(a, b):
    if len(a) != len(b):
        raise ValueError("lists a and b must be same length")
    count = len(a)
    sum = 0
    mean_a = zmean(a)
    mean_b = zmean(b)

    for i in range(0, count):
        sum += (a[i] - mean_a) * (b[i] - mean_b)
    c = sum / (count - 1)
    return c


def zcorr(datax: List[float], datay: List[float]) -> float:
    if len(datax) != len(datay):
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

