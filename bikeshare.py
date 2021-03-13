import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True :
        city = input("Would you like to see data for Chicago, New York City, or Washington?")
        if city.lower() in CITY_DATA:
            break
        else:
            print("Not Valid input")
    # get user input for filter by month or day or not at all
    right_choice = ["month", "day", "not at all"]
    while True :
        user_choice = input("Would you like to filter the data by month, day, or not at all?")
        if user_choice.lower() in right_choice:
            break
        else:
            print("Not Valid input")
    # get user input for month (january, february, ... , june)
    available_months = ["january", "february", "march", "april", "may", "june"]
    day_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if user_choice.lower() == "month":
        day = "all"
        while True:
            month = input("Which month - January, February, March, April, May, or June?")
            if month.lower() in available_months:
                break
            else:
                print("Not Valid input")

    # get user input for day of week ( monday, tuesday, ... sunday)
    elif user_choice.lower() == "day" :
        month = "all"
        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
            if day.lower() in day_of_week:
                break
            else:
                print("Not Valid input")
    else:
        month = "all"
        day = "all"

    print('-'*40)
    city = city.lower()
    month = month.lower()
    day = day.lower()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    list_of_monthes = ["january", "february", "march", "april", "may", "june"]
    popular_month_num = df['month'].mode()[0]
    popular_month = list_of_monthes[popular_month_num - 1]

    print('Most Popular Start Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Start Day Of Week:', popular_day)
    # display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)



    # display most frequent combination of start station and end station trip
    popular_combination = ('\n From ' + df['Start Station'] + ' TO ' + df['End Station']).mode()[0]

    print('Most Popular combination of start station and end station trip:', popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types is:', user_types)

    # Display counts of gender
    if city in ['chicago', 'new york city']:
        user_gender = df['Gender'].value_counts()
        print('Counts of gender is:', user_gender)
        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].max()
        most_recent_birth = df['Birth Year'].min()
        most_common_birth = df['Birth Year'].mode()
        print('Earliest year of birth is: ', earliest_birth, '/n Most recent year of birth is: ', most_recent_birth, '/n Most common year of birth is: ', most_common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disply_row_data(df):
    i = 0
    while True:
        display_data = input("would you like want to see the raw data?Yes or No")
        if display_data.lower() == 'yes':
            print('The raw data: ', df.iloc[i:i+5])
            i += 5
        elif display_data.lower() == 'no' :
            break
        else:
            print("Not Valid input")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        disply_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()