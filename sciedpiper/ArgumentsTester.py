# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


"""
Tests the arguments module.
"""


__author__ = "Timothy Tickle"
__copyright__ = "Copyright 2016"
__credits__ = ["Timothy Tickle", "Brian Haas"]
__license__ = "MIT"
__maintainer__ = "Timothy Tickle"
__email__ = "ttickle@broadinstitute.org"
__status__ = "Development"


import argparse
import Arguments
import ParentPipelineTester
import unittest


class ArgumentsTester(ParentPipelineTester.ParentPipelineTester):
    """
    Tests the Argument object.
    """

    str_help = "".join(["--help: {u'default': '==SUPPRESS==', ",
                        "u'var_name': 'help', ",
                        "u'type': u\"<type 'bool'>\", ",
                        "u'option_strings': ['-h', '--help'], ",
                        "u'choices': None}"])
    str_empty_positionals = "".join(["__positional_arguments__: ",
                                     "{u'var_name': [], ",
                                     "u'type': u\"<type 'list'>\", ",
                                     "u'option_strings': [], ",
                                     "u'choices': []"])

    ########################
    # func_extract_arguments
    ########################
    def test_func_extract_arguments_for_one_string_flag(self):
        """ Testing extract_arguments for one string flag. """
        prsr_arguments = argparse.ArgumentParser(prog="test_func_extract_arguments_for_one_string_flag",
                                                 description="Custom Script",
                                                 conflict_handler="resolve",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        prsr_arguments.add_argument("-b",
                                    dest="str_one",
                                    default=None)
        str_answer = Arguments.Arguments.func_extract_argument_info(prsr_arguments)
        str_result = "".join(["{",
                              self.str_help,
                              ", ",
                              "-b: {u'default': None, ",
                              "u'var_name': u'str_one', ",
                              "u'type': u\"<type 'str'>\", ",
                              "u'option_strings': [u'-b'], ",
                              "u'choices': None}",
                              ", ",
                              self.str_empty_positionals,
                              "}}"])
        self.func_test_equals(str_result, self.func_dict_to_string(str_answer))

    def test_func_extract_arguments_for_one_string_flag_default(self):
        """ Testing extract_arguments for one string flag checking the default. """
        prsr_arguments = argparse.ArgumentParser(prog="test_func_extract_arguments_for_one_string_flag",
                                                 description="Custom Script",
                                                 conflict_handler="resolve",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        prsr_arguments.add_argument("-b",
                                    dest="str_one",
                                    default="DEFAULT")
        str_answer = Arguments.Arguments.func_extract_argument_info(prsr_arguments)
        str_result = "".join(["{",
                              self.str_help,
                              ", ",
                              "-b: {u'default': u'DEFAULT', ",
                              "u'var_name': u'str_one', ",
                              "u'type': u\"<type 'str'>\", ",
                              "u'option_strings': [u'-b'], ",
                              "u'choices': None}",
                              ", ",
                              self.str_empty_positionals,
                              "}}"])
        self.func_test_equals(str_result, self.func_dict_to_string(str_answer))

    def test_func_extract_arguments_for_one_positional(self):
        """ Testing extract_arguments for one positional argument. """
        prsr_arguments = argparse.ArgumentParser(prog="test_func_extract_arguments_for_one_positional",
                                                 description="Custom Script",
                                                 conflict_handler="resolve",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        prsr_arguments.add_argument(dest="str_one")
        str_answer = Arguments.Arguments.func_extract_argument_info(prsr_arguments)
        str_result = "".join(["{",
                              self.str_help,
                              ", ",
                              "__positional_arguments__: ",
                              "{u'var_name': [u'str_one'], ",
                              "u'type': u\"<type 'list'>\", ",
                              "u'option_strings': [], ",
                              "u'choices': []",
                              "}}"])
        self.func_test_equals(str_result, self.func_dict_to_string(str_answer))

    def test_func_extract_arguments_for_three_positional(self):
        """ Testing extract_arguments for three positional argument. """
        prsr_arguments = argparse.ArgumentParser(prog="test_func_extract_arguments_for_three_positional",
                                                 description="Custom Script",
                                                 conflict_handler="resolve",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        prsr_arguments.add_argument(dest="str_a")
        prsr_arguments.add_argument(dest="str_b")
        prsr_arguments.add_argument(dest="str_c")
        str_answer = Arguments.Arguments.func_extract_argument_info(prsr_arguments)
        str_result = "".join(["{",
                              self.str_help,
                              ", ",
                              "__positional_arguments__: ",
                              "{u'var_name': [u'str_a', u'str_b', u'str_c'], ",
                              "u'type': u\"<type 'list'>\", ",
                              "u'option_strings': [], ",
                              "u'choices': []",
                              "}}"])
        self.func_test_equals(str_result, self.func_dict_to_string(str_answer))

    def test_func_extract_arguments_for_one_positional_one_flag(self):
        """ Testing extract_arguments for one positional and one flag argument. """
        prsr_arguments = argparse.ArgumentParser(prog="test_func_extract_arguments_for_one_positional_one_flag",
                                                 description="Custom Script",
                                                 conflict_handler="resolve",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        prsr_arguments.add_argument(dest="str_one")
        prsr_arguments.add_argument("-b",
                                    dest="str_one",
                                    default="DEFAULT")
        str_answer = Arguments.Arguments.func_extract_argument_info(prsr_arguments)
        str_result = "".join(["{",
                              self.str_help,
                              ", ",
                              "-b: {u'default': u'DEFAULT', ",
                              "u'var_name': u'str_one', ",
                              "u'type': u\"<type 'str'>\", ",
                              "u'option_strings': [u'-b'], ",
                              "u'choices': None}",
                              ", ",
                              "__positional_arguments__: ",
                              "{u'var_name': [u'str_one'], ",
                              "u'type': u\"<type 'list'>\", ",
                              "u'option_strings': [], ",
                              "u'choices': []",
                              "}}"])
        self.func_test_equals(str_result, self.func_dict_to_string(str_answer))

    def test_func_extract_arguments_for_many_types(self):
        """ Testing extract_arguments for flags of many types and features. """
        prsr_arguments = argparse.ArgumentParser(prog="test_func_extract_arguments_for_many_types",
                                                 description="Custom Script",
                                                 conflict_handler="resolve",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        # str
        prsr_arguments.add_argument("-b",
                                    dest="str_one",
                                    default=None)
        # str default
        prsr_arguments.add_argument("-c",
                                    dest="str_two",
                                    default="test")
        # int
        prsr_arguments.add_argument("-i",
                                    dest="int_one",
                                    type=int,
                                    default=8)
        # boolean true
        prsr_arguments.add_argument("-a",
                                    dest="f_one",
                                    default=True,
                                    action="store_false")
        # boolean false
        prsr_arguments.add_argument("-f",
                                    dest="f_two",
                                    default=False,
                                    action="store_true")
        # list
        prsr_arguments.add_argument("-d",
                                    dest="list_one",
                                    default=[],
                                    nargs="*")
        # str choices
        prsr_arguments.add_argument("-e",
                                    dest="str_choices",
                                    default=None,
                                    choices=["one", "two", "three"])
        str_answer = Arguments.Arguments.func_extract_argument_info(prsr_arguments)
        str_result = "".join(["{",
                              self.str_help,
                              ", ",
                              "-a: {u'default': True, ",
                              "u'var_name': u'f_one', ",
                              "u'type': u\"<type 'bool'>\", ",
                              "u'option_strings': [u'-a'], ",
                              "u'choices': None}, ",
                              "-b: {u'default': None, ",
                              "u'var_name': u'str_one', ",
                              "u'type': u\"<type 'str'>\", ",
                              "u'option_strings': [u'-b'], ",
                              "u'choices': None}, ",
                              "-c: {u'default': u'test', ",
                              "u'var_name': u'str_two', ",
                              "u'type': u\"<type 'str'>\", ",
                              "u'option_strings': [u'-c'], ",
                              "u'choices': None}, ",
                              "-d: {u'default': [], ",
                              "u'var_name': u'list_one', ",
                              "u'type': u\"<type 'list'>\", ",
                              "u'option_strings': [u'-d'], ",
                              "u'choices': None}, ",
                              "-e: {u'default': None, ",
                              "u'var_name': u'str_choices', ",
                              "u'type': u\"<type 'str'>\", ",
                              "u'option_strings': [u'-e'], ",
                              "u'choices': [u'one', u'two', u'three']}, ",
                              "-f: {u'default': False, ",
                              "u'var_name': u'f_two', ",
                              "u'type': u\"<type 'bool'>\", ",
                              "u'option_strings': [u'-f'], ",
                              "u'choices': None}, ",
                              "-i: {u'default': 8, ",
                              "u'var_name': u'int_one', ",
                              "u'type': <type 'int'>, ",
                              "u'option_strings': [u'-i'], ",
                              "u'choices': None}",
                              ", ",
                              self.str_empty_positionals,
                              "}}"])
        self.func_test_equals(str_result, self.func_dict_to_string(str_answer))


#Creates a suite of tests
def suite():
    """ Suite aggregates tests and is used to run tests. """
    return unittest.TestLoader().loadTestsFromTestCase(ArgumentsTester)
