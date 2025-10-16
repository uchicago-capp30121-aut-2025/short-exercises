import sys
import os
import csv
import json
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())
BASE_DIR = os.path.dirname(__file__)
TEST_DIR = os.path.join(BASE_DIR, "tests")

import se3
import test_helpers
import helpers

MODULE = "se3"
voters = test_helpers.read_CSV_file("tests/new_voter_registrations.csv")

### Helper
def read_config_file(filename):
    '''
    Load the test cases from a JSON file.

    Inputs:
      filename (string): the name of the test configuration file.

    Returns: (list) test cases
    '''

    full_path = os.path.join(TEST_DIR, filename)
    return test_helpers.read_JSON_file(full_path)

@pytest.mark.parametrize("list_of_words, expected", 
                         [
                             (["hello", "bye"], {"hello": 5, "bye": 3}),
                             (["hello", "bye", "hi", "a"], {"hello": 5, 
                                                            "bye": 3, "hi": 2, 
                                                            "a": 1}),
                             (["what"], {"what": 4}),
                             ([],{})
                         ])
def test_word_length(list_of_words, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "word_length", [], *(list_of_words,))

    try:
        actual = se3.word_length(list_of_words)
    except Exception as e: #pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_dict(actual,expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("list_of_words, expected",
                        [  
                            (["hello"], {"h": 1}),
                            (["hello", "bye"], {"h": 1, "b": 1}),
                            (["hello", "bye", "hi", "a"], {"h": 2, "b": 1, 
                                                           "a": 1}),
                            (["hello", "bye", "hi", "a", "hannah", "hi", "blue",
                               "what", "ape"], {"h": 4, "b": 2, "a": 2, 
                                                "w": 1}),
                            ([], {})
                        ])
def test_words_start_with(list_of_words, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "word_start_with", [], *(list_of_words,))

    try:
        actual = se3.words_start_with(list_of_words)
    except Exception as e: #pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("registered_voters, target, expected",
                         [
                            (voters, 200000, [('California', '2020', 'Feb')]),
                            (voters, 150000, [('California', '2016', 'Mar'),
                                              ('California', '2016', 'Apr'),
                                              ('California', '2020', 'Jan'),
                                              ('California', '2020', 'Feb'),
                                              ('California', '2020', 'Mar'),
                                              ('Texas', '2016', 'Mar')]),
                            (voters, 100000, [('California', '2016', 'Feb'),
                                              ('California', '2016', 'Mar'),
                                              ('California', '2016', 'Apr'),
                                              ('California', '2020', 'Jan'),
                                              ('California', '2020', 'Feb'),
                                              ('California', '2020', 'Mar'),
                                              ('Florida', '2020', 'Feb'),
                                              ('North Carolina', '2020', 'Jan'),
                                              ('Texas', '2016', 'Jan'),
                                              ('Texas', '2016', 'Feb'),
                                              ('Texas', '2016', 'Mar'),
                                              ('Texas', '2016', 'Apr'),
                                              ('Texas', '2020', 'Jan'),
                                              ('Texas', '2020', 'Feb'),
                                              ('Texas', '2020', 'Mar')])

                         ])
def test_num_of_new_voters(registered_voters, target, expected):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  voters = test_helpers.read_CSV_file('tests/new_voter_registrations)\n"
    recreate_msg += "  se3.num_of_new_voters(voters, {})".format(target)

    try:
        actual = se3.num_of_new_voters(registered_voters, target)
    except Exception as e: #pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("registered_voters, month_and_year, expected",
                        [
                            (voters, ('Jan', '2020'), {'Arizona': '33229',
                                                      'California': '151595',
                                                      'Colorado': '20260',
                                                      'Delaware': '3276',
                                                      'District of Columbia': '3334',
                                                      'Florida': '77466',
                                                      'Georgia': '38573',
                                                      'Illinois': '44443',
                                                      'Maryland': '21532',
                                                      'North Carolina': '111990',
                                                      'Texas': '134559',
                                                      'Virginia': '25934'}),
                            (voters, ('Jan', '2016'), {'Arizona': '25852',
                                                      'California': '87574',
                                                      'Colorado': '17024',
                                                      'Delaware': '3007',
                                                      'District of Columbia': '2840',
                                                      'Florida': '50231',
                                                      'Georgia': '34952',
                                                      'Illinois': '44040',
                                                      'Maryland': '19580',
                                                      'North Carolina': '35213',
                                                      'Texas': '132860',
                                                      'Virginia': '20032'}),
                            (voters, ('Feb', '2016'), {'Arizona': '51155',
                                                      'California': '103377',
                                                      'Colorado': '20707',
                                                      'Delaware': '3629',
                                                      'District of Columbia': '2954',
                                                      'Florida': '87351',
                                                      'Georgia': '40976',
                                                      'Illinois': '99674',
                                                      'Maryland': '29122',
                                                      'North Carolina': '84357',
                                                      'Texas': '143795',
                                                      'Virginia': '36911'})
                        ])
def test_total_registered_voters(registered_voters, month_and_year, expected):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  voters = test_helpers.read_CSV_file('tests/new_voter_registrations)\n"
    recreate_msg += "  se3.total_registered_voters(voters, {})".format(month_and_year)

    try:
        actual = se3.total_registered_voters(registered_voters, month_and_year)
    except Exception as e: #pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("registered_voters, month_and_year, expected",
                        [
                            (voters, ('Jan', '2016'), {'Arizona': '25852',
                                                      'California': '87574',
                                                      'Colorado': '17024',
                                                      'Delaware': '3007',
                                                      'District of Columbia': '2840',
                                                      'Florida': '50231',
                                                      'Georgia': '34952',
                                                      'Illinois': '44040',
                                                      'Maryland': '19580',
                                                      'North Carolina': '35213',
                                                      'Texas': '132860',
                                                      'Virginia': '20032'}),
                            (voters, ('Feb', '2016'), {'Arizona': '51155',
                                                      'California': '103377',
                                                      'Colorado': '20707',
                                                      'Delaware': '3629',
                                                      'District of Columbia': '2954',
                                                      'Florida': '87351',
                                                      'Georgia': '40976',
                                                      'Illinois': '99674',
                                                      'Maryland': '29122',
                                                      'North Carolina': '84357',
                                                      'Texas': '143795',
                                                      'Virginia': '36911'}),
                            (voters, ('Mar', '2016'), {'Arizona': '48614',
                                                      'California': '174278',
                                                      'Colorado': '25627',
                                                      'Delaware': '5124',
                                                      'District of Columbia': '4706',
                                                      'Florida': '73627',
                                                      'Georgia': '44150',
                                                      'Illinois': '52782',
                                                      'Maryland': '40497',
                                                      'North Carolina': '58272',
                                                      'Texas': '170607',
                                                      'Virginia': '44171'})
                        ])
def test_total_registered_voters(registered_voters, month_and_year, expected):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  voters = test_helpers.read_CSV_file('tests/new_voter_registrations)\n"
    recreate_msg += "  se3.total_registered_voters(voters, {})".format(month_and_year)

    try:
        actual = se3.total_registered_voters(registered_voters, month_and_year)
    except Exception as e: #pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("registered_voters, year, expected",
                        [
                            (voters, '2016', {'Jan': ['25852','87574','17024','3007','2840','50231','34952','44040','19580','35213','132860','20032'],
                                              'Feb': ['51155','103377','20707','3629','2954','87351','40976','99674','29122','84357','143795','36911'],
                                              'Mar': ['48614','174278','25627','5124','4706','73627','44150','52782','40497','58272','170607','44171'],
                                              'Apr': ['30668','185478','22204','3818','4157','52508','37028','76098','26655','73341','143199','20460'],
                                              'May': ['5714', '5828', '29374', '91205', '26239']}),
                            (voters, '2020', {'Jan': ['33229','151595','20260','3276','3334','77466','38573','44443','21532','111990','134559','25934'],
                                              'Feb': ['50853','238281','33374','3353','3348','109859','55386','68455','20708','54053','130080','29507'],
                                              'Mar': ['31872','176810','18990','2535','2225','54872','26284','47899','23864','54807','129424','31492'],
                                              'Apr': ['10249','38970','6034','589','1281','21031','15484','21332','10061','35484','34694','5467'],
                                              'May': ['1925', '23488', '23517', '35678', '8239']})
                        ])
def test_new_voters_by_month(registered_voters, year, expected):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  voters = test_helpers.read_CSV_file('tests/new_voter_registrations)\n"
    recreate_msg += "  se3.new_voters_by_month(voters, {})".format(year)

    try:
        actual = se3.new_voters_by_month(registered_voters, year)
    except Exception as e: #pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
