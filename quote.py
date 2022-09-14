#THIS IS FOR THE QUOTE
import random
#Connect to DB

list = []
# generates a year's worth of random values
r = random.sample(range(0,(365*4)), k=365)


# Get the quote that belongs at the given location
def get_quote(day):
    day = r[day]
    query = 'SELECT quote FROM quotetable WHERE day = %t'

    # execute query
    result = ''
    return result
