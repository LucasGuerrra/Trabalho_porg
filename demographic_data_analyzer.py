import pandas as pd


def calculate_demographic_data(print_data=True):
    import pandas as pd

    filename = '/content/census_data.xlsx'
    d = pd.read_excel(filename)

    race_count = {}
    first = True
    for i in range(len(d.iloc[:,8])):
        if d.iloc[i,8] not in races:
            races[d.iloc[i,8]] = 1
            continue
        races[d.iloc[i,8]] += 1

    man = 0
    average_age_men = 0
    for i in range(len(d.iloc[:,0])):
        if d.iloc[i,9] == 'Male':
            man += 1
            average_age_men += d.iloc[i,0]

    if man == 0:
    man = 1

    average_age_men /= man

    percentage_bachelors = 0
    for diploma in d.iloc[:,3]:
        if diploma == 'Bachelors':
            percentage_bachelors += 1
    percentage_bachelors /= len(d.iloc[:,3])
    percentage_bachelors *= 100

    he = 0
    le = 0
    higher_education_rich = 0
    lower_education_rich = 0
    for diploma in d.iloc[:,3]:
        if diploma == 'Bachelors' or diploma == 'Masters' or diploma == 'Doctorate':
            he += 1
            if d.iloc[i,14] == '>=50K':
                higher_education_rich += 1
    else:
        if d.iloc[i,14] == '>=50K':
            lower_education_rich += 1

    if he == 0:
        he = 1
    if le == 0:
        le = 1

    higher_education_rich /= he
    higher_education_rich *= 100
    lower_education_rich /= len(d.iloc[:,3]) - he
    lower_education_rich *= 100

    min_work_hours = d.iloc[:,12].min()

    minimo = d.iloc[:,12].min()
    t = 0
    regular = 0
    for i in range(len(d.iloc[:,12])):
        if d.iloc[i,12] >= min_work_hours:
            t += 1
            if d.iloc[i,14] == '>=50K':
                regular += 1

    if t == 0:
        t = 1

    rich_percentage /= t
    rich_percentage *= 100

    highest_earning_country = {}
    highest_earning_country_percentage = {}
    for i in range(len(d.iloc[:,14])):
    if d.iloc[i,14] == '>=50K':
        if d.iloc[i,13] not in highest_earning_country:
        highest_earning_country[d.iloc[i,13]] = 1
        highest_earning_country_dinehiro[d.iloc[i,13]] = 1
        continue
        highest_earning_country[d.iloc[i,13]] += 1
        highest_earning_country_dinehiro[d.iloc[i,13]] += 1

    for pais in highest_earning_country:
        highest_earning_country[pais] /= highest_earning_country_percentage[pais]
        highest_earning_country[pais] *= 100

    top_IN_occupation = {}
    for i in range(len(d.iloc[:,13])):
    if d.iloc[i,13] == 'India' and d.iloc[i,14] == '>=50K':
        if d.iloc[i,6] not in top_IN_occupation:
            top_IN_occupation[d.iloc[i,6]] = 1
            continue
        top_IN_occupation[d.iloc[i,6]] += 1

    maior = 0
    valor = 0
    for ocupacion in top_IN_occupation:
        if top_IN_occupation[ocupacion] > maior:
            maior = top_IN_occupation[ocupacion]
            valor = top_IN_occupation

    top_IN_occupation = valor

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
