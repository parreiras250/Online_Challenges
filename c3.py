# Challenge 3
# solução pessoal 
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def count_on(dict):
   mapped_dict =[]
   for key, value in dict.items():
      if value == "online":
         mapped_dict.append(value)
   count = len(mapped_dict)
   return count

#solução do site: 

# long version
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])