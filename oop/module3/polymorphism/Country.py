# create two country classes, Argentina and Brazil, with two methods, capital and official language 
class Argentina:
    def capital(self):
        return "Buenos Aires is the capital of Argentina"
    
    def official_language(self):
        return "The spanish is the official language of Argentina"
    
class Brazil:
    def capital(self):
        return "Brasilia is the capital of Brazil"
    
    def official_language(self):
        return "The brazilian portuguese is the official language of Brazil"
    
# create an instance for each class

argentina = Argentina()
brazil = Brazil()

# print the capital and official language for each class, using loop structure for

for country in (argentina, brazil):
    print(country.capital())
    print(country.official_language())