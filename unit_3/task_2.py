def collection(**data):
    a = []
    for key, value in data.items():
        a.append("{}".format(value, key))
    print(" ".join(a))


collection(Firstname=input("Имя : "), Lastname=input("Фамилия : "), Year=int(input("Год : ")), City=input("Город : "),
           Email=input("Эл. адрес: "), Phone=int(input("Телефон: ")))
