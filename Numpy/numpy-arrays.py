import numpy as np

result =np.array([1,3,5,7,9])   # Böyle bir dizi oluşturur.

result = np.arange(1,10) # 1'den 10 a kadar dizi oluşturur. 10 dahil değil.
result = np.arange(10,100,3)  # 3 er 3 er artar.

result = np.zeros(10)   # 10 tane 0 dan oluşan dizi oluşturur.

result = np.ones(10)    # 10 tane 1 den oluşan dizi oluşturur

result = np.linspace(0,100,5) # 0 la 100 arasını 5 eşit parçaya ayırarak
                              # bir dizi oluşturur. Çıktısı 0.25.50.75.100
result = np.linspace(0,5,5) # 1.25, 2.5, 3.75, 5.

result = np.random.randint(0,10) # 0 10 arası bir sayı seçer.
result = np.random.randint(20) # 0 20 arası bir sayı seçer.
result = np.random.randint(1,10,3) # 1 10 arası 3 sayı seçer

result = np.random.rand(5) # 0 ile 1 arasında 5 sayıdan oluşan dizi üretir!

result = np.random.randn(5) # -1 ile 1 arasında 5 sayıdan oluşan dizi üretir.

result = np.arange(50) # 50 ye kadar ki sayılardan bir dizi

np_array = np.arange(50)

np_multi = np_array.reshape(5,10) # 50 ye kadadr olan sayılardan 5'e 10 luk dizi

# print(np_multi.sum(axis=1)) # her satırın toplamından bir dizi yazdırır.
# print(np_multi.sum(axis=0)) # her sütunun toplamından bir dizi yazdırır.

rnd_numbers = np.random.randint(1,100,10) # 1 100 arası 10 sayı
print(rnd_numbers)
result = rnd_numbers.max() # rnd_numbers'ın maksimum sayısını yazdırır.

result = rnd_numbers.min() # rnd_numbers'ın minimum sayısını yazdırır.

result = rnd_numbers.mean() # rnd_numbers'ın ortalamasını yazdırır.

result = rnd_numbers.argmax() # rnd_numbers'ın maksimunun indisini yazdırır.

result = rnd_numbers.argmin() # rnd_numbers'ın minimunun indisini yazdırır.

print(result)