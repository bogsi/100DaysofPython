capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}
print(travel_log["France"]["cities_visited"][1]["total_visits"][0])
print(travel_log["Germany"]["cities_visited"][0]["total_visits"][0])
# print(travel_log['USA'][0])

# nested_list  = ['A', 'B', ['C', 'D','24','25','27',],['E','F']]
# #print(nested_list[2][3])
# #nested_list[2].append('26')
# nested_list[2].insert(4,'26')
# print(nested_list)
