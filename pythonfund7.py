import random
# the random function will return a floating point number,
# that is 0.0 <= random_num < 1.0

def tossCoin():
  times = raw_input("Enter the number of time you want to toss a coin. --> ")
  tossing(times)
  print "All done thank you for playing!"

def tossing(times):
    headsCount = 0
    tailsCount = 0
    counter = 0
    random_num = 0
    result_rounded = 0
    for i in range (int(times)):
        counter = counter + 1
        random_num = random.random()
        result_rounded = round(random_num)
        if result_rounded == 1:
            headsCount = headsCount +1
            result = "head"
        if result_rounded == 0:
            tailsCount = tailsCount +1
            result = "tail"
        print "Attempt #", counter, ": Thowing a Coin... It's a ", result , "! ... Got ", headsCount , " heads(s) so far and ", tailsCount , " tail(s) so far..."
tossCoin()
