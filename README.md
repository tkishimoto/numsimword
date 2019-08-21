numsimword
====

In Machine Learning algorithms to analyze text similarity, such as Doc2Vec, different number words generally show randome similarity. The numsimword convert numbers to words, which show (almost) linear similarity based on magnitude of numbers.   

## Installation

    $ git clone https://github.com/tkishimoto/numsimword.git
    $ cd numsimword
    $ pip3.6 install -e .  
   
## Usage

    import numsimword
    myclass = numsimword.NumsimWord()
    myclass.get_sim_word(25)
    
## Example
Text sentences "xx time(s)", wehre xx is from 0 to 20, are vectorized using Doc2Vec. The figure shows vector distribution with and without numsimword.
![figure](https://user-images.githubusercontent.com/4026405/63408602-62fe1500-c42a-11e9-9082-6bc8f3d0fb11.png)
   
