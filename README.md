numsimword
====

In Machine Learning algorithms to analyze text similarity, such as Doc2Vec, different number words generally show randome similarity. The numsimword convert numbers to words, which show (almost) linear similarity based on magnitude of numbers (Figure 1), or similarity based on number of digits (Figure 2).   

## Installation

    $ git clone https://github.com/tkishimoto/numsimword.git
    $ cd numsimword
    $ pip3.6 install -e .  
   
## Usage

    import numsimword
    myclass = numsimword.NumsimWord()
    myclass.get_linear_word(25)
    myclass.get_digit_word(25)

## Example
Text sentences "xx time(s)", wehre xx is from 0 to 199, are vectorized using Doc2Vec. The figure 1 (figure 2) shows vector distribution without and with get_linear_word (get_digit_word).
* Figure 1
![figure](https://user-images.githubusercontent.com/4026405/63408602-62fe1500-c42a-11e9-9082-6bc8f3d0fb11.png)
* Figure 2
![figure](https://user-images.githubusercontent.com/4026405/63480989-f7ba4e80-c4ce-11e9-81ff-37bac312763a.png)
