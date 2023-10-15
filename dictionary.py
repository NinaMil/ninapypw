"""phones = {
    "adam smith": "11-12-13",
    "britney spears": "44-55-66",
    "bob marley": "99-77-66"
}
for key in phones:
    print(key)"""

"""person = {
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "email": "johndoe@example.com"
}"""

dictionary={}
commands=["new","show"]
while True:
    command= input(f"peek an option:{commands}")
    while command not in command:
        print("unknown command, try again")
        command=input(f"peek an option:{command}")
    if command=="new_contact" or "n":
        name_sur=(input("your name_surnate:"))
        age=(input("your age:"))
        dictionary[name_sur]=age

    elif command=="show_contacts" or "s":
        print(dictionary)
    #else:
    #    print("unknown command")

    command=input("want continue? Y/N?")
    if command=="N" or "n":
        break


