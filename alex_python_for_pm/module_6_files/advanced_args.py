import argparse #библиотека

parser = argparse.ArgumentParser() #
parser.add_argument('amount', 
                    help='Initial currency amount',
                    type=float) 
#добавили обязательный, позиционный аргумент amount при запуске программы

parser.add_argument('--exchange_rate', 
                    help='Initial currency amount',
                    type=float,
                    action='store', 
                    default=1) #дефолтное значение переменной
#добавили необязательный аргумент exchange rate

parser.add_argument('--verbose', 
                    help='Verbosity Level',
                    action='store_true') 

args = parser.parse_args() # Парсим аргументы

result = args.amount * args.exchange_rate

if args.verbose:
    print(f'{args.amount} is converted using {args.exchange_rate}, and the result is {result}')
else:
    print(result)

          

# print(args.amount) # python advanced_args.py 100 → 
#                      # Namespace(amount='100')
# print(args.exchange_rate) # python advanced_args.py 100 --exchange_rate 100 →
#                             # Namespace(amount='100', exchange_rate=100)
