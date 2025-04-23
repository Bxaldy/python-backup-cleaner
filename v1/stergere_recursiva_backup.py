import os
import time
import logging
import sys
import datetime
from configparser import ConfigParser

print('Script by Ionut Gabriel Buicu 2019')

file = 'config.ini'
config = ConfigParser()
config.read(file)


logging.basicConfig(format='%(message)s', filename='deletion.log', level=logging.INFO)
logger = logging.getLogger()
sys.stdout.write = logger.info

current_time = time.time()
daysToDelete = int(config.get('variabile', 'daysToDelete'))
directory = config.get('variabile', r'directory')
executionDate = datetime.datetime.now()
exceptionMonth1 = int(config.get('variabile', 'exceptionMonth1'))
exceptionMonth2 = int(config.get('variabile', 'exceptionMonth2'))
exceptionMonths = {exceptionMonth1, exceptionMonth2}


for dirpath, _, filenames in os.walk(directory):
    dirname = dirpath.split(os.path.sep)[-1]
    print('----------------------------------------------------------')
    print('----------------------------------------------------------')
    print(dirname)
    print('----------------------------------------------------------')
    print('----------------------------------------------------------')
    for f in filenames:
        fileWithPath = os.path.abspath(os.path.join(dirpath, f))
        modified_time = os.path.getmtime(fileWithPath)
        ltime = int(time.strftime('%m', time.localtime(modified_time)))
        print('File month : ', ltime)
        print('File :  ', fileWithPath)

        if ltime not in exceptionMonths :
            if (current_time - modified_time) // (24 * 3600) >= daysToDelete :
                os.unlink(fileWithPath)
                print('{} has been deleted'.format(fileWithPath))
                print("\n")
            else:
                print('{} was NOT deleted'.format(fileWithPath))
        else:
            print('{} was NOT deleted'.format(fileWithPath))

print(' ----------  Execution Finished  ---------- ')
print(' ---------- ', executionDate, ' ---------- ')