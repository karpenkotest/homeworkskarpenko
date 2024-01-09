sizes = {'xxs':{'de':36,'usa':8,'fr':38,'gb':24}, 'xs':{'de':38,'usa':10,'fr':40,'gb':26}, 's':{'de':40, 'usa':12,'fr':42,'gb':28}, 'm':{'de':42,'usa':14,'fr':44,'gb':30}, 'l':{'de':44,'usa':16,'fr':46,'gb':32}, 'xl':{'de:':46,'usa':18,'fr':48,'gb':34}, 'xxl':{'de':48,'usa':20,'fr':50, "gb":36},'xxxl':{'de':50,'usa':22,'fr':52, "gb":38}}
size_raw = str(input("Please input size (from xxs to xxxl):", ))
size=size_raw.lower()
country_raw=str(input("Please input country (DE-Germany, USA-USA, FR-France, GB-Grait Britain):", ))
country=country_raw.lower()
converted_size=sizes.get(size).get(country)
print(f'You should buy this size and it will fit perfectly:{converted_size}')
