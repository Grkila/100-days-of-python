MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resource ={
    "water": 200,
    "milk": 150,
    "coffee": 24,
    "money":0
}
coins={
    "quarters":0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies":0.01
}
def provera_sastojaka(answer,MENU,resource):

    for ingredient in MENU[answer]["ingredients"]:
        if resource[ingredient]<MENU[answer]["ingredients"][ingredient]:
            print("Nedovoljno resursa, problematican resurs"+" "+ingredient)
            return False
    return True



if __name__ == '__main__':
    print(MENU["espresso"]['cost'])

while True:

    # TODO Izlistaj opcije
        answer=input("What would you like espresso/cappuccino/latte?")

    # TODO Opcija da se ugasi sa off
        if answer.upper()=="OFF":
            print("Machine is turned off")
            break
    # TODO Print report sa "report"
        if answer.upper()=="REPORT":
            for item in resource:
                print(item,resource[item])
            continue

    # TODO Kad izabere kafu proveri da li ima dovoljno resursa

        if answer in MENU:
            if not provera_sastojaka(answer, MENU, resource):
                print("nije uspelo")
                continue
        else:
            print("No item in menu")
            continue


    # TODO Uzmi novcice
        money=0
        for coin in coins:
            kolicina=input(coin+" ")
            # TODO izracunaj novcice
            money+=int(kolicina)*coins[coin]


    # TODO proveri da li je transakcija uspesna - da li ima para
        if MENU[answer]["cost"]>money:
            # TODO ako nema vrati pare
            print("not enough money")
            continue
        elif MENU[answer]["cost"]<money:
            # TODO ako ima izracunaj kusur i dodaj pare u banku
            change=money-MENU[answer]["cost"]
            print("POVRACAJ NOVCA JE ", change)

        print("Transakcija je uspesna")
    # TODO dodaj pare u banku
        resource["money"]+=MENU[answer]["cost"]



    # TODO oduzmi mleko, kafu i secer potreban za pravljenje kafe
        for ingredient in MENU[answer]["ingredients"]:
            resource[ingredient] -= MENU[answer]["ingredients"][ingredient]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
