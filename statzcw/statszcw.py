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
    std_dev = sqrt.zvariance(data)
    return std_dev


def zstderr(data: List[float]) -> float:
    s_error = zstddev(data)/ sqrt.zcount(data)
    return s_error


def cov(a, b):
    sum = 0
    count = len(a)
    c = sum/(count(a)-1)
    if len(a) == len(b):
        for i in range(0, count):
            sum += ((a[i] - zmean(a)) * (b[i] - zmean(b)))
    return c


def zcorr(datax: List[float], datay: List[float]) -> float:
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
