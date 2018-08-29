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


class FixCamelcaseinkls(BaseFix):

    _accept_type = token.NAME

    def transform(self, node, results):
        print (results)
        print (node, dir(node))
        fixnode = results
        newname = to_snake_case(str(node))
        fixnode.replace(Name(newname, prefix=fixnode.prefix))

    def match(self, node):
        npp = node.parent.parent.parent
        if npp is None:
            return False
        if node.parent.type != syms.funcdef: # only fix function names
            return False
        #print ("parentkls", node.parent.type, repr(node), node.parent, npp)
        #print ("parentparent", type(npp), npp.type)
        if npp.type == syms.classdef:
            #print ("classdef", dir(npp))
            #print ("children", npp.children)
            classname = npp.children[1].value
        if not npp.type == syms.classdef:
            return False
        s = node.value
        if not camel(s):
            # exclude some outliers
            if s.startswith("__") and s.endswith("__"):
                return False
            if "_" not in s:
                return False
            if s.startswith("_") and "_" not in s[1:] and not camel(s[1:]):
                print ("skip ", s)
                return False
            if check_camel_case:
                if self.filename.endswith("__init__.py"):
                    modname = os.path.dirname(self.filename)
                    modname = os.path.split(modname)[0]
                else:
                    modname = os.path.basename(self.filename)
                    modname = os.path.splitext(modname)[0]
                fn_name = "%s.%s.%s" % (modname, classname, node.value)
                if fn_name not in camel_case_fn_list:
                    camel_case_fn_list.append(fn_name)
            if not action_camel_case:
                return False
            # actioning to be done
            return node
        return False
