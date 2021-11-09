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
                2: '�t',
                3: 'st',
                4: '�t',
                5: 'p�',
                6: 'so',
            },
            'narrow': {
                0: 'N',
                1: 'P',
                2: '�',
                3: 'S',
                4: '�',
                5: 'P',
                6: 'S',
            },
            'short': {
                0: 'ne',
                1: 'po',
                2: '�t',
                3: 'st',
                4: '�t',
                5: 'p�',
                6: 'so',
            },
            'wide': {
                0: 'ned�le',
                1: 'pond�l�',
                2: '�ter�',
                3: 'st�eda',
                4: '�tvrtek',
                5: 'p�tek',
                6: 'sobota',
            },
        },
        'months': {
            'abbreviated': {
                1: 'led',
                2: '�no',
                3: 'b�e',
                4: 'dub',
                5: 'kv�',
                6: '�vn',
                7: '�vc',
                8: 'srp',
                9: 'z��',
                10: '��j',
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
                2: '�nora',
                3: 'b�ezna',
                4: 'dubna',
                5: 'kv�tna',
                6: '�ervna',
                7: '�ervence',
                8: 'srpna',
                9: 'z���',
                10: '��jna',
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
                'one': '{0} m�s�c',
                'few': '{0} m�s�ce',
                'many': '{0} m�s�ce',
                'other': '{0} m�s�c�',
            },
            'week': {
                'one': '{0} t�den',
                'few': '{0} t�dny',
                'many': '{0} t�dne',
                'other': '{0} t�dn�',
            },
            'day': {
                'one': '{0} den',
                'few': '{0} dny',
                'many': '{0} dne',
                'other': '{0} dn�',
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
                    'other': 'p�ed {0} lety',
                    'one': 'p�ed {0} rokem',
                    'few': 'p�ed {0} lety',
                    'many': 'p�ed {0} roku',
                },
            },
            'month': {
                'future': {
                    'other': 'za {0} m�s�c�',
                    'one': 'za {0} m�s�c',
                    'few': 'za {0} m�s�ce',
                    'many': 'za {0} m�s�ce',
                },
                'past': {
                    'other': 'p�ed {0} m�s�ci',
                    'one': 'p�ed {0} m�s�cem',
                    'few': 'p�ed {0} m�s�ci',
                    'many': 'p�ed {0} m�s�ce',
                },
            },
            'week': {
                'future': {
                    'other': 'za {0} t�dn�',
                    'one': 'za {0} t�den',
                    'few': 'za {0} t�dny',
                    'many': 'za {0} t�dne',
                },
                'past': {
                    'other': 'p�ed {0} t�dny',
                    'one': 'p�ed {0} t�dnem',
                    'few': 'p�ed {0} t�dny',
                    'many': 'p�ed {0} t�dne',
                },
            },
            'day': {
                'future': {
                    'other': 'za {0} dn�',
                    'one': 'za {0} den',
                    'few': 'za {0} dny',
                    'many': 'za {0} dne',
                },
                'past': {
                    'other': 'p�ed {0} dny',
                    'one': 'p�ed {0} dnem',
                    'few': 'p�ed {0} dny',
                    'many': 'p�ed {0} dne',
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
                    'other': 'p�ed {0} hodinami',
                    'one': 'p�ed {0} hodinou',
                    'few': 'p�ed {0} hodinami',
                    'many': 'p�ed {0} hodiny',
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
                    'other': 'p�ed {0} minutami',
                    'one': 'p�ed {0} minutou',
                    'few': 'p�ed {0} minutami',
                    'many': 'p�ed {0} minuty',
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
                    'other': 'p�ed {0} sekundami',
                    'one': 'p�ed {0} sekundou',
                    'few': 'p�ed {0} sekundami',
                    'many': 'p�ed {0} sekundy',
                },
            },
        },
        'day_periods': {
            'midnight': 'p�lnoc',
            'am': 'dop.',
            'noon': 'poledne',
            'pm': 'odp.',
            'morning1': 'r�no',
            'morning2': 'dopoledne',
            'afternoon1': 'odpoledne',
            'evening1': 've�er',
            'night1': 'v noci',
        },
    },
    'custom': custom_translations
}
