# Default Modules
import datetime,time,os,sys,unittest

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

# Get our current directory
OUTPUT_FILE_DIRECTORY = os.getcwd()

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

# Create variables for all the paths
if((OS_TYPE == 'windows')):
    # Clear Screen Windows
    os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux')):
    sys.path.insert(0,'../classes/')
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')

import time

# < --- Begin Custom Classes Import --- >
# Benchmark for tracking the time it takes for the programs tasks
from benchmark import *

# Used for downloading a web page
from reuseable_methods import download_webpage

from reuseable_methods import get_difficulty
# < ---  End  Custom Classes Import --- >

while(True):
    # start the clock
    program_runtime = Benchmark()

    # Track difficulty check
    difficulty_clock = Benchmark()
    download_webpage('https://explorer.ryo-currency.com/',
                     'ryo_block_explorer.html',
                     OUTPUTS_DIR)

    difficulty_number = get_difficulty(OUTPUTS_DIR+'ryo_block_explorer.html')
    print(str(difficulty_number))
    difficulty_clock.stop()

    program_runtime.stop()
    print(program_runtime.get_string_runtime())

    print("Slept For:")

    time.sleep(60)
    print("1 Minute")
    time.sleep(60)
    print("2 Minutes")
    time.sleep(60)
    print("3 Minutes")
    time.sleep(60)
    print("4 Minutes")
    time.sleep(60)
    print("5 Minutes")

    os.system('cls')
