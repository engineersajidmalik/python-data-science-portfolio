"""
Q21. Create a tuple containing your name, age, and city.
Use destructuring to print the values.
"""
my_info = ("Sajid",24,"Multan")
name,age,city = my_info
print(name,age,city,sep="\n")

"""
Q22. Create a list of tuples containing (student_name, marks). 
Use destructuring to print each student's name and marks.
"""
std_info = [("Waseem",45),("Usman",44),("Rizwan",55)]
for name, marks in std_info:
    print(name,marks)

"""
Q23. Create a list of tuples containing (product_name, price).
 Use destructuring to print only products whose price is greater than 1000.
"""
product_info = [("Pen",2000),("Marker",300),("Ink",5000),("Clipboard",100)]
for p_name,p_price in product_info:
    if p_price > 1000:
        print(p_name,p_price)

"""
Q24. Create a list of tuples containing (x, y) coordinates.
 Use destructuring inside a for loop  to print each coordinate.
"""
coordinates = [(60,90),(40,80),(30,86)]
for x,y in coordinates:
    print(x,y)

"""
Q25. Create a list of tuples containing (country, capital).
 Use destructuring to display each  country with its capital.
"""
country_info = [("Pak","Isl"),("USA","DC"),("Iran","Tehran")]
for country,capital in country_info:
    print(country,capital)