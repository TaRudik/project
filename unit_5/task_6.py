with open("units.txt", encoding="utf-8") as f:
    str = f.readlines()
    dict = {}
    for line in str:
            num = []
            list = line.split()
            for el in list:
                k = list[0]
                k = k[0:len(k) - 1]

                if el[0].isdigit():
                    num.append(el)
            sun = []
            for digits in num:
                i = 0
                for numers in digits:
                    if digits[i].isdigit():
                        i += 1
                    if digits[i] == "(":
                        sun.append(int(digits[0:i]))
                        i += 1


            def listsum(sun):
                sum = 0
                for j in sun:
                    sum = sum + j
                return sum


            dict.update({k: listsum(sun)})
    print(dict)