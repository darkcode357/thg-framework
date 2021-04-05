import argparse
import threading
import time
from importlib import import_module, reload
from pathlib import Path
from queue import Queue

from colorama import Style
from tabulate import tabulate

from lib.thg.core.BaseXmodeClass.BaseOption import BaseOption
from lib.thg.core.Interpreter.Submenu import AddSubmenu
from lib.thg.core.Interpreter.submenu.Crypto import CryptoLevel
from lib.thg.core.Interpreter.submenu.Exploitation import Exploitation
from lib.thg.core.Interpreter.submenu.Forensics import ForensicLevel
from lib.thg.core.Interpreter.submenu.Miscellaneous import MiscellaneousLevel
from lib.thg.core.Interpreter.submenu.Networking import NetworkingLevel
# menus da aplicação
##GERENCIAODR DE MENUS Decorator
##MENUS CLASS
from lib.thg.core.Interpreter.submenu.PPC import PPCLevel
from lib.thg.core.Interpreter.submenu.Reversing import ReversingLevel
from lib.thg.core.Interpreter.submenu.WebHacking import WebHackingLevel
from lib.thg.core.Interpreter.thgcmd.thgcmd import Cmd, with_category, with_argparser
from lib.thg.core.constants import *
from lib.thg.core_import import ModuleNotUseException
from utils import module


@AddSubmenu(
    PPCLevel(),
    command="PPC",
    shared_attributes=dict(
        second_level_attr="second_level_attr", top_level_attr="top_level_attr"
    ),
)
@AddSubmenu(
    ForensicLevel(),
    command="Forensic",
    shared_attributes=dict(
        second_level_attr="second_level_attr", top_level_attr="top_level_attr"
    ),
)
@AddSubmenu(
    WebHackingLevel(),
    command="WebHacking",
    shared_attributes=dict(
        second_level_attr="second_level_attr", top_level_attr="top_level_attr"
    ),
)
@AddSubmenu(
    MiscellaneousLevel(),
    command="Miscellaneous",
    shared_attributes=dict(
        second_level_attr="second_level_attr", top_level_attr="top_level_attr"
    ),
)
@AddSubmenu(
    ReversingLevel(),
    command="Reversing",
    shared_attributes=dict(
        second_level_attr="second_level_attr", top_level_attr="top_level_attr"
    ),
)
@AddSubmenu(
    NetworkingLevel(),
    command="Networking",
    shared_attributes=dict(
        second_level_attr="second_level_attr", top_level_attr="top_level_attr"
    ),
)
@AddSubmenu(CryptoLevel(), command="Crypto",
            shared_attributes=dict(second_level_attr="second_level_attr", top_level_attr="top_level_attr"), )
@AddSubmenu(Exploitation(), command="ExploitationLevel",
            shared_attributes=dict(second_level_attr="second_level_attr", top_level_attr="top_level_attr"), )
class ThgInterpreter(Cmd, Database):
    colors = "Always"

    console_prompt = "{COLOR_START}THG{COLOR_END}".format(
        COLOR_START=Fore.BLUE, COLOR_END=Fore.RESET
    )
    doc_header = "PRIME COMMAND HELP"
    doc_leader = ""
    intro = None
    lastcmd = ""
    misc_header = "Miscellaneous help topics:"
    nohelp = "*** No help on %s"
    prompt = "(lib)"
    ruler = "="
    undoc_header = "Undocumented commands:"
    console_prompt_end = ">"
    module_name = None
    module_class = None
    module_instance = None
    __version__ = 1.0

    # command categories

    ########################
    def __init__(self):
        super(ThgInterpreter, self).__init__()
        Database.__init__(self)
        self.prompt = self.console_prompt + self.console_prompt_end
        self.top_level_attr = 123456789
        self.second_level_attr = 987654321

    @with_category(CMD_CORE)
    def thg_banner(self, args):
        """Print lib banner"""
        self.poutput("\n\n")
        self.poutput(Menu().menu())

    @with_category(CMD_MODULE)
    def thg_list(self, args):
        """List all modules"""
        local_modules = module.get_local_modules()
        self._print_modules(local_modules, "Module List:")

    @with_category(CMD_MODULE)
    def thg_search(self, args):
        """
        Search modules

        Support fields:
            name, module_name, description, author, disclosure_date, service_name, service_version, check
        Eg:
            search redis
            search service_name=phpcms  service_version=9.6.0
        """
        search_conditions = args.split(" ")
        db_conditions = {}
        for condition in search_conditions:
            cd = condition.split("=")
            if len(cd) == 1:
                [module_name] = cd
                db_conditions["module_name"] = module_name
            else:
                [field, value] = cd
                if field in self.searchable_fields:
                    db_conditions[field] = value

        modules = self.search_modules(db_conditions)

        self._print_modules(modules, "Search results:")
        self._print_item("The search is only retrieved from the database")
        self._print_item("search <search term> Search for appropriate module")
        self._print_item("search osint/auxiliary/exploit ")
        self._print_item(
            "If you add/delete some new modules, please execute `db_rebuild` first\n\n"
        )

    def complete_set(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            completion_items = []
        else:
            completion_items = ["debug"]
            if self.module_instance:
                completion_items += [
                    option.name for option in self.module_instance.options.get_options()
                ]
        return self.basic_complete(text, line, begidx, endidx, completion_items)

    set_parser = argparse.ArgumentParser()
    set_parser.add_argument("name", help="The name of the field you want to set")
    set_parser.add_argument(
        "-f", "--file", action="store_true", help="Specify multiple targets"
    )
    set_parser.add_argument("value", help="The value of the field you want to set")




    #####################################
    @with_argparser(set_parser)
    @with_category(CMD_MODULE)
    def thg_set(self, args):
        """Set module option value/ set program config"""
        if args.name == "debug":
            self.debug = args.value
            return None

        if not self.module_instance:
            raise ModuleNotUseException()

        if args.file and args.name in ["HOST", "URL"]:
            try:
                open(args.value, "r")
                self.module_instance.multi_target = True

            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False
        elif not args.file and args.name in ["HOST", "URL"]:
            self.module_instance.multi_target = False
            self.module_instance.targets = None

        self.module_instance.options.set_option(args.name, args.value)

    def complete_use(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            modules = []
        else:
            modules = [local_module[0] for local_module in module.get_local_modules()]
        return self.basic_complete(text, line, begidx, endidx, modules)

    @with_category(CMD_MODULE)
    def thg_use(self, module_name, module_reload=False):
        """Chose a module"""
        module_file = module.name_convert(module_name)
        module_type = module_name.split("/")[0]

        if Path(module_file).is_file():
            self.module_name = module_name
            if module_reload:
                self.module_class = reload(self.module_class)
            else:
                self.module_class = import_module(
                    "modules.{module_name}".format(
                        module_name=module_name.replace("/", ".")
                    )
                )
            self.module_instance = self.module_class.Exploit()
            self.set_prompt(module_type=module_type, module_name=module_name)
        else:
            self.poutput("Module/Exploit not found.")

    @with_category(CMD_MODULE)
    def thg_back(self, args):
        """Clear module that chose"""
        self.module_name = None
        self.module_instance = None
        self.prompt = self.console_prompt + self.console_prompt_end

    def complete_show(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            completion_items = []
        else:
            completion_items = ["info", "options", "missing"]
        return self.basic_complete(text, line, begidx, endidx, completion_items)

    @with_category(CMD_MODULE)
    def thg_show(self, content):
        """
        Display module information

        Eg:
            show info
            show options
            show missing
        """
        if not self.module_instance:
            raise ModuleNotUseException()

        if content == "info":
            info = self.module_instance.get_info
            info_table = []
            self.poutput("Module info:")
            for item in info.keys():
                info_table.append([item + ":", info.get(item)])
            self.poutput(tabulate(info_table, colalign=("right",), tablefmt="plain"))

        if content == "options" or content == "info":
            options = self.module_instance.options.get_options()
            default_options_instance = BaseOption()
            options_table = []
            for option in options:
                options_table_row = []
                for field in default_options_instance.__dict__.keys():
                    options_table_row.append(getattr(option, field))
                options_table.append(options_table_row)

            self.poutput("Module options:")
            self.poutput(
                tabulate(
                    options_table,
                    headers=default_options_instance.__dict__.keys(),
                )
            )

        if content == "missing":
            missing_options = self.module_instance.get_missing_options()
            if len(missing_options) == 0:
                self.poutput("No option missing!")
                return None

            default_options_instance = BaseOption()
            missing_options_table = []
            for option in missing_options:
                options_table_row = []
                for field in default_options_instance.__dict__.keys():
                    options_table_row.append(getattr(option, field))
                missing_options_table.append(options_table_row)
            self.poutput("Missing Module options:")
            self.poutput(
                tabulate(
                    missing_options_table,
                    headers=default_options_instance.__dict__.keys(),
                )
            )

    @with_category(CMD_MODULE)
    def thg_run(self, args):
        """alias to exploit"""
        try:
            self.thg_exploit(args=args)
        except Exception:
            self.thg_check(args=args)

    def exploit_thread(self, target, target_type, thread_queue):
        target_field = None
        port = None

        if target_type == "tcp":
            [target, port] = module.parse_ip_port(target)
            target_field = "HOST"
        elif target_type == "http":
            target_field = "URL"
        exp = self.module_class.Exploit()
        exp.options.set_option(target_field, target)
        exp.options.set_option(
            "TIMEOUT", self.module_instance.options.get_option("TIMEOUT")
        )
        if port:
            exp.options.set_option("PORT", port)
        else:
            exp.options.set_option(
                "PORT", self.module_instance.options.get_option("PORT")
            )

        exploit_result = exp.exploit()

        if exploit_result.status:
            self._print_item(exploit_result.success_message)
        else:
            self._print_item(exploit_result.error_message, color=Fore.RED)
        thread_queue.get(1)

    @with_category(CMD_MODULE)
    def thg_exploit(self, args):
        """Execute module exploit"""
        if not self.module_instance:
            raise ModuleNotUseException()

        [validate_result, validate_message] = self.module_instance.options.validate()
        if not validate_result:
            for error in validate_message:
                self._print_item(error, color=Fore.RED)
            return False

        if self.module_instance.multi_target:
            target_type = self.module_instance.target_type
            target_field = None

            if target_type == "tcp":
                target_field = "HOST"
            elif target_type == "http":
                target_field = "URL"

            target_filename = self.module_instance.options.get_option(target_field)

            try:
                target_file = open(target_filename, "r")
                self.module_instance.targets = []
                for line in target_file.readlines():
                    self.module_instance.targets.append(line.strip())
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False

            targets = self.module_instance.targets
            targets_queue = Queue()
            for target in targets:
                targets_queue.put(target)

            if not targets_queue.empty():
                thread_count = int(self.module_instance.options.get_option("THREADS"))
                thread_queue = Queue(maxsize=thread_count)

                try:
                    while not targets_queue.empty():
                        while thread_queue.full():
                            time.sleep(0.1)

                        target = targets_queue.get()
                        thread_queue.put(1)
                        _thread = threading.Thread(
                            target=self.exploit_thread,
                            args=(target, target_type, thread_queue),
                        )
                        _thread.start()

                    while not thread_queue.empty():
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    self._print_item(
                        "Wait for existing process to exit...", color=Fore.RED
                    )
                    while threading.activeCount() > 1:
                        time.sleep(0.5)
                    return None

            self.poutput(
                "{style}[*]{style_end} module execution completed".format(
                    style=Fore.BLUE + Style.BRIGHT, style_end=Style.RESET_ALL
                )
            )
            return False

        exploit_result = self.module_instance.exploit()
        if exploit_result.status:
            self._print_item("Exploit success!")
            self._print_item(exploit_result.success_message)
        else:
            self._print_item("Exploit failure!", color=Fore.RED)
            self._print_item(exploit_result.error_message, color=Fore.RED)
        self.poutput(
            "{style}[*]{style_end} module execution completed".format(
                style=Fore.BLUE + Style.BRIGHT, style_end=Style.RESET_ALL
            )
        )

    def check_thread(self, target, target_type, thread_queue):
        target_field = None
        port = None

        if target_type == "tcp":
            [target, port] = module.parse_ip_port(target)
            target_field = "HOST"
        elif target_type == "http":
            target_field = "URL"
        exp = self.module_class.Exploit()
        exp.options.set_option(target_field, target)
        exp.options.set_option(
            "TIMEOUT", self.module_instance.options.get_option("TIMEOUT")
        )
        if port:
            exp.options.set_option("PORT", port)
        else:
            exp.options.set_option(
                "PORT", self.module_instance.options.get_option("PORT")
            )

        exploit_result = exp.check()

        if exploit_result.status:
            self._print_item(exploit_result.success_message)
        else:
            self._print_item(exploit_result.error_message, color=Fore.RED)
        thread_queue.get(1)

    @with_category(CMD_MODULE)
    def thg_check(self, args):
        """Execute module check"""
        if not self.module_instance:
            raise ModuleNotUseException('foo', 'FOO', 'bar')


        [validate_result, validate_message] = self.module_instance.options.validate()
        if not validate_result:
            for error in validate_message:
                self._print_item(error, Fore.RED)
            return False

        if self.module_instance.multi_target:

            target_type = self.module_instance.target_type
            target_field = None

            if target_type == "tcp":
                target_field = "HOST"
            elif target_type == "http":
                target_field = "URL"
            elif target_type == "query":
                target_field = "QUERY"
            elif target_type == "crawler":
                target_type = "CRAWLER"
            elif target_type == "url":
                target_field = "URL"
            target_filename = self.module_instance.options.get_option(target_field)

            try:
                target_file = open(target_filename, "r")
                self.module_instance.targets = []
                for line in target_file.readlines():
                    self.module_instance.targets.append(line.strip())
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False

            targets = self.module_instance.targets
            targets_queue = Queue()
            for target in targets:
                targets_queue.put(target)

            if not targets_queue.empty():
                thread_count = int(self.module_instance.options.get_option("THREADS"))
                thread_queue = Queue(maxsize=thread_count)

                try:
                    while not targets_queue.empty():
                        while thread_queue.full():
                            time.sleep(0.1)

                        target = targets_queue.get()
                        thread_queue.put(1)
                        _thread = threading.Thread(
                            target=self.check_thread,
                            args=(target, target_type, thread_queue),
                        )
                        _thread.start()

                    while not thread_queue.empty():
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    self._print_item(
                        "Wait for existing process to exit...", color=Fore.RED
                    )
                    while threading.activeCount() > 1:
                        time.sleep(0.5)
                    return None

            self.poutput(
                "{style}[*]{style_end} module execution completed".format(
                    style=Fore.BLUE + Style.BRIGHT, style_end=Style.RESET_ALL
                )
            )
            return None

        exploit_result = self.module_instance.check()

        if exploit_result is None:
            self._print_item("Check Error: check function no results returned")
            return None

        if exploit_result.status:
            self._print_item("Check success!")
            self._print_item(exploit_result.success_message)
        else:
            self._print_item("Exploit failure!", color=Fore.RED)
            self._print_item(exploit_result.error_message, color=Fore.RED)
        self.poutput(
            "{style}[*]{style_end} module execution completed".format(
                style=Fore.BLUE + Style.BRIGHT, style_end=Style.RESET_ALL
            )
        )

    @with_category(CMD_CORE)
    def thg_db_rebuild(self, args):
        """Rebuild database for search"""
        check = args.split(" ")
        for condition in check:
            self.db_rebuild(debug=condition)
        self.poutput("Database rebuild done.\nuse db_rebuild debug ")

    @with_category(CMD_MODULE)
    def thg_reload(self, args):
        """reload the chose module"""
        self.thg_use(self.module_name, module_reload=True)

    def set_prompt(self, module_type, module_name):
        module_prompt = " {module_type}({color}{module_name}{color_end})".format(
            module_type=module_type,
            module_name=module_name.replace(module_type + "/", ""),
            color=Fore.RED,
            color_end=Fore.RESET,
        )
        self.prompt = self.console_prompt + module_prompt + self.console_prompt_end

   #todo: def thg_save(self,args):
   #todo: def thg_load_session(self,args):


    def _print_modules(self, modules, title):
        self.poutput(title)
        self.poutput(
            tabulate(
                modules,
                tablefmt="grid",
                headers=(
                    Fore.CYAN + "module_name" + Fore.RESET,
                    Fore.CYAN + "check" + Fore.RESET,
                    Fore.CYAN + "disclosure_date" + Fore.RESET,
                    Fore.CYAN + "description" + Fore.RESET,
                ),
            )
        )

    def _print_item(self, message, color=Fore.RESET):
        self.poutput(
            "{style}[+]{style_end} {message}".format(
                style=color + Style.BRIGHT,
                style_end=Style.RESET_ALL,
                message=message,
            )
        )
