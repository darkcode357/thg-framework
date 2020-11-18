import os
from utils.files import ROOT_PATH
from fnmatch import fnmatchcase
from importlib import import_module
from ipaddress import ip_address
from urllib.parse import urlparse
"""
      self.module_info_by_path = {}
      self.enablement_by_type = {}
      self.module_load_error_by_path = {}
      self.module_load_warnings = {}
      self.module_paths = []
      self.module_set_by_type = {}
      self.aliases = {}
      self.inv_aliases = self.aliases.invert
todo:dsadsa
"""

def name_convert(name):
    if name.find(".py") != -1:
        module_name = name.replace("modules/", "").replace(".py", "")
        return module_name
    else:
        full_name = "{ROOT}/modules/{MODULE}.py".format(ROOT=ROOT_PATH, MODULE=name)
        return full_name


def get_local_modules():
    local_modules = []
    for directory_name, directories, filenames in os.walk("modules/"):
        for filename in filenames:
            if (
                filename not in ["__init__.py"]
                and not fnmatchcase(filename, "*.pyc")
                and fnmatchcase(filename, "*.py")
            ):
                full_name = "{directory}/{filename}".format(
                    directory=directory_name, filename=filename
                )
                module_name = name_convert(full_name)
                try:
                    module_class = import_module(
                        "modules.{module_name}".format(
                            module_name=module_name.replace("/", ".")
                        )
                    )
                except SyntaxError:
                    pass
                module_instance = module_class.Exploit()
                module_info = module_instance.get_info
                module_info["module_name"] = module_name
                try:
                    getattr(module_instance, "check")
                    module_info["check"] = "True"
                except AttributeError:
                    module_info["check"] = "False"
                local_modules.append(
                    (
                        module_info["module_name"],
                        module_info["check"],
                        module_info["disclosure_date"],
                        module_info["description"],
                    )
                )
    return local_modules


def parse_ip_port(netloc):
    """
    parse netloc to [ip, port]
    :param netloc: string eg:127.0.0.1:80
    :return: array eg: [127.0.0.1, 80]
    """
    try:
        ip = str(ip_address(netloc))
        port = None
    except ValueError:
        parsed = urlparse("//{}".format(netloc))
        ip = str(ip_address(parsed.hostname))
        port = parsed.port
    return ip, port
