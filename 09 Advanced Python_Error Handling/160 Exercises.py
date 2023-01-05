while True:
    try: 
        age = int(input('what is your age? '))
        10/age
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
    print('will i run?')
# that's the difference between FINALLY and after "try: {}" commands!