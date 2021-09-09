import configparser

config = configparser.ConfigParser()

try:
    config.read('config/properties.conf')
except Exception  as e:
    print(e)