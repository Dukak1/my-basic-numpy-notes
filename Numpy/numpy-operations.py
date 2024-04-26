import numpy as np

numbers1 = np.random.randint(10,100,6) # 10 la 100 arası 6 sayı
numbers2 = np.random.randint(10,100,6) 

print(numbers1)
print(numbers2)

result = numbers1 + numbers2 # Yazdırınca her sütunu toplayıp yeni dizi oluşturur
result = numbers1 + 10 # her sütuna 10 ekleyip yeni dizi ol.
result = numbers1 - numbers2 # Sütunları birbirinden çıkarıp yeni dizi ol
result = numbers1 * numbers2 # Sütunları birbiriyle çarpıp yeni dizi ol
result = numbers1 / numbers2 # Sütunları birbiriyle bölüp yeni dizi ol

result = np.sin(numbers1) # sinüsünü alır.
result = np.cos(numbers1) # cosünüsü alır.

result = np.sqrt(numbers1) # Karakök alır.

result = np.log(numbers1) # Logaritma alır.

mnumbers1 = numbers1.reshape(2,3) # matris oluşturur
mnumbers2 = numbers2.reshape(2,3)

# print(mnumbers1)
# print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2)) # 2 matrisi dikey birleştirir.
result = np.hstack((mnumbers1,mnumbers2)) # 2 matrisi yatay birleştirir.

result = numbers1 >= 5 # 6 true döndürür
result = numbers1 >= 50 # True false lardan oluşan bir dizi
result = numbers1 %2 == 0 

print(numbers1[result]) # çift olanları yazdırır

print(result)