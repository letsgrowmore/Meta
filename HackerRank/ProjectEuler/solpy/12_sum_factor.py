count_dict = [
    (1, 1),
    (2, 2),
    (4, 3),
    (6, 7),
    (9, 8),
    (16, 15),
    (18, 24),
    (20, 32),
    (24, 35),
    (36, 63),
    (40, 80),
    (48, 104),
    (90, 224),
    (112, 384),
    (128, 560),
    (144, 935),
    (162, 1224),
    (168, 1664),
    (192, 1728),
    (240, 2015),
    (320, 2079),
    (480, 5984),
    (576, 12375),
    (648, 14399),
    (768, 21735),
    (1024, 41040)]

    
for i in range(int(input())):
    N = int(input())
    for tup in count_dict:
        x, t = tup
        if x > N:
            print(int((t*(t+1))/2))
            break
