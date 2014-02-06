# -*- coding: utf-8 -*-

from docutils import nodes
from sphinx import addnodes
from sphinx.errors import SphinxWarning
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType, Index
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.roles import XRefRole

class IEEE829Document(Directive):
    """
    Base class of IEEE829 document directives.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 1
    
    option_spec = {
        'title': lambda x: x
    }

    doctype = None
    
    final_argument_whitespace = False

    def run(self):
        env = self.state.document.settings.env
        ident = self.arguments[0].strip()
        title = self.doctype.upper() + '-' + ident
        if 'title' in self.options:
            title += ' ' + self.options['title']
        if ident in env.domaindata['ieee829'][self.doctype.lower()]:
            (docname, existing_title) = env.domaindata['ieee829'][self.doctype.lower()][ident]
            raise SphinxWarning("`{0}-{1}' was already declared in `{2}': `{3}'\t({4}:{5})".format(self.doctype.upper(), ident, docname, existing_title, env.docname, self.lineno))
        env.temp_data['ieee829:ltp'] = ident
        env.domaindata['ieee829'][self.doctype.lower()][ident] = (env.docname, title)
        idx = addnodes.index()
        idx['entries'] = [('single', title, '', '')]
        t = nodes.title(text=title)
        t.line = self.lineno
        t.append(idx)
        sec = nodes.section('', t, ids=[self.get_ids_string(ident)])
        return [sec]
        
    def get_ids_string(self, ident):
        return self.doctype.lower() + '-' + ident

class MasterTestPlan(IEEE829Document):
    """
    Directive for master test plan.
    """
    doctype = 'MTP'

class LevelTestPlan(IEEE829Document):
    """
    Directive for level test plan.
    """
    doctype = 'LTP'

class LevelTestDesign(IEEE829Document):
    """
    Directive for level test design.
    """
    doctype = 'LTD'


class LevelTestCase(IEEE829Document):
    """
    Directive for level test case.
    """
    doctype = 'LTC'

class LevelTestProcedure(IEEE829Document):
    """
    Directive for level test plan.
    """
    doctype = 'LTPR'

class LevelTestLog(IEEE829Document):
    """
    Directive for level test log.
    """
    doctype = 'LTL'

class AnomalyReport(IEEE829Document):
    """
    Directive for anomaly report.
    """
    doctype = 'AR'
    
class LevelInterimTestStatusReport(IEEE829Document):
    """
    Directive for level interim test status report.
    """
    doctype = 'LITSR'
    
class LevelTestReport(IEEE829Document):
    """
    Directive for level test report.
    """
    doctype = 'LTR'

class MasterTestReport(IEEE829Document):
    """
    Directive for master test report.
    """
    doctype = 'MTR'

class IEEE829DocumentIndex(Index):
    """
    Index subclass to provide the document index.
    """

    name = 'modindex'
    localname = l_('Index of Testing Documents')
    shortname = None

    def generate(self, docnames=None):
        # list of prefixes to ignore
        ignores = self.domain.env.config['modindex_common_prefix']
        ignores = sorted(ignores, key=len, reverse=True)
        contents = {}
        documents = dict((k, v) for k, v in self.domain.data.items() if type(v) == dict and len(v) > 0)
        for doctype in documents:
            for ident, pair in documents[doctype].items():
                docname, title = pair
                if not docnames or (docnames and docname in docnames):
                    letter = doctype.upper()
                    if not letter in contents:
                        contents[letter] = []
                    contents[letter].append( [title, 0, docname, doctype.lower() + '-' + ident, '', '', ''])
        return list(contents.items()), False

        
class IEEE829Domain(Domain):
    """IEEE829 testing documentation domain."""
    name = 'ieee829'
    label = 'IEEE829'

    object_types = {
        'mtp':  ObjType(l_('mtp'),  'dir'),
        'ltp':  ObjType(l_('ltp'),  'dir'),
        'ltd':  ObjType(l_('ltd'),  'dir'),
        'ltc':  ObjType(l_('ltc'),  'dir'),
        'ltpr': ObjType(l_('ltpr'), 'dir'),
        'ltl':  ObjType(l_('ltl'),  'dir'),
        'ar':   ObjType(l_('ar'),   'dir'),
        'litsr':   ObjType(l_('litsr'),   'dir'),
        'ltr':  ObjType(l_('ltr'),  'dir'),
        'mtr':  ObjType(l_('mtr'),  'dir'),
    }
    
    directives = {
        'mtp':  MasterTestPlan,
        'ltp':  LevelTestPlan,
        'ltd':  LevelTestDesign,
        'ltc':  LevelTestCase,
        'ltpr': LevelTestProcedure,
        'ltl':  LevelTestLog,
        'ar':   AnomalyReport,
        'litsr': LevelInterimTestStatusReport,
        'ltr':  LevelTestReport,
        'mtr':  MasterTestReport
    }
    
    roles = {
        'mtp':  XRefRole(),
        'ltp':  XRefRole(),
        'ltd':  XRefRole(),
        'ltc':  XRefRole(),
        'ltpr': XRefRole(),
        'ltl':  XRefRole(),
        'ar':   XRefRole(),
        'litsr': XRefRole(),
        'ltr':  XRefRole(),
        'mtr':  XRefRole(),
        'ref': XRefRole(),
    }
    
    initial_data = {
        'mtp': {},
        'ltp': {},
        'ltd': {},
        'ltc': {},
        'ltpr': {},
        'ltl': {},
        'ar': {},
        'litsr': {},
        'ltr': {},
        'mtr': {},
    }
    
    indices = [IEEE829DocumentIndex]
    
    def clear_doc(self, docname):
        for doctype in self.directives.keys():
            for ident, fn in self.data[doctype.lower()].items():
                if fn == docname:
                    del self.data[doctype.lower()][ident]
    
    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        if typ in self.directives.keys():
            docname, title = self.data[typ].get(target)
            return make_refnode(builder, fromdocname, docname, typ.lower() + '-' + target, nodes.title_reference(text=typ.upper() + '-' + target), title)
        else:
            return None
    
    def get_objects(self):
        for doctype in self.directives.keys():
            for ident, (docname, title) in self.data[doctype].items():
                yield (ident, doctype.upper() + '-' + ident, doctype.lower(), docname, doctype.lower() + '-' + ident, 0)
                
def setup(app):
    app.add_domain(IEEE829Domain)
