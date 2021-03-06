# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`{{full_name}} <{{email}}>`
'''

# Import Python Libs
from __future__ import absolute_import, unicode_literals, print_function

# Import Salt Testing Libs
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.unit import TestCase, skipIf
from tests.support.mock import (
    patch,
    NO_MOCK,
    NO_MOCK_REASON
)
import salt.states.{{module_name}} as {{module_name}}



@skipIf(NO_MOCK, NO_MOCK_REASON)
class {{module_name|capitalize}}TestCase(TestCase, LoaderModuleMockMixin):

    def setup_loader_modules(self):
        return {% raw -%} {
            {% endraw -%} {{module_name}} {%- raw -%}: {
                '__env__': 'base'
            }
        } {%- endraw %}

    def test_behaviour(self):
        #  Test inherent behaviours
        pass
