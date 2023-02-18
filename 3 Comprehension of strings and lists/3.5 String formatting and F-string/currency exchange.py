# Enter (each on a new line): the dollar exchange rate (real value)
# and the number of rubles (an integer) to exchange rubles for dollars.
# Calculate the integer number of dollars received (with the fractional
# part discarded) and form a string using the F-string:
#
# 'You can get <dollars>$ for <the number of rubles>rubles at the exchange <rate of the dollar>.'
#
# Print the result to the screen (without quotes).

rate_dollar, rub = float(input('enter dollar exchange rate: ')), int(input('How many: '))
print(f'You can get {int(rub // rate_dollar)}$ for {rub} rubles at the exchange {rate_dollar}')
