# def get_name(person):
#    return person["name"]

# def get_favourite_tv_show(person):
#     return person["favourites"]["tv_show"]

# def likes_to_eat(person, food):
#     if food in person["favourites"]["snacks"]:
#         return True
#     else:
#         return False

# def add_friend(person, new_friend):
#     person["friends"].append(new_friend)
#     print(len(person["friends"]))

# def remove_friend(person, remove_friend):
#     person["friends"].remove(remove_friend)
#     print(len(person["friends"]))


# def total_money(thingy):
#     total_monies = 0
#     for thing in thingy:
#         total_monies += thing["monies"]
#     return total_monies


def l_money(giver, reciever, amount):
    if amount > giver["monies"]:
        return "Can't do"
    else:
        giver["monies"] -= amount
        reciever["monies"] += amount
    # return giver["monies"], reciever["monies"]


# locate giver money. Minus amount from their monies.
# locate reciever money. Add amount to their monies. 
