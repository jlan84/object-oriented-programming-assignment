#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapes import Circle, Rectangle
from operators import UnionShape, IntersectionShape, DiffShape
from collections import OrderedDict

class ShapeScriptParser():
    """A parser for a scripting language
    that would generate shapes (as objects defined in shapes.py)
    and display the result on screen (using SimpleGUI).

    Parameters
    ----------
    gui : {SimpleGUI} a gui object for drawing pixels.

    Attributes
    ----------
    TBD
    """
    def __init__(self, gui):
        """instanciates a shape factory, gui is provided for future drawing"""
        pass

    def parse(self, filename):
        """parses a file line by line"""
        pass

    def parse_line(self, string):
        """parses one string (one line), and creates the corresponding object"""
        pass

    def draw(self):
        """draws objects that have been created previously with parse()"""
        pass
