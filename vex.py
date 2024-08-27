import platform
import os
import sys
import logging
from threading import Thread

logging.basicConfig(
    level=logging.INFO,
    format=' •\x1b[38;5;196m ×͜× \x1b[37m %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

global arc

def update_repository():
    logging.info('CHECKING FOR UPDATES')
    exit_code = os.system('git pull --quiet')
    if exit_code != 0:
        logging.error('Failed to pull updates from repository.')
        sys.exit(1)
    logging.info('Repository is up to date.')

def check_python_architecture():
    global arc
    architecture = platform.architecture()[0]
    try:
        if architecture == '32bit':
            arc = "32BIT"
            logging.info('32BIT DETECTED')
            logging.info('STARTING Luffy (vex32)')
            import upp32 as Luffy
        elif architecture == '64bit':
            arc = "64BIT"
            logging.info('64BIT DETECTED')
            logging.info('STARTING Luffy (vex64)')
            import upp64 as Luffy
        else:
            arc = "INVALID"
            logging.error('Unsupported architecture detected.')
            sys.exit(1)
        
        thread = Thread(target=Luffy.start)
        thread.start()
        thread.join()
    
    except ImportError as e:
        logging.error(f'Failed to import module: {e}')
        sys.exit(1)

if __name__ == "__main__":
    update_repository()
    check_python_architecture()
