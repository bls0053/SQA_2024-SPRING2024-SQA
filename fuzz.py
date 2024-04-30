# This file will fuzz 5 python methods and record any exceptions that occur
import sys
import os


new_directory_path = os.path.join(os.getcwd(), 'empirical')
os.chdir(new_directory_path)
sys.path.append(os.getcwd())
# print(os.getcwd())
from report import Average, Median, giveTimeStamp
# from dataset.stats import getFileLength
def simple_fuzz():
    test_list = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [10,10,10,10,10,10,10],
    [1.0, 1, 1, 2.5])
    try:
        for x in test_list:
            print(Average(x))
            print(Median(x))
            print(giveTimeStamp())
        # print(getFileLength("report.py"))
        os.chdir("..")
        # print(os.getcwd())
        new_directory_path = os.path.join(os.getcwd(), 'FAME-ML')
        os.chdir(new_directory_path)
        sys.path.append(os.getcwd())
        from main import getAllPythonFilesinRepo
        print(getAllPythonFilesinRepo(os.getcwd()))


        os.chdir("..")
        # print(os.getcwd())
        new_directory_path = os.path.join(os.getcwd(), 'mining')
        os.chdir(new_directory_path)
        sys.path.append(os.getcwd())
        from mining import checkPythonFile
        print(checkPythonFile(os.getcwd()))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    simple_fuzz()
