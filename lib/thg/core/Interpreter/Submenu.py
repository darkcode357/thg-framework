#
# coding=utf-8
import copy
import os
from typing import List

import readline

from lib.thg.core.Interpreter.thgcmd.thgcmd import with_category
from .thgcmd.rl_utils import rl_type, RlType

MNTHG = "Menus THG"
MNTHGH = "MENU HELP"


@with_category(MNTHG)
class AddSubmenu(object):
    """Conveniently add a submenu (Cmd-like class) to a Cmd
    e.g. given "class SubMenu(Cmd): ..." then
    @AddSubmenu(SubMenu(), 'sub')
    class MyCmd(cmd.Cmd):
        ....
    will have the following effects:
    1. 'sub' will interactively enter the cmdloop of a SubMenu instance
    2. 'sub cmd args' will call thg_cmd(args) in a SubMenu instance
    3. 'sub ... [TAB]' will have the same behavior as [TAB] in a SubMenu cmdloop
       i.e., autocompletion works the way you think it should
    4. 'help sub [cmd]' will print SubMenu's help (calls its thg_help())
    """

    @with_category(MNTHG)
    class _Nonexistent(object):
        """
        Used to mark missing attributes.
        Disable __dict__ creation since this class does nothing
        """

        __slots__ = ()  #

    @with_category(MNTHG)
    def __init__(
        self,
        submenu,
        command,
        aliases=(),
        reformat_prompt="{super_prompt}::{sub_prompt}",
        shared_attributes=None,
        require_predefined_shares=True,
        create_subclass=False,
        preserve_shares=False,
        persistent_history_file=None,
    ):
        """Set up the class decorator
        submenu (Cmd):              Instance of something cmd.Cmd-like
        command (str):              The command the user types to access the SubMenu instance
        aliases (iterable):         More commands that will behave like "command"
        reformat_prompt (str):      Format str or None to disable
            if it's a string, it should contain one or more of:
                {super_prompt}:     The current cmd's prompt
                {command}:          The command in the current cmd with which it was called
                {sub_prompt}:       The subordinate cmd's original prompt
            the default is "{super_prompt}{command} {sub_prompt}"
        shared_attributes (dict):   dict of the form {'subordinate_attr': 'parent_attr'}
            the attributes are copied to the submenu at the last moment; the submenu's
            attributes are backed up before this and restored afterward
        require_predefined_shares: The shared attributes above must be independently
            defined in the subordinate Cmd (default: True)
        create_subclass: put the modifications in a subclass rather than modifying
            the existing class (default: False)
        """
        self.submenu = submenu

        self.command = command
        self.aliases = aliases
        if persistent_history_file:
            self.persistent_history_file = os.path.expanduser(persistent_history_file)
        else:
            self.persistent_history_file = None

        if reformat_prompt is not None and not isinstance(reformat_prompt, str):
            raise ValueError("reformat_prompt should be either a format string or None")
        self.reformat_prompt = reformat_prompt

        self.shared_attributes = {} if shared_attributes is None else shared_attributes
        if require_predefined_shares:
            for attr in self.shared_attributes.keys():
                if not hasattr(submenu, attr):
                    raise AttributeError(
                        "The shared attribute '{attr}' is not defined in {cmd}. Either define {attr} "
                        "in {cmd} or set require_predefined_shares=False.".format(
                            cmd=submenu.__class__.__name__, attr=attr
                        )
                    )

        self.create_subclass = create_subclass
        self.preserve_shares = preserve_shares

    @with_category(MNTHG)
    def _get_original_attributes(self):
        return {
            attr: getattr(self.submenu, attr, AddSubmenu._Nonexistent)
            for attr in self.shared_attributes.keys()
        }

    @with_category(MNTHG)
    def _copy_in_shared_attrs(self, parent_cmd):
        for sub_attr, par_attr in self.shared_attributes.items():
            setattr(self.submenu, sub_attr, getattr(parent_cmd, par_attr))

    @with_category(MNTHG)
    def _copy_out_shared_attrs(self, parent_cmd, original_attributes):
        if self.preserve_shares:
            for sub_attr, par_attr in self.shared_attributes.items():
                setattr(parent_cmd, par_attr, getattr(self.submenu, sub_attr))
        else:
            for attr, value in original_attributes.items():
                if attr is not AddSubmenu._Nonexistent:
                    setattr(self.submenu, attr, value)
                else:
                    delattr(self.submenu, attr)

    @with_category(MNTHG)
    def __call__(self, cmd_obj):
        """Creates a subclass of Cmd wherein the given submenu can be accessed via the given command"""

        @with_category(MNTHG)
        def enter_submenu(parent_cmd, statement):
            """
            This function will be bound to thg_<submenu> and will change the scope of the CLI to that of the
            submenu.
            """
            submenu = self.submenu
            original_attributes = self._get_original_attributes()
            history = _pop_readline_history()

            if self.persistent_history_file and rl_type != RlType.NONE:
                try:
                    readline.read_history_file(self.persistent_history_file)
                except FileNotFoundError:
                    pass

            try:
                # copy over any shared attributes
                self._copy_in_shared_attrs(parent_cmd)

                if statement.args:
                    # Remove the menu argument and execute the command in the submenu
                    submenu.onecmd_plus_hooks(statement.args)
                else:
                    if self.reformat_prompt is not None:
                        prompt = submenu.prompt
                        submenu.prompt = self.reformat_prompt.format(
                            super_prompt=parent_cmd.prompt[:-1],
                            command=self.command,
                            sub_prompt=prompt,
                        )
                    submenu.cmdloop()
                    if self.reformat_prompt is not None:
                        # noinspection PyUnboundLocalVariable
                        self.submenu.prompt = prompt
            finally:
                # copy back original attributes
                self._copy_out_shared_attrs(parent_cmd, original_attributes)

                # write submenu history
                if self.persistent_history_file and rl_type != RlType.NONE:
                    readline.write_history_file(self.persistent_history_file)
                # reset main app history before exit
                _push_readline_history(history)

        @with_category(MNTHG)
        def complete_submenu(_self, text, line, begidx, endidx):
            """
            This function will be bound to complete_<submenu> and will perform the complete commands of the submenu.
            """
            submenu = self.submenu
            original_attributes = self._get_original_attributes()
            try:
                # copy over any shared attributes
                self._copy_in_shared_attrs(_self)

                # Reset the submenu's tab completion parameters
                submenu.allow_appended_space = True
                submenu.allow_closing_quote = True
                submenu.completion_header = ""
                submenu.display_matches = []
                submenu.matches_delimited = False
                submenu.matches_sorted = False

                return _complete_from_cmd(submenu, text, line, begidx, endidx)
            finally:
                # copy back original attributes
                self._copy_out_shared_attrs(_self, original_attributes)

                # Pass the submenu's tab completion parameters back up to the menu that called complete()
                _self.allow_appended_space = submenu.allow_appended_space
                _self.allow_closing_quote = submenu.allow_closing_quote
                _self.completion_header = submenu.completion_header
                _self.display_matches = copy.copy(submenu.display_matches)
                _self.matches_delimited = submenu.matches_delimited
                _self.matches_sorted = submenu.matches_sorted

        original_thg_help = cmd_obj.thg_help
        original_complete_help_command = cmd_obj.complete_help_command

        @with_category(MNTHGH)
        def help_submenu(_self, line):
            """
            This function will be bound to help_<submenu> and will call the help commands of the submenu.
            """
            tokens = line.split(None, 1)
            if tokens and (tokens[0] == self.command or tokens[0] in self.aliases):
                self.submenu.thg_help(tokens[1] if len(tokens) == 2 else "")
            else:
                original_thg_help(_self, line)

        @with_category(MNTHG)
        def _complete_submenu_help(_self, text, line, begidx, endidx):
            """autocomplete to match help_submenu()'s behavior"""
            tokens = line.split(None, 1)
            if len(tokens) == 2 and (
                not (
                    not tokens[1].startswith(self.command)
                    and not any(tokens[1].startswith(alias) for alias in self.aliases)
                )
            ):
                return self.submenu.complete_help(
                    text,
                    tokens[1],
                    begidx - line.index(tokens[1]),
                    endidx - line.index(tokens[1]),
                )
            else:
                return original_complete_help_command(_self, text, line, begidx, endidx)

        if self.create_subclass:

            class _Cmd(cmd_obj):
                thg_help = help_submenu
                complete_help = _complete_submenu_help

        else:
            _Cmd = cmd_obj
            _Cmd.thg_help = help_submenu
            _Cmd.complete_help = _complete_submenu_help

        # Create bindings in the parent command to the submenus commands.

        setattr(_Cmd, "thg_" + self.command, enter_submenu)
        setattr(_Cmd, "complete_" + self.command, complete_submenu)

        # Create additional bindings for aliases
        for _alias in self.aliases:
            setattr(_Cmd, "thg_" + _alias, enter_submenu)
            setattr(_Cmd, "complete_" + _alias, complete_submenu)
        return _Cmd


@with_category(MNTHG)
def _pop_readline_history(clear_history: bool = True) -> List[str]:
    """Returns a copy of readline's history and optionally clears it (default)"""
    # noinspection PyArgumentList
    if rl_type == RlType.NONE:
        return []

    history = [
        readline.get_history_item(i)
        for i in range(1, 1 + readline.get_current_history_length())
    ]
    if clear_history:
        readline.clear_history()
    return history


@with_category(MNTHG)
def _push_readline_history(history, clear_history=True):
    """Restores readline's history and optionally clears it first (default)"""
    if rl_type != RlType.NONE:
        if clear_history:
            readline.clear_history()
        for line in history:
            readline.add_history(line)


@with_category(MNTHG)
def _complete_from_cmd(cmd_obj, text, line, begidx, endidx):
    """Complete as though the user was typing inside cmd's cmdloop()"""
    from itertools import takewhile

    command_subcommand_params = line.split(None, 3)

    if len(command_subcommand_params) < (3 if text else 2):
        n = len(command_subcommand_params[0])
        n += sum(1 for _ in takewhile(str.isspace, line[n:]))
        return cmd_obj.completenames(text, line[n:], begidx - n, endidx - n)

    command, subcommand = command_subcommand_params[:2]
    n = len(command) + sum(1 for _ in takewhile(str.isspace, line))
    cfun = getattr(cmd_obj, "complete_" + subcommand, cmd_obj.complete)
    return cfun(text, line[n:], begidx - n, endidx - n)
