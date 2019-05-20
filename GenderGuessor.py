from gender_detector import GenderDetector
detector = GenderDetector('us') # It can also be ar, uk, uy.


count=0

### guesses gender based on firstname.good for mostly english names
with open('/Users/ankitkumar/Downloads/firstname.csv') as f:
    for line in f:
        try:
            if detector.guess(line) == 'unknown':
                print count
                count = count + 1
        except(KeyError, NameError):
            print "skip"


print count
