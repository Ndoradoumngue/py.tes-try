import pytest

# function to turn a string to upper case

def capitalize_string(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
        return x.capitalize()

# test capitalize string function

def test_raise_exception_for_non_string_inputs():
    with pytest.raises(TypeError):
        capitalize_string(9)

# writing fixtures


@pytest.fixture
def first_try(request):
    projector = {'status': 'doing fine', 'flashing': "dicts can't flash!"}
    def fin():
        projector['status'] = 'torn down by finalizer!'
    request.addfinalizer(fin)
    return projector

def test_nothing(first_try):
    assert first_try['status'] == 'doing fine'

# testing test skip

@pytest.mark.skip(True, reason='successfuly skiped')
def test_skipped_function():
    print ('This test has been skipped')

@pytest.mark.skip(True, reason='successfuly skiped')
def test_not_skipped_function():
    print ('This test cannot be skipped')

























