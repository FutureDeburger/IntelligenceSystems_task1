import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (12,8)
pd.options.mode.chained_assignment = None


# df = pd.read_csv("data.csv")
# df = df.iloc[17000:18000] # Вариант 18
# print("Размер набора данных:")
# print(df.shape)
# print("\nТипы данных:")
# print(df.dtypes)




# а) ОБНАРУЖЕНИЕ ПРОПУЩЕННЫХ ДАННЫХ
# print("АНАЛИЗ ПРОПУЩЕННЫХ ДАННЫХ")


# 1) Тепловая карта пропусков
# cols = df.columns
# colours = ['#000099', '#ffff00']
# plt.figure(figsize=(14,8))
# sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours), cbar=False)
# plt.xticks(rotation=90)
# plt.title("Тепловая карта пропущенных данных")
# plt.show()


# 2) Процент пропущенных значений
# print("\nПроцент пропущенных значений:")
# list_empties = []
# for col in df.columns:
#     pct_missing = np.mean(df[col].isnull())
#     str_empties = '{} - {}%'.format(col, round(pct_missing*100))
#     # print(str_empties)
#     list_empties.append(round(pct_missing*100))
#
# sorted_list = sorted(list_empties)
# print(sorted_list)


# print("\nПроцент пропущенных значений (по убыванию):")
# empties_dict = {}
# for col in df.columns:
#     pct_missing = np.mean(df[col].isnull()) * 100
#     empties_dict[col] = round(pct_missing, 2)
#
# sorted_empties = sorted(empties_dict.items(), key=lambda x: x[1], reverse=True)
# # for col, pct in sorted_empties:
# #     print(f'{col} - {pct}%')
#
#
# threshold = 40 # Порог для удаления
# columns_to_drop = [col for col in df.columns if df[col].isnull().mean() * 100 > threshold]
# df_cleaned = df.drop(columns=columns_to_drop)

# print(f"Удалено столбцов: {len(columns_to_drop)}") # 4
# print(f"Осталось столбцов: {df_cleaned.shape[1]}") # 288

# df_cleaned.to_csv("data_without_empty_cols.csv", index=False) # сохраняю файл без пустых столбцов


# 3) Гистограмма пропущенных данных
# for col in df.columns:
#     missing = df[col].isnull()
#     num_missing = np.sum(missing)
#     if num_missing > 0:
#         df[col + "_ismissing"] = missing
#
# ismissing_cols = [col for col in df.columns if "ismissing" in col]
# df["num_missing"] = df[ismissing_cols].sum(axis=1)
# df["num_missing"].value_counts().sort_index().plot.bar()
# plt.title("Гистограмма количества пропусков в строках")
# # plt.show()


# def create_hist_empties_in_strings(table_data):
#     df_result = table_data.copy()
#
#     for _ in df_result.columns:
#         missing = df_result[_].isnull()
#         num_missing = np.sum(missing)
#         if num_missing > 0:
#             df_result[_ + "_ismissing"] = missing
#
#     ismissing_cols = [_ for _ in df_result.columns if "ismissing" in _]
#     df_result["num_missing"] = df_result[ismissing_cols].sum(axis=1)
#
#     df_result["num_missing"].value_counts().sort_index().plot.bar()
#     plt.title("Гистограмма количества пропусков в строках")
#     plt.show()
#
#     return df_result

# df_with_stats_1 = create_hist_empties_in_strings(df_cleaned)



# for col in df_cleaned.columns:
#     missing = df_cleaned[col].isnull()
#     num_missing = np.sum(missing)
#     if num_missing > 0:
#         df_cleaned[col + "_ismissing"] = missing
#
# ismissing_cols = [col for col in df_cleaned.columns if "ismissing" in col]
# df_cleaned["num_missing"] = df_cleaned[ismissing_cols].sum(axis=1)
# df_cleaned["num_missing"].value_counts().sort_index().plot.bar()
# plt.title("Гистограмма количества пропусков в строках")
# plt.show()




# Удаляем строки с 16 и более пропусками
# df_without_empties_in_strings = df_with_stats_1[df_with_stats_1["num_missing"] < 16].copy()
#
# print(f"Всего строк в df_cleaned: {len(df_with_stats_1)}")
# print(f"Строк с 16+ пропусками: {(df_with_stats_1['num_missing'] >= 16).sum()}")
# print(f"Осталось строк после удаления: {len(df_without_empties_in_strings)}")
#
# # Удаляем временные колонки с индикаторами пропусков
# df_without_empties_in_strings = df_without_empties_in_strings.drop(columns=[col for col in df_without_empties_in_strings.columns if "ismissing" in col or col in ["num_missing", "missing_percent"]])
# print(f"\nФинальный датасет: {df_without_empties_in_strings.shape}")
#
#
# # df_with_stats_2 = create_hist_empties_in_strings(df_without_empties_in_strings)
#
# df_with_drop_cols_n_rows = df_without_empties_in_strings.copy()
# df_with_drop_cols_n_rows.to_csv("data_with_drop_cols_n_rows.csv", index=False)



# 4) Обработка пропусков
# Заполнение пропущенных значений медианой
# df = pd.read_csv("data_with_drop_cols_n_rows.csv")
# numeric_cols = df.select_dtypes(include=[np.number]).columns
# for col in numeric_cols:
#     if df[col].isnull().sum() > 0:
#         med = df[col].median()
#         df[col] = df[col].fillna(med)
#
# df_new = df.copy()
# df_new.to_csv("data_filled_cols_n_rows.csv", index=False)
# print(df.shape)


# тепловая карта для наглядности того, что таблица теперь заполнена
# cols = df_new.columns
# colours = ['#000099', '#ffff00']
# plt.figure(figsize=(14,8))
# sns.heatmap(df_new[cols].isnull(), cmap=sns.color_palette(colours), cbar=False)
# plt.xticks(rotation=90)
# plt.title("Тепловая карта пропущенных данных")
# plt.show()




# б) ПОИСК ВЫБРОСОВ
# print("АНАЛИЗ ВЫБРОСОВ")

# df = pd.read_csv("data_filled_cols_n_rows.csv")
# print(df.shape)
# main_feature = "price_doc"

# if main_feature in df.columns:
    # print("\nОписательная статистика price_doc")
    # print(df[main_feature].describe())

    # гистограмма
    # df[main_feature].hist(bins=100)
    # plt.title("Гистограмма признака price_doc")
    # plt.show()


    # boxplot
    # df.boxplot(column=[main_feature])
    # plt.title("Boxplot признака price_doc")
    # plt.show()


# print(df.loc[df["full_sq"] < 15, "full_sq"])
# print(df.loc[df["price_doc"] < 1000000, ["price_doc", "full_sq", "build_year"]])
# print(df.loc[df["price_doc"] > 40000000, ["price_doc", "full_sq", "build_year"]])


# Удаление строк, в которых price_doc < 1 000 000
# mask = df["price_doc"] >= 1000000
#
# df_cleaned = df[mask].copy()
#
# print(f"Было строк: {len(df)}")
# print(f"Стало строк: {len(df_cleaned)}")
# print(f"Удалено строк: {len(df) - len(df_cleaned)}")
# print(df_cleaned.shape)
#
# df_after_emissions = df_cleaned.copy()
# df_after_emissions.to_csv("data_after_emissions.csv", index=False)
# print(df_after_emissions.shape)






# в) ПОИСК НЕНУЖНЫХ ДАННЫХ
# print("ПОИСК НЕИНФОРМАТИВНЫХ ПРИЗНАКОВ")

# df = pd.read_csv("data_after_emissions.csv")
# print(df.shape)

# num_rows = len(df)
# low_information_cols = []
# df: pd.DataFrame
#
# for col in df.columns:
#     counts = df[col].value_counts(dropna=False)
#
#     top_pct = (counts / num_rows).iloc[0]
#     if top_pct > 0.95:
#         low_information_cols.append(col)
#         print(col, df[col].dtype, " - ", round(top_pct*100,2), "% одинаковых значений")



# удаляем неинформативные признаки
# df = pd.read_csv("data_after_emissions.csv")
# print("До удаления:", df.shape)
#
# # Удаляем ненужные колонки
# cols_to_remove = [
#     'cafe_count_500_price_high',
#     'mosque_count_500',
#     'cafe_count_1000_price_high',
#     'mosque_count_1000',
#     'mosque_count_1500'
# ]
#
# df = df.drop(columns=cols_to_remove)
# print("После удаления:", df.shape)
#
# df.to_csv("data_deleted_duplicates.csv", index=False)
# print(df.shape)



# ------------------------------
# поиск дубликатов
# ------------------------------

# print("\nПроверка дубликатов")
# print("Размер до удаления:", df.shape)
# df = df.drop_duplicates()
# print("Размер после удаления:", df.shape)


# key = ['timestamp', 'full_sq', 'life_sq', 'floor', 'build_year', 'num_room', 'price_doc']
# df_dedupped2 = df.drop_duplicates(subset=key)
#
# print(df.shape)
# print(df_dedupped2.shape)





# г) НЕСОГЛАСОВАННЫЕ ДАННЫЕ
# print("ПРОВЕРКА НЕСОГЛАСОВАННЫХ ДАННЫХ")

# df = pd.read_csv("data_deleted_duplicates.csv")
# print(df.shape)
#
# str_columns = df.select_dtypes(include=['object']).columns.tolist()
# print(f"Всего найдено: {len(str_columns)} столбцов\n")
# for i, col in enumerate(str_columns, 1):
#     print(f"{i:2d}. {col}")
# print(str_columns)
#
#
# for col in str_columns:
#     df[col] = df[col].astype(str).str.lower()
# df.to_csv("data_after_lowercase.csv", index=False)



# df = pd.read_csv("data_after_lowercase.csv")
# print(df.shape)
#
# if 'timestamp' in df.columns:
#
#     # Преобразуем в datetime
#     df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d')
#
#     # Создаем новые столбцы
#     df['year'] = df['timestamp'].dt.year
#     df['month'] = df['timestamp'].dt.month
#     df['day'] = df['timestamp'].dt.day
#     df['weekday'] = df['timestamp'].dt.weekday
#
# df.to_csv("data_final.csv", index=False)
#
# print(df.shape)