'''
Purpose: main function for the tile placement problem.
Create Date: 2/21/2022
Author: Kusch
'''
import fileReader

DEFAULT_FILE = 'input1.txt'
def main(file_name: str):
    # Use a breakpoint in the code line below to debug your script.
    print(fileReader.readTxt(input_str))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_str = input("Input file name: ")
    if input_str == '':
        input_str = DEFAULT_FILE
    print(main(input_str))