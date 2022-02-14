import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    avg_age = men['age'].mean()
    average_age_men = avg_age.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    x = len(df[df['education']=="Bachelors"])
    y = len(df) 
    percentage_bachelors = round(x/y*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    he = df.query('salary == ">50K" and education in ["Bachelors","Doctorate","Masters"]').shape[0]
    total_he = df.query('education in ["Bachelors","Doctorate","Masters"]').shape[0]
    higher_education = round(he/total_he*100,1)  
    
    le = df.query('salary == ">50K" and education not in ["Bachelors","Doctorate","Masters"]').shape[0]
    total_le = df.query('education not in ["Bachelors","Doctorate","Masters"]').shape[0]
    lower_education = round(le/total_le*100,1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == 1) & (df['salary']==">50K")].shape[0]
    total_rich = df[df['hours-per-week']== 1].shape[0]
    rich_percentage = round(num_min_workers/total_rich*100,1)

    # What country has the highest percentage of people that earn >50K?
    country = df.value_counts('native-country')
    rich_countries = df.query('salary == ">50K"').value_counts("native-country")
    highest_earning_country = round(rich_countries/country*100,1).sort_values(ascending=False).keys()[0]
    highest_earning_country_percentage = round(rich_countries/country*100,1).sort_values(ascending=False)[0]


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.query('salary == ">50K" and `native-country` == "India"').value_counts('occupation').keys()[0]

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
