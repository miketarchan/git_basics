#!/usr/bin/env python3
"""Calculate deposit percent yield based on time period.
Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...
Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.
Let's implement this.
A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.
Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""
BANK_DEPOSIT_PREPOSITION_FILE_NAME = 'bank-deposit-preposition.csv'
EFFECTIVE_PERCENTS_FILE_NAME = 'effective-percents-result.txt'
USAGE = f"""
This script calculates the deposit you can earn
based on input data you provided
it also uses '{BANK_DEPOSIT_PREPOSITION_FILE_NAME}'
to calculated affective additional deposits income
by percents placed in that file
the result of script's job also storing into '{EFFECTIVE_PERCENTS_FILE_NAME}'
USAGE: initial_sum:<value> percent:<value> fixed_period:<value> set_period:<value>
"""
USAGE = USAGE.strip()


result_file = open(EFFECTIVE_PERCENTS_FILE_NAME, mode='w')

COMMON_PERIODS = {
    '1 Month': 1/12,
    '6 Months': 1/2,
    '1 Year': 1,
    '2 Years': 2,
    '5 Years': 5,
    '10 Years': 10
}


def getGrowth(percent, set_period, fixed_period):
    """Calculate growth coefficient"""
    percent = percent / 100
    return (1 + percent) ** (set_period / fixed_period)


def formatAmount(amount):
    return "{:.2f}".format(amount)


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    res = initial_sum * getGrowth(percent,
                                  fixed_period=fixed_period,
                                  set_period=set_period
                                  )
    return formatAmount(res)


def print_and_store(msg):
    print(msg)
    print(msg, file=result_file)


def print_common_periods(initial_sum, percent, fixed_period):
    for key in COMMON_PERIODS:
        res = deposit(initial_sum, percent, fixed_period, COMMON_PERIODS[key])
        print_and_store(f'{key} :  {res}')


def main(args):
    config = {
        'initial_sum': None,
        'percent': None,
        'fixed_period': None,
        'set_period': None
    }

    for value in args:
        parts = value.split(":")
        if len(parts) != 2:
            continue
        key, value = value.split(":")
        if key in config:
            config[key] = float(value)

    if config['percent'] is None or config['fixed_period'] is None:
        exit(USAGE.format(script=script))

    if config['initial_sum'] is None:
        for key in COMMON_PERIODS:
            growth = getGrowth(
                config['percent'],
                COMMON_PERIODS[key],
                config['fixed_period'])

            print(key + ' : ' + formatAmount(growth * 100) + '%')

        if config['set_period'] is not None:
            growth = getGrowth(config['percent'],
                               config['set_period'],
                               config['set_period'])

            print('Your period ('
                  + str(config['set_period']) + ') : '
                  + formatAmount(growth * 100) + '%')
    else:

        print_common_periods(config['initial_sum'],
                             config['percent'],
                             config['fixed_period'])

        if config['set_period'] is not None:
            msg = f"Your period ({str(config['set_period'])}) : "
            msg += deposit(config['initial_sum'],
                           config['percent'],
                           config['fixed_period'],
                           config['set_period'])
            print_and_store(msg)

        print()
        print_and_store("AND ALSO HERE A BANKS PREPOSITIONS DOWN BELOW:")
        with open(BANK_DEPOSIT_PREPOSITION_FILE_NAME) as file:
            data = file.readlines()
            for line in data:
                line = line.strip()
                bank_name, percent = line.split(',')
                print()
                print_and_store(f'{bank_name} ({percent}%)')
                print_common_periods(
                    config['initial_sum'],
                    float(percent),
                    config['fixed_period']
                )

        print()


if __name__ == '__main__':
    import sys
    """Gets called when run as a script."""
    script, *argv = sys.argv

    main(argv)
