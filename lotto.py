"""Calculate when you win in Lotto game and what's cost that play :)"""
import random

draw_cost = int(input('Podaj koszt jednego zakładu na jedno losowanie: '))
my_numbers = set()
all_numbers = range(1, 50)

while len(my_numbers) < 6:
    try:
        num = int(input("Podaj liczbę do losowania: "))
        if num in all_numbers:
            my_numbers.add(num)
    except ValueError:
        print("Tylko liczby w zakresie 1-49")

def draw_numbers():
    """Machine draw 6 random numbers"""
    return set(random.sample(all_numbers, k=6))

def play_unitl_win(numbers):
    """Machine play that long unitl get win numbers and calculate tries"""
    win_numbers = {}
    counter: int = 0

    while numbers != win_numbers:
        win_numbers = draw_numbers()
        counter += 1

    return counter

if __name__ == '__main__':
    COUNTER: int = play_unitl_win(my_numbers)
    total_cost: int = draw_cost * COUNTER

    print(f'Twoje podabe liczby to: {my_numbers}')
    print(f'Koszt inwestycji przy wkładzie {draw_cost}pln wyniósł: {total_cost:,} pln')
    print(f'Ilość losować zanim trafiliśmy wszystkie liczby wyniósł: {COUNTER:,}.')
