# Задание 2.2 — M2M relations

## Что сделано

- Созданы модели Article и Tag
- Реализована связь ManyToManyField
- Загружены данные из articles.json
- Реализован вывод тегов у статей в query.py

## Пример работы

В "Детском мире"...
  - Общество

Ученые доказали...
  - Наука

Директор ИКИ РАН...
  - Наука
  - Космос

## Как запустить

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata articles.json
python query.py
