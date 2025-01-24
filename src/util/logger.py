import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

log_folder = 'log'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

date = datetime.datetime.now()
file_name = f'{log_folder}/app-' + str(date.year) + str(date.month) + str(date.day) + '.log'

log_format = logging.Formatter('[%(levelname)s] - [%(asctime)s] - [%(name)s] %(message)s')

main_log = logging.getLogger('')
main_log.setLevel(logging.INFO)

logging.basicConfig(filename=f'{log_folder}/app.log',
                    format='[%(levelname)s] - [%(asctime)s] - [%(name)s]  %(message)s',
                    level=logging.INFO)

file_handler = RotatingFileHandler(file_name, mode='a', backupCount=1)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(log_format)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(log_format)

main_log.addHandler(console)
main_log.addHandler(file_handler)


def get_logger(name):
    return logging.getLogger(name)
