# LATIHAN BUAT KALKULATOR KOMPLEKS
# VERAI 2.0

def menu_utama():
  print('==== KALKULATOR SHL ====')
  print('======================')
  print('  A.Pilih perhitungan ')
  print('======================')
  print('')
  print('')
  print('======= LAINNYA =======')
  print('  B.info aplikasi')
  print('  C.list')
  print('  D.keluar')
  
def menu_pilih_perhitungan():
  print('==== PILIH PERHITUNGAN ====')
  print(' ')
  print('== Pilih penjumlahan \n== yang ingin anda lakukan :')
  print(' ')
  print('  1.Pertambahan (+)')
  print('  2.Perkurangan (-)')
  print('  3.Perkalian   (×)')
  print('  4.Pembagian   (/)')
  print('  5.Pangkat     (^)')
  print('  6.modulus     (%)')
  pilih = input("Pilih perhitungan : ")
  print(' ')
  print('=========================')
  return pilih
  
def info_aplikasi():
  print('==========================')
  print('====\tINFO APLIKASI\t====')
  print('==========================')
  print(' dibuat oleh\t\t: sahal')
  print(' tanggal rilis\t\t: 6-07-2026')
  print(' versi\t\t\t: 1.0.2')
  print(' nama aplikasi\t: Kalkulator SHL')
  print('==========================')
  input(' Tekan enter untuk kembali : ')
  
def pilih_menu():
  while True:
    menu_utama()
    
    pilih_menu_utama = input('pilih menu : ').upper()
    
    if pilih_menu_utama not in ['A','B','C','D']:
      print(' menu tidak ada ')
      print(' mohon pilih dengan benar')
      continue
    
    if pilih_menu_utama == 'D':
      print(' anda sudah berhenti\n menggunakan aplikasi')
      break
    
    if pilih_menu_utama == 'C':
      print(' maaf list belum dibuat')
      continue
    
    if pilih_menu_utama == 'B':
      info_aplikasi()
      continue
    
    if pilih_menu_utama == 'A':
      return menu_pilih_perhitungan()
    
   # break

def input_angka():
  
  
  while True:
    try:
      angka_satu = float(input(' masukan angka ke satu :'))
      angka_dua = float(input(' masukan angka ke dua :'))
      return angka_satu, angka_dua
    
    except ValueError:
      print('input harua berupa angka!')

def hitung(pilih, angka_satu, angka_dua):
  if pilih == '1':
    return angka_satu + angka_dua
  
  elif pilih == '2':
    return angka_satu - angka_dua
    
  elif pilih == '3':
    return angka_satu * angka_dua
    
  elif pilih == '4':
    if angka_dua == 0:
      return None
    return angka_satu / angka_dua
    
  elif pilih == '5':
    return angka_satu ** angka_dua
    
  elif pilih == '6':
    return angka_satu % angka_dua

def ulang():
    pilihan = input("\nHitung lagi? (y/t): ")

    if pilihan.lower() == "t":
        print("Terima kasih telah menggunakan kalkulator.")
        return False

    return True

#======================
#====  CODE UTAMA  ====
#======================
while True:
  
  pilih = pilih_menu()
  
  if pilih not in ['1','2','3','4','4','5','6']:
    print(' menu tidak ada')
    print(' harap pilih dengan benar')
    continue
  
  
  angka_satu, angka_dua = input_angka()
  
  hasil = hitung(pilih, angka_satu, angka_dua)
  
  if hasil is None:
    print(' tidak bisa dibagi dengan nol')
    continue
  
  print('================')
  print(f"Hasil = {hasil}")
  print('================')
  
  if not ulang():
    break