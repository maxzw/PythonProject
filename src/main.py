import os
import sys
import argparse

# import logging
from log_tools import create_logger

# set file directory as working directory
os.chdir(os.path.dirname(sys.argv[0]))

# imported scripts that can be run
from test import testscript

SCRIPTS = {
        'test': testscript
    }

# main function
def main(config):
    logging = create_logger(config.log)

    if config.script not in SCRIPTS:
        logging.error("Unknown script")
    else:
        script = SCRIPTS[config.script]
        script(logging, config)
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l',
        '--log',
        type=bool,
        default=False,
        help='Logging (default: False)'
    )

    parser.add_argument(
        '-s',
        '--script',
        type=str,
        default='',
        help="Which script is executed (default: '')"
    )
    
    args = parser.parse_args()
    
    main(args)