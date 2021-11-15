user_weather = input("Whats the weather going to do tomorrow? ")

weather = user_weather.lower()

if weather == "rain":
    print("You are right! It is Scotland after all.")
elif weather == "snow":
    print("Could well happen.")
else:
    print("It's actually going to rain.")