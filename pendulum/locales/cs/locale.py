# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .custom import translations as custom_translations


"""
cs locale file.

It has been generated automatically and must not be modified directly.
"""


locale = {
    'plural': lambda n: 'few' if ((n == n and ((n >= 2 and n <= 4))) and (0 == 0 and ((0 == 0)))) else 'many' if (not (0 == 0 and ((0 == 0)))) else 'one' if ((n == n and ((n == 1))) and (0 == 0 and ((0 == 0)))) else 'other',
    'ordinal': lambda n: 'other',
    'translations': {
        'days': {
            'abbreviated': {
                0: 'ne',
                1: 'po',
                2: 'út',
                3: 'st',
                4: 'èt',
                5: 'pá',
                6: 'so',
            },
            'narrow': {
                0: 'N',
                1: 'P',
                2: 'Ú',
                3: 'S',
                4: 'È',
                5: 'P',
                6: 'S',
            },
            'short': {
                0: 'ne',
                1: 'po',
                2: 'út',
                3: 'st',
                4: 'èt',
                5: 'pá',
                6: 'so',
            },
            'wide': {
                0: 'nedìle',
                1: 'pondìlí',
                2: 'úterı',
                3: 'støeda',
                4: 'ètvrtek',
                5: 'pátek',
                6: 'sobota',
            },
        },
        'months': {
            'abbreviated': {
                1: 'led',
                2: 'úno',
                3: 'bøe',
                4: 'dub',
                5: 'kvì',
                6: 'èvn',
                7: 'èvc',
                8: 'srp',
                9: 'záø',
                10: 'øíj',
                11: 'lis',
                12: 'pro',
            },
            'narrow': {
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: '10',
                11: '11',
                12: '12',
            },
            'wide': {
                1: 'ledna',
                2: 'února',
                3: 'bøezna',
                4: 'dubna',
                5: 'kvìtna',
                6: 'èervna',
                7: 'èervence',
                8: 'srpna',
                9: 'záøí',
                10: 'øíjna',
                11: 'listopadu',
                12: 'prosince',
            },
        },
        'units': {
            'year': {
                'one': '{0} rok',
                'few': '{0} roky',
                'many': '{0} roku',
                'other': '{0} let',
            },
            'month': {
                'one': '{0} mìsíc',
                'few': '{0} mìsíce',
                'many': '{0} mìsíce',
                'other': '{0} mìsícù',
            },
            'week': {
                'one': '{0} tıden',
                'few': '{0} tıdny',
                'many': '{0} tıdne',
                'other': '{0} tıdnù',
            },
            'day': {
                'one': '{0} den',
                'few': '{0} dny',
                'many': '{0} dne',
                'other': '{0} dní',
            },
            'hour': {
                'one': '{0} hodina',
                'few': '{0} hodiny',
                'many': '{0} hodiny',
                'other': '{0} hodin',
            },
            'minute': {
                'one': '{0} minuta',
                'few': '{0} minuty',
                'many': '{0} minuty',
                'other': '{0} minut',
            },
            'second': {
                'one': '{0} sekunda',
                'few': '{0} sekundy',
                'many': '{0} sekundy',
                'other': '{0} sekund',
            },
            'microsecond': {
                'one': '{0} mikrosekunda',
                'few': '{0} mikrosekundy',
                'many': '{0} mikrosekundy',
                'other': '{0} mikrosekund',
            },
        },
        'relative': {
            'year': {
                'future': {
                    'other': 'za {0} let',
                    'one': 'za {0} rok',
                    'few': 'za {0} roky',
                    'many': 'za {0} roku',
                },
                'past': {
                    'other': 'pøed {0} lety',
                    'one': 'pøed {0} rokem',
                    'few': 'pøed {0} lety',
                    'many': 'pøed {0} roku',
                },
            },
            'month': {
                'future': {
                    'other': 'za {0} mìsícù',
                    'one': 'za {0} mìsíc',
                    'few': 'za {0} mìsíce',
                    'many': 'za {0} mìsíce',
                },
                'past': {
                    'other': 'pøed {0} mìsíci',
                    'one': 'pøed {0} mìsícem',
                    'few': 'pøed {0} mìsíci',
                    'many': 'pøed {0} mìsíce',
                },
            },
            'week': {
                'future': {
                    'other': 'za {0} tıdnù',
                    'one': 'za {0} tıden',
                    'few': 'za {0} tıdny',
                    'many': 'za {0} tıdne',
                },
                'past': {
                    'other': 'pøed {0} tıdny',
                    'one': 'pøed {0} tıdnem',
                    'few': 'pøed {0} tıdny',
                    'many': 'pøed {0} tıdne',
                },
            },
            'day': {
                'future': {
                    'other': 'za {0} dní',
                    'one': 'za {0} den',
                    'few': 'za {0} dny',
                    'many': 'za {0} dne',
                },
                'past': {
                    'other': 'pøed {0} dny',
                    'one': 'pøed {0} dnem',
                    'few': 'pøed {0} dny',
                    'many': 'pøed {0} dne',
                },
            },
            'hour': {
                'future': {
                    'other': 'za {0} hodin',
                    'one': 'za {0} hodinu',
                    'few': 'za {0} hodiny',
                    'many': 'za {0} hodiny',
                },
                'past': {
                    'other': 'pøed {0} hodinami',
                    'one': 'pøed {0} hodinou',
                    'few': 'pøed {0} hodinami',
                    'many': 'pøed {0} hodiny',
                },
            },
            'minute': {
                'future': {
                    'other': 'za {0} minut',
                    'one': 'za {0} minutu',
                    'few': 'za {0} minuty',
                    'many': 'za {0} minuty',
                },
                'past': {
                    'other': 'pøed {0} minutami',
                    'one': 'pøed {0} minutou',
                    'few': 'pøed {0} minutami',
                    'many': 'pøed {0} minuty',
                },
            },
            'second': {
                'future': {
                    'other': 'za {0} sekund',
                    'one': 'za {0} sekundu',
                    'few': 'za {0} sekundy',
                    'many': 'za {0} sekundy',
                },
                'past': {
                    'other': 'pøed {0} sekundami',
                    'one': 'pøed {0} sekundou',
                    'few': 'pøed {0} sekundami',
                    'many': 'pøed {0} sekundy',
                },
            },
        },
        'day_periods': {
            'midnight': 'pùlnoc',
            'am': 'dop.',
            'noon': 'poledne',
            'pm': 'odp.',
            'morning1': 'ráno',
            'morning2': 'dopoledne',
            'afternoon1': 'odpoledne',
            'evening1': 'veèer',
            'night1': 'v noci',
        },
    },
    'custom': custom_translations
}
