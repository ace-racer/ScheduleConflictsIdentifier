"""The input processor - Read from the CSV and process the subjects by the dates"""
import pandas as pd
import datetime as dt
import Constants
from OutputProcessor import OutputProcessor


class InputProcessorDataFrameUpdater:
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
                    
                    date_column_names = []
                    details_column_names = []               
                  
                    for column_name in column_names:
                        if str(column_name).isdigit():
                            date_column_names.append(column_name)
                        else:
                            details_column_names.append(column_name)
                   
                    # convert the required columns to date objects
                    for date_column_name in date_column_names:
                        df[date_column_name] = df[date_column_name].apply(self.convert_to_date_time)
                    
                    print(df[:])                   
                else:
                    raise ValueError("The input file must be a CSV file")
            except Exception as exp:
                print("An exception occurred while processing the file. Details: " + str(exp))
                raise
        else:
            raise ValueError("No input file location is specified")
                

    def convert_to_date_time(self, candidate_to_convert):
        """Convert a candidate string to a Python date time object"""
        if candidate_to_convert and not pd.isnull(candidate_to_convert):
            return dt.datetime.strptime(str(candidate_to_convert), Constants.DATE_FORMAT)
        else:
            return None