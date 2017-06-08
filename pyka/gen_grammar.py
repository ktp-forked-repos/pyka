#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class KaleidoscopeBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=';.*?$',
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(KaleidoscopeBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class KaleidoscopeParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=';.*?$',
        ignorecase=None,
        left_recursion=True,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=KaleidoscopeBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(KaleidoscopeParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @tatsumasu()
    def _toplevel_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._extern_()
                with self._option():
                    self._definition_()
                with self._option():
                    self._expr_()
                self._error('no available options')
        self.name_last_node('@')
        self._check_eof()

    @tatsumasu()
    def _extern_(self):  # noqa
        self._token('extern')
        self._prototype_()
        self.name_last_node('@')

    @tatsumasu()
    def _definition_(self):  # noqa
        self._token('def')
        self._prototype_()
        self.add_last_node_to_name('@')
        self._expr_()
        self.add_last_node_to_name('@')

    @tatsumasu()
    def _prototype_(self):  # noqa
        self._symbol_()
        self.add_last_node_to_name('@')
        self._token('(')
        self._param_list_()
        self.add_last_node_to_name('@')
        self._token(')')

    @tatsumasu()
    def _param_list_(self):  # noqa

        def sep0():
            self._token(',')

        def block0():
            self._symbol_()
        self._gather(block0, sep0)

    @tatsumasu()
    def _expr_(self):  # noqa
        self._arith_()

    @tatsumasu()
    def _arith_(self):  # noqa
        self._term_()

        def block0():
            with self._group():
                with self._choice():
                    with self._option():
                        self._token('+')
                    with self._option():
                        self._token('-')
                    self._error('no available options')
            self._term_()
        self._closure(block0)

    @tatsumasu()
    def _term_(self):  # noqa
        self._factor_()

        def block0():
            with self._group():
                with self._choice():
                    with self._option():
                        self._token('*')
                    with self._option():
                        self._token('/')
                    self._error('no available options')
            self._factor_()
        self._closure(block0)

    @tatsumasu()
    def _factor_(self):  # noqa
        self._atom_expr_()

    @tatsumasu()
    def _atom_expr_(self):  # noqa
        self._trailer_expr_()

    @tatsumasu()
    def _trailer_expr_(self):  # noqa
        self._atom_()

        def block0():
            self._trailer_()
        self._closure(block0)

    @tatsumasu()
    def _trailer_(self):  # noqa
        self._token('(')
        self._arg_list_()
        self._token(')')

    @tatsumasu()
    def _arg_list_(self):  # noqa

        def sep0():
            self._token(',')

        def block0():
            self._expr_()
        self._gather(block0, sep0)

    @tatsumasu()
    def _atom_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('(')
                self._expr_()
                self.name_last_node('@')
                self._token(')')
            with self._option():
                self._symbol_()
            with self._option():
                self._number_()
            self._error('no available options')

    @tatsumasu()
    def _symbol_(self):  # noqa
        self._pattern(r'[a-zA-Z_][a-zA-Z0-9_]*')

    @tatsumasu()
    def _number_(self):  # noqa
        self._pattern(r'[0-9]*([0-9]\.|\.[0-9]|[0-9])[0-9]*([eE][+-]?[0-9]+)?')


class KaleidoscopeSemantics(object):
    def toplevel(self, ast):  # noqa
        return ast

    def extern(self, ast):  # noqa
        return ast

    def definition(self, ast):  # noqa
        return ast

    def prototype(self, ast):  # noqa
        return ast

    def param_list(self, ast):  # noqa
        return ast

    def expr(self, ast):  # noqa
        return ast

    def arith(self, ast):  # noqa
        return ast

    def term(self, ast):  # noqa
        return ast

    def factor(self, ast):  # noqa
        return ast

    def atom_expr(self, ast):  # noqa
        return ast

    def trailer_expr(self, ast):  # noqa
        return ast

    def trailer(self, ast):  # noqa
        return ast

    def arg_list(self, ast):  # noqa
        return ast

    def atom(self, ast):  # noqa
        return ast

    def symbol(self, ast):  # noqa
        return ast

    def number(self, ast):  # noqa
        return ast


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = KaleidoscopeParser()
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, KaleidoscopeParser, name='Kaleidoscope')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()