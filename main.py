"""Module for validation info about scientific staff

Takes data from input file, validates it using templates, and then uploads data to output file.
At the end of execution, show info about validation processing.
"""
import re
import json
import argparse
from pprint import pprint, pformat
from dataclasses import dataclass, asdict
from typing import Collection, List

from tqdm import tqdm

@dataclass
class Record:
    """Data class for storing info about scientific staff"""
    telephone: str
    weight: int
    inn: str
    passport_number: int
    occupation: str
    work_experience: int
    academic_degree: str
    worldview: str
    address: str