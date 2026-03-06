import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (12,8)
pd.options.mode.chained_assignment = None


df = pd.read_csv("data.csv")
df = df.iloc[17000:18000] # Вариант 18
# print("Размер набора данных:")
# print(df.shape)
# print("\nТипы данных:")
# print(df.dtypes)


# ==========================================================
# а) ОБНАРУЖЕНИЕ ПРОПУЩЕННЫХ ДАННЫХ
# ==========================================================

# print("\n==============================")
# print("АНАЛИЗ ПРОПУЩЕННЫХ ДАННЫХ")
# print("==============================")

# 1) Тепловая карта пропусков
cols = df.columns
colours = ['#000099', '#ffff00']
plt.figure(figsize=(14,8))
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours), cbar=False)
plt.xticks(rotation=90)
plt.title("Тепловая карта пропущенных данных")
# plt.show()

# 2) Процент пропущенных значений
# print("\nПроцент пропущенных значений:")
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    # print('{} - {}%'.format(col, round(pct_missing*100)))

# 3) Гистограмма пропущенных данных
for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(missing)
    if num_missing > 0:
        df[col + "_ismissing"] = missing

ismissing_cols = [col for col in df.columns if "ismissing" in col]
df["num_missing"] = df[ismissing_cols].sum(axis=1)
df["num_missing"].value_counts().sort_index().plot.bar()
plt.title("Гистограмма количества пропусков в строках")
# plt.show()

# 4) Обработка пропусков
# Заполнение пропущенных значений медианой
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        med = df[col].median()
        df[col] = df[col].fillna(med)

df_new = df.copy()
df_new = df_new.iloc[:, :292]
df_new.to_csv("output_new.csv", index=False)
# print(df_new.shape)


# ==========================================================
# б) ПОИСК ВЫБРОСОВ
# ==========================================================
# print("\n==============================")
# print("АНАЛИЗ ВЫБРОСОВ")
# print("==============================")


main_feature = "full_sq"

if main_feature in df_new.columns:
    print("\nОписательная статистика full_sq")
    print(df_new[main_feature].describe())

    # гистограмма
    df_new[main_feature].hist(bins=100)
    plt.title("Гистограмма признака full_sq")
    # plt.show()

    # boxplot
    df_new.boxplot(column=[main_feature])
    plt.title("Boxplot признака full_sq")
    # plt.show()

print(df_new.loc[df_new["full_sq"] > 200, "full_sq"])



# # ==========================================================
# # в) ПОИСК НЕНУЖНЫХ ДАННЫХ
# # ==========================================================
#
# print("\n==============================")
# print("ПОИСК НЕИНФОРМАТИВНЫХ ПРИЗНАКОВ")
# print("==============================")
#
# num_rows = len(df)
#
# low_information_cols = []
#
# for col in df.columns:
#
#     counts = df[col].value_counts(dropna=False)
#
#     top_pct = (counts / num_rows).iloc[0]
#
#     if top_pct > 0.95:
#
#         low_information_cols.append(col)
#
#         print(col, " - ", round(top_pct*100,2), "% одинаковых значений")
#
#
# # удаляем неинформативные признаки
#
# if len(low_information_cols) > 0:
#
#     df = df.drop(low_information_cols, axis=1)
#
#
# # ------------------------------
# # поиск дубликатов
# # ------------------------------
#
# print("\nПроверка дубликатов")
#
# print("Размер до удаления:", df.shape)
#
# df = df.drop_duplicates()
#
# print("Размер после удаления:", df.shape)
#
#
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