import value_return

def main():
    seconds = value_return.get_seconds(3800)
    minutes = value_return.get_minutes(3800)
    hours = value_return.get_hours(3800)
    print ("0",hours,":0", minutes,":",seconds)
main()