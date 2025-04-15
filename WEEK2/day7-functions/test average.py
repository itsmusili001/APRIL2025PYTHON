def calc_average(test1,test2,test3,test4,test5):
    return(test1+test2+test3+test4+test5)/5

def determine_grade(test):
    if test>100 or test<0:
        print("error!!! Enter a valid mark 0-100")
    elif test>=90:
        return "A"
    elif test>=80:
        return "B"
    elif test>=70:
        return "C"
    elif test>=60:
        return "D"
    else:
        return"F"
def main():
    test1=int(input("enter test1 score-"))        
    test2=int(input("enter test2 score-"))        
    test3=int(input("enter test3 score-"))        
    test4=int(input("enter test4 score-"))        
    test5=int(input("enter test5 score-"))  

    print(f" grade of test 1 is {determine_grade(test1)}")
    print(f" grade of test 2 is {determine_grade(test2)}")
    print(f" grade of test 3 is {determine_grade(test3)}")
    print(f" grade of test 4 is {determine_grade(test4)}")
    print(f" grade of test 5 is {determine_grade(test5)}")

    average =calc_average(test1,test2,test3,test4,test5)
    print(f"the average score is:{average}")
     
main()
