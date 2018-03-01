import assign_cars as ac
import sort_rides as sr

def solve(list_of_cars, list_of_rides, sim_steps):
    # Currently a stub
    available_cars = {}
    result = {}
    for car in list_of_cars:
        available_cars[car.id] = car
        result[car.id] = []

    sorted_rides = sr.sort_rides(list_of_rides)
    for t in range(0, sim_steps):
        assignments = ac.assign_cars(
            available_cars = available_cars,
            sorted_rides = sorted_rides,
            t = t
        )

        for car_id, ride_id in assignments.items():
            # TODO: Remove cars from available cars list
            # TODO: add cars to cars in flight
            # TODO: add the rides to the result
            pass

    # TODO: use the simulator

    return {
        0: [0, 2, 6],   # car 0 does rides 0, 2 and 6
        1: [1, 3, 4, 5] # car 1 does rides 1, 3, 4 and 5
    }