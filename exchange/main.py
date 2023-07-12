import threading
from helpers import fetch_data

_currency_state = {
    'nbu': None,
    'privat': None
}


def process_nbu():
    list = fetch_data('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    _currency_state['nbu'] = {}
    for item in list:
        _currency_state['nbu'][item['cc']] = float(item['rate'])
    do_compare()


def process_privat():
    list = fetch_data('https://api.privatbank.ua/p24api/pubinfo?exchange=&coursid=5')
    _currency_state['privat'] = {}
    for item in list:
        _currency_state['privat'][item['ccy']] = float(item['buy'])
    do_compare()


def do_compare():
    for i in _currency_state:
        if _currency_state[i] is None:
            return

    threading.Thread(target=compare_currencies).start()


def compare_currencies():
    max_count = 0
    last_max_count_key = ''
    for i in _currency_state:
        if len(_currency_state[i]) > max_count:
            max_count = len(_currency_state[i])
            last_max_count_key = i

    for currency_name in _currency_state[last_max_count_key]:
        better_currency_value = None
        better_bank_name = ''
        for i in _currency_state:
            if currency_name in _currency_state[i] \
                    and (better_currency_value is None
                         or _currency_state[i][currency_name]
                         < better_currency_value):
                better_currency_value = _currency_state[i][currency_name]
                better_bank_name = i
        
        print(f'{currency_name} {better_bank_name}: {better_currency_value}')
        pass


if __name__ == "__main__":
    all_threads = [
        threading.Thread(target=process_nbu),
        threading.Thread(target=process_privat)
    ]
    for i in all_threads:
        i.start()
