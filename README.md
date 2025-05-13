# Запуск smtp сервера и отправка email

## 📦 Установка

1. скачайте Docker
2. ```bash
   docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev
   ```

3. ```bash
   git clone https://github.com/vikachernenko/project_with_email
   cd ваш-репозиторий
   ```

4. переключитесь на ветку templates

## 🛠 Использование

```python
python main.py --input example.jpg
```

- после использования не забудьте завершить использование контейнера в Docker
