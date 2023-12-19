from icecream import ic
# from simp import Function_in_simp, SimpMdl_used - not finished

# create sumofdigits- gets number and returns sum of digits-done

def sumofdigits():
     # not finished
    # global SimpMdl_used
    # if not SimpMdl_used:
    #     print("please use at lesst one function from simp module (add or subtract)")
    #     return 
    # SimpMdl_used = True

    NumberIput= input("enter a number: ")
    SumVar=0
    for digit in NumberIput:
        SumVar += int(digit)
    
    return  ic(SumVar)


# create ispal- return true if number is pilandrum
def ispal(number):
    # not finished
    # global SimpMdl_used
    # if not SimpMdl_used:
    #     print("please use at lesst one function from simp module (add or subtract)")
    #     return 
    # SimpMdl_used = True

    numberSng=str(number)
    
    reversed_Number = numberSng[::-1]
    return numberSng == reversed_Number
    

# code not finished
# def function_in_comp():
#     if not SimpMdl_used:
#         print("Error: Please use at least one function from simp module before using from comp.")
#         return

#     print("Function in comp is called.")

    