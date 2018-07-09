#!/usr/bin/env python3

def ground_shipping(weight):
  if weight > 10:
    cost = weight * 4.75
  elif weight > 6:
    cost = weight * 4.00
  elif weight > 2:
    cost = weight * 3.00
  else:
    cost = weight * 1.50
  cost += 20
  return(cost)

def drone_shipping(weight):
  if weight > 10:
    cost = weight * 14.25
  elif weight > 6:
    cost = weight * 12.00
  elif weight > 2:
    cost = weight * 9.00
  else:
    cost = weight * 4.50
  return(cost)
      
def choose_shipping_method(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if ground < drone:
    if ground < premium:
      cheapest = "Ground"
      cheapest_cost = ground
    else:
      cheapest = "Premium"
      cheapest_cost = premium
  else:
    cheapest = "Drone"
    cheapest_cost = drone
  print ("The cheapest shipping method is " + cheapest + " and the cost is $" + str(cheapest_cost))

weight = input("What is the weight of the parcel?")
premium = 125.00


print(choose_shipping_method(3.4))
print(ground_shipping(8.4))
print(drone_shipping(1.5))
