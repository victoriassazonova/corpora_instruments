# Репозиторий для проекта "Инструменты для создания корпуса литературных текстов на малоресурсных языках"
## Файлы:
* [парсер файлов формата .xml, извлечение словаря <корень,тип>=[глосса]](https://github.com/victoriassazonova/corpora_instruments/blob/main/corpus_parser.py)
* [скрипт для транслитерации в кириллицу](https://github.com/victoriassazonova/corpora_instruments/blob/main/transliteration.py)
* [скрипт для работы с библиотекой hfst, генерация полных парадигм по лемме](https://github.com/victoriassazonova/corpora_instruments/blob/main/hfst_task)
* [извлечение списка слов с толкованиями из словаря формата .dsl](https://github.com/victoriassazonova/corpora_instruments/blob/main/dsl_dict)
* [скрипт для добавления слоя с морфологической разметкой к параллельному тексту](https://github.com/victoriassazonova/corpora_instruments/tree/main/analyze_aligned_text)
* [конвертер полученных файлов для корпуса tsakorpus](https://github.com/victoriassazonova/corpora_instruments/tree/main/customtxt2json.py)
* [словарь hunalign](https://github.com/victoriassazonova/corpora_instruments/tree/main/g.dic)
* [разбиение на предложения для hunalign](https://github.com/victoriassazonova/corpora_instruments/blob/main/split_texts.ipynb)

### Сам корпус пока доступен [здесь](https://drive.google.com/drive/folders/1LjB1m8oUrQo-YRfkNo48i9DdSsZGOpwN?usp=sharing)
#### Для запуска необходимо:
* скачать всю папку
* запустить на компьютере elasticsearch 5.5 или 5.6
* запустить скрипт indexator.py
* запустить tsakorpus.wsgi
* корпус будет доступен по адресу http://127.0.0.1:7342/search
* при возникновении необходимости, более подробные инструкции есть внутри корпуса в папке docs
![alt text](img/corpus.png "Описание будет тут")
