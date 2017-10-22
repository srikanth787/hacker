if __name__ == '__main__':
  n = int(raw_input())
  if n < 1 or n > 100:
    print "n should be between 1 and 100"
  else:
    if n % 2 == 1:
      print "weird"
    else:
      if n in range(2,6):
         print "not weird"
      if n in range(6,21):
         print "weird"
      if n > 20:
        print "not weird"


