"""The output processor - Write the results to a CSV"""
import pandas as pd
import os
import Config
import Constants


class OutputProcessor:
    """Contains methods to generate the output"""
    def __init__(self, file_location):
        self._file_location = file_location

    
    def generate_output(self, dates_with_row, records_data_frame, details_column_names):
        """Generates the output in the mentioned file"""
        try:
            output_rows = []
            for date_with_row in dates_with_row:            
                
                row_number = int(date_with_row[1])
                item_date = date_with_row[0]

                output_row = [item_date]
                records_for_row = records_data_frame.loc[row_number][details_column_names]
                for record in records_for_row.values:
                    output_row.append(record)
                output_rows.append(output_row)
                
            
            output_file_location = os.path.join(Constants.OUTPUT_FOLDER_NAME, Config.OUTPUT_FILE_NAME)
            output_file_handler = open(output_file_location, "w")


            for row in output_rows:
                for item in row:
                    output_file_handler.write("\"" + str(item) + "\", ")
                output_file_handler.write("\n")
           
            print("File created successfully inside the {0} folder".format(Constants.OUTPUT_FOLDER_NAME))
        except Exception as ex:
            print("An error occurred while writing the output to the file. Details: " + str(ex))
            raise 
        finally:
             output_file_handler.close()


