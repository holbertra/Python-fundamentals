from komo_data import Badges

current_badges = Badges()

def add_badge(badge_num, access_doors):                  # called from Option #1 in komo_ui.py
    return "Added Badge" if current_badges.add_badge(badge_num, access_doors) else "Error"

def delete_badge(badge_num):
    return "Badge successfully deleted" if current_badges.delete_badge(badge_num) else "Error"

def list_badges():  # List all badges
    return current_badges.list_badges()

def edit_badge(badge_num):  # Edit the selected badge
    return "Badge successfully edited" if current_badges.edit_badge(badge_num) else "Error"

def get_badge(badge_num):
    return current_badges.get_badge(badge_num)

def add_door()
