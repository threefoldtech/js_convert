import os

from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Name, Leaf, syms
from lib2to3.pgen2 import token

from config_info import check_camel_case, action_camel_case
from config_info import (camel_case_fn_list, exclude_camel_case_fn_list,
                         camel_case_log)

from util import camel, to_snake_case, strip_back_to_jumpscale_or_digitalme

for sname in dir(syms):
    print (sname, getattr(syms, sname))

def get_container_classname(node):
    while node:
        if node.type == syms.classdef:
            return node.children[1].value
        node = node.parent

class FixCamelcasecallers(BaseFix):

    _accept_type = token.NAME

    def transform(self, node, results):
        #print ("results transform", results)
        #print ("transform", repr(str(node)))
        fixnode = results
        newname = to_snake_case(str(node))
        fixnode.replace(Name(newname, prefix=fixnode.prefix))

    def match(self, node):
        if not isinstance(node, Leaf):
            return False
        if not camel(node.value): # already converted, ignore
            return False
        classname = get_container_classname(node)
        #print ("parentkls", node.parent.type, repr(node), node.parent, npp)
        if self.filename.endswith("__init__.py"):
            modname = os.path.dirname(self.filename)
            modname = os.path.split(modname)[0]
        else:
            modname = os.path.basename(self.filename)
            modname = os.path.splitext(modname)[0]
        fname = strip_back_to_jumpscale_or_digitalme(self.filename)
        lineno = node.get_lineno()
        k = (str(fname), lineno, str(modname),)
        if k in camel_case_log:
            ccl = camel_case_log[k]
            print ("to action", node.value, node.type, k, "\n\t", ccl)
            if node.value != ccl[2]: # match function name
                return False
        else:
            #print ("not found", classname, node.value, node.type, k)
            return False

        return node
