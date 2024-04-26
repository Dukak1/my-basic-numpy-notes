import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5] # 5. indis
result = numbers[-1] # Son indis
result = numbers[0:3] # İlk 3 indis
result = numbers[:3] # İlk 3 indis
result = numbers[3:] # Sondan 3. indise kadar
result = numbers[::] # Komple
result = numbers[::-1] # Tersten komple
result = numbers[::-2] # Tersten yarı yarıya


numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = numbers2[0] # [0,5,10]
result = numbers2[2] # [50,75,85]

result = numbers2[0,2] # 0. indisin 2. indisi. Yani 10
result = numbers2[2,1] # 2. indisin 1. indisi. Yani 75

result = numbers2[:] # Komple
result = numbers2[:,2] # Her indisin 2. indisleri yani 10 25 85
result = numbers2[:,0] # Her indisin 0. indisleri yani 0 15 50
result = numbers2[:,0:2] # Her indisin 0 ile 2. indislerinin arasındakiler
result = numbers2[-1,:] # Son indisin elemanları
result = numbers2[:2,:2] # 0 5 15 20


# print(result)

arr1 = np.arange(0,10)
arr2 = arr1 # referans kopyalaması

# print(arr1)  # İkiside aynı çıktı çıkarır
# print(arr2)

arr2[0] = 20

print(arr1) # değişiklik arr1 de de geçerli
print(arr2)


arr2 = arr1.copy() # Bu sefer adresleri farkı bu yüzden arr2 de yapılan
                    # bir değişiklik arr1 de geçerli olmaz