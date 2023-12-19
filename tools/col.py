from icecream import ic

def myzip(it1,it2):
    result = zip(it1,it2)
    result_list = list(result)
    return ic(result_list)