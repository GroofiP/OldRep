import pandas as pd

data = pd.read_csv('titanic.csv')

print(data.head(10))
print(data.describe())
print(data["Age"].head().sort_values())


# def age_category(data_base):
#     age_categories = []
#     for a in data_base["Age"]:
#         if a < 18:
#             age_categories.append(0)
#         elif 18 <= a < 30:
#             age_categories.append(1)
#         elif 30 <= a < 50:
#             age_categories.append(2)
#         elif a >= 50:
#             age_categories.append(3)
#         else:
#             age_categories.append(None)
#     data_base['age_category'] = age_categories
#     print(data_base["age_category"].head(50).sort_values())
#     data_base.drop("age_category", axis=1)

# def age_category(a):
#     if a < 18:
#         return 0
#     elif 18 <= a < 30:
#         return 1
#     elif 30 <= a < 50:
#         return 2
#     elif a >= 50:
#         return 3
#     else:
#         return a


# data['Age_category'] = data['Age'].apply(age_category)
# print(data['Age_category'].head(100))
