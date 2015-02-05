__author__ = 'sh.ahn'

class Conf(object):
    # reading config file
    def __init__(self, result):
        vars(self).update(result)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def create_conf(conf_file_path):
        import json
        conf = None
        with open(conf_file_path, 'r') as f:
            conf = json.loads(f.read(), object_hook=Conf)

        return conf

