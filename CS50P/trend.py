sales = [6, 10, 2, 2, 7]

prev_month = sales[0]
result = ()

for i in sales[1:]:
    if i > prev_month:
        result = False
    else: 
        prev_month = i
print(result)