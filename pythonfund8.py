import random
random_num = random.random()
# the random function will return a floating point number,
# that is 0.0 <= random_num < 1.0
times = 0
counter = 0
result_rounded = 0
headsCount = 0
tailsCount = 0

def tossCoin():
	times = input('Hit enter to toss a virtual coin 5000 times, or enter the number of time you want to toss. -->')
	for i in range (int(times)):
		tossing()
		# for i in range (5001):
		# tossing()
	print "All done thank you for playing!"

def tossing():
  for i in range (2):
  counter = counter + 1
  result_rounded = round(random_num)
  if result_rounded == 1:
      headsCount = headsCount +1
      result = "head"
  if result_rounded == 0:
      tailsCount = tailsCount +1
      result = "tail"
  print "Attempt #", times, ": Throwing a Coin... It's a ", result , "! ... Got ", headsCount , " heads(s) so far and ", tailsCount , " tail(s) so far..."

tossing()
