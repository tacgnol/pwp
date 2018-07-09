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
  if (ground < drone) and (ground < premium):
    cheapest = "Ground"
    cheapest_cost = ground
  elif (drone < premium):
    cheapest = "Drone"
    cheapest_cost = drone
  else:
    cheapest = "Premium"
    cheapest_cost = premium
    cheapest_cost = round(cheapest_cost,2)
  print("The cheapest shipping method is " + cheapest)
  print("The cost is ${0:.2f}".format(cheapest_cost))

        
premium = 125.00

#Uncomment next two lines to prompt for user input
#weight = input("What is the weight of the parcel in pounds? ")
#choose_shipping_method(weight)

#Test out choose_shipping_method function with
#some predefined weights.
choose_shipping_method(4.8)
choose_shipping_method(41.5)
