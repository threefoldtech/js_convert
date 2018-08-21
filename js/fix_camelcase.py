from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Name
from lib2to3.pgen2 import token

class FixCamelcase(BaseFix):

    PATTERN = "fixnode='oldname'"
    _accept_type = token.NAME

    def transform(self, node, results):
        print (results)
        print (node, dir(node))
        fixnode = results
        fixnode.replace(Name('newname', prefix=fixnode.prefix))

    def match(self, node):
        return False
        if node.value == 'oldname':
            return node
        #if isinstance(node, Leaf):
        return False

