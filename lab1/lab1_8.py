####
prices={
   'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# min
min_price=min(zip(prices.values(),prices.keys()))
print("min:{}".format(min_price))

# max
max_price=max(zip(prices.values(),prices.keys()))
print("max:{}".format(max_price))

#sorted
prices_sorted=sorted(zip(prices.values(),prices.keys()))
print("sort:{}".format(prices_sorted))

print(">>>>>>>")
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 } #min=max
zippa=zip(prices.values(),prices.keys())
print("min:{}".format(min(zippa)))
zippa=zip(prices.values(),prices.keys())
'''直接输报ValueError: max() arg is an empty sequenc的错'''
print("min:{}".format(max(zippa)))
