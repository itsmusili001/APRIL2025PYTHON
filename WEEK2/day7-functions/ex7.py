def rectangle_area(l,w):
    return l*w
def rectangle_perimeter(l,w):
    return 2*(l+w)
length=float(input("Enter the length-"))
width=float(input("Enter the width-"))

print(f"Area of the rectangle is-{rectangle_area(length,width)}")
print(f"perimeter of the rectangle is-{rectangle_perimeter(length,width)}")



