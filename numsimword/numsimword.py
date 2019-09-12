class NumsimWord:

    def __init__(self):

        self.max_digit = 2
        self.max_bit   = 10
        self.meta_info1 = 'bit'
        self.meta_info2 = 'digit'
   

    def get_max_linear_number(self):
        return pow(self.max_bit, self.max_digit)


    def get_linear_word(self, number):
        result = '' 

        counters = [0]*self.max_digit
        counters[0] = number

        for ii in range(1, self.max_digit):
            count = number // (self.max_bit*ii)
            if count == 0:
                break

            counters[ii] = count

        for ii, count in enumerate(counters):
            result = self.get_bits(count, ii) + result

        return result


    def get_bits(self, count, digit):
        result = ''

        iter  = count // self.max_bit

        for ii in range(self.max_bit):
            if ii > (count % self.max_bit):
                result = '%s%sto%s ' % (self.meta_info1, digit, iter) + result
            else:
                result = '%s%sto%s ' % (self.meta_info1, digit, iter + 1) + result

        return result


    def get_digit_word(self, num):
        result = '' 
    
        num_str = str(int(num))
        n_digits = len(num_str)

        pre_bit = ''
        for ii in range(self.max_digit):

            if ii >= self.max_digit:
                break

            if ii >= n_digits:
                bit = '0'
            else:
                bit = num_str[ii]

            if pre_bit:
                bit = pre_bit + 'to' + bit

            result += '%s%sto%s %s%sto%s ' % (self.meta_info2, n_digits, n_digits-ii,
                                              self.meta_info1, n_digits, bit) 

            pre_bit = bit 
        
        return result
