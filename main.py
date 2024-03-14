from tasks.task_manager import TaskManager

def main():
    task_manager = TaskManager('data/tasks.json')
    while True:
        print("\nTask Manager")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Tugas Selesai")
        print("4. Exit")

        pilihan = input("Masukkan Pilihan: ")

        if pilihan == '1':
            tasks = task_manager.view_tasks()
            if tasks:
                print("Tugas:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['title']} - {'Selesai' if task['completed'] else 'Proses'}")
            else:
                print("Tidak ada tugas yang tersedia")

        elif pilihan == '2':
            title = input("Masukkan Tugas: ")
            task_manager.add_task({'title': title, 'completed': False})
            print("Tugas Berhasil Ditambahkan")

        elif pilihan == '3':
            tasks = task_manager.view_tasks()
            if tasks:
                print("Pilih tugas yang akan ditandai selesai:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['title']}")
                try:
                    task_title = input("Masukkan judul tugas: ")
                    task_index = next((index for index, task in enumerate(tasks) if task['title'] == task_title), None)
                    if task_index is not None:
                        task_manager.complete_task(task_index)
                        print("Tugas Berhasil Ditandai Selesai")
                    else:
                        print("Tugas tidak ditemukan")
                except ValueError:
                    print("Salah Masukkan, Tolong Inputkan Judul Tugas")

        elif pilihan == '4':
            break

        else:
            print("Pilihan gagal, Coba Lagi")

if __name__ == "__main__":
    main()
