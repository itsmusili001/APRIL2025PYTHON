def main():
    try:
        replacement_cost=float(input("Enter the replcement cost of the building"))

        minimum_insuarance = replacement_cost*0.80
        print(f"the minimum amount of insuarance you should buy for the property is: kshs{minimum_insuarance:.2f}")
    except ValueError:
        print("invalid input.please enter a valid number")
if __name__=="__main__":
    main()