def read_config():
    config = {}
    with open("config.txt", "r") as config_file:
        for line in config_file:
            key, value = line.strip().split("=")
            config[key] = value
    return config


def get_gui_scale():
    return int(read_config().get("gui_scale"))


def get_sleep_between_reads():
    return float(read_config().get("sleep_between_reads"))
