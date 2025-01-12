
# или from math import sin, sqrt
# import math
# print(math.sin(30)) # -0.9880316240928618
# print(math.sqrt(2))


# import datetime

# txt = '2023-01-01'
# dt = datetime.datetime.strptime(txt, '%Y-%m-%d') #strg parsing time. 
# #                                       извлеки из строки время
# print(dt)

# import pandas

from datetime import datetime
a_time = datetime.now()
print(a_time.strftime('%a'))

