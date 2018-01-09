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
            
            row_number = int(date_with_row[1])
            item_date = date_with_row[0]

            output_row = [item_date]
            records_for_row = records_data_frame.loc[row_number][details_column_names]
            for record in records_for_row.values:
                output_row.append(record)
            output_rows.append(output_row)
            

        for row in output_rows:
            for item in row:
                print(item, end=' ')
            print()

