
def get_cats_info(path):
    cats_list=[]
    
    try:
        with open(path, "r") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        id,name,age= line.split(",")
                        cat = { "id":id,"name":name,"age":age}
                        cats_list.append(cat)
                    except ValueError:
                        print(f"Помилка обробки рядка: {line}")
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено!")

    
    return cats_list



print(get_cats_info("C:/Users/Олександр/Desktop/python/vs code/First_repo/HW4/123.txt"))

