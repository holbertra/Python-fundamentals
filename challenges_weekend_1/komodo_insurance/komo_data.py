from datetime import datetime

badge_dict = { }

class Badges:
    def __init__(self, badge_num=0, access_doors=[]):
        self.badge_num = badge_num
        self.access_doors = access_doors

    def add_badge(self, badge_num, access_doors):
        badge_dict.update({ badge_num:access_doors })   #Put Badge # and doors into dictionary
        # print("komo_data:class Badges:add_badge() . .added badge:", badge_num, access_doors )
        # print("badge_dict", badge_dict)
        return 1

    def delete_badge(self, badge_num):
#       print("lookup badge to delete:", badge_num )
        self.badge_num = badge_num
        for x in badge_dict:     # deleting a key-value from a dictionary
            if x == badge_num:
#               print("found badge_num:", self.badge_num)
                del badge_dict[self.badge_num]
                break
        
        print("Amended badge_dict:", badge_dict )
        return 1

    def list_badges(self):
        message = ""
        for id, doors in badge_dict.items():
            message += f'{id}  {doors}\n'
        return message

    def edit_badge(self, badge_num):     # add or remove access for a given badge
        print("Editing badge:", badge_num )
        return 1

    def get_badge(self, badge_num):
        print("get_badge():", badge_num)
        access = []
        access.append(badge_num)
        # Enter in the key & get back the value(s)
        access.append(badge_dict.get(badge_num))
        # Need to return this in better format - research casting a list into a string
        return access

    def add_door(self, badge_num, access_doors):
        self.badge_num = badge_num
        self.access_doors = access_doors
        badge_dict[self.badge_num].append(self.access_doors)
        print("Added door:", self.access_doors, "to badge:", self.badge_num )

    def delete_door(self, badge_num, access_doors):
        self.badge_num = badge_num
        self.access_doors = access_doors
        print("Deleted door:", self.access_doors, "from badge:", self.badge_num )





