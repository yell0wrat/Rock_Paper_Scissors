import random
choice = int(input('pick a number 1-3, rock is 1, paper is 2, scissors is 3: '))
if choice == 1:
    print('you have picked rock')
elif choice == 2:
    print('you have picked paper')
elif choice == 3:
    print('you have picked scissors')
else:
    print('you did not choose a number 1-3, fuck you.')
print('the computer is deciding what to pick')
computer=random.randint(4,6)
if computer == 4:
    print('the computer has picked rock')
elif computer == 5:
    print('the computer has picked paper')
elif computer == 6:
    print('the computer has picked scissors')
else:
    print('error.')
if choice == 1 and computer == 4:
    print('you tie! : /')
elif choice == 1 and computer == 5:
    print('you lose! : (')
elif choice == 1 and computer == 6:
    print('you win! : )')
elif choice == 2 and computer == 4:
    print('you win! : )')
elif choice == 2 and computer == 5:
    print('you tie! : /')
elif choice == 2 and computer == 6:
    print('you lose! : (')
elif choice == 3 and computer == 4:
    print('you lose! : (')
elif choice == 3 and computer == 5:
    print('you win! : )')
elif choice == 3 and computer == 6:
    print('you tie! : /')
else:
    print('this is awkward.')