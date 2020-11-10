from THG.View.Interpreter.THGInterpreter import ThgInterpreter
from THG.View.Interpreter.thgcmd.thgcmd import with_argparser

import argparse



class THG(ThgInterpreter):
    """
    ponto de entrada para iniciar o thg

    """

    def run(self):
        self.cmdloop()



def main(argv=None):
    """Run when invoked from the operating system shell"""
    parser = argparse.ArgumentParser()

    generalGroup = parser.add_argument_group('General Options')
    generalGroup.add_argument('--debug', nargs='?', const='1',help='Debug level for output (default of 1, 2 for msg display).')
    console = parser.add_argument_group('Console options')
    console.add_argument('-a', '--ask', nargs='?', const='1', help='Ask before exiting thg or accept "exit -y"')
    console.add_argument('-H', '--history-file FILE', action='store_true', help='Save command history to the specified file')
    console.add_argument('-L', '--real-readline', action='store_true', help='Use the system Readline library instead of RbReadline')
    console.add_argument('-O', '--output FILE', action='store_true', help='Output to the specified file')
    console.add_argument('-p', '--plugin PLUGIN', action='store_true', help=' Load a plugin on startup')
    console.add_argument('-q', '--quiet', action='store_true', help='Do not print the banner on startup')
    console.add_argument('-r', '--resource FILE', action='store_true', help='Execute the specified resource file (- for stdin)')
    console.add_argument('-x', '--execute-command COMMAND', action='store_true', help='Execute the specified console commands (use ; for multiples)')
    generalGroup.add_argument('-v', '--version', action='store_true', help='Display current Empire version.')
    DataBase = parser.add_argument_group('Database options')
    DataBase.add_argument('-M', '--migration-path', nargs='?', const='1',
                      help='Specify a directory containing additional DB migrations')
    DataBase.add_argument('-n', '--no-database', nargs='?', const='1', help='Disable database support')
    DataBase.add_argument('-y', '--yaml', nargs='?', const='1',
                             help='Specify a YAML file containing database settings')

    FrameworkOP = parser.add_argument_group('Framework options')
    FrameworkOP.add_argument('-c File', nargs='?', const='1', help='Load the specified configuration file')

    moduleop = parser.add_argument_group('Module options')
    moduleop.add_argument('--defer-module-loads', nargs='?', const='1',
                          help='Defer module loading unless explicitly asked')
    moduleop.add_argument('-m', '--module-path DIRECTORY', nargs='?', const='1', help='Load an additional module path')



    cliGroup = parser.add_argument_group('CLI Payload Options')
    cliGroup.add_argument('-l', '--listener', nargs='?', const="list",
                          help='Display listener options. Displays all listeners if nothing is specified.')
    cliGroup.add_argument('-s', '--stager', nargs='?', const="list",
                          help='Specify a stager to generate. Lists all stagers if none is specified.')
    cliGroup.add_argument('-o', '--stager-options', nargs='*',
                          help="Supply options to set for a stager in OPTION=VALUE format. Lists options if nothing is specified.")

    restGroup = parser.add_argument_group('RESTful API Options')
    launchGroup = restGroup.add_mutually_exclusive_group()
    launchGroup.add_argument('--rest', action='store_true', help='Run thg and the RESTful API.')
    launchGroup.add_argument('--headless', action='store_true',
                             help='Run thg and the RESTful API headless without the usual interface.')
    restGroup.add_argument('--restport', type=int, nargs=1, help='Port to run the thg RESTful API on.')
    restGroup.add_argument('--username', nargs=1,
                           help='Start the RESTful API with the specified username instead of pulling from thg.db')
    restGroup.add_argument('--password', nargs=1,
                           help='Start the RESTful API with the specified password instead of pulling from thg.db')

    args = parser.parse_args()

    thgcli = THG()

    sys_exit_code = 0
    if args.command:
        # we have a command, run it and then exit
        c.onecmd_plus_hooks('{} {}'.format(args.command, ' '.join(args.command_args)))
    else:
        # we have no command, drop into interactive mode
        sys_exit_code = thgcli.cmdloop()

    return sys_exit_code


if __name__ == '__main__':
    import sys
    sys.exit(main())














