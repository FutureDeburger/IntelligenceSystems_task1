import pandas as pd
import re
import numpy as np
from datetime import datetime



# Форматирование формата 18.09.1938

# df = pd.read_csv("birth-dates.csv")
#
# months = {
#     'янв':'01','января':'01',
#     'фев':'02','февраля':'02',
#     'мар':'03','марта':'03',
#     'апр':'04','апреля':'04',
#     'май':'05','мая':'05',
#     'июн':'06','июня':'06',
#     'июл':'07','июля':'07',
#     'авг':'08','августа':'08',
#     'сен':'09','сентября':'09',
#     'окт':'10','октября':'10',
#     'ноя':'11','ноября':'11',
#     'дек':'12','декабря':'12'
# }
#
# def normalize_date(s):
#     s = str(s).lower()
#
#     # фикс опечатки
#     s = s.replace("мак", "май")
#
#     for m, num in months.items():
#         s = s.replace(m, num)
#
#     s = re.sub(r'[^0-9]', ' ', s)
#     s = re.sub(r'\s+', ' ', s).strip()
#
#     return s
#
#
# def parse_date(s):
#     original = s
#     s = normalize_date(s)
#
#     nums = re.findall(r'\d+', s)
#
#     if len(nums) != 3:
#         return None, None, None, original
#
#     day, month, year = nums
#
#     year = int(year)
#     if year < 100:
#         year += 1900
#
#     try:
#         date = f"{year:04d}-{int(month):02d}-{int(day):02d}"
#         return day, month, year, date
#     except:
#         return None, None, None, original
#
#
# parsed = df['Дата рождения'].apply(parse_date)
#
# df[['day','month','year','birth_date']] = pd.DataFrame(parsed.tolist(), index=df.index)
# df['year'] = df['year'].astype('Int64')
# df.to_csv("birth-dates_clean.csv", index=False)
#
#
# # отображение строк Только с отформатированной датой
# mask = df[['day','month','year','birth_date']].notna().all(axis=1)
# clean_df = df[mask]
# clean_df.to_csv('birth-dates_clean_only.csv', index=False)
#
#
#
# mask_bad = df[['day','month','year','birth_date']].isna().any(axis=1)
# bad_dates_df = df[mask_bad]
# bad_dates_df.to_csv('birth-dates_unparsed.csv', index=False)


# print(df.shape)
# print(clean_df.shape)
# print(bad_dates_df.shape)



# Форматирование других форматов данных

# df = pd.read_csv('birth-dates_unparsed.csv')
#
# import pandas as pd
# import numpy as np
# import re
# from dateutil import parser
#
# data = {
#     'Дата рождения': [
#         'дата 05101986', '2-я-1990', '1947', '1951 год', '1986 Feb 10 Питер'
#     ],
#     'Имя': ['Аникита', 'Авдей', 'Адам', 'Андриян', 'Азарий']
# }
#
# # df = pd.DataFrame(data)
#
#
# def parse_birth_date(date_str):
#     date_str = str(date_str)
#
#     # удалить лишние слова
#     date_str = re.sub(r'\b(год|дата|Москва|Питер|Санкт-Петербург)\b', '', date_str, flags=re.IGNORECASE)
#     date_str = date_str.strip()
#
#     # только год
#     if re.fullmatch(r'\d{4}', date_str):
#         return np.nan, np.nan, int(date_str)
#
#     # формат 2-я-1990
#     match = re.match(r'(\d+)-[а-я]+-(\d{4})', date_str)
#     if match:
#         day, year = match.groups()
#         return int(day), np.nan, int(year)
#
#     # строго DDMMYYYY (8 цифр)
#     match = re.fullmatch(r'(\d{2})(\d{2})(\d{4})', date_str)
#     if match:
#         day, month, year = match.groups()
#         return int(day), int(month), int(year)
#
#     # строго YYYYMMDD (8 цифр)
#     match = re.fullmatch(r'(\d{4})(\d{2})(\d{2})', date_str)
#     if match:
#         year, month, day = match.groups()
#         return int(day), int(month), int(year)
#
#     # текстовый месяц
#     try:
#         dt = parser.parse(date_str, dayfirst=True, fuzzy=True)
#         has_month = bool(re.search(
#             r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|январ|февр|мар|апр|ма[йя]|июн|июл|авг|сент|окт|нояб|дек)',
#             date_str, re.IGNORECASE))
#         day = dt.day if has_month else np.nan
#         month = dt.month if has_month else np.nan
#         return day, month, dt.year
#     except:
#         # если только год остался
#         match = re.search(r'(\d{4})', date_str)
#         if match:
#             return np.nan, np.nan, int(match.group(1))
#         return np.nan, np.nan, np.nan
#
#
# df[['day', 'month', 'year']] = df['Дата рождения'].apply(lambda x: pd.Series(parse_birth_date(x)))
#
# # формируем birth_date только если есть день и месяц
# df['birth_date'] = df.apply(
#     lambda row: f"{int(row['year']):04d}-{int(row['month']):02d}-{int(row['day']):02d}"
#     if not pd.isna(row['day']) and not pd.isna(row['month']) else None, axis=1
# )
#
#
# df['year'] = df['year'].astype('Int64')
# df['month'] = df['month'].astype('Int64')
# df['day'] = df['day'].astype('Int64')
#
# df.to_csv('birth-dates_parsed_1.csv', index=False)






# Конкатенация двух таблиц

# df1 = pd.read_csv('birth-dates_parsed_1.csv')
# df2 = pd.read_csv('birth-dates_clean_only.csv')
#
#
# df_new = pd.concat([df1, df2], ignore_index=True)
# df_new = df_new.sort_values(by='Код клиента', ascending=True).reset_index(drop=True)
# df_new['month'] = df_new['month'].astype('Int64')
# df_new['day'] = df_new['day'].astype('Int64')
#
#
# df_new.to_csv('birth-dates_result1.csv', index=False)






# Проверка на аномалии в дате

# df = pd.read_csv('birth-dates_result1.csv')
#
# from datetime import datetime
#
# current_year = datetime.now().year
#
# bad_rows = df[
#     (df['day'].notna() & ~df['day'].between(1, 31)) |
#     (df['month'].notna() & ~df['month'].between(1, 12)) |
#     (df['year'].notna() & ~df['year'].between(1800, current_year))
# ].copy()
#
#
# bad_rows.to_csv('birth-dates_bad_rows.csv', index=False)

# print(bad_rows)




# Правка аномалий в дате, парсинг оставшихся ошибок


# df = pd.read_csv('birth-dates_bad_rows.csv')
#
# current_year = datetime.now().year
#
# def is_anomaly_year(year):
#     if pd.isna(year):
#         return True
#     return year > current_year or year < 1800
#
#
# # Функция для парсинга первой колонки
# def parse_date_from_first_column(value):
#     if pd.isna(value):
#         return pd.Series([None, None, None, None])
#
#     value = str(value).strip()
#
#     try:
#         # Паттерн 1: "19861005 Москва" (YYYYMMDD город)
#         match1 = re.match(r'^(\d{4})(\d{2})(\d{2})\s+(.+)$', value)
#         if match1:
#             groups = match1.groups()
#             if len(groups) >= 3:
#                 year, month, day = groups[0], groups[1], groups[2]
#
#                 # Проверяем год на аномальность
#                 year_int = int(year)
#                 month_int = int(month)
#                 day_int = int(day)
#
#                 if is_anomaly_year(year_int):
#                     # Если год аномальный, не вставляем данные
#                     return pd.Series([None, None, None, None])
#                 else:
#                     # Формат birth_date: YYYY-MM-DD
#                     birth_date = f"{year}-{month}-{day}"
#                     return pd.Series([day_int, month_int, year_int, birth_date])
#
#         # Паттерн 2: "05.10.2226" (DD.MM.YYYY)
#         match2 = re.match(r'^(\d{2})\.(\d{2})\.(\d{4})$', value)
#         if match2:
#             groups = match2.groups()
#             if len(groups) >= 3:
#                 day, month, year = groups[0], groups[1], groups[2]
#
#                 year_int = int(year)
#                 month_int = int(month)
#                 day_int = int(day)
#
#                 # Проверяем год на аномальность
#                 if is_anomaly_year(year_int):
#                     return pd.Series([None, None, None, None])
#                 else:
#                     # Формат birth_date: YYYY-MM-DD
#                     birth_date = f"{year}-{month}-{day}"
#                     return pd.Series([day_int, month_int, year_int, birth_date])
#
#         # Паттерн 3: "05.10.2226,Имя" (DD.MM.YYYY,имя)
#         match3 = re.match(r'^(\d{2})\.(\d{2})\.(\d{4})(?:,|$)', value)
#         if match3:
#             groups = match3.groups()
#             if len(groups) >= 3:
#                 day, month, year = groups[0], groups[1], groups[2]
#
#                 year_int = int(year)
#                 month_int = int(month)
#                 day_int = int(day)
#
#                 # Проверяем год на аномальность
#                 if is_anomaly_year(year_int):
#                     return pd.Series([None, None, None, None])
#                 else:
#                     # Формат birth_date: YYYY-MM-DD
#                     birth_date = f"{year}-{month}-{day}"
#                     return pd.Series([day_int, month_int, year_int, birth_date])
#
#         # Если ничего не подошло, пробуем извлечь просто 8 цифр подряд
#         match4 = re.search(r'(\d{4})(\d{2})(\d{2})', value)
#         if match4:
#             groups = match4.groups()
#             if len(groups) >= 3:
#                 year, month, day = groups[0], groups[1], groups[2]
#
#                 year_int = int(year)
#                 month_int = int(month)
#                 day_int = int(day)
#
#                 if not is_anomaly_year(year_int):
#                     birth_date = f"{year}-{month}-{day}"
#                     return pd.Series([day_int, month_int, year_int, birth_date])
#
#         # Пробуем извлечь дату в формате DD.MM.YYYY из любого места
#         match5 = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', value)
#         if match5:
#             groups = match5.groups()
#             if len(groups) >= 3:
#                 day, month, year = groups[0], groups[1], groups[2]
#
#                 year_int = int(year)
#                 month_int = int(month)
#                 day_int = int(day)
#
#                 if not is_anomaly_year(year_int):
#                     birth_date = f"{year}-{month}-{day}"
#                     return pd.Series([day_int, month_int, year_int, birth_date])
#
#     except Exception as e:
#         # В случае любой ошибки просто пропускаем строку
#         pass
#
#     return pd.Series([None, None, None, None])
#
#
#
# result = df.iloc[:, 0].apply(parse_date_from_first_column)
# df[['new_day', 'new_month', 'new_year', 'new_birth_date']] = result
#
# df['day'] = df['new_day'].astype('Int64')
# df['month'] = df['new_month'].astype('Int64')
# df['year'] = df['new_year'].astype('Int64')
# df['birth_date'] = df['new_birth_date']
#
# # Удаляем временные колонки
# df = df.drop(['new_day', 'new_month', 'new_year', 'new_birth_date'], axis=1)
#
# df.to_csv('birth-dates_fixed.csv', index=False, encoding='utf-8-sig')






# Парсинг аномальных ячеек

# df = pd.read_csv('birth-dates_fixed.csv')
#
# def extract_day_month(row):
#     # Проверяем, что в колонке 'day' пусто (NaN) и в 'Дата рождения' не пусто
#     if pd.isna(row['day']) and pd.notna(row['Дата рождения']):
#         match = re.match(r'(\d{2})\.(\d{2})\.(\d{4})', str(row['Дата рождения']))
#         if match:
#             day, month, year = match.groups()
#             row['day'] = int(day)       # день
#             row['month'] = int(month)    # месяц
#             # year оставляем пустым (или можно удалить, если требуется)
#     return row
#
# df = df.apply(extract_day_month, axis=1)
# df.to_csv('birth-dates_fixed_upt.csv', index=False)






# Конкатенация

# df_fixed = pd.read_csv('birth-dates_fixed_upt.csv')
# df_result = pd.read_csv('birth-dates_result1.csv')
#
#
# # Создаем словарь для быстрого поиска по коду клиента
# fixed_dict = {}
# for _, row in df_fixed.iterrows():
#     client_code = row['Код клиента']
#     if pd.notna(client_code):
#         # Приводим к одному типу (int)
#         try:
#             client_code = int(float(client_code))
#             fixed_dict[client_code] = {
#                 'day': row['day'] if pd.notna(row['day']) else np.nan,
#                 'month': row['month'] if pd.notna(row['month']) else np.nan,
#                 'year': row['year'] if pd.notna(row['year']) else np.nan,
#                 'birth_date': row['birth_date'] if pd.notna(row['birth_date']) else np.nan
#             }
#         except:
#             print(f"  ⚠ Проблемный код клиента: {client_code}")
#
#
# # Обновляем result1
# updated_count = 0
# not_found = []
# for idx, row in df_result.iterrows():
#     client_code = row['Код клиента']
#
#     if pd.notna(client_code):
#         try:
#             client_code = int(float(client_code))
#
#             if client_code in fixed_dict:
#                 # Обновляем данные
#                 df_result.at[idx, 'day'] = fixed_dict[client_code]['day']
#                 df_result.at[idx, 'month'] = fixed_dict[client_code]['month']
#                 df_result.at[idx, 'year'] = fixed_dict[client_code]['year']
#                 df_result.at[idx, 'birth_date'] = fixed_dict[client_code]['birth_date']
#                 updated_count += 1
#             else:
#                 not_found.append(client_code)
#         except:
#             print(f"  ⚠ Проблемный код клиента в result1: {client_code}")
#             not_found.append(client_code)
#
# output_file = 'birth_date_result1_updated.csv'
# df_result.to_csv(output_file, index=False, encoding='utf-8-sig')




# Приведение столбцов в один формат
# df = pd.read_csv('birth_date_result1_updated.csv')
# df['day'] = df['day'].astype('Int64')
# df['month'] = df['month'].astype('Int64')
# df['year'] = df['year'].astype('Int64')
#
# df.to_csv('birth_date_final.csv', index=False)



# На данный момент итоговый файл - birth_date_final.csv (отформатированы даты)



# Небольшая работа со строками
# df = pd.read_csv('birth_date_final.csv')
#
# columns_to_clean = ['Имя', 'Фамилия', 'Отчество']
#
# def clean_name(value):
#     if isinstance(value, str):
#         # Убираем пробелы в начале и конце
#         value = value.strip()
#         # Убираем кавычки, если они есть (например, "Уваровна," -> Уваровна,)
#         value = value.strip('"')
#         # Убираем запятые в конце (оставляем тире, если это часть отчества)
#         value = value.rstrip(',')
#         # Снова убираем пробелы, если они появились после удаления запятых
#         value = value.strip()
#     return value
#
# for col in columns_to_clean:
#     if col in df.columns:
#         df[col] = df[col].apply(clean_name)
#
#
# df.to_csv('birth_date_final_cleaned.csv', index=False, sep=',')







# Поиск дубликатов
# df = pd.read_csv('birth_date_final_cleaned.csv', sep=',')
#
# duplicates = df[df.duplicated(keep=False)]
#
# if len(duplicates) > 0:
#     print(f"Найдено дубликатов: {len(duplicates)} строк")
#     print("\nДубликаты:")
#     print(duplicates.to_string())
# else:
#     print("Дубликатов не найдено")




# На данный момент итоговый файл - birth_date_final_cleaned.csv


# Проверка дубликатов (пока не нужно)

# df = pd.read_csv('birth_date_final_cleaned.csv', sep=',')
#
# # Создаем колонку с полным ФИО
# df['ФИО'] = df['Фамилия'] + ' ' + df['Имя'] + ' ' + df['Отчество']
#
# # Ищем дубликаты по ФИО
# fio_duplicates = df[df.duplicated('ФИО', keep=False)]
#
# if len(fio_duplicates) > 0:
#     print(f"Найдено людей с одинаковыми ФИО: {len(fio_duplicates)} строк")
#     print("\nДубликаты по ФИО:")
#
#     # Группируем для удобства
#     for fio, group in fio_duplicates.groupby('ФИО'):
#         print(f"\n{fio}:")
#         print(group[['Код клиента', 'Дата рождения']].to_string(index=False))
# else:
#     print("Людей с одинаковыми ФИО не найдено")


# import pandas as pd
#
# df = pd.read_csv('birth_date_final_cleaned.csv', sep=',')
#
# # Создаем колонку с полным ФИО
# df['ФИО'] = df['Фамилия'] + ' ' + df['Имя'] + ' ' + df['Отчество']
#
# # Ищем дубликаты по ФИО + дате рождения
# df['ФИО_дата'] = df['ФИО'] + ' | ' + df['birth_date']
# duplicates = df[df.duplicated('ФИО_дата', keep=False)]
#
# if len(duplicates) > 0:
#     print(f"Найдено дубликатов по ФИО + дате рождения: {len(duplicates)} строк")
#     print("\nДубликаты (одинаковые люди с одинаковыми датами):")
#     print("=" * 60)
#
#     for (fio, date), group in duplicates.groupby(['ФИО', 'birth_date']):
#         print(f"\n{fio} | {date}:")
#         print(f"Коды клиентов: {', '.join(map(str, group['Код клиента'].tolist()))}")
#         print(f"Всего записей: {len(group)}")
# else:
#     print("Дубликатов по ФИО + дате рождения не найдено")
