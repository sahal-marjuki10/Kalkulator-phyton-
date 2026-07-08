# PENYIMPANAN DAN IMPORT
daftar_tugas = []
Catatan = []
Keuangan = []
import textwrap

# TAMPILAN MENU UTAMA
def menu_utama():
  print('=================')
  print('==== To Do List ====')
  print('=================')
  print(' ')
  print('=================')
  print(' A. Tugas')
  print('————————————')
  print(' B. Catatan')
  print('————————————')
  print(' C. Keuangan')
  print('————————————')
  print(' D. Tutup')
  print('=================')
  print(' Pilih Menu :')

# MEMILIH MENU BAGIAN UTAMAN
# DAN SISTEM OPERAIS
def pilih_menu_utama():
  while True:
    menu_utama()
    pilih_menu_abc = input().upper()
    
    if pilih_menu_abc == 'D':
      print('Anda sudah keluar')
      break
    
    if pilih_menu_abc == 'C':
      pilih_menu_keuangan(Keuangan)
      continue
    
    if pilih_menu_abc == 'B':
      pilih_menu_catatan(Catatan)
      continue
    
    if pilih_menu_abc == 'A':
      pilih_menu_tugas(daftar_tugas)
      continue

# TAMPILAN MEMU CATATAN
def menu_catatan(Catatan):
  print('=================')
  print('=== Menu Catatan ===')
  print('=================')
  print(' ')
  print('=================')
  print(' 1. Lihat Catatan')
  print('————————————')
  print(' 2. Tambah Catatan')
  print('————————————')
  print(' 3. Hapus Catatan')
  print('————————————')
  print(' 4. Tutup')
  print('=================')
  pilih_catatan = input(' Pilih Menu')
  return pilih_catatan

# MEMILIH MENU BAGIAN CATATAN
# DAN SISTEM OPERAIS
def pilih_menu_catatan(Catatan):
  while True:
    pilih_catatan = menu_catatan(Catatan)
    
    if pilih_catatan == '1':
      if len(Catatan) == 0:
        print(' Tugas belum tersedia')
      else:
        for nomor, data in enumerate(Catatan, start=1):
            print('————————————————————————')
            print(f"{nomor}. {data['judul']}")
            print(textwrap.fill(data["isi"], width=40))
            print('————————————————————————')
    elif pilih_catatan == '2':
      judul = input('judul :')
      isi = input(' isi :')
      
      Catatan.append({
        "judul": judul,
        "isi": isi
      })
      
      print(' Catatan berhasil ditambahkan')
  
    elif pilih_catatan == "3":
      nomor = int(input("Nomor tugas yang ingin dihapus: "))
      Catatan.pop(nomor - 1)
      print(' Catatan berhasil dihapus')
   
    elif pilih_catatan == '4':
      break
   
    else:
      print('pilih dengan benar')

# TAMPILAN MENU TUGAS
def menu_tugas(daftar_tugas):
  print('=================')
  print('=== Menu Tugas ===')
  print('=================')
  print(' ')
  print('=================')
  print(' 1. Lihat Tugas')
  print('————————————')
  print(' 2. Tambah Tugas')
  print('————————————')
  print(' 3. Hapus tugas')
  print('————————————')
  print(' 4. Tutup')
  print('=================')
  pilih_tugas = input(' Pilih Menu')
  return pilih_tugas

# MEMILIH MENU BAGIAN TUGAS
# DAN SISTEM OPERAIS
def pilih_menu_tugas(daftar_tugas):
  while True:
    pilih_tugas =  menu_tugas(daftar_tugas)
    
    if pilih_tugas == '1':
      if len(daftar_tugas) == 0:
        print(' belum ada tugas')
      else:
          print("========================")
          print("======= Daftar Tugas ======")
          print("========================")
          for nomor, tugas in enumerate(daftar_tugas, start=1):
              print(f"{nomor}. {tugas}")
              print('—————————————————')
    
    elif pilih_tugas == '2':
      tugas = input("Masukkan tugas baru: ")
      daftar_tugas.append(tugas)
      print("Tugas berhasil ditambahkan.")
    
    elif pilih_tugas == "3":
      nomor = int(input("Nomor tugas yang ingin dihapus: "))
      daftar_tugas.pop(nomor - 1)
    
    elif pilih_tugas == '4':
      break
    
    else:
      print('menu tidak ada')

# TAMPILAN MEMU KEUANGAN
# DAN SISTEM OPERAIS
def memu_keuangan(Keuangan):
  print('=================')
  print('=== Menu Catatan ===')
  print('=================')
  print(' ')
  print('=================')
  print(' 1. Lihat Riwayat')
  print('————————————')
  print(' 2. Hapus Riwayat')
  print('————————————')
  print(' 3. Tambah Pemasukan')
  print('————————————')
  print(' 4. Tambah Pengeluaran')
  print('————————————')
  print(' 5. Lihat Saldo')
  print('————————————')
  print(' 6. Tutup')
  print('=================')
  pilih_keuangan = input(' Pilih Menu')
  return pilih_keuangan

# MEMILIH MENU KEUANGAN
# DAN SISTEM OPERAIS
def pilih_menu_keuangan(Keuangan):
  while True:
    
    pilih_keuangan = memu_keuangan(Keuangan)
    
    if pilih_keuangan == '1':
      if len(Keuangan) == 0:
        print(' Tidak ada Riwayat')
      else:
        for nomor, data in enumerate(Keuangan, start=1):
            print('—————————————')
            print(f"{nomor}. {data['jenis']}")
            print(f"Nominal : Rp {data['nominal']}")
            print(f"Keterangan : {data['keterangan']}")
    
    elif pilih_keuangan == '2':
      nomor = int(input("Nomor Riwayat yang ingin dihapus: "))
      Keuangan.pop(nomor - 1)
      print(' Catatan berhasil dihapus')
    
    elif pilih_keuangan == '3':
      nominal = int(input("Nominal : "))
      keterangan = input("Keterangan : ")
      
      Keuangan.append({
            "jenis": "Pemasukan",
            "nominal": nominal,
            "keterangan": keterangan
        })
      
      print("Pemasukan berhasil ditambahkan.")
    
    elif pilih_keuangan == '4':
      nominal = int(input("Nominal : "))
      keterangan = input("Keterangan : ")
      
      Keuangan.append({
            "jenis": "Pengeluaran",
            "nominal": nominal,
            "keterangan": keterangan
        })
      
      print("Pengeluaran berhasil ditambahkan.")
      
    elif pilih_keuangan == '5':
      saldo = 0
      
      for data in Keuangan:
        if data["jenis"] == "Pemasukan":
            saldo += data["nominal"]

        else:
            saldo -= data["nominal"]
        
        print(f"Saldo : Rp {saldo}")
    
    elif pilih_keuangan == "6":
      break
    
    else:
      print(' mohon pilih yang benar')

# MENJALAN KAN PROFRAM
pilih_menu_utama()