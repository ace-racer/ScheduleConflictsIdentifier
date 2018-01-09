"""The main script to pass inputs to the required modules"""
from InputProcessor import InputProcessor
import Config


def main():
    """The entry point for the command line application"""
    input_processor = InputProcessor(Config.INPUT_FILE_LOCATION)
    input_processor.parse_file()


if __name__ == "__main__":
    main()


