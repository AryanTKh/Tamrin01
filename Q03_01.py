try:
    name = list(input().split())

    health = list( map(int , input().split()))
    damage = list( map(int , input().split()))
    one = list(input().split())
    two = list(input().split())
    three = list(input().split())
    card = [one, two, three]
    dmg1 = 0
    dmg2 = 0
    scr1 = 0
    scr2 = 0

    for i in range(3):
        m = card[i][0]
        if m == "A":
            dmg1 += damage[0]
        if m == "B":
            dmg1 += damage[1]
        if m == "C":
            dmg1 += damage[2]

    for i in range(3):
        m = card[i][1]
        if m == "A":
            dmg2 += damage[0]
        if m == "B":
            dmg2 += damage[1]
        if m == "C":
            dmg2 += damage[2]
    A = damage[0]
    B = damage[1]
    C = damage[2]

    for i in range(3):
        if card[i][0] == "A":
            if card[i][1] == "B":
                if A > B:
                    scr1 += 1
                if B > A:
                    scr2 += 1
            if card[i][1] == "C":
                if A > C:
                    scr1 += 1
                if C > A:
                    scr2 += 1

        if card[i][0] == "B":
            if card[i][1] == "A":
                if A < B:
                    scr1 += 1
                if B < A:
                    scr2 += 1
            if card[i][1] == "C":
                if B > C:
                    scr1 += 1
                if C > B:
                    scr2 += 1

        if card[i][0] == "C":
            if card[i][1] == "B":
                if C > B:
                    scr1 += 1
                if B > C:
                    scr2 += 1
            if card[i][1] == "A":
                if C > A:
                    scr1 += 1
                if A > C:
                    scr2 += 1

    health[0] -= dmg2
    health[1] -= dmg1

    print(name[0], " -> Score: ", scr1, ", Health: ", health[0], sep='')
    print(name[1], " ->", " Score: ", scr2, ", Health: ", health[1], sep='')

except:
    print("Invalid Command." );









