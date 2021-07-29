import decimal

from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(val):
    cyr_dict = {}
    cyr_name = content.replace('><', ' ').split()
    nominal = 0
    key_t = ''
    for i in cyr_name:
        if i[:9] == 'CharCode>':
            key_t = i[9:12]
        """some of the exchange rates are reduced to 10, 100 or 1000 units to the ruble. The 'nominal' is responsible 
        for this. """
        if i[:10] == 'Nominal>1<':
            nominal = 1
        elif i[:11] == 'Nominal>10<':
            nominal = 10
        elif i[:12] == 'Nominal>100<':
            nominal = 100
        elif i[:13] == 'Nominal>1000<':
            nominal = 1000
        if i[:6] == 'Value>':
            val_t = i[6:13].replace(',', '.')
            cyr_dict.setdefault(key_t, decimal.Decimal(val_t) / nominal)  # Using Decimal
            # cyr_dict.setdefault(key_t, float(val_t) / nominal) # Using Float
    for i in cyr_dict:
        if val.upper() == i:
            result = f'1 {i} стоит {cyr_dict[i]:.2f} рублей'
            return result


print(currency_rates('GBP'))
print(currency_rates('usd'))
print(currency_rates('Eur'))
print(currency_rates('RRR'))
