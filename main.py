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

    @staticmethod
    def validation_telephone(telephone: str) -> bool:
        """Validates telephone number

         Checks telephone number
         for following pattern "+7-(111)-222-33-44".

        Args:
            telephone: string contains checking number of telephone
        Returns:
            bool result of validation
        """
        pattern = r"^\+\d-\(\d{3}\)-\d{3}-\d{2}-\d{2}$"
        try:
            return True if re.match(pattern, telephone) else False
        except TypeError:
            return False

    @staticmethod
    def validation_weight(weight: int) -> bool:
        """Validates weight

         Checks weights for realness.
         Adult can't weight more than 610 kilo and less than 30 kilo.

        Args:
            weight: integer weight of human
        Returns:
            bool result of validation
        """
        try:
            return 30 < weight < 610
        except TypeError:
            return False

    @staticmethod
    def validation_inn(inn: str) -> bool:
        """Validates inn

         Checks inn for following format.
         It can contains only 12 numbers.

        Args:
            inn: string contains inn(tax identification number)
        Returns:
            bool result of validation
        """
        pattern = r"^\d{12}$"
        try:
            return True if re.match(pattern, inn) else False
        except TypeError:
            return False

    @staticmethod
    def validation_passport_number(passport_number: int) -> bool:
        """Validates passport number.

         Checks passport number for following format.
         It can contains only 6 numbers.

        Args:
            passport_number: integer passport number
        Returns:
            bool result of validation
        """
        pattern = r"^\d{6}$"
        try:
            return True if re.match(pattern, str(passport_number)) else False
        except TypeError:
            return False

    @staticmethod
    def validation_text_properties(text_properties: str) -> bool:
        """Validates text properties.

         Checks text properties for
         not containing special symbol and numbers

        Args:
            text_properties: string properties
        Returns:
            bool result of validation
        """
        pattern = r"^[^\d.,?]{2,}$"
        try:
            return True if re.match(pattern, str(text_properties)) else False
        except TypeError:
            return False

    @staticmethod
    def validation_work_experience(number_of_years: int) -> bool:
        """Validates work experience.

         Checks work experience for realness.
         Work experience can't be more than 99 years and less than 0 years.

        Args:
            number_of_years: integer number of years of work experience
        Returns:
            bool result of validation
        """
        try:
            return 0 < number_of_years < 99
        except TypeError:
            return False

    @staticmethod
    def validation_address(address: str) -> bool:
        """Validates address.

         Checks address
         for following pattern ""(улица) (номер дома)"".

        Args:
            address: string contains checking address
        Returns:
            bool result of validation
        """
        pattern = r"^[А-Яа-я.,\-0-9()\s]{2,}[\s]?\d+$"
        try:
            return True if re.match(pattern, str(address)) else False
        except TypeError:
            return False