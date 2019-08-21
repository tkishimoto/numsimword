numsimword
====

In Machine Learning algorithms to analyze text similarity, such as Doc2Vec, different number words generally show randome similarity. The numsimword convert numbers to words, which show linear similarity based on magnitude of numbers.   

## Installation

    $ git clone https://github.com/tkishimoto/numsimword.git
    $ cd numsimword
    $ pip3.6 install -e .  
   
## Usage

    import numsimword
    myclass = numsimword.NumsimWord()
    myclass.get_sim_word(25)
    
## Example

   
