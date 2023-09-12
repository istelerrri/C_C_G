import ccard

def repeat(times):
  for generate in range(times):
    visa = ccard.visa()
    mastercard = ccard.mastercard()
    discover = ccard.discover()
    ame = ccard.americanexpress()
    if type == "visa" :
      print(visa)
    elif type == "discover":
      print(discover)
    elif type == "americanexpress":
      print(ame)
    elif type == "mastercard":
      print(mastercard)
    else:
      print("Not Found !!!!!")
    

print("CCG \n")
print("Hello Sir In CCG , We Here To Create The FAKE Credit Cards You Want ◉⁠‿⁠◉ . \n")

type = input("Enter your credit card type (visa, mastercard, americanexpress, discover) : ")

times = int(input("Enter number of the Credit Cards you need : \n\n"))

repeat(times)