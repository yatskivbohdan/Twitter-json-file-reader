import json


def json_to_dict(path, options):
    '''
    (str, lst) -> None
    Reads a Twitter JSON file and rewrites in a new one only
    that info that was chosen in options list
    e.g. ["screen_name", "description"]
    options:
    -screen_name
    -location
    -description
    -followers_count
    -friends_count
    -created_at

    '''
    f = open(path, 'r', encoding='utf-8')
    users = json.load(f)
    f.close()
    friends = {}
    for friend in users["users"]:
        friends[friend["name"]]={}
        for option in options:
            friends[friend["name"]][option]=friend[option]
    with open("new_info.json", "w") as outfile:
        json.dump(friends, outfile)
