from route4me import Route4Me
from route4me.constants import ALGORITHM_TYPE, DISTANCE_UNIT, TRAVEL_MODE, OPTIMIZE

#Sets the name of the batch
batch = input("Please enter the name of the route in the format\
 Week number/batch number eg: 19B862:")

#Takes a list of postcodes for the batch
print('\nPlease enter a list of postcodes seperated by a ","\n')
postcodes_list = input()
postcodes_list = postcodes_list.split(',')

#checks the area of the batch to add the outbase to the beginning of the postcodes list
if batch[-2] =='0':
    postcodes_list.insert(0,'S72 7EZ')
elif batch[-2] =='2':
    postcodes_list.insert(0,'GL2 7PD')
elif batch[-2] =='3':
    postcodes_list.insert(0,'NN5 7UL')
elif batch[-2] =='4':
    postcodes_list.insert(0,'WA11 9UX')
elif batch[-2] =='5':
    postcodes_list.insert(0,'EN11 0DE')
elif batch[-2] =='6':
    postcodes_list.insert(0,'CM77 8QN')
elif batch[-2] =='7':
    postcodes_list.insert(0,'WV11 3QG')
elif batch[-2] =='8':
    postcodes_list.insert(0,'DL4 1PX')
elif batch[-2] =='9':
    postcodes_list.insert(0,'ML8 5EH')

#creates a list of dictionarys for the postcodes
addresses = []
for pc in postcodes_list:
     postcode = {'address':pc}
     addresses.append(postcode)


# Each individual has a unique API key found in the "My Account tab"
API_KEY = "3A8B3341D5B4DDB4BA6F42B64C1EA5E3"
r4m = Route4Me(API_KEY)
optimization = r4m.optimization
r4m_addresses = r4m.address
optimization.algorithm_type(ALGORITHM_TYPE.TSP)
optimization.share_route(0)
optimization.store_route(0)
optimization.route_time(7 * 600)
optimization.rt(True)
optimization.route_max_duration(86400)
optimization.route_name(batch)
optimization.optimize(OPTIMIZE.TIME)
optimization.distance_unit(DISTANCE_UNIT.MI)
optimization.travel_mode(TRAVEL_MODE.DRIVING)
for i, address in enumerate(addresses):
    #The below line will pull lng/lat coordinates from the postcodes which are
    #needed to work with the API
    geocode_error, address = r4m.address.fix_geocode(address)
    address["time"] = 60
    if i == 0:
        address.pop("time")
        address["is_depot"] = True
    r4m_addresses.add_address(**address)

response = r4m.run_optimization()