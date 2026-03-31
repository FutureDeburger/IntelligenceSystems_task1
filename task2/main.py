import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Задача 3.2. Экспорт минеральных удобрений.csv', sep=';', decimal=',')

df_long = df.melt(
    id_vars=["Минеральные удобрения", "Страны", "Год"],
    var_name="Месяц",
    value_name="Объем"
)
# print(df_long)



# Зависимость суммарного объёма по странам и типам удобрений

# cube1 = pd.pivot_table(
#     df_long,
#     values="Объем",
#     index=["Страны"],
#     columns=["Минеральные удобрения"],
#     aggfunc="sum"
# )

# # cube1.to_csv('cube1.csv', sep=';', decimal=',')
# # print(f"{cube1}\n")
# cube_percent = cube1.div(cube1.sum(axis=1), axis=0) * 100
# # print(f"{cube_percent}\n")
# cube_percent_1 = f"{(cube1 / cube1.values.sum() * 100).round(2)}"
# # print(f"{cube_percent_1}\n")
#
# # Визуализация
# cube1.plot(kind='bar', figsize=(10,6))
# plt.ylabel("Объем экспорта")
# plt.title("Экспорт минеральных удобрений по странам и типам")
# plt.xticks(rotation=0)
# plt.legend(title="Тип удобрений")
# plt.grid(True)
# # plt.show()



# Зависимость суммарного объёма удобрений по годам и по странам

# cube2 = pd.pivot_table(
#     df_long,
#     values="Объем",
#     index=["Год", "Страны"],
#     columns=["Минеральные удобрения"],
#     aggfunc="sum"
# )
# print(cube2)
# cube2.to_csv("cube2.csv", sep=';', decimal=',')


# Визуализация
# df_far = cube2.loc[(slice(None), "Дальнего зарубежья"), :]
# df_far.index = df_far.index.droplevel(1)
#
# df_far.plot(kind='line', marker='o', figsize=(10,6))
# plt.title("Динамика экспорта (Дальнее зарубежье)")
# plt.ylabel("Объем")
# plt.xticks(df_far.index)
# plt.grid(True)
# plt.show()
#
#
#
# df_far = cube2.loc[(slice(None), "СНГ (без России)"), :]
# df_far.index = df_far.index.droplevel(1)
#
# df_far.plot(kind='line', marker='o', figsize=(10,6))
# plt.title("Динамика экспорта (СНГ (без России))")
# plt.ylabel("Объем")
# plt.xticks(df_far.index)
# plt.grid(True)
# plt.show()


# cube_reset = cube2.reset_index()
# sns.lineplot(
#     data=cube_reset,
#     x="Год",
#     y="Калийные",
#     hue="Страны",
#     marker="o"
# )
# plt.title("Сравнение стран по калийным удобрениям")
# plt.show()



# Анализ среднего экспорта по странам и месяцам

# cube3 = pd.pivot_table(
#     df_long,
#     values="Объем",
#     index=["Страны", "Месяц"],
#     columns=["Минеральные удобрения"],
#     aggfunc="mean"
# )
# print(cube3)
# cube3.to_csv("cube3.csv", sep=';', decimal=',')


# Визуализация
# months_order = [
#     "январь","февраль","март","апрель","май","июнь",
#     "июль","август","сентябрь","октябрь","ноябрь","декабрь"
# ]
#
# # Дальнее зарубежье
# df_far = cube3.loc["Дальнего зарубежья"]
# df_far = df_far.reindex(months_order)
#
# # СНГ
# df_cis = cube3.loc["СНГ (без России)"]
# df_cis = df_cis.reindex(months_order)
#
# # График для Дальнего зарубежья
# df_far.plot(kind='bar', figsize=(12,6))
# plt.title("Экспорт удобрений по месяцам (Дальнее зарубежье)")
# plt.ylabel("Средний объем")
# plt.xticks(rotation=45)
# plt.legend(title="Тип удобрения")
# plt.tight_layout()
# plt.show()
#
# # График для СНГ
# df_cis.plot(kind='bar', figsize=(12,6))
# plt.title("Экспорт удобрений по месяцам (СНГ без России)")
# plt.ylabel("Средний объем")
# plt.xticks(rotation=45)
# plt.legend(title="Тип удобрения")
# plt.tight_layout()
# plt.show()


# Куб экспорта по типам удобрений по годам (в процентах)

# cube4 = pd.pivot_table(
#     df_long,
#     values="Объем",
#     index=["Год"],
#     columns=["Минеральные удобрения"],
#     aggfunc="sum"
# )

# cube4_percent = (cube4.div(cube4.sum(axis=1), axis=0) * 100).round(2)
# print(cube4_percent)
# cube4_percent.to_csv("cube4.csv", sep=';', decimal=',')
#
#
# # Визуализация
# cube4_percent.plot(figsize=(10,6), marker='o')
# plt.title("Структура экспорта минеральных удобрений по годам")
# plt.ylabel("Доля (%)")
# plt.xlabel("Год")
# plt.xticks(cube4_percent.index)
# plt.legend(title="Тип удобрения")
# plt.grid(True)
# # plt.show()
#
#
# cube4_percent.plot(kind='area', stacked=True, figsize=(10,6))
# plt.title("Изменение структуры экспорта удобрений")
# plt.ylabel("Доля (%)")
# plt.xlabel("Год")
# plt.xticks(cube4_percent.index)
# plt.legend(title="Тип удобрения")
# # plt.show()

