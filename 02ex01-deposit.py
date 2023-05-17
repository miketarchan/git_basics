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
# TODO: add lines to calculate yields for some common periods
# of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
# as well
# TODO: (extra) Output only percents if the initial SUM is
# not known at the moment the script is run

USAGE = """This script calculates the deposit you can earn based on input data you provided
USAGE: {script} initial_sum:<value> percent:<value> fixed_period:<value> set_period:<value>
"""
USAGE = USAGE.strip()

COMMON_PERIODS = {
    '1 Month': 1/12,
    '6 Months': 1/2,
    '1 Year': 1,
    '2 Years': 2,
    '5 Years': 5,
    '10 Years': 10
}

def getGrowth(percent, set_period, fixed_perid):
    """Calculate growth coefficient"""
    percent = percent / 100
    return (1 + percent) ** (set_period / fixed_perid)

def formatAmount(amount):
    return "{:.2f}".format(amount)

def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    res = initial_sum * getGrowth(percent,fixed_perid=fixed_period,set_period=set_period)
    return formatAmount(res)

def main(args):
    """Gets called when run as a script."""
    script, *args = args
    
    config = {
        'initial_sum' : None,
        'percent' : None,
        'fixed_period' : None,
        'set_period' : None
    }

    for value in args:
        parts = value.split(":")
        if len(parts) != 2:
            continue
        key, value = value.split(":")
        if key in config:
            config[key]=float(value)
    
    if(config['percent'] is None or config['fixed_period'] is None):
        exit(USAGE.format(script=script))

    if config['initial_sum'] is None:
        for key in COMMON_PERIODS:
            growth = getGrowth(config['percent'], COMMON_PERIODS[key], config['fixed_period'])
            print(key + ' : ' + formatAmount(growth * 100)+ '%')
        
        if config['set_period'] is not None:
            growth = getGrowth(config['percent'], config['set_period'], config['set_period'])
            print('Your period (' + str(config['set_period']) + ') : ' + formatAmount(growth * 100)+ '%')
    else:
        for key in COMMON_PERIODS:
            print(key + ' : ' + deposit(config['initial_sum'], config['percent'], config['fixed_period'], COMMON_PERIODS[key]))
        
        if config['set_period'] is not None:
            print('Your period (' + str(config['set_period']) + ') : ' + deposit(config['initial_sum'], config['percent'], config['fixed_period'], COMMON_PERIODS[key]))

if __name__ == '__main__':
    import sys
    main(sys.argv)