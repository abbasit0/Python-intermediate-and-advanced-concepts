import logging
# we will the logging module to record the the program execution

# to record the messages of a program what it is doing. These messages are called logs
"""There are five levels of Logging.
1. DEBUG (will give us the detailed inforamtion, helps in debugging)
2. INFO (will tell us that the program ran successfully, evaluated successfully)
3. WARNING (tell us that there is issue but will not affect the program)
4. ERROR (tell us about a serious problem due to which some functionallity will not work but still program will not be stoped)
5. CRITICAL (a serious problem which might stop the program)"""

# the default level is WARNING 
# to set it to another level we will do it as


# by simply setting level or using it directly it will show the logging messages on the console 
# if we want them to be in a file we can do it as by setting filename = filename


# we can also change the format by which it would show as we want by changing the format 


logging.basicConfig(level=logging.DEBUG, filename="logging_learning.log",
format="%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(filename)s") # now the level has been set to the debug


logging.info("Program evaluation has been started")
try:
    print(10 / 0)
except ZeroDivisionError:
    logging.critical("critical error occured due to division by a zero") # by this we replace the print statements by logs and will track the progess of the program

logging.info("Evaluation has been ended")