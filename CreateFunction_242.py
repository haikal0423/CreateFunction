# Fungsi untuk mengubah suhu antara Celsius dan Fahrenheit
def konversisuhu(temperature, value):

    # Jika 'value' adalah 'C', maka konversi dari Fahrenheit ke Celsius
    if value == 'C':
        temperaturesuhu = (temperature - 32) * 5 / 9
        return temperaturesuhu, 'C'
    
    # Jika tidak, berarti konversi dari Celsius ke Fahrenheit
    else:
        temperaturesuhu = (temperature * 9 / 5) + 32
        return temperaturesuhu, 'F'
    
# Contoh pengubahan dari Celsius ke Fahrenheit
celsius_temperature = 30  # Suhu awal dalam Celsius
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')

# Menampilkan hasil perubahan suhu dari Celsius ke Fahrenheit
print(f"{celsius_temperature}°C diubah menjadi Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Contoh pengubahan dari Fahrenheit ke Celsius
fahrenheit_temperature = 86  # Suhu awal dalam Fahrenheit
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')

# Menampilkan hasil perubahan suhu dari Fahrenheit ke Celsius
print(f"{fahrenheit_temperature}°F diubah menjadi Celsius adalah {temperaturesuhu}°{target_value}")
