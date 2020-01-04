import itertools
from datetime import datetime


def immediately_right(house_first, house_second):
    """House first is immediately right of second if first - second == 1."""
    return house_first - house_second == 1


def next_to(house_first, house_second):
    """Two houses are next to each other if they differ by 1."""
    return abs(house_first - house_second) == 1


def zebra_puzzle_my():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]  # 1
    orderings = list(itertools.permutations(houses))
    
    for (Kools, OldGold, Chesterfields, LuckyStrike, Parliaments) in orderings:  # SMOKE
        for (dog, snails, fox, horse, ZEBRA) in orderings:  # ANIMAL
            
            if OldGold != snails: continue  # smoke animal
            if not next_to(Chesterfields, fox): continue  # smoke animal
            if not next_to(Kools, horse): continue  # smoke animal
            
            for (Norwegian, Englishman, Spaniard, Ukrainian, Japanese) in orderings:  # NATION
                if Norwegian != first: continue  # nation nation
                if Spaniard != dog: continue  # nation animal
                if Japanese != Parliaments: continue  # nation smoke
                
                for (green, red, ivory, yellow, blue) in orderings:  # COLOR
                    if not immediately_right(green, ivory): continue  # color color
                    
                    if Englishman != red: continue  # nation color
                    if not next_to(Norwegian, blue): continue  # nation color
                    if Kools != yellow: continue  # smoke color
                    
                    for (milk, coffee, tea, orange_juice, WATER) in orderings:  # DRINK
                        if milk != middle: continue  # drink drink
                        
                        if coffee != green: continue  # drink color
                        if Ukrainian != tea: continue  # nation drink
                        if LuckyStrike != orange_juice: continue  # smoke drink
                        
                        return WATER, ZEBRA


def zebra_puzzle_their():
    """Return a tuple (WATER, ZEBRA) indicating """
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
                for (coffee, tea, milk, orange_juice, WATER) in orderings
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Englishman is red
                if Spaniard is dog
                if coffee is green
                if Ukranian is tea
                if immediately_right(green, ivory)
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if Norwegian is first
                if next_to(Chesterfields, fox)
                if next_to(Kools, horse)
                if LuckyStrike is orange_juice
                if Japanese is Parliaments
                if next_to(Norwegian, blue)
                )


def main():
    time_start = datetime.now()
    
    water, zebra = zebra_puzzle_my()
    print(f'{water=}')
    print(f'{zebra=}')
    
    time_end = datetime.now()
    time_all = (time_end - time_start).total_seconds()
    print('time_all:', time_all)
    
    # 628.371489 with pass
    # 0.00884 with optimized


if __name__ == '__main__':
    main()
