"""The input processor - Read from the CSV and process the subjects by the dates"""
import pandas as pd
from OutputProcessor import OutputProcessor
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
                    
                    date_column_names = []
                    details_column_names = []               
                  
                    for column_name in column_names:
                        if str(column_name).isdigit():
                            date_column_names.append(column_name)
                        else:
                            details_column_names.append(column_name)
                   
                    # Get the dates in the range
                    course_dates_df = df.loc[:][date_column_names]

                    # Get the date object for each of the item
                    # Details on below operation here: https://stackoverflow.com/questions/39992411/to-datetime-value-error-at-least-that-year-month-day-must-be-specified-pand
                    course_dates = pd.to_datetime(course_dates_df.stack(), format = Constants.DATE_FORMAT).unstack()  
                    # print(course_dates[:]) 

                    # Get the course dates with the row number
                    course_dates_with_row_list = []
                    for row_number, row in course_dates.iterrows():                        
                        for column_name in course_dates.columns.values:                            
                            date_value = row[column_name]
                            if not pd.isnull(date_value):                                
                                course_dates_with_row_list.append((date_value, row_number))

                   
                    course_dates_with_row_list = sorted(course_dates_with_row_list, key = lambda item: item[0])                    
                    op = OutputProcessor("test.csv")
                    op.generate_output(course_dates_with_row_list, df, details_column_names)
                else:
                    raise ValueError("The input file must be a CSV file")
            except Exception as exp:
                print("An exception occurred while processing the file. Details: " + str(exp))
                raise
        else:
            raise ValueError("No input file location is specified")
                
