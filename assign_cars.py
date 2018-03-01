import sort_rides as sr

# Takes a list of cars and a ride and returns the closest car
# cars must be a non-empty array
def closest_car(cars, ride):
  return sorted(cars, key=lambda car: sr.get_distance(ride.row, ride.col, car.x, car.y))[0]

# At a single time step
# Given all the available cars
# And all the sorted rides
# sorted_rides should be sorted by last possible start time (i.e. finish time - distance)
# Return a map from car_id to ride_id
# available_cars is a map from car_id to car
def assign_cars(available_cars, sorted_rides, t):
  assignments = {}
  for ride in sorted_rides:
    # Make sure we still have cars
    if not available_cars:
      return assignments
    # Get the closest car
    cc = closest_car(available_cars.values(), ride)
    # Make the assignment and remove the car from available cars
    assignments[cc.id] = ride.ride_id
    del(available_cars[cc.id])
  return assignments