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

    class Validator:
        """Class for providing validation of Record's instance"""

        def __init__(self, records: Collection[Record]):
            """Initialization instance of Validator

            Args:
                records: list of instance of class Records
            """
            self.records = records
            self.processing_log = {
                'number_valid_records': 0,
                'number_invalid_records': 0,
                'invalid_telephone': 0,
                'invalid_weight': 0,
                'invalid_inn': 0,
                'invalid_passport_number': 0,
                'invalid_occupation': 0,
                'invalid_work_experience': 0,
                'invalid_academic_degree': 0,
                'invalid_worldview': 0,
                'invalid_address': 0,
            }

            def processing(self) -> List[Record]:
                """Validates record

                Returns:
                    list of valid records
                """
                valid_records = []
                for record in tqdm(self.records):
                    self.processing_log['number_invalid_records'] += 1

                    if not self.validation_telephone(record.telephone):
                        self.processing_log['invalid_telephone'] += 1
                    elif not self.validation_weight(record.weight):
                        self.processing_log['invalid_weight'] += 1
                    elif not self.validation_inn(record.inn):
                        self.processing_log['invalid_inn'] += 1
                    elif not self.validation_passport_number(record.passport_number):
                        self.processing_log['invalid_passport_number'] += 1
                    elif not self.validation_text_properties(record.occupation):
                        self.processing_log['invalid_occupation'] += 1
                    elif not self.validation_work_experience(record.work_experience):
                        self.processing_log['invalid_work_experience'] += 1
                    elif not self.validation_text_properties(record.academic_degree):
                        self.processing_log['invalid_academic_degree'] += 1
                    elif not self.validation_text_properties(record.worldview):
                        self.processing_log['invalid_worldview'] += 1
                    elif not self.validation_address(record.address):
                        self.processing_log['invalid_address'] += 1
                    else:
                        self.processing_log['number_invalid_records'] -= 1
                        self.processing_log['number_valid_records'] += 1
                        valid_records.append(record)

                return valid_records
