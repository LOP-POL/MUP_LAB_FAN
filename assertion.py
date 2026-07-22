import numpy as np


def assert_density(rho):
    if 1.0 < rho < 1.4:
        print(f'The density of air seems to be correct: {rho:f} kg/m^3. Well done!')
    else:
        print(f'The density seems to be wrong: {rho:f} kg/m^3! What do you expect for the density of air?')

        
        
def assert_mmWC_to_Pa(func):
    try:
        user_res = func(10.5, density=1000.0, gravity=9.81)
    except Exception as e:
        print(f'Your function could not be called. Check for errors. Here is the orig. Error message: {e}')
        return
    if round(user_res, 3) != 103.005:
        print('The function does not give the expected result. Your computation seems to be wrong. Please check again')
    else:
        print('Your implementation gives correct results. Well done.')