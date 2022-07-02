########################################
# Script for Housekeeping              #
# Version V1                           #
########################################
import os
import time
import logging
from datetime import datetime
#from configparser import SafeConfigParser
import configparser
#logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
#logging.basicConfig(filename='Housekeeping.log', format='%(name)s - %(levelname)s - %(asctime)s- %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s- %(message)s')

file_handler = logging.FileHandler('logging.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# Get current Date Time
curr_Time=datetime.now()
# Format current Date Time
format_curr_Time=curr_Time.strftime("%d/%m/%Y %H:%M:%S")
logger.info("Starting with Housekeeping at {0} ".format(format_curr_Time))

parser = configparser.ConfigParser()
parser.read('config.ini')
n = parser.get('Housekeeping_config', 'Path')
timePeriod=parser.get('Housekeeping_config', 'INTERVAL')
print(timePeriod)
#print(n)
#files_path = [os.path.abspath(x) for x in os.listdir(n)]
#print(files_path)
now = time.time()
#print ("%s Current", now)
for f in os.listdir(n):
    if os.stat(os.path.join(n,f)).st_mtime < (now - int(timePeriod)):
        #print(os.stat(os.path.join(n,f)).st_mtime)
        #print("File Name :",f)
        if os.path.isfile(os.path.join(n,f)):
            logger.info("Found File for removal")
            print(f)
            logger.info("Going ahead with File Removal File Name :-  {0}".format(f))
            os.remove(os.path.join(n,f))
            logger.info("File removed successfully !")
        else :
            logger.info("No file found to delete !!")