
from configparser import ConfigParser
from tools.handle_path import conf_dir


# HandleIni   ConfigParser   RawConfigParser
class HandleIni(ConfigParser):
    def __init__(self,filenames):
        super().__init__() # 继承的时候，如果初始化方法被函数用到了，就先调用父类的初始化方法
        self.read(filenames=filenames,encoding='utf-8')
conf = HandleIni(conf_dir)
