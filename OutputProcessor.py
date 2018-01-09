"""The output processor - Write the results to a CSV"""
import pandas as pd


class OutputProcessor:
    """Contains methods to generate the output"""
    def __init__(self, file_location):
        self._file_location = file_location

    
    def generate_output(self, dates_with_row, records_data_frame, details_column_names):
        """Generates the output in the mentioned file"""
        output_rows = []
        for date_with_row in dates_with_row:
            records_for_row = records_data_frame.loc[int(date_with_row[1]), :]
            output_rows.append(' '.join(str(records_for_row)))

        #for output_row in output_rows:
            #print(output_row)

        for date, id in dates_with_row:
            print("Id: {0} - Date: {1}".format(id, date))

