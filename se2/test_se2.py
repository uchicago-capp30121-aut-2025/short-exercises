import sys
import os
import copy

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se2
import pytest
import helpers

MODULE = "se2"

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 8, 7, True),
        (5, 8, 7, True),
        (5, 21, 19, True),
        (3, 9, 7, False),
        (4, 8, 7, False),
        (3, 8, 6, False),
    ]
)
def test_eisenstein_triple(a, b, c, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "eisenstein_triple", *(a, b, c))
    try:
        actual = se2.eisenstein_triple(a, b, c)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_type(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([-1, 0], -1),
        ([0, -1], -1),
        ([0, -1, -3], -1),
        ([0, 1, -3, 2], -3),
        ([0, 1, 3, 2, 4, -5], -5),
        ([0, 1, 3, 2, 4, 5], 0),
        ([], 0),
        ([-1], -1)
    ]
)
def test_first_negative_param(lst, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "first_negative", *(lst,))

    orig = lst[:]
    try:
        actual = se2.first_negative(lst)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_type(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))
    err_msgs.append(helpers.check_list_unmodified("lst", orig, lst))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)



@pytest.mark.parametrize(
    "lst, lb, ub, expected",
    [
        ([], 0, 2, []),
        ([1], 0, 2, [1]),
        ([0, 1, 2], 0, 2, [0, 1, 2]),
        ([1, 4, 4, 3, -3], -2, 5, [1, 4, 4, 3, -2]),
        ([-1, 9, 0, 3, 3, 7], -2, 5, [-1, 5, 0, 3, 3, 5]),
        ([0, -1, 2, 4, -5, 7, 1], 0, 2, [0, 0, 2, 2, 0, 2, 1]),
    ]
)
def test_clip_in_range_param(lst, lb, ub, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "clip_in_range", *(lst, lb, ub))

    lst_copy = lst[:]
    try:
        actual = se2.clip_in_range(lst_copy, lb, ub)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, None))
    err_msgs.append(helpers.check_equals(lst_copy, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 1, [0, 1]),
        (1, 2, [1, 2]),
        (0, 2, [0, 1, 2]),
        (0, 6, [0, 1, 2, 3, 4, 5, 6]),
        (4, 9, [4, 5, 6, 7, 8, 9]),
        (12, 25, [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),
    ]
)
def test_expand_param(a, b, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "expand", *(a, b))
    try:
        actual = se2.expand(a, b)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_type(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize(
    "lst_of_lsts, expected",
    [
        ([[1], [2], [3]], True),
        ([[1, 1], [2, 2], [3, 3]], True),
        ([[], []], True),
        ([[1, 1], [2, 2], [3]], False),
        ([[1, 1], [2, 2, 2, 3], [3, 3]], False),
        ([[1, 1, 1], [2, 2], [3, 3]], False),
        ([[1, 1], [2, 2], [3, 3], [4]], False),
    ]
)
def test_same_length_param(lst_of_lsts, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "same_length", *(lst_of_lsts,))

    orig = copy.deepcopy(lst_of_lsts)
    try:
        actual = se2.same_length(lst_of_lsts)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_type(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))
    err_msgs.append(helpers.check_list_unmodified("lst_of_lsts", orig, lst_of_lsts))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)