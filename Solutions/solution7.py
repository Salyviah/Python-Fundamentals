def sort_by_age(people):
   
    return sorted(people, key=lambda person: person[1])


people = [("Salyviah", 12), ("Bilania", 2), ("Felincy", 10)]
sorted_people = sort_by_age(people)


print(sorted_people)
