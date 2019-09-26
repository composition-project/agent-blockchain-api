from configparser import ConfigParser
import os

def read_configuration():
    parser = ConfigParser()
    parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'config.ini'))

    return parser
