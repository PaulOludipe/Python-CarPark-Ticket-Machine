acceptcoins = [1,2,5,10,20,50,100,200]
carvisits = []
engineeringcode = "`¬`"

def printticket(total,reg):
       print("***********************")
       print("*   Parking Ticket    *")
       print("----------------------*")
       print("*Reg Number : ",reg,"* ")
       print("*Paid :",total,"      *")
       print("***********************")

print("#################### Paul's Parking Providing Plus ####################")

p_fee = 90
coins = 0
change = 0
total = 0
reg = ""

while True:
       coins = 0
       change = 0
       total = 0
       
       reg = input("enter reg number : ")
       if reg == "`¬`":
              p_fee = int(input("Enter new parking fee : "))
              
       carvisits.append(reg)

             
       coins = int(input("enter coins to the value of 90p: "))
       total = total + coins

       while total < p_fee:
              coins = int(input("enter coins to the value of 90p : "))
              if coins in acceptcoins:
                     total = total + coins
              else:
                      print("bad coin")
             
       if total > p_fee:
              change = total - p_fee
              print("Change : ",change)

       printticket(total,reg)

              

