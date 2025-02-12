# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#
# for item in self.partree.childs[0].opts['children']:
#    print item
#print self.partree.getValues()
#print self.partree.param('Basic', 'Oil').value()
#self.partree.param('Basic', 'Oil').setValue(15)

#self.ui.widget_parTree.mb_read(self.mb, 03, 0, 1)


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType


# test subclassing parameters
# This parameter automatically generates two child parameters which are always reciprocals of each other
class ComplexParameter(pTypes.GroupParameter):
    def __init__(self, **opts):
        opts['type'] = 'bool'
        opts['value'] = True
        pTypes.GroupParameter.__init__(self, **opts)

        self.addChild({'name': 'A = 1/B', 'type': 'float',
                       'value': 7, 'suffix': 'Hz', 'siPrefix': True})
        self.addChild({'name': 'B = 1/A', 'type': 'float',
                       'value': 1/7., 'suffix': 's', 'siPrefix': True})
        self.a = self.param('A = 1/B')
        self.b = self.param('B = 1/A')
        self.a.sigValueChanged.connect(self.aChanged)
        self.b.sigValueChanged.connect(self.bChanged)

    def aChanged(self):
        self.b.setValue(1.0 / self.a.value(), blockSignal=self.bChanged)

    def bChanged(self):
        self.a.setValue(1.0 / self.b.value(), blockSignal=self.aChanged)


# test add/remove
# this group includes a menu allowing the user to add new parameters into its child list
class ScalableGroup(pTypes.GroupParameter):
    def __init__(self, **opts):
        opts['type'] = 'group'
        opts['addText'] = "Add"
        opts['addList'] = ['str', 'float', 'int']
        pTypes.GroupParameter.__init__(self, **opts)

    def addNew(self, typ):
        val = {
            'str': '',
            'float': 0.0,
            'int': 0
        }[typ]
        self.addChild(dict(name="ScalableParam %d" % (
            len(self.childs)+1), type=typ, value=val, removable=True, renamable=True))


params = [
    {'name': 'Basic parameter data types', 'type': 'group', 'children': [
        {'name': 'Integer', 'type': 'int', 'value': 10},
        {'name': 'Float', 'type': 'float', 'value': 10.5, 'step': 0.1},
        {'name': 'String', 'type': 'str', 'value': "hi"},
        {'name': 'List', 'type': 'list', 'values': [1, 2, 3], 'value': 2},
        {'name': 'Named List', 'type': 'list', 'values': {
            "one": 1, "two": "twosies", "three": [3, 3, 3]}, 'value': 2},
        {'name': 'Boolean', 'type': 'bool',
            'value': True, 'tip': "This is a checkbox"},
        {'name': 'Color', 'type': 'color', 'value': "FF0",
            'tip': "This is a color button"},
        {'name': 'Gradient', 'type': 'colormap'},
        {'name': 'Subgroup', 'type': 'group', 'children': [
            {'name': 'Sub-param 1', 'type': 'int', 'value': 10},
            {'name': 'Sub-param 2', 'type': 'float', 'value': 1.2e6},
        ]},
        {'name': 'Text Parameter', 'type': 'text', 'value': 'Some text...'},
        {'name': 'Action Parameter', 'type': 'action'},
    ]},
    {'name': 'Numerical Parameter Options', 'type': 'group', 'children': [
        {'name': 'Units + SI prefix', 'type': 'float', 'value': 1.2e-6,
            'step': 1e-6, 'siPrefix': True, 'suffix': 'V'},
        {'name': 'Limits (min=7;max=15)', 'type': 'int',
         'value': 11, 'limits': (7, 15), 'default': -6},
        {'name': 'DEC stepping', 'type': 'float', 'value': 1.2e6,
            'dec': True, 'step': 1, 'siPrefix': True, 'suffix': 'Hz'},

    ]},
    {'name': 'Save/Restore functionality', 'type': 'group', 'children': [
        {'name': 'Save State', 'type': 'action'},
        {'name': 'Restore State', 'type': 'action', 'children': [
            {'name': 'Add missing items', 'type': 'bool', 'value': True},
            {'name': 'Remove extra items', 'type': 'bool', 'value': True},
        ]},
    ]},
    {'name': 'Extra Parameter Options', 'type': 'group', 'children': [
        {'name': 'Read-only', 'type': 'float', 'value': 1.2e6,
            'siPrefix': True, 'suffix': 'Hz', 'readonly': True},
        {'name': 'Renamable', 'type': 'float', 'value': 1.2e6,
            'siPrefix': True, 'suffix': 'Hz', 'renamable': True},
        {'name': 'Removable', 'type': 'float', 'value': 1.2e6,
            'siPrefix': True, 'suffix': 'Hz', 'removable': True},
    ]},
    ComplexParameter(name='Custom parameter group (reciprocal values)'),
    ScalableGroup(name="Expandable Parameter Group", children=[
        {'name': 'ScalableParam 1', 'type': 'str', 'value': "default param 1"},
        {'name': 'ScalableParam 2', 'type': 'str', 'value': "default param 2"},
    ]),
]

parinit = [
    {'name': 'Basic', 'type': 'group', 'children': [
    ]},
]


class ParTreeWrapper(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # Create tree of Parameter objects
        self.partree = Parameter.create(
            name='params', type='group', children=parinit)

        # self.partree.sigTreeStateChanged.connect(self.change)
        # Too lazy for recursion:
        # for child in self.partree.children():
        #    child.sigValueChanging.connect(self.valueChanging)
        #    for ch2 in child.children():
        #        ch2.sigValueChanging.connect(self.valueChanging)

        self.t = ParameterTree()
        self.t.setParameters(self.partree, showTop=False)
        # layout
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.t)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def LoadPar(self, pars):
        self.partree = Parameter.create(
            name='params', type='group', children=pars)
        # self.partree.sigTreeStateChanged.connect(self.change)
        # Too lazy for recursion:
        # for child in self.partree.children():
        #    child.sigValueChanging.connect(self.valueChanging)
        #    for ch2 in child.children():
        #        ch2.sigValueChanging.connect(self.valueChanging)
        self.t.setParameters(self.partree, showTop=False)

    # If anything changes in the tree, print a message
    def change(self, param, changes):
        print("tree changes:")
        for param, change, data in changes:
            path = self.partree.childPath(param)
            if path is not None:
                childName = '.'.join(path)
            else:
                childName = param.name()
            print('  parameter: %s' % childName)
            print('  change:    %s' % change)
            print('  data:      %s' % str(data))
            print('  ----------')

    def valueChanging(self, param, value):
        print("Value changing (not finalized): %s %s" % (param, value))

    # def mb_read(self, mb, Func, Start, Length):
    #    return mb.read(Func, Start, Length)

    # def mb_write(self, mb, Func, Start, val):
    #    return mb.write(Func, Start, val)

    def setVal(self, basic, child, value):
        self.partree.param(basic, child).setValue(value)
