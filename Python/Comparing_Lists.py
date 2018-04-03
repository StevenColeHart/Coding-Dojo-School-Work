def Comparing_Lists(list_one,list_two):
    if set(list_one) == set(list_two):
        print "The lists are the same"
    elif set(list_one) != set(list_two):
        print "The lists are not the same." 

Comparing_Lists(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])