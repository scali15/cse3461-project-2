
"""
Lab 1 for CSE 3461
@author: jps73
"""
import configparser
import logging
import datetime

# Function procesess input accoring to directions.
# First, tokenizes input with split, utilizing the default behavior of splitting based on any whitespace
# Second, creates processes string using join method on the separator string ' ', which iterates through
# the list and creates a string of tokens with ' ' strings between them
def process_input(input_string):
    tokens = input_string.split()
    processed_string = ' '.join([tokens[0].upper()] + tokens[1:])
    return processed_string


def main():
    # Read configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Instantiate default logger with name, level, and formatting with time
    logging.basicConfig(filename='myapp.log', level=logging.INFO, format='%(asctime)s: %(levelname)s %(message)s', filemode = 'w')
    
    # Begin creation of log file
    logging.info('Application starting')
    
    # Main loop
    # Repetedly askes for and processes user input until the world quit is entered
    # Each entered string and processed string is saved in a log file
    while True:
        user_input = input('Enter a string: ')
        logging.info(f'Entered string = {user_input}')
        print(f'Entered string = {user_input}')
        print('%(asctime)s: %(levelname)s %(message)s')
        
        processed_string = process_input(user_input)
        logging.info(f'Processed string = {processed_string}')
        print(f'Processed string = {processed_string}')
        
        #end program nad log 'Shutting down' if quit is called
        if processed_string.startswith('QUIT'):
            logging.info('Shutting down...')
            break
    
if __name__ == "__main__":
    main()