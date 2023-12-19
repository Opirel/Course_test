from icecream import ic
import tools.numbers.simp
import tools.numbers.comp
import tools.col

num1=6
num2=2

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
def main():
    tools.numbers.simp.add(num1,num2)
    tools.numbers.simp.subtract(num1,num2)
   
    tools.numbers.comp.sumofdigits(42)
    tools.numbers.comp.ispal(161)
    if tools.numbers.comp.ispal(61): ic("the number is a palindrom") 
    else: ic("the number is not a palindrom")
    
    tools.col.myzip(list1,list2)




    #  # not finished
    # tools.numbers.comp.function_in_comp()
    # tools.numbers.simp.Function_in_simp()
    # tools.numbers.comp.function_in_comp()
if __name__ == "__main__":
    main()