while True:
    try: 
        age = int(input('what is your age? '))
        10/age
        3/aged
    except ValueError:
        print('please enter a number!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    except:
        print('error was caught')
    else:
        print('thank you')
        break