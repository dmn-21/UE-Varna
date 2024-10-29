def flights(*args):
    flights_dict = {}
    for i in range(len(args)):
        if args[i] == 'Finish':
            break

        if i % 2 == 0:
            if args[i] not in flights_dict.keys():
                flights_dict[args[i]] = 0
        else:
            flights_dict[args[i - 1]] += int(args[i])

    return flights_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))