#! bin/bash
weather = input("what's the weather like today? (sunny/rainy/cold):")
if "sunny" :recommendation = "Wear a t-shirt and sunglasses."
elif "rainy" :recommendation = "Don't forget your umbrella and a raincoat."
elif "cold" :recommendation = "Make sure to wear a warm coat and a scarf."
else:recommendation = "Sorry, I don't have recommendations for this weather."
print(recommendation)
