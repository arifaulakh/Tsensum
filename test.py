import indicoio
indicoio.config.api_key = 'b3962258311d6c73574642b4877813b9'

print(indicoio.sentiment([
    "I love writing code!",
    "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
]))