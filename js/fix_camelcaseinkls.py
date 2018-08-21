from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Name, Leaf, syms
from lib2to3.pgen2 import token

for sname in dir(syms):
    print (sname, getattr(syms, sname))


def camel(s):
    return s != s.lower() and s != s.upper() and "_" not in s

def to_snake_case(not_snake_case):
    final = ''
    for i in range(len(not_snake_case)):
        item = not_snake_case[i]
        if i < len(not_snake_case) - 1:
            next_char_will_be_underscored = (not_snake_case[i+1] == "_"  \
                    or not_snake_case[i+1] == " " \
                    or not_snake_case[i+1].isupper())
        if (item == " " or item == "_") and next_char_will_be_underscored:
            continue
        elif (item == " " or item == "_"):
            final += "_"
        elif item.isupper():
            final += "_"+item.lower()
        else:
            final += item
    if final[0] == "_":
        final = final[1:]
    return final


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
        print ("parentkls", node.parent.type, repr(node), node.parent, npp)
        print ("parentparent", type(npp), npp.type)
        if npp.type == syms.classdef:
            print ("suite")
            print ("children", npp.parent.children)
        if not npp.type == syms.classdef:
            return False
        if camel(node.value):
            return node
        return False
