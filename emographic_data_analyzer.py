import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):

    df = pd.read_csv('adult.data.csv', header=None, names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(df['education'].value_counts()['Bachelors'] / len(df) * 100, 1)
  
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich_percentage = round(len(higher_education_rich) / len(higher_education) * 100, 1)

    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    lower_education_rich_percentage = round(len(lower_education_rich) / len(lower_education) * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_min_workers_percentage = round(len(rich_min_workers) / len(num_min_workers) * 100, 1)

    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = round((df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100, 1)

    top_IN_occupation = df[df['native-country'] == 'India'][df['salary'] == '>50K']['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:n", race_count) 
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich_percentage)
        print("Percentage without higher education that earn >50K:", lower_education_rich_percentage)
        print("Min work hours:", min_work_hours)
        print("Percentage of rich who work minimum hours:", rich_min_workers_percentage)
        print("Country with highest percentage of rich:", highest_earning_country, highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count.to_dict(),
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich_percentage': higher_education_rich_percentage,
        'lower_education_rich_percentage': lower_education_rich_percentage,
        'min_work_hours': min_work_hours,
        'rich_min_workers_percentage': rich_min_workers_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
  
    in_work_hours,
        'rich_min_workers_percentage': rich_min_workers_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
