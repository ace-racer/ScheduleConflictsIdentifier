"""The input processor - Read from the CSV and process the subjects by the dates"""
import pandas as pd
import Constants


class InputProcessor:
    """Contains methods to process the input"""
    def __init__(self, file_location):
        self._file_location = file_location


    def parse_file(self):
        """Parse the input CSV file and load the data into an in memory data structure"""
        if self._file_location:
            print("The input file at location {0} will now be processed".format(self._file_location))
            try:
                stripped_file_location = self._file_location.strip()
                if stripped_file_location[-4:] == ".csv":
                    # Get the data frame from the CSV
                    df = pd.read_csv(stripped_file_location)

                    # Remove the rows for which all values are NaN's
                    df = df.dropna(axis=0,how='all')
                    
                    # Get the number of records in the data frame
                    num_records = len(df.index)

                    #Get the column numbers of the columns which only contain digit
                    column_names = df.columns.values
                    print("Column names type: " + str(type(column_names)))
                    column_positions = [position for position, column_name in enumerate(column_names) if str(column_name).isdigit()]
                    sorted(column_positions)
                    inclusive_start = column_positions[0]
                    inclusive_end = column_positions[-1]
                    print("Date values start from {0} and end at {1}".format(inclusive_start, inclusive_end))
                    print(column_names)

                    print(df[:10])
                else:
                    raise ValueError("The input file must be a CSV file")
            except Exception as e:
                print("An exception occurred while processing the file. Details: " + str(e))
        else:
            raise ValueError("No input file location is specified")
                
