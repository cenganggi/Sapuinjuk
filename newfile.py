# Program Ulang Tahun dengan Passcode

# Passcode yang benar
passcode = "221298"

# Meminta passcode dari pengguna
input_passcode = input("Masukkan passcode: ")

# Periksa apakah passcode benar
if input_passcode == passcode:
    print("Passcode benar! Akses diterima.")
    
    # Tampilkan link
    print("Klik link berikut untuk melihat detail lebih lanjut:")
    print("https://hbdnita.carrd.co/")  # Ganti link ini dengan link Anda
else:
    print("Passcode salah! Akses ditolak.")