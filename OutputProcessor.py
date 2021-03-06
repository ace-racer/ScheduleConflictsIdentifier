"""The output processor - Write the results to a CSV"""
import pandas as pd
import os
import Config
import Constants


class OutputProcessor:
    """Contains methods to generate the output"""   
    def generate_output(self, dates_with_row, records_data_frame, details_column_names):
        """Generates the output in the mentioned file"""
        try:
            output_rows = []
            last_date = None
            for date_with_row in dates_with_row:            
                
                row_number = int(date_with_row[1])
                item_date = date_with_row[0]


                conflict = False
                if last_date is not None and last_date == item_date:
                    conflict = True

                last_date = item_date
                output_row = [item_date, conflict]
                records_for_row = records_data_frame.loc[row_number][details_column_names]
                for record in records_for_row.values:
                    output_row.append(record)
                output_rows.append(output_row)
                
            if not os.path.exists(Constants.OUTPUT_FOLDER_NAME):
                os.makedirs(Constants.OUTPUT_FOLDER_NAME)
            
            output_file_location = os.path.join(Constants.OUTPUT_FOLDER_NAME, Config.OUTPUT_FILE_NAME)
            output_file_handler = open(output_file_location, "wb")

            # Populate the file headers for the output file
            output_file_headers = self.get_output_file_headers("Date", "Conflict with earlier item", details_column_names)
            output_file_text = ""
            output_file_text += ", ".join(output_file_headers)
            output_file_text += "\n\n"            

            for row in output_rows:
                for item in row:
                    cell_value = "Data not available"
                    if not pd.isnull(item):
                        cell_value = str(item)          
                    output_file_text += "\"" + cell_value + "\", "
                output_file_text += "\n"                                    
           
            output_file_handler.write(output_file_text.encode(Constants.ENCODING))
            print("File created successfully inside the {0} folder".format(Constants.OUTPUT_FOLDER_NAME))
        except Exception as ex:
            print("An error occurred while writing the output to the file. Details: " + str(ex))
            raise 
        finally:
             output_file_handler.close()


    def get_output_file_headers(self, *args):
        """Get the headers for the output CSV file as a list with each member in a quote"""
        if args:
            headers = []
            for items in args:
                if type(items) is list:
                    for item in items:
                        headers.append("\"" + str(item) + "\"")
                else:
                    headers.append("\"" + str(items) + "\"")
            return headers 






