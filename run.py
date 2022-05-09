from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency('AZN')
    bot.select_place_to_go('New York')
    bot.search_date('2022-05-16','2022-06-04')
    bot.search_adults(2)
    bot.search_children(4,[2,4,8,9])
    bot.search_room(4)
    bot.search_all_possible_situation()