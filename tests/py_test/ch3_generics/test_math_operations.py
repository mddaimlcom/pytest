import pytest

pytestmark = [pytest.mark.donotrun] # module level marker

# test defined as functions
@pytest.mark.addition
def test1():
    assert eval('1+1') == 2

@pytest.mark.addition
@pytest.mark.negative
def test2():
    assert eval('-1+1') != 1


@pytest.mark.substraction
def test3():
    assert eval('8-1') == 7


@pytest.mark.substraction
@pytest.mark.negative
def test4():
    assert eval('-8-1') == -9


@pytest.mark.division
def test5():
    assert eval('9/3') == 3


@pytest.mark.division
@pytest.mark.negative
def test6():
    assert eval('10/-2') == -5


# tests as class methods encapsulated into the class. Methods automatically inherit the markers set at the class level
@pytest.mark.multiplication
class TestMultiplication:

    def test7(self):
        assert eval('3*2') == 6

    @pytest.mark.negative
    def test8(self):
        assert eval('-2*6') == -12

    @pytest.mark.negative
    def test9(self):
        assert eval('-5*-2') == 10


## uncomment this to have the test logic separated from the test data
test_data = [
    {'description': 'Two positive numbers when added return a positive outcome', 'operation': '1+1', 'expected': 2},
    {'description': 'If subtract a bigger number out of a smaller one, we get a negative outcome', 'operation': '1-2', 'expected': -1},
    {'description': 'Divide 2 positive numbers', 'operation': '9/3', 'expected': 3},
    {'description': "Multiply two positive numbers", 'operation': '9*2', 'expected': 18},

]

@pytest.mark.data_driven
@pytest.mark.parametrize(argnames=['operation', 'expected'],
                         argvalues=[(i['operation'], i['expected']) for i in test_data],
                         ids=[i['description'] for i in test_data])
def test_generic_eval(operation, expected):
    assert eval(operation) == expected
