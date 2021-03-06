import pandas as pd
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

file2 = pd.read_excel('Open-source-data.xls')
file3 = pd.read_excel('Open-source-data.xls', index_col=None, na_values=['NA'], usecols='A')
print(file3)
file = pd.ExcelFile('Open-source-data.xls')
continents = file.sheet_names
for continent in continents:
    print(continent)
print(file2)

