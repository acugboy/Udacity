import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_item(input_print, error_input, input_list):
    while True:
        s = input(input_print).lower()
        if s in input_list:
            return s
        else:
            print(error_input)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    city = get_item('Please input the name of the city you want to analyze:(chicago, new york city, washington)\n',
        'Please input the correct city name:(chicago, new york city, washington)\n',
        ['chicago', 'new york city', 'washington'])

    month = get_item('Please input the month you want to analyze:(all,1,2,3,4,5,6)\n',
        'Please input the correct month:(all,1,2,3,4,5,6)\n',
        ['all', '1', '2', '3', '4', '5', '6'])

    day = get_item('Please input what day of the week you want to analyze:(all, 1, 2, 3, 4, 5, 6, 7)\n',
        'Please enter the correct day of the week:(all, 1, 2, 3, 4, 5, 6, 7)\n',
        ['all', '1', '2', '3', '4', '5', '6', '7'])

    print('-'*40)
    return city, month, day

#利用时间元祖—获取月份
def struct_month(times):
    return time.strptime(times, '%Y-%m-%d  %H:%M:%S').tm_mon
#利用时间元祖——获取星期几
def struct_wday(times):
    return time.strptime(times, '%Y-%m-%d  %H:%M:%S').tm_wday + 1
#利用时间元祖——获取小时
def struct_hour(times):
    return time.strptime(times, '%Y-%m-%d  %H:%M:%S').tm_hour

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

#判断是否需要过滤月份和星期几
    if month != 'all':
        df = df[df['Start Time'].apply(struct_month) == int(month)]
    if day != 'all':
        df = df[df['Start Time'].apply(struct_wday) == int(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nthe most common month...\n',
        pd.value_counts((df['Start Time'].apply(struct_month)).values,sort=False).idxmax())


    # TO DO: display the most common day of week
    print('\nthe most common day of week...\n',
        pd.value_counts((df['Start Time'].apply(struct_wday)).values,sort=False).idxmax())


    # TO DO: display the most common start hour
    print('\nthe most common start hour...\n',
        pd.value_counts((df['Start Time'].apply(struct_hour)).values,sort=False).idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station:\n',
        pd.value_counts(df['Start Station'].values,sort=False).idxmax())


    # TO DO: display most commonly used end station
    print('The most commonly used end station:\n',
        pd.value_counts(df['End Station'].values,sort=False).idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination stations:\n',
        pd.value_counts((df['Start Station'] + ' to ' + df['End Station']).values,sort=False).idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time:\n',df['Trip Duration'].sum())



    # TO DO: display mean travel time
    print('The mean travel time:\n',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types:\n',pd.value_counts(df['User Type'].values,sort=False))


    try:
        # TO DO: Display counts of gender
        print('The counts of gender:\n',pd.value_counts(df['Gender'].values,sort=False))

        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth:\n',df['Birth Year'].min())
        print('The most recent year of birth:\n',df['Birth Year'].max())
        print('The most common year of birth:\n',pd.value_counts(df['Birth Year'].values,sort=False).idxmax())

    except KeyError:
        pass


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
