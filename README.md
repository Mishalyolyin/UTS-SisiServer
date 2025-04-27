
# README

Proyek ini adalah pengembangan aplikasi manajemen inventaris sederhana berbasis web menggunakan Django. Berikut alur pengerjaan proyek ini mulai dari inisialisasi hingga selesai:

1. **Inisialisasi Proyek Django**
   - Membuat virtual environment lokal.
   - Menginstal Django 5.2.
   - Membuat project Django baru bernama `inventory_project`.
   - Membuat app baru bernama `inventory_app`.
   - Setting awal `settings.py`, termasuk konfigurasi `INSTALLED_APPS`, `TEMPLATES`, dan `STATICFILES_DIRS`.

2. **Konfigurasi Database**
   - Menyiapkan file `docker-compose.yml` untuk menjalankan service MySQL.
   - Menyambungkan Django ke database MySQL dengan setting:
     - Nama database: `inventory_db`
     - Username: `inventory_user`
     - Password: `password123`
     - Host: `127.0.0.1`
     - Port: `3306`
   - Membuat file migrasi awal dan migrasi database (`makemigrations` dan `migrate`).

3. **Membuat Model Database**
   - Membuat model `Category`, `Supplier`, dan `Item` di `models.py`.
   - Menambahkan relasi ForeignKey antara `Item` dengan `Category` dan `Supplier`.
   - Melakukan migrasi ulang untuk model-model baru.

4. **Membuat CRUD Operasi**
   - Membuat `forms.py` untuk masing-masing entitas (CategoryForm, SupplierForm, ItemForm).
   - Membuat views CRUD untuk:
     - Category: List, Add, Edit, Delete
     - Supplier: List, Add, Edit, Delete
     - Item: List, Add, Edit, Delete

5. **Membangun Sistem Autentikasi**
   - Membuat login dan logout custom.
   - Menggunakan `@login_required` untuk mengamankan akses halaman.
   - Mengatur `LOGIN_URL`, `LOGIN_REDIRECT_URL`, dan `LOGOUT_REDIRECT_URL` di `settings.py`.

6. **Membangun Dashboard**
   - Membuat halaman dashboard berisi:
     - Total Stock
     - Total Value
     - Average Price
     - Daftar barang stok rendah (<5)
   - Membuat summary sederhana untuk overview inventaris.

7. **Menyusun Struktur Template**
   - Menyiapkan struktur folder di dalam `templates/`:
     - `admin/login.html`
     - `dashboard.html`
     - `categories/`
     - `suppliers/`
     - `items/`
     - `low_stock/`
     - `summary/`
     - `profile/`
   - Membuat `base.html` sebagai layout utama.

8. **Menyusun Style dan Frontend**
   - Membuat file `static/css/style.css`.
   - Mendesain tampilan sidebar, navbar, tabel, form input, tombol "Add New", dan card dashboard.
   - Menggunakan kombinasi warna biru gradien untuk tampilan profesional.

9. **Testing Proyek**
   - Menjalankan server lokal dengan `python manage.py runserver`.
   - Melakukan testing login, CRUD category, supplier, item, dan testing fungsi dashboard.
   - Debugging jika terjadi error pada URL pattern, redirect setelah login, atau akses tanpa login.

10. **Finalisasi**
    - Menambahkan `.gitignore` untuk mengecualikan file yang tidak perlu di Git (contoh: `__pycache__`, `db.sqlite3`, `env/`).
    - Menyusun file `docker-compose.yml` agar database dapat dijalankan otomatis.
    - Membuat file README.md berisi dokumentasi pengerjaan.
    - Menyiapkan project untuk dipush ke GitHub.

11. **Upload ke Git Repository**
    - Inisialisasi repository Git lokal.
    - Commit semua file project.
    - Push ke repository GitHub sesuai ketentuan tugas.

---

# Cara Menggunakan Aplikasi

1. Clone atau download project ini dari repository GitHub.
2. Pastikan Docker sudah berjalan dan database MySQL tersedia.
3. Jalankan `python manage.py migrate` untuk membuat struktur database.
4. Buat superuser admin dengan perintah `python manage.py createsuperuser`.
5. Jalankan server Django dengan perintah `python manage.py runserver`.
6. Akses `http://127.0.0.1:8000/login/` untuk login.
7. Setelah login, pengguna langsung diarahkan ke halaman dashboard.
8. Gunakan menu sidebar untuk mengelola Categories, Suppliers, Items, atau melihat Summary dan Low Stock.

---

# Penutup

Proyek ini bertujuan untuk mengimplementasikan pemahaman tentang Django basic CRUD, autentikasi user, serta pengelolaan tampilan berbasis template yang modern dan responsif.
Seluruh alur pengerjaan disusun berurutan mulai dari inisialisasi project, pembuatan model, pengembangan CRUD, desain antarmuka, sampai ke dokumentasi dan deployment project.
