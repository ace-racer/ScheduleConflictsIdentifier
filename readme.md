# A command line application to Create a CSV which contains a day wise routine from a time table #
## This is specially useful for students who would want to upload their time table to an application like Google Calendar to be always aware of the courses that will take place at any time ##

### How to run the application ###
1. Create a CSV file which has all the details of all the courses for which required visibility is available
2. A sample CSV format can be found in the Sample input formats section
3. Provide the complete path to this CSV in the Config.py file's INPUT_FILE_LOCATION parameter. Please note that this file needs to be created as it is not put under source control due to local computer information
4. Provide the folder where the output CSV will be generated in the Config.py file's OUTPUT_FILE_NAME parameter. A folder with this name will be created in the same location where the **main.py** is present if it does not already exist and the output files will be created inside it.
5. Once all the above steps are followed, please open a command line in your system where Python is installed and issue the below command: __python main.py__ to start the execution
6. Please follow the on screen logs in the command line to check if there are any issues with the input file parsing or the generation of the output file

### Dependencies ###
1. Application is built using Python 3.2.X
2. Pandas for processing of CSV files