import numpy as np
from data_processing.database import Card, CardDatabase

def unit_test(func, input_args : tuple, expected_output : tuple, title : str | None = None) -> None:
    """ Conduct unit test on a function and compare given input and output

    Args:
        func(function object): The function waiting to be tested
        input_args(tuple): A tuple containing all input arguments of the function
        expected_output(tuple): A tuple of the desired output of the function
        title(str): The title to be displayed for unit test
                    default is None, which does not print
    """
    if title is not None: print(title)
    expected_output_list = [expected_output]
    print(f'Name: {func.__name__}')
    print(f'Input:')
    print(input_args)
    print(f'Expected output:')
    print(*expected_output_list)
    try:
        if isinstance(input_args,str) or (np.array(input_args).size == 1) or isinstance(input_args,np.ndarray):
            actual_output = [func(input_args)]
        else:
            actual_output = [func(*input_args)]
    except Exception as e:
        print(f'Exception raised\n{type(e).__name__}: {e}')
        try:
            assert expected_output == None
            print('PASSED')
        except AssertionError:
            print('FAILED')
    else:
        print(f'Actual output:')
        print(*actual_output, end='')
        try:
            assert np.array_equal(actual_output, expected_output_list)
            print('\nPASSED')
        except AssertionError as e:
            print('\nFAILED')
            # print(e)
    print()

def sample_func() -> CardDatabase:
    return CardDatabase()

if __name__=='__main__':
    unit_test(sample_func, (), (CardDatabase()))
    unit_test()