class NumsimWord:

    def __init__(self, max_digit=2, 
                       max_bit=10,
                       meta_info='num'):

        self.max_digit = max_digit
        self.max_bit   = max_bit
        self.meta_info = meta_info
   

    def get_max_number(self):
        return pow(self.max_bit, self.max_digit)


    def get_sim_word(self, number):
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
                result = '%s%sto%s ' % (self.meta_info, digit, iter) + result
            else:
                result = '%s%sto%s ' % (self.meta_info, digit, iter + 1) + result

        return result

