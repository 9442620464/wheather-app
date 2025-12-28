from django.shortcuts import render
import requests



def weather(request):
    weather = None

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            api = "50221fc99e63e942d7088425cd2a897f"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
            data = requests.get(url).json()

            if data.get("name"):      
                weather = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temp": round(data["main"]["temp"]),
                    "desc": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"]
                }

    return render(request, "weather.html", {"weather": weather})