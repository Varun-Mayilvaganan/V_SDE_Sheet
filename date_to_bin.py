# using in-built functions - just to explore more
from datetime import datetime
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Parse the date string into a date object
        date_obj = datetime.strptime(date,"%Y-%m-%d")
        # extract the each value and save it separate
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        # convert the isolated value into binary form and concatenate it with "-"
        return bin(year)[2:]+"-"+bin(month)[2:]+"-"+bin(day)[2:]

#Alternate solution for this problem without using the in-built functions

# class Solution:
#     def convertDateToBinary(self, date: str) -> str:
#         # Manually parse the date string
#         year = int(date[0:4])
#         month = int(date[5:7])
#         day = int(date[8:10])
        
#         # Convert to binary
#         return bin(year)[2:] + "-" + bin(month)[2:] + "-" + bin(day)[2:]
