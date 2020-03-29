import configparser as ConfigParser

# Configs parameters configParser.get('your-config', 'path1')
configParser = ConfigParser.RawConfigParser()
configFilePath = r'eneo_config.txt'
configParser.read(configFilePath)

# Parameters
USERNAME = configParser.get('eneo-config', 'USERNAME')
PASSWORD = configParser.get('eneo-config', 'PASSWORD')
LOGIN_URL = configParser.get('eneo-config', 'LOGIN_URl')

LOGIN_FIELD = "login"
PASSWORD_FIELD = "password"
