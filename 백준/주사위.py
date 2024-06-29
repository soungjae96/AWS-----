import random

주사위1, 주사위2, 주사위3 = map(int, input().split())
# 주사위1 = random.randint(1, 6)
# 주사위2 = random.randint(1, 6)
# 주사위3 = random.randint(1, 6)

# if 주사위(0) == 주사위2 == 주사위3:
#     print(10000+주사위1 * 1000)
# elif 주사위1 == 주사위2:
#     print(1000+주사위1*100)
# elif 주사위1 == 주사위3:
#     print(1000+주사위1*100)
# elif 주사위2 == 주사위3:
#     print(1000+주사위2*100)
# else:
#     lagest=max(주사위1,주사위2,주사위3)
#     print(lagest * 100)
if 주사위1 == 주사위2 == 주사위3:
    print(10000+주사위1 * 1000)
elif 주사위1 == 주사위2:
    print(1000+주사위1*100)
elif 주사위1 == 주사위3:
    print(1000+주사위1*100)
elif 주사위2 == 주사위3:
    print(1000+주사위2*100)
else:
    lagest=max(주사위1,주사위2,주사위3)
    print(lagest * 100)