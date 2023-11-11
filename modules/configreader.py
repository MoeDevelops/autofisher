def readConfig():
    config = {}
    with open("config.txt", "r") as config_file:
        for line in config_file:
            key, value = line.strip().split("=")
            config[key] = value
    return config

def getGuiScale():
    return int(readConfig().get('gui_scale'))