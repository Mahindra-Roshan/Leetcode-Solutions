
def currencycounter(amount):
    currency = [2000,1000,500,200,100,50,20,10,5,2,1]
    for i in currency:
        if amount >= i:
            count = amount// i
            amount = amount - (count *i)
            print(f"{count} notes/ coins of {i}")
currencycounter(1234)
