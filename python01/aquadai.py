n = int(input("dòng đầu chứa số nguyên là : "))
for i in range(n):
    word = input()
    if len(word)>10:
        new_word = word[0] + str(len(word)-2)+word[-1]
        print(new_word)
    else:
        print(word)