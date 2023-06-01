import random
# 5 Star Character List
fivestarcharlist = ['Yae Miko', 'Klee', 'Tartaglia', 'Eula', 'Shenhe', 'Xiao', 'Ayato', 'Itto', 'Kokomi',
                    'Venti', 'Albedo', 'Yoimiya', 'Zhongli', 'Hu Tao', 'Ayaka', 'Ganyu', 'Yelan', 'Kazuha', 'Raiden', 'Nahida']
eventwish = int(random.randint(0, 19))

# 4 Star Character List
fourstarcharlist = ['Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl', 'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun',
                    'Diona', 'Xinyan', 'Rosaria', 'Yanfei', 'Sayu', 'Sara', 'Gorou', 'Thoma', 'Heizou', 'Shinobu', 'Yun Jin', 'Collei', 'Dori', 'Candace', 'Layla']
fourstareventwish = []
for i in range(0, 3):
    fourstar = random.randint(0, (len(fourstarcharlist)-1))
    fourstarchar = fourstarcharlist[fourstar]
    del fourstarcharlist[fourstar]
    fourstareventwish.append(fourstarchar)
# How can we select no two of the same element? Maybe too complicated?

# Altering the Five star character list without the featured character
featuredchar = fivestarcharlist[eventwish]
othercharacter = ['Diluc', 'Mona', 'Jean', 'Qiqi', 'Keqing']

# 3 Star Weapon List
threestarweaponlist = ['White Tassel', 'Skyrider Greatsword', 'Skyrider Sword', 'Thrilling Tales of Dragon Slayers',
                       'Magic Guide', 'Slingshot', 'Sharpshooter\'s Oath', 'Harbinger of Dawn', 'Fillet Blade', 'Cool Steel']

# Inventory
inv = {}

# Introduction
print(f'Welcome to the {featuredchar} Character Event Wish Banner!')
print(
    f'The featured four-star Characters are {fourstareventwish[0]}, {fourstareventwish[1]}, and {fourstareventwish[2]}!')
print('''\nEvery set of 90 wishes on this banner is guaranteed a five-star character! With every wish\nthere is a 0.6% chance to get a five-star character early! Additionally, there is a 50/50 \nchance to get the featured character in your first 90 pulls and if you don't get the \nfeatured character, the next set of 90 wishes will get you the featured character.\nIt is worth noting that, every set of 10 wishes also guarantees a four-star character.\nYou either get one of the three featured four-star characters or any other four-star unit from \nthe standard banner pool.''')
done = 0
pity = 0
pity4 = 0
fivestar = random.randint(0, 100)
while done != 1:
    pull = input('\nWould you like to Wish 1x or Wish 10x\n')
    if pull == '1':
        i = 0
        while i < 1:
            i += 1
            pity += 1
            pity4 += 1
            roll = random.random()
            if roll <= 0.006 + (1/(90 - pity)):

                print('\nGet a 5 star character!\nYour pity has been reset!')
                pity = 0
            elif roll <= 0.025 + (1/(11.025 - pity4)):
                print('\nGet a 4 star character!')
                pity4 = 0
            else:
                threestar = random.randint(0, len(threestarweaponlist))
                threestarweapon = threestarweaponlist[threestar]
                print(f'\nGet a {threestarweapon}!')

    elif pull == '10':
        i = 0
        while i < 10:
            i += 1
            pity += 1
            pity4 += 1
            roll = random.random()
            if roll <= 0.006 + (1/(90 - pity)):
                if fivestar <= 49:
                    fivestarchar = featuredchar
                    fivestar = random.randint(0, 100)
                else:
                    fivestarchar = othercharacter[random.randint(
                        0, (len(othercharacter)-1))]
                    fivestar = random.randint(0, 49)
                print(
                    f'\nYou got a 5 star character!\nGet a {fivestarchar}.\nYour pity has been reset!')
                pity = 0
                # testing: print(pity)
            elif roll <= 0.025 + (1/(11.025 - pity4)):
                if fourstar <= 49:
                    fourstarcharacter = fourstareventwish[random.randint(
                        0, (len(fourstareventwish)-1))]
                else:
                    fourstarcharacter = fourstarcharlist[random.randint(
                        0, (len(fourstarcharlist)-1))]
                print(
                    f'\nYou got a four-star character!\nGet a {fourstarcharacter}!')
                pity4 = 0
                # testing: print(pity)
            else:
                threestar = random.randint(0, (len(threestarweaponlist)-1))
                threestarweapon = threestarweaponlist[threestar]
                print(
                    f'\nYou got a three-star weapon!\nGet a {threestarweapon}!')

    elif pull == 'done':
        done += 1
    elif pull == 'pity':
        print(pity)
    elif pull == 'inventory':
        print(inv)
    else:
        print('Try again')
