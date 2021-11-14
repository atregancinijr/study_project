#Userful function to performs a modulus division "%" of two numbers, then return both quotient and remainder
# quocient, remaider = divmod(x,y)
import datetime
import time
if __name__ == '__main__':
    start = datetime.datetime.now()
    # insert here ANY FUNCTION in order to calculate it's process time
    time.sleep(3)
    #
    end = datetime.datetime.now()

    seconds_runtime = (end - start).seconds

    hour, remainder = divmod(seconds_runtime, 3600)
    mins, secs = divmod(remainder, 60)

    print(f'{hour:02d}:{mins:02d}:{secs:02d}')