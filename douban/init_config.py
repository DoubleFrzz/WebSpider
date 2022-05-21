from configparser import ConfigParser, RawConfigParser
import os
import sys

"""
https://www.cnblogs.com/machangwei-8/p/11213113.html
可以作为参考
"""

class PraseConfig(ConfigParser):
    def __init__(self):
        super().__init__()
        current_path = os.path.dirname(__file__)
        super().read(os.path.join(current_path, "douban.conf"))

    def value_2_dict(self, section):
        if super().has_section(section):
            return dict(super().items(section))
        else:
            print("config is not section: %s" % section)
            sys.exit()

