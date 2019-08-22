import numsimword

myclass = numsimword.NumsimWord()
myclass.max_digit = 3
for ii in range(1000):
    print(myclass.get_digit_word(ii))
