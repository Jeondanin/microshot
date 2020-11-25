'''
common.py
'''
import os
import configparser

CONF = configparser.ConfigParser()
CURDIR = os.path.dirname(os.path.abspath(__file__))

CONF.read(os.path.join(CURDIR, 'config.ini'))

def getEnv():
    '''
    get current Environment

    '''
    os_env = 'local'
    if "target" in os.environ:
        os_env = os.environ["target"]
    return os_env

def getVolume(target):
    '''
    get Volume path

    '''
    return CONF.get(target, 'volume_path')


# environment 
TARGET = getEnv()
VOLUME = getVolume(TARGET)