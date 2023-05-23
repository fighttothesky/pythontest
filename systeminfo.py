import platform


class SystemInfo:
    def __init__(self):
        self.system_info = self.get_system_info()

    def get_system_info(self):
        system_info = {'System': platform.system(), 'Node Name': platform.node(), 'Release': platform.release(),
                       'Version': platform.version(), 'Machine': platform.machine(), 'Processor': platform.processor()}

        return system_info

    def print_system_info(self):
        for key, value in self.system_info.items():
            print(key + ':', value)


if __name__ == '__main__':
    system = SystemInfo()
    system.get_system_info()
    system.print_system_info()
