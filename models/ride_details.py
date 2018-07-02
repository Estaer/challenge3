from .ride import Ride
from .request import MakeRequest

class All_Rides:
    def __init__(self):
        self.rides = []
        self.riderequest = []
        
    # lists of all rides
    # rides = []

    def get_rides(self):
        return [ride.__dict__ for ride in self.rides] 

    def get_single_ride(self, rideId):

        for ride in self.rides:
            if ride.rideId == rideId:
                return {'message':'Here are the details for this ride','ride': ride.__dict__}
        else:
            return {'message':'Ride doesnot exist'}
    
    def post_ride(self, rideId, driver_id, meetingpoint, departure, destination, slots):
        new_ride = Ride(rideId, driver_id, meetingpoint, departure, destination, slots)
        self.rides.append(new_ride)
    
    def make_request(self, rideId, request_id, status):
        new_request = MakeRequest(rideId, request_id, status)
        self.riderequest.append(new_request)



# All_Rides.rides.append(Ride('R01', 'D01', 'Buziga', '12/06/18 9:00am', 'Nakawa', 5))
# All_Rides.rides.append(Ride('R02', 'D02', 'Makerere', '14/06/18 9:00am', 'Kyanja', 3))
# All_Rides.rides.append(Ride('R03', 'D03', 'Kololo', '15/06/18 9:00am', 'Kisaasi', 1))
# All_Rides.rides.append(Ride('R04', 'D04', 'Kiwatule', '16/06/18 9:00am', 'Bukoto', 4))

    