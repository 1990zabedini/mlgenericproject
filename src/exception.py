import sys 
import logging
def error_message_detail(error,error_detail:sys):
    _,_,exce_tb=error_detail.exc_info()
    file_name=exce_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python scrip name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exce_tb.tb_lineno,str(error)
    )

    return error_message

# when ever an error happeneds we call the above function        
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

# the last fuction os for pronting the error_message

    

#  whenever calling customeexception, it is inheriting the parent exception called Exception, 
# the output of the function will be considered as the variable in the class named error_message 
# error_detail will be retrieved by sys 

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divide by zero ")
        raise CustomException(e,sys)

# the above line of code is for checking the error file and if it is working a message must be written inside the log file