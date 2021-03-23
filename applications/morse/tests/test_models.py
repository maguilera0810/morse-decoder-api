import requests
import pytest
import sys
import os
from applications.morse.models import CodigoMorse
from applications.morse.scripts.upload_codes import read_files
from familifyTest.settings import BASE_DIR
# @pytest.mark.django_db(transaction=True)
TEST_DATA = [
    (".... --- .-.. .-   -- ..- -. -.. ---", "HOLA MUNDO"),
    (".... --- .-.. .-", "HOLA"),
    ("-- ..- -. -.. ---", "MUNDO"),
    ('.-.. --- .-. ---', 'LORO'),
    ('.--. . .-. .. -.-. ---', 'PERICO'),
    ('.--. . .-. .-. ---', 'PERRO'),
    ('.- ..- -.. .- --..', 'AUDAZ'),
    ('-- .- ..- .-. .. -.-. .. ---', 'MAURICIO'),
    ('.-.. --- .-. ---   .--. . .-. .. -.-. ---   .--. . .-. .-. ---   .- ..- -.. .- --..   -- .- ..- .-. .. -.-. .. ---',
     'LORO PERICO PERRO AUDAZ MAURICIO'),
]
TEST_DATA_BINARY = [
    ('00000000110110110011100000111111001111110011111100000111011111111011101110000001100011111100000000011111100111111000001110110011111100000111111000111000001111110011001111000001111110001111110011111100000000', '.... --- .-.. .-   -- ..- -. -.. ---','HOLA MUNDO'),
    ('000000001101101100111000001111110011111100111111000001110111111110111011100000011000111111000000000', '.... --- .-.. .-','HOLA'),
    ('00000000011111100111111000001110110011111100000111111000111000001111110011001111000001111110001111110011111100000000','-- ..- -. -.. ---', 'MUNDO'),
    ('00000000011111110011111110000011100011111100000011111100111111000001100011111100000000', '-- .- -- .-','MAMA'),

]


@pytest.mark.django_db(transaction=True)
@pytest.fixture
def codes_dict():
    read_files(name_file=BASE_DIR / 'applications/morse/scripts/codes.txt')
    return CodigoMorse.get_code_dict()


@pytest.fixture
def codigo_morse_instance():
    return CodigoMorse


@pytest.mark.parametrize(
    "morse, expected",
    TEST_DATA
)
@pytest.mark.django_db(transaction=True)
def test_translate_to_human(morse, expected, codes_dict):
    assert CodigoMorse.translate2Human(morse)[0] == expected


@pytest.mark.parametrize(
    "expected, human",
    TEST_DATA
)
@pytest.mark.django_db(transaction=True)
def test_translate_to_morse(expected, human, codes_dict):
    assert CodigoMorse.translate2Morse(human)[0] == expected

@pytest.mark.parametrize(
    "binary, morse, human",
    TEST_DATA_BINARY
)
@pytest.mark.django_db(transaction=True)
def test_translate_to_morse(binary, morse, human, codes_dict):
    morse_test = CodigoMorse.decodeBits2Morse(binary)
    assert morse_test == morse
