# считаем косты
def get_cost(clicks, cpc):
    return clicks * cpc

# считаем роас
def get_roas(cost, revenue):
    return revenue / cost

# считаем обмен курс
def exchange(value, exchange_rate):
  return value * exchange_rate