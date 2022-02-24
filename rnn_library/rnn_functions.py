from numpy import tanh, sign, add, where

def ask_user_integer():
    while True:
        try:
            result = int(input())
        except:
            print("\tThe entry is not an integer. Please try again!")
            continue
        else:
            print('\tEntry accepted')
            return result

def ask_user_float():
    while True:
        try:
            result = float(input())
        except:
            print("\tThe entry is not a number. Please try again!")
            continue
        else:
            print('\tEntry accepted')
            return result
        

def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

def half_max_x(x, y):
    half = max(y)/2.0
    signs = sign(add(y, -half))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = where(zero_crossings)[0]
    return [lin_interp(x, y, zero_crossings_i[0], half)]

    
def FWHM_funct(time_list , autocorrelation, start = 0, end = -1):
    try:
        hmx = half_max_x(time_list[start:end], autocorrelation[start:end])
        return hmx[0] 

    except IndexError:
        print('The ACF did not drop to its half height.')
        print('Consider Increasing the length of your simulation.')
       
