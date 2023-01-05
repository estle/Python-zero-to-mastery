while True:
    try: 
        age = int(input('what is your age? '))
        10/age
        raise Exception('hey, cut it out!') # Throwing our own errors
    except ValueError:
        print('please enter a number!')
        break
    except ZeroDivisionError:
        print('please enter age higher than 0')
        continue
    else:
        print('thank you')
        break
    finally:
        print('ok, i\'m finally done')
# Our Job as a Programmer is to CATCH ERRORS, because Programs are IMPERFECT