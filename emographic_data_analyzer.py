import pandas as pd

def calculate_demographic_data(print_data=True):
  df = pd.read_csv("adult.data.csv")
    race_count =df['race'].value_counts()
    print("Number of each race:",race_count)

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex']=='Male'.'age']).mean(),1)
    print("Avearage age of men:",average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education']=='Bachelors'])/len(df)*100,1)
    print("percentage with Bachelors degrees:{percentage_bachelors}%")
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education["income"]==">50k"])/len(higher_education)*100,1)
    print(f"Percentage with higher education that earn >50k:{higher_education_rich}%")
    lower_education_rich = round(len(lower_education[lower_education["income"]==">50k"])/len(lower_education)*100,1)
    print(f"Percentage without higher education that  earn >50k:{lower_education}%")

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = len(df[df['hours.per.week'] == min_work_hours])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =  len(df[df['hours.per.week'] == min_work_hours])

    rich_percentage = round(len(df[(df['hours.per.week'] == min_work_hours) & (df['income'] == '>50K')]) / num_min_workers * 100, 1)
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country =(df.loc[df['income'] == ">50K", 'native.country'].value_counts() / df['native.country'].value_counts()).fillna(0).sort_values(ascending=False).index[0]
    highest_earning_country_percentage = round(len(df[(df['native.country'] == highest_earning_country) & (df['income'] == '>50K')]) / len(df[df['native.country'] == highest_earning_country]) * 100, 1)
    print("Country with highest percentage of rich:", highest_earning_country)
   print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['income'] == ">50K") & (df['native.country'] == "India")]["occupation"].value_counts().index[0]
print("Top occupations in India:", top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
