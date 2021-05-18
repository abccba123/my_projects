'''
(Guess the capitals) Rewrite Exercise 11.40 using a dictionary to store the pairs
of states and capitals so that the questions are randomly displayed.
'''

States_capital_dict = {"Alabama":"Montgomery","Alaska":"Juneau","Arizona":"Phoenix","Arkansas":"Little Rock","California":"Sacramento","Colorado":"Denver",
"Connecticut":"Hartford",
"Delaware":"Dover",
"Florida":"Tallahassee",
"Georgia":"Atlanta",
"Hawaii":"Honolulu",
"Idaho":"Boise",
"Illinois":"Springfield",
"Indiana":"Indianapolis",
"Iowa":"Des Moines",
"Kansas":"Topeka",
"Kentucky":"Frankfort",
"Louisiana":"Baton Rouge",
"Maine":"Augusta",
"Maryland":"Annapolis",
"Massachusetts":"Boston",
"Michigan":"Lansing",
"Minnesota":"Saint Paul",
"Mississippi":"Jackson",
"Missouri":"Jefferson City",
"Montana":"Helena",
"Nebraska":"Lincoln",
"Nevada":"Carson City",
"New Hampshire":"Concord",
"New Jersey":"Trenton",
"New Mexico":"Santa Fe",
"New York":"Albany",
"North Carolina":"Raleigh",
"North Dakota":"Bismarck",
"Ohio":"Columbus",
"Oklahoma":"Oklahoma City",
"Oregon":"Salem",
"Pennsylvania":"Harrisburg",
"Rhode Island":"Providence",
"South Carolina":"Columbia",
"South Dakota":"Pierre",
"Tennessee":"Nashville",
"Texas":"Austin",
"Utah":"Salt Lake City",
"Vermont":"Montpelier",
"Virginia":"Richmond",
"Washington":"Olympia",
"West Virginia":"Charleston",
"Wisconsin":"Madison",
"Wyoming":"Cheyenne"}

count = 0
States = States_capital_dict.keys()
for States in States_capital_dict:
    Capital = input("What is the Capital of: " + States + "?").strip()
    if Capital.lower() == States_capital_dict[States].lower():
        print("Correct answer!")
        count += 1
    else:
        print("The correct answer is: " + States_capital_dict[States])
print("The correct total answer count is:", count)
