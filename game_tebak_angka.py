import random

def menu_game():
  print(' ')
  print('====================')
  print('======= GAME =======')
  print('====================')
  print(' A. Game tebak angka')
  print('====================')
  print(' B. Info aplikasi')
  print(' C. Keluar')
  print('====================')

def info_apk():
  print('====================')
  print('======= INFO ========')
  print('====================')
  print(' Nama apk\t: Sal App')
  print(' Pencipta\t: Sahal')
  print(' Versi\t\t: 2.0')
  print(' Tanggal rilis\t: 19-6-2026')
  print('====================')
  input(' clik enter untuk kembali :')

def game():
  while True:
    print(' masukan angka dari 1-100')
    nilai = int(input('masukan angka :'))
    return nilai
    
    

def pilih_menu():
  while True:
    menu_game()
    
    pilih_menu = input(' pilih menu : ').upper()
    
    if pilih_menu not in ['A','B','C']:
      print(' menu tidak ada\n mohon pilih dengan benar')
      continue
    
    if pilih_menu == 'C':
      print(' terimakasih sudah coba game saya\n !ANDA SUDAH KELUAR DARI APLIKASI!')
      break
    
    if pilih_menu == 'B':
      info_apk()
      continue
    
    if pilih_menu == 'A':
      return game()
      continue

angka_rahasia = random.randint(1, 100)

while True:
  tebakan = pilih_menu()
  while True:
    if tebakan > angka_rahasia:
      print('terlalu besar')
    elif tebakan < angka_rahasia:
      print('terlalu kecil')
    else:
      print('kamu benar')
      input('klik enter untuk ke menu utama')
      break
    
    tebakan = game()