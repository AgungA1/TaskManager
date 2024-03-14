# Task Manager

Sistem manajemen tugas sederhana yang memungkinkan pengguna membuat, melihat, dan menyelesaikan tugas.

## Menjalankan Skrip Utama

Untuk menjalankan skrip utama aplikasi, ikuti langkah-langkah berikut:

1. Buka terminal atau command prompt.
2. Navigasikan ke direktori `TaskManager`.
3. Jalankan perintah berikut:

    ```bash
    python main.py
    ```

Skrip ini akan mengeksekusi fungsi utama aplikasi.

## Menjalankan Pengujian

Untuk menjalankan pengujian, ikuti langkah-langkah berikut:

1. Buka terminal atau command prompt.
2. Navigasikan ke direktori `TaskManager`.
3. Jalankan perintah berikut:

    ```bash
    python -m unittest test.test_task_manager
    ```

Skrip ini akan menjalankan semua pengujian yang didefinisikan dalam file `test_task_manager.py`.

## Implementasi Design Pattern Singleton

```python
class TaskManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

```
Penjelasan:

1. `class TaskManager`: Ini adalah definisi kelas TaskManager.

2. `_instance = None`: Variabel kelas yang digunakan untuk menyimpan instance tunggal dari kelas TaskManager.

3. `def __new__(cls, *args, **kwargs)`: Metode khusus `__new__` dipanggil saat mencoba membuat instance kelas. Di sini, kita memeriksa apakah `_instance` sudah ada. Jika belum, kita membuat instance menggunakan `super().__new__(cls)` dan menyimpannya di `_instance`. Jika sudah ada, kita hanya mengembalikan instance yang sudah ada.


```python
def __init__(self, data_file):
    if not hasattr(self, 'initialized'):
        self.data_file = data_file
        self.tasks = self.load_tasks()
        self.initialized = True
```

Penjelasan:

1. `def __init__(self, data_file)`: Metode inisialisasi kelas yang dipanggil setelah instance dibuat. Di sini, kita menggunakan atribut `initialized` untuk memeriksa apakah inisialisasi kelas sudah dilakukan sebelumnya.

2. `if not hasattr(self, 'initialized')`: Kita memeriksa apakah atribut `initialized` sudah ada di dalam instance saat ini. Jika tidak, artinya inisialisasi belum dilakukan sebelumnya, dan kita melanjutkan dengan inisialisasi kelas.

3. Jika inisialisasi belum dilakukan, kita mengatur atribut `data_file` untuk menyimpan lokasi file data, memuat daftar tugas menggunakan metode `load_tasks()`, dan mengatur `initialized` ke `True` untuk menandai bahwa inisialisasi telah selesai.