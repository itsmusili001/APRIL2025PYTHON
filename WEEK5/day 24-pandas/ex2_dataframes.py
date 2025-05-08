import pandas as pd
grades_dict ={"tom":[87,96,70],"diana":[99,78,90],"fred":[100,99,78],"mary":[89,81,83]}
grades_df = pd.DataFrame(grades_dict,index=["java","c#","python"])
print(grades_df)
print()

#creating a dataframe from a list of lists
grades_df2 = pd.DataFrame([[87,96,70],[99,78,90],[100,99,78],[89,81,83]])


# Adding column headers and row headers to grades_df2
grades_df2.index = ["tom", "diana", "fred", "mary"]
grades_df2.columns = ["java", "c#", "python"]
print(grades_df2.transpose())

