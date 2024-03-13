# Tip Calculator
# Taylor Sayson
# 28 February 2024

def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip(" $!%/"))
    percent = percent_to_float(input("What percentage would you like to tip? ").strip(" $!%/"))
    total_cost = dollars * (1 + percent)
    print(f"Your total cost is ${round(total_cost, 2)}")
   
def dollars_to_float(d):
   return float(d)

def percent_to_float(p):
   return float(p) /100

main()