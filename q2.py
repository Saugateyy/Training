pname=input("Enter your product name")
pquan=int(input("Enter the quantity of products purchased"))
pcost=int(input("Enter the per pcs cost of product"))
total_cost=pquan*pcost
print(f"The total cost of {pname} of {pquan} is Rs.{total_cost}")