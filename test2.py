test = [(1, '/lCfKAAFyANPFn04xOPqazd8jwnc.jpg', 'The Grinch', 90, '2018-11-08', 'Animation', 
	'The Grinch hatches a scheme to ruin Christmas when the residents of Whoville plan their annual holiday celebration.', 
	"(['Benedict Cumberbatch', 'Cameron Seely', 'Rashida Jones', 'Angela Lansbury', 'Kenan Thompson'],)", 
	"['/wz3MRiMmoz6b5X3oSzMRC9nLxY1.jpg', '/wpo7g3DdcOBkkgZJPBAsXwpkZ1b.jpg', '/jjp33eRM6oavyesW0UM6XBCxQSa.jpg', '/vHnkT39YwSRVoiFbvG7wFqwXA2Y.jpg', '/As3n7ZdAoUnaB39Jl19eJBZOPbl.jpg']")]

#################### Starring images
res = test[0][8]
a = res.split()
result_url = []

for i in range(5):
	a[i] = a[i].replace(',', '')
	a[i] = a[i].replace("'", '')
	a[i] = a[i].replace("[", '')
	a[i] = a[i].replace("]", '')
	url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2' + a[i]
	result_url.append(url)
print(result_url)


# #################### Starring lists
# res = test[0][7]
# a = res.split()
# c = []
# index = 0
# for i in range(5):
# 	b = str(a[index:index+2])
# 	b = b.replace(",", "")
# 	b = b.replace("'", '')
# 	b = b.replace('[', '')
# 	b = b.replace(']', '')
# 	b = b.replace('(', '')
# 	b = b.replace(')', '')
# 	b = b.replace('"', '')
# 	c.append(b)
# 	index += 2

# print(c)