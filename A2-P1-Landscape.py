#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     
#Student Name:  Mathew Akunyili

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Declare variables
    labour = 1000
  

    #Title
    print("Landscape Calculator")
    print("")

    #Ask user for house number
    address = input("Enter House Number: ")
    print("")

    #Ask for proberty length and width
    length = float(input("Enter property length(feet): "))
    width = float(input("Enter property width(feet): "))

    #Ask user for type of grass
    grass = input("Enter type of grass (fescue, bentgrass, campus): ").lower()

    #Ask user for number of trees
    trees = int(input("Enter the number of trees: "))

    #calculatuons
    squareFeet = length * width # This is the calculation for yhe area of the house

    if grass == "fescue":
        grassPrice = 0.05 * squareFeet # i use this to find houmuch the grass would be depending on the area or square feet of the landscape
    elif grass == "bentgrass":
        grassPrice = 0.02 * squareFeet
    elif grass == "campus":
        grassPrice = 0.01 * squareFeet

    if squareFeet > 5000:
        upCharge = 500
    else: 
        upCharge = 0

    totalCost = grassPrice + (trees * 100) + labour + upCharge # This calculates the total cost required
        
    
    print("Total cost for house", address, f"is: ${totalCost:.2f}")

    

    # YOUR CODE ENDS HERE

main()