number = int(input('numero: '))
ePrimo = 0

for i in range(1,  (number + 1)):
  if number % i == 0:
    ePrimo += 1

if ePrimo == 2:
  print ('numero primo')
else:
   print('numero não e primo')
for i in range (number > 0):
   print('numero e positivo')
for i in range (number < 0):
   print('numero e negativo')