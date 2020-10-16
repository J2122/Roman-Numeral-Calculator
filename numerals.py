import numvalue as numb
import numbers
import time

print("""\n
  ___       
               \||      
             ,'_,-\     
             ;'____\    
             || =\=|    
             ||  - |                               
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\      / , ;                            
     /  ,' | _ - ',/, ;
    (  (   |     /, ,,;
     \  \  |     ',,/,; ROMAN NUMERAL CALCULATOR
      \  \ |    /, / ,;             by j21
     (| ,^.|   / ,, ,/;
      `-'./ `-._,, ,/,;        Press Enter... 
           \-._ `-._,,;     
           |/,,`-._ `-.
           |, ,;, ,`-._\ """)
input()
print("\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n")
while True:

    num1 = input("Enter first numeral: ")
    op = input("Enter Operation: ")
    num2 = input("Enter second numeral: ")

    for c in num1:
        if c not in ["I","V","X","L","C","D","M"]:
            print('Not a valid numeral')
            continue

    for x in op:
        if x not in ["+", "-", "/", "*"]:
            print('Not a valid operation(use +,-,/,*')
            continue

    num1total = 0
    for letter in num1:
        num1total += numb.values[letter]

    num2total = 0
    for letter in num2:
        num2total += numb.values[letter]

    if op == "+":
        print(num1total + num2total)
        time.sleep(10)
    elif op == "-":
        print(num1total - num2total)
        time.sleep(10)
    elif op == "*":
        print(num1total * num2total)
        time.sleep(10)
    elif op == "/":
        print(num1total / num2total)
        time.sleep(10)
    else:
        print("An Error has occured please try again")
        time.sleep(10)

    break

#num1_int = numb.value(num1)
