'''
Purpose: main function for the tile placement problem.
Create Date: 2/21/2022
Author: Kusch
'''
import fileReader

DEFAULT_FILE = 'input1.txt'
def main(file_name: str):
    landScape, tiles, targets = fileReader.readTxt(file_name)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_str = input("Input file name: ")
    if input_str == '':
        input_str = DEFAULT_FILE
    print(main(input_str))