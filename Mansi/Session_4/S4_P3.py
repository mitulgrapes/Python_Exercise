print("3) Create list with 5 items and print each item using iter() & next() method.\n")

City = ["Ahmedabad","Baroda","Surat","Nadiad","Amreli"]
demo = iter(City)

for no in range(len(City)):
	print(next(demo))
