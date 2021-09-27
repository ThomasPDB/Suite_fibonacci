#coding: UTF-8
import time
# demande utilisateur
nombre = int(input("entrer la quantité de nombre à afficher : "))

# temps execution
start_timer = time.time()

# variables
a = 0
b = 1
total = 0


# suite fibonacci
def Fibo():
    global a, b, total

    for _ in range(nombre):
        a = b
        b = total
        total = a + b
        print(total)


# résultat
Fibo()
end_timer = time.time()
print(f"le temps est de {round(end_timer - start_timer, 3)} sec")
