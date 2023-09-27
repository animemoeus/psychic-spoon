import unittest

from .utils import format_date, get_jakarta_weather


class TestJakartaWeather(unittest.TestCase):
    def test_jakarta_weather(self) -> None:
        response = get_jakarta_weather()
        weather_list = response.get("list")

        print("Weather Forecast:")
        for index, weather in enumerate(weather_list):
            # Only show once for each date
            if format_date(weather.get("dt")) == format_date(
                weather_list[index - 1].get("dt")
            ):
                continue

            print(
                f'{format_date(weather.get("dt"))}: {weather.get("main").get("temp")}°C'
            )
