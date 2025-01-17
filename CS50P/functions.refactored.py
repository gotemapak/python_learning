

campaigns = [
    {'clicks': 100, 'cpc': 0.50, 'revenue': 120},
    {'clicks': 150, 'cpc': 0.60, 'revenue': 200},
    {'clicks': 90, 'cpc': 0.55, 'revenue': 100},
    {'clicks': 200, 'cpc': 0.65, 'revenue': 280},
    {'clicks': 80, 'cpc': 0.52, 'revenue': 95},
]

exchange_rate = 100

# считаем косты
def get_cost(clicks, cpc):
    return clicks * cpc

# считаем роас
def get_roas(cost, revenue):
    return revenue / cost

# считаем обмен курс
# def exchange(value, exchange_rate):
#   return value * exchange_rate

exchange = lambda value, exchange_rate: value * exchange_rate

# показываем роас кампаний
for i, campaign in enumerate(campaigns):
    cost = get_cost(campaign['clicks'],
                    campaign['cpc'])
    cost_new_cur = exchange(cost, exchange_rate)

    roas = get_roas(cost_new_cur, campaign['revenue'])
    print(f'ROAS for campaign {i}: {round(roas,2)}')

