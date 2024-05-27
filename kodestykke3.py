def mySqrt(number, guess, step, tol):
    # We need to take out negative numbers...
    if number < 0:
        print('Error - we do not work with complex numbers here...')
        return float("NaN")

    # If we set guess to zero, we have to provide a number - we assume this is the initial call
    if guess == 0:
        if number > 1:  # If we have numbers larger than one, we can safely guess half as the sqrt
            guess = 0.5 * number
        else:
            guess = number * 2  # If we have numbers smaller than one, we need to double our guess

    tmp = guess * guess  # Now compute the square of our guess

    if abs(tmp - number) < tol:  # Check if the (guess^2 - number) is lower than our tolerance level
        return guess
    else:
        if tmp > number:  # If our guess was too high, then iterate by calling ourselves again with a slightly lower guess
            return mySqrt(number, (1 - step) * guess, step, tol)
        else:  # Else, our guess was too small, we need to increase the guess for our next call
            return mySqrt(number, (1 + step) * guess, step, tol)


# White test:
# -1 0 0 0 --> NaN
#  2 0 0 0 --> 1 RecursionError: maximum recursion depth exceeded in comparison
#  0.5 0 0 0 --> RecursionError: maximum recursion depth exceeded in comparison
#  2 0 0.1 0.01 --> 1.4132563827500702
#  0.5 0 0.1 0.01 --> 0.6561000000000001
#  2 0 0.01 0.1 --> 1.3886900853164088
#  0.5 0 0.01 0.1 --> 0.7700431458051551


# black test. Focus on the first values where the others are fixed (x, 0, 0.01, 0.1)
# False --> 0
# True --> 1.0406810453006128
# None --> TypeError: '<' not supported between instances of 'NoneType' and 'int'
# A --> TypeError: '<' not supported between instances of 'str' and 'int'
# 1.321 --> 1.108113532626275
# [3,1,1,5] TypeError: '>' not supported between instances of 'list' and 'int'
# {"a": 1, "b": 2} TypeError: '>' not supported between instances of 'dict' and 'int'

# Focus on the second value where the others are fixed (4, x, 0.01, 0.1)
# True --> 1.9868944241538475
# False --> 2.0
# None --> TypeError: '<' not supported between instances of 'NoneType' and 'int'
# A --> TypeError: '<' not supported between instances of 'str' and 'int'
# 1.321 --> 1.9864568819907409
# [3,1,1,5] TypeError: '>' not supported between instances of 'list' and 'int'
# {"a": 1, "b": 2} TypeError: '>' not supported between instances of 'dict' and 'int'

# Focus on the third value where the others are fixed (8, 0, x, 0.1)
# True --> RecursionError: maximum recursion depth exceeded in comparison
# False --> RecursionError: maximum recursion depth exceeded in comparison
# None --> TypeError: '<' not supported between instances of 'NoneType' and 'int'
# A --> TypeError: '<' not supported between instances of 'str' and 'int'
# 1.321 --> -2.831321872010049
# [3,1,1,5] TypeError: '>' not supported between instances of 'list' and 'int'
# {"a": 1, "b": 2} TypeError: '>' not supported between instances of 'dict' and 'int'

# Focus on the third value where the others are fixed (8, 0, 0.01, x)
# True --> 2.9886883773263846
# False --> RecursionError: maximum recursion depth exceeded in comparison
# None --> TypeError: '<' not supported between instances of 'NoneType' and 'int'
# A --> TypeError: '<' not supported between instances of 'str' and 'int'
# 1.321 --> 3.049370857388414
# [3,1,1,5] TypeError: '>' not supported between instances of 'list' and 'int'
# {"a": 1, "b": 2} TypeError: '>' not supported between instances of 'dict' and 'int'

testVal = 1.321


print('Squareroot of ' + str(testVal) + ' is ')
print(mySqrt(8, 0, 0.01, testVal))


def mySqrt(number, guess, step, tol):
    # We need to take out negative numbers...
    if number < 0:
        print('Error - we do not work with complex numbers here...')
        return float("NaN")

    # If we set guess to zero, we have to provide a number - we assume this is the initial call
    if guess == 0:
        if number < 1:  # If we have numbers larger than one, we can safely guess half as the sqrt
            guess = 0.5 * number
        else:
            guess = number * 2  # If we have numbers smaller than one, we need to double our guess

    tmp = guess * guess  # Now compute the square of our guess
    if (tmp - number) > tol:  # Check if the (guess^2 - number) is lower than our tolerance level
        return guess
    else:
        if tmp > number:  # If our guess was too high, then iterate by calling ourselves again with a slightly lower guess
            return mySqrt(number, (1 + step) * guess, step, tol)
        else:  # Else, our guess was too small, we need to increase the guess for our next call
            return mySqrt(number, (1 - step) * guess, step, tol)