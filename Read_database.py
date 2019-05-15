import numpy as np
import pandas as pd
import os
from enum import Enum


class XMLTagsUpperLevel:

    """
    This class defines the XML tag constants at the higher levels of XML
    tree. The tag <record> us found below the tag <page> in the tree
    hierarchy.
    """

    PAGE = "page"
    RECORD = "record"


class XMLTagsLowerLevel:
    """
    This class defines all the XML tag constants that are one level below
    the <record> tag. This is defined as an enumerated type for ease of
    iterating oevr all tags
    """
