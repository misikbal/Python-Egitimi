my_list = ["elma", "armut", "muz"]
for x in my_list:
    print(x)

my_set = {"elma", "armut", "muz"}

new_set = {"portakal","cilek","kivi"}
my_set.update(new_set)

my_set.remove("elma")

my_book_dict = {
"name" : "Sherlock Holmes",
"year" : "1967",
"series" : "Asla Şüphe Uyumaz",

}

print(my_book_dict["name"])