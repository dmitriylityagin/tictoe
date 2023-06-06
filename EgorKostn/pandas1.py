import pandas as pd

# fruits = pd.DataFrame({'Apples' : [30], 'Bananas' : [31]})

fruits = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

print(fruits, '\n',  ingredients)


reviews = pd.read_csv('../data_files/winemag-data_first150k.csv', index_col=0)

print(reviews)



animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals)


animals.to_csv("cows_and_goats.csv")


print(reviews.head())
print(reviews.columns)
print(reviews.iloc[0])

print(reviews.iloc[:, 0])
print(reviews.iloc[:3, 0])
print(reviews.iloc[1:3, 0])
print(reviews.iloc[[0, 1, 2], 0])
print(reviews.iloc[-5:, 1])


print(reviews.loc[0:4, ['region_1', 'region_2', 'variety', 'winery']])








