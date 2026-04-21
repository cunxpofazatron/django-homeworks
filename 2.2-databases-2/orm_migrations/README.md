# Задание 2.2 — ORM migrations

## Что сделано

- Созданы модели Teacher и Student
- Реализована связь ForeignKey (Student → Teacher)
- Выполнены миграции
- Загружены данные из school.json
- Реализованы ORM-запросы в query.py

## Пример работы

Вывод студентов по учителю:

Алексей (10А) — Иван
Мария (10А) — Иван
Олег (11Б) — Петр

## Как запустить

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata school.json
python query.py
