import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from school.models import Teacher, Student


def get_students_by_teacher(teacher_name):
    students = Student.objects.filter(teacher__name__icontains=teacher_name)

    if not students:
        print("Ничего не найдено")
        return

    for s in students:
        print(f"{s.name} ({s.group}) — {s.teacher.name}")


if __name__ == "__main__":
    name = input("Введите имя учителя: ")
    get_students_by_teacher(name)

