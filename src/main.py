# setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# now import everything else
import time
import argparse
from rich import print  # print to the console with rich.print() instead of print()
from dotenv import load_dotenv, dotenv_values

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)

######################################################## SETUP #########################################################

# CONSTANTS
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2

# CONFIGURATION
log = Log()
start_time = time.perf_counter()  # monitor script performance

# setup any command-line arguments we need
parser = argparse.ArgumentParser(description='<insert a brief tool/script description>')
parser.add_argument('argname', help='<describe the arg here>')   # define arguments like this


###################################################### EXECUTION #######################################################

def main():
    """Add functionality for your script here."""
    
    args = parser.parse_args()  # pull in command-line arguments

    # report the results
    log.hbar('Results')
    print('[bold magenta]Hello, world.')  # try to avoid print(), but it works with formatting too if required
    
    if testFunction():  # let's test out calling a function
        log.success('Function was called!')

    # use log.debug() when developing or debugging - not used in production
    log.debug(f'You passed in this argument: [bold italic white]{args.argname}[/bold italic white]') 
    
    # log.inspect() is also useful for debugging
    log.hbar(f'Inspect Object (example)')
    log.inspect(cfg)


def testFunction():
    return True


##################################################### ENTRY POINT ######################################################

if __name__ == '__main__':
    main()  
    log.info(f"Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")  # log performance data