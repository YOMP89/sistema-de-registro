import sqlite3

class StudentRegistrationSystem:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        ''')
        self.conn.commit()

    def add_student(self, name, age, grade):
        self.cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)',
                            (name, age, grade))
        self.conn.commit()
        print(f"Estudiante {name} agregado exitosamente.")

    def get_all_students(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def get_student(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        return self.cursor.fetchone()

    def update_student(self, student_id, name, age, grade):
        self.cursor.execute('''
            UPDATE students
            SET name = ?, age = ?, grade = ?
            WHERE id = ?
        ''', (name, age, grade, student_id))
        self.conn.commit()
        print(f"Estudiante con ID {student_id} actualizado exitosamente.")

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.conn.commit()
        print(f"Estudiante con ID {student_id} eliminado exitosamente.")

    def close_connection(self):
        self.conn.close()

def main():
    srs = StudentRegistrationSystem()

    while True:
        print("\n1. Agregar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Ver estudiante por ID")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            name = input("Nombre del estudiante: ")
            age = int(input("Edad del estudiante: "))
            grade = input("Grado del estudiante: ")
            srs.add_student(name, age, grade)

        elif choice == '2':
            students = srs.get_all_students()
            for student in students:
                print(student)

        elif choice == '3':
            student_id = int(input("ID del estudiante: "))
            student = srs.get_student(student_id)
            if student:
                print(student)
            else:
                print("Estudiante no encontrado.")

        elif choice == '4':
            student_id = int(input("ID del estudiante a actualizar: "))
            name = input("Nuevo nombre: ")
            age = int(input("Nueva edad: "))
            grade = input("Nuevo grado: ")
            srs.update_student(student_id, name, age, grade)

        elif choice == '5':
            student_id = int(input("ID del estudiante a eliminar: "))
            srs.delete_student(student_id)

        elif choice == '6':
            srs.close_connection()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()