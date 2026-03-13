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


# cols = df_new.columns
# colours = ['#000099', '#ffff00']
# plt.figure(figsize=(14,8))
# sns.heatmap(df_new[cols].isnull(), cmap=sns.color_palette(colours), cbar=False)
# plt.xticks(rotation=90)
# plt.title("Тепловая карта пропущенных данных")
# plt.show()




# б) ПОИСК ВЫБРОСОВ
# print("АНАЛИЗ ВЫБРОСОВ")

#
#
# main_feature = "full_sq"
#
# if main_feature in df_new.columns:
#     print("\nОписательная статистика full_sq")
#     print(df_new[main_feature].describe())
#
#     # гистограмма
#     df_new[main_feature].hist(bins=100)
#     plt.title("Гистограмма признака full_sq")
#     # plt.show()
#
#     # boxplot
#     df_new.boxplot(column=[main_feature])
#     plt.title("Boxplot признака full_sq")
#     # plt.show()
#
#
# # print(df_new.loc[df_new["full_sq"] < 10, "full_sq"])
# # print(df_new.loc[df_new["price_doc"] < 1000000, "price_doc"])
#
#
# indices_to_drop = df_new[df_new["full_sq"] < 10].index
# df_new = df_new.drop(indices_to_drop)
# df_new.to_csv("output_new.csv", index=False)
# # print(df_new.shape)



# # ==========================================================
# # в) ПОИСК НЕНУЖНЫХ ДАННЫХ
# # ==========================================================
# # print("\n==============================")
# # print("ПОИСК НЕИНФОРМАТИВНЫХ ПРИЗНАКОВ")
# # print("==============================")
#
# num_rows = len(df_new)
# low_information_cols = []
# df_new: pd.DataFrame
#
# for col in df_new.columns:
#     counts = df_new[col].value_counts(dropna=False)
#
#     top_pct = (counts / num_rows).iloc[0]
#     if top_pct > 0.95:
#         low_information_cols.append(col)
#         print(col, df_new[col].dtype, " - ", round(top_pct*100,2), "% одинаковых значений")
#
# # удаляем неинформативные признаки
# if len(low_information_cols) > 0:
#     df_new = df_new.drop(low_information_cols, axis=1)
#
# # ------------------------------
# # поиск дубликатов
# # ------------------------------
#
# print("\nПроверка дубликатов")
# print("Размер до удаления:", df.shape)
# df = df.drop_duplicates()
# print("Размер после удаления:", df.shape)


# # ==========================================================
# # г) НЕСОГЛАСОВАННЫЕ ДАННЫЕ
# # ==========================================================
#
# print("\n==============================")
# print("ПРОВЕРКА НЕСОГЛАСОВАННЫХ ДАННЫХ")
# print("==============================")
#
# # ------------------------------
# # приведение текста к нижнему регистру
# # ------------------------------
#
# if "sub_area" in df.columns:
#
#     df["sub_area"] = df["sub_area"].str.lower()
#
#     print("Колонка sub_area приведена к нижнему регистру")
#
#
# # ------------------------------
# # преобразование даты
# # ------------------------------
#
# if "timestamp" in df.columns:
#
#     df["timestamp"] = pd.to_datetime(df["timestamp"])
#
#     df["year"] = df["timestamp"].dt.year
#     df["month"] = df["timestamp"].dt.month
#
#     print("Дата преобразована в формат datetime")
#
#
# # ==========================================================
# # ИТОГ
# # ==========================================================
#
# print("\n==============================")
# print("ОЧИСТКА ДАННЫХ ЗАВЕРШЕНА")
# print("==============================")
#
# print("Финальный размер датасета:")
# print(df.shape)