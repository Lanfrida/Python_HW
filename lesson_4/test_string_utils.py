import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
         ("skypro", "Skypro"),           
         ("", ""),                       
         ("Skypro", "Skypro"),           
         ("a", "A"),                     
         ("123", "123"),                 
         ("test string", "Test string"), 
     ])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
         (" skypro", "skypro"),           
         ("", ""),                       
         ("Skypro", "Skypro"),           
         ("a ", "a "),                     
         ("12 3", "12 3"),                 
         ("   test string", "test string"), 
     ])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, simbol, expected", [
         ("skypro", "s", True),           
         ("", "", True),                       
         ("Skypro", "Y", False),           
         ("Skypro", "A", False),                     
         ("123", "123", True),                 
         ("test string", " ", True), 
     ])
def test_contains(input_str, simbol, expected):
    assert utils.contains(input_str, simbol) == expected


@pytest.mark.parametrize("input_str, simbol, expected", [
         ("skypro", "s", "kypro"),           
         ("", "", ""),                     
         ("Skypro", "Y", "Skypro"),           
         ("Skypro", "A", "Skypro"),                     
         ("123", "123", ""),                 
         ("test string", " ", "teststring"), 
     ])
def delete_symbol(input_str, simbol, expected):
    assert utils.delete_symbol(input_str, simbol) == expected