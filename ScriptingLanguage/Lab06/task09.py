# Narysuj histogram rozkładu wyników
# testu u studentów. Przyjmij, że dane
# odnośnie do wyników to lista przechowująca
# procent uzyskanych punktów przez studentów
# np. dane = [60, 70, 80, 90, 100, 70, 80, 80, 85, 95]

import matplotlib.pyplot as plt

dane = [60, 70, 80, 90, 100, 70, 80, 80, 85, 95]

plt.figure(figsize=(8, 6))
plt.hist(dane, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Procent uzyskanych punktów')
plt.ylabel('Liczba studentów')
plt.title('Rozkład wyników testu')
plt.grid(True)  # Dodanie siatki
plt.show()
