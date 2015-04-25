from __future__ import absolute_import

from openpyxl.compat import safe_string
from openpyxl.xml.functions import Element

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    Float,
    MinMax,
    Bool,
    Set,
    NoneSet,
    String,
    Integer,
    Alias,
)

from openpyxl.descriptors.excel import(
    Coordinate,
    Percentage,
    HexBinary,
    TextPoint,
    ExtensionList,
)
from openpyxl.descriptors.nested import (
    NestedBool,
    NestedFloat,
    NestedMinMax,
    NestedNoneSet,
)

from .layout import Layout
from .shapes import *
from .text import *
from .error_bar import *


class PictureOptions(Serialisable):

    applyToFront = Bool(allow_none=True, nested=True)
    applyToSides = Bool(allow_none=True, nested=True)
    applyToEnd = Bool(allow_none=True, nested=True)
    pictureFormat = NoneSet(values=(['stretch', 'stack', 'stackScale']), nested=True)
    pictureStackUnit = Float(allow_none=True, nested=True)

    def __init__(self,
                 applyToFront=None,
                 applyToSides=None,
                 applyToEnd=None,
                 pictureFormat=None,
                 pictureStackUnit=None,
                ):
        self.applyToFront = applyToFront
        self.applyToSides = applyToSides
        self.applyToEnd = applyToEnd
        self.pictureFormat = pictureFormat
        self.pictureStackUnit = pictureStackUnit


def _marker_symbol(tagname, value):
    """
    Override serialisation because explicit none required
    """
    return Element(tagname, val=safe_string(value))



class Marker(Serialisable):

    tagname = "marker"

    symbol = NestedNoneSet(values=(['circle', 'dash', 'diamond', 'dot', 'picture',
                              'plus', 'square', 'star', 'triangle', 'x', 'auto']),
                           to_tree=_marker_symbol)
    size = NestedMinMax(min=2, max=72, allow_none=True)
    spPr = Typed(expected_type=ShapeProperties, allow_none=True)
    ShapeProperties = Alias('sprPr')
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    __elements__ = ('symbol', 'size', 'spPr')

    def __init__(self,
                 symbol=None,
                 size=None,
                 spPr=None,
                 extLst=None,
                ):
        self.symbol = symbol
        self.size = size
        self.spPr = spPr


class DataPoint(Serialisable):

    idx = Integer(nested=True)
    invertIfNegative = Bool(allow_none=True, nested=True)
    marker = Typed(expected_type=Marker, allow_none=True)
    bubble3D = Bool(allow_none=True, nested=True)
    explosion = Integer( allow_none=True)
    spPr = Typed(expected_type=ShapeProperties, allow_none=True)
    pictureOptions = Typed(expected_type=PictureOptions, allow_none=True)
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    def __init__(self,
                 idx=None,
                 invertIfNegative=None,
                 marker=None,
                 bubble3D=None,
                 explosion=None,
                 spPr=None,
                 pictureOptions=None,
                 extLst=None,
                ):
        self.idx = idx
        self.invertIfNegative = invertIfNegative
        self.marker = marker
        self.bubble3D = bubble3D
        self.explosion = explosion
        self.spPr = spPr
        self.pictureOptions = pictureOptions
