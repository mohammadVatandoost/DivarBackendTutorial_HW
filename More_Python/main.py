# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_file(file_name):
    for line in open(file_name):
        print(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file('sample.srt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
