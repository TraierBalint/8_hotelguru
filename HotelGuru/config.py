import configparser

def db_config(filename='config.ini', section='Database'):
    config = configparser.ConfigParser()
    config.read(filename)
    
    return {
        'host' : config.get(section, 'host'),
        'user' : config.get(section, 'user'),
        'password' : config.get(section, 'password'),
        'database' : config.get(section, 'database')
    }