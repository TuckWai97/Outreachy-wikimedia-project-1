# csv module is built-in module in Python, so do not need to install, but need to import in script in order to use it.
# csv module implements classes to read and write tabular data in CSV format
#
import csv
import requests

# input_csv variable is used to assign the csv file name as a string, as it encases in double quotes "", this is better than hardcoded it into the code, makes it easier to reuse again next time, by just replace the csv file with desired csv file.
input_csv = "Task 2 - Intern.csv"

# get_status_code function is a user-defined function for getting the status code from the url given in the csv file. 
# Arg: 
#     csv_url: url string
# Return: 
#     return response status code of  by the specific url.
#
def get_status_code(csv_url):
    # send a GET request, with the URL of the .csv file as url, for accessing data from the url variable, return all data sent from server. 
    response = requests.get(csv_url)
    status_code = response.status_code
    return status_code


# catch_status_code_exception_error function is used handling the status code exception error and get the final output into the required format in task as below:
# (STATUS_CODE) URL

# Args:
#      url: url string
# Returns:
#      f"(status_code) url" : if HTTP request successfully and get response status code
#      f"(ConnectionError) {url}" : HTTP request failed with connection error
#      f"(URLRequired) {url}"     : HTTP request failed with invalid URL
#      f"(ReadTimeout) {url}"     : HTTP request failed with server not sending any data in the allotted time
#      f"(TooManyRedirects) {url}": HTTP request has too many redirects
#
def catch_status_code_exception_error(url):
    try:
        # calls "get_status_code()" function and store status code in "status_code" variable    
        status_code = get_status_code(url)
        return f"({status_code}) {url}"
    
    # ConnectionError : the request timed out while trying to connect to the remote server
    except requests.ConnectionError:
        return f"(ConnectionError) {url}"
    
    # URLRequired: A valid URL is required to make a request 
    except requests.URLRequired:
        return f"(URLRequired) {url}"
    
    # ReadTImeout: The server did not send any data in the allotted amount of time
    except requests.ReadTimeout:
        return f"(ReadTimeout) {url}" 

    # TooManyRedirects: the request has too many redirects  
    except requests.TooManyRedirects:
        return f"(TooManyRedirects) {url}"
    

# Implement code using "with open(filename, mode) as alias_filename", by replacing "filename" with your file, and select "mode" as below and "alias_filename" with the alias you would name the file for more convenient.
# "with()" statement is used in exception handling to make code cleaner and much more readable, so there is no need to call file.close() since with statement automatically closes the file after completed reading it.
# ".open()" function opens a file, return it as file object, `mode` defines which mode you want to open the file.
# 'r' - to read an existing file,
# 'w' - to create a new file if given file doesn't exist and write to it,
# 'a' - to append to existing file content,
# '+' - to create a new file for reading and writing

# in this case, 'r' is used to read the existing file(the Task 2-Intern.csv that assigned as 'input_csv' as on the line 11)
with open(input_csv, "r") as inputfile: 

    # "csv.reader()" function iterates through the csv file row by row and store the result in "csv_file" variable
    csv_file = csv.reader(inputfile)

    # "next()" return the next row of the reader's object as list, as it skips the 1st row in the csv file as it contains the header of csv file, which is 'urls'
    next(csv_file)

    # loop through the rows in the "csv_file" list of strings with all the urls, "url_row" stores each url as list
    for url_row in csv_file:

        # in Task 2 = Intern.csv, the first column which is column 0 contains the url
        # indexes 0 to get the first item for the "url_row" list
        url = url_row[0]
        
        # calls "catch_status_code_exception_error()" function and store the result in "output_status_code_url" variable
        output_status_code_url = catch_status_code_exception_error(url)

        # prints out the final output as format "(STATUS_CODE) URL"
        print(output_status_code_url)


         

         

