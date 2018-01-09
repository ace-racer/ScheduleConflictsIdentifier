"""The main script to pass inputs to the required modules"""
from InputProcessor import InputProcessor


def main():
    input_processor = InputProcessor("C:\\Users\\anura\\Desktop\\ISS documents\\Basic electives selection_wc.csv")
    input_processor.parse_file()



if __name__ == "__main__":
    main()


