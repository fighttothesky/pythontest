import configparser


class ConfigReader:
    def __init__(self, file_name="config.ini"):
        self.file_name = file_name
        self.config = configparser.ConfigParser()
        self.config.read(self.file_name)

    def getvar(self, section, variable):
        return self.config.get(section, variable)