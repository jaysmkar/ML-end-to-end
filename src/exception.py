# importing the libraries
import sys 
import logging 

# This function will be taking error and returning the exact information about the error with line number.  
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message
    
# This is the custom exception creation for the error generation. 
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    # this function returns the function in the string format as __str__ is a magic method
    def __str__(self):
        return self.error_message