#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

#input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
#output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

# Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function `get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`. Your function will return an instance of an `Answer` tuple that has the following form:
# ```
# (zero, one)
# ```
# where each element represents the item weights of the two packages. _**The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index.**_ If such a pair doesn’t exist for the given inputs, your function should return `None`.

# _NOTE:_ When calling `hash_table_retrieve` with a key that doesn't exist in the hash table, `hash_table_retrieve` will return `None`.
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #add the weights as the keys and index as the value to hashtable
    for i in range(length):
        hash_table_insert(ht, weights[i], i )
    #loop through hash table to see which key == limit-weight
    for i in range(length):
        s = hash_table_retrieve(ht, limit-weights[i])
        #arange order so 0 index is bigger value
        if s is not None:
            if s > i:
                return(s,i)
            else:
                return(i, s)
        
            
    return 


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
