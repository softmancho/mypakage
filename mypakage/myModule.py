    

def top_n(items, n):
    """
        Return the top n items in an array in desending order
    
    Args: 
        items(array): lists or array-like objects containing numerical values.
        n(int): numbers of top items to return.

    Return: 
        array: topn items in decending order

    Examples:
        >>>top_n([8,3,2,7,4], 3)
            [8,7,3]
    """
    #keep sorting until we have the top n items
    for i in range(items):
        for j in range(len(items)-1-i):

            #if item is bigger than the nest item 
            if items[j] > items[j+1]:
                #swap the two
                items[j], items[j+1] = items[j+1], items[j]
            
    # get the last nth item in the list
    top_n = items[-n:]

    #return in decending order
    return top_n[::-1]
    
