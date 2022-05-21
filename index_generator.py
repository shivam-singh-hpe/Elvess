import datetime


def index_generator(num_of_items):
    """
    Function to generate an item index for a ten minute period,
    i.e [0-9 mins].

    This is useful when you have a list of items and need to 
    know which one will be chosen for xyz work for a ten-minute 
    period at any time of day.

    The generated index will be in the range [0, num of items-1], 
    determined by the current time of day (i.e. which tenth minute 
    slot) and the number of items. The indexes continue to repeat 
    themselves within that range throughout the day.

    There are 1440 minutes in a day. That means we have 144 ten-
    minute slots in a day [i.e. until time 23:59], allowing us 
    to have a maximum of 143 indexes in a 0-based indexing. If 
    the number of items exceeds 144, the function will run, but 
    no indexes above 143 will be generated.

    :EXAMPLE:
        num_of_items = 5,
        now = 2022-03-23 11:21:52.935171,
        index = 68 % 5 = 3

        i.e. For the next ten minutes [11:20 - 11:29], the 3rd 
        index item will be used for xyz work.

    :param num_of_items: total number of items. Range is [1-144]
    :type num_of_items: int

    :returns: the item's index for the current ten-minute period
    :rtype: int
    """

    now = datetime.datetime.now()
    num_of_min = now.hour * 60 + now.minute
    which_tenth_min = num_of_min//10
    index = which_tenth_min % num_of_items
    return index
