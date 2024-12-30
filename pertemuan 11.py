print("Print Perulangan Pertama")
for i in range(10):
    print(i)

print("Print Perulangan Kedua")
for j in range(1,10):
    print(j)

print("Print Perulangan dengan step")
for k in range(1,20,34):
    print(k)

print("Print Perulangan for untuk menghitung nilai dalam list")
numbers = [11, 23, 45, 55]
total = 0

for num in numbers:
    total += num

print("Total nilai:", total)

number = int(input("Masukkan angka: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")
