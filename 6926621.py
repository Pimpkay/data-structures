


carBrands={'Toyota','Mercedes-Benz','Range Rover','Porsche','Honda','Rolls Royce'}

carModel={'Camry':78000,'Corolla':65000,'Vitz':35000,'Yaris':30000,'Tundra':300000,
          'Land Cruiser':400000,'Highlander':110000,'Rav-4':110000,'Vensa':95000,
          'Sport':520000,'Velar':510000,'Autobiography':550000,'Discovery':530000,
          'Evoque':390000,'C300':120000,'E300':150000,'E350':158000,'S550':400000,
          'S63':560000,'ML350':130000,'GLC300':187000,'GLS450':205000,'Accord':110000,
          'CR-V':125000,'HR-V':135000,'Civic':90000,'Cayenne':230000,'Cayman':245000,
          'Panamara':235000,'Boxster Spyder':205000,'911 GT':220000,'Ghost':400000,'Cullinan':500000}


#Get customer input for car brand
carName=input('Kindly enter your car of interest: ')

#Checks if care in is in the list of cars
if carName in carBrands:
    print('Your car of interest is currently available')
else:
    print('So sorry to inform your choice currently unavailable') 

#If car name is present,find the price
carModelRequest=input('What specific model of {} are you interested in? '.format(carName))
if carModelRequest in carModel :
    print('Yes it is available')
else:
    print('Your choice currently unavailable')
    carPrice=carModel[carModelRequest]
    print('The price of {} is ${}'.format(carName,carPrice))