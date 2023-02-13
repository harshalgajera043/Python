import requests
import datetime as dt
# from data_manager import DataManager

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "cShzhQu2PchVn-qZ_f64hRbmxK06Tfvv"

today = dt.datetime.now()

# start date
start_day = today.day+1
start_month = today.month
start_year = today.year
tommorrow = dt.date(start_year, start_month, start_day)
tommorrow_formated = tommorrow.strftime("%d/%m/%Y")
print(tommorrow_formated)

# End date
end_day = today.day+1
end_month = today.month+6
end_year = today.year

try:
    six_month_later = dt.date(end_year, end_month, end_day).strftime("%d/%m/%Y")
except ValueError:
    new_years = round(end_month/12)
    end_year += new_years
    end_month %= 12
    print(end_month)
finally:
    six_month_later = dt.date(end_year, end_month, end_day).strftime("%d/%m/%Y")
    print(six_month_later)

class FlightData:

    def __init__(self):
        # self.flight_details = DataManager()
        self.flight_search_api = f"{TEQUILA_ENDPOINT}/v2/search"
        self.header = {"apikey": TEQUILA_API_KEY}


    def trip(self, city_code, lowest_price):
        self.search_for_flight(city_code, lowest_price)
        self.return_details(city_code, lowest_price)

    def search_for_flight(self, city_code, lowest_price):
        self.quary = {
            "fly_from": "LON",
            "fly_to": f"{city_code}",
            "date_from": f"{tommorrow_formated}",
            "date_to": f"{six_month_later}",
        }
        self.response = requests.get(url=self.flight_search_api, headers=self.header, params=self.quary)
        print(self.cheapest_flight(lowest_price))

    def cheapest_flight(self, lowest_price):

        self.lowest_ticket = {}

        for i in range(0, 100):
            try:
                self.response.json()["data"][i]["price"]
            except IndexError:
                pass
            else:
                short = self.response.json()["data"][i]
                flight = short["price"]
                if flight <= lowest_price:
                    try:
                        flight < self.lowest_ticket["lowest_price"]
                    except KeyError:
                        self.lowest_ticket["lowest_price"] = flight
                    else:
                        if flight < self.lowest_ticket["lowest_price"]:
                            self.lowest_ticket.clear()
                            self.lowest_ticket["lowest_price"] = flight
                    finally:
                        self.lowest_ticket["city_from"] = short["cityFrom"]
                        self.lowest_ticket["city_code_from"] = short["cityCodeFrom"]
                        self.lowest_ticket["city_to"] = short["cityTo"]
                        self.lowest_ticket["city_code_to"] = short["cityCodeTo"]
                        local_arrival = self.response.json()["data"][i]["local_arrival"].split("T")[0]
                        self.lowest_ticket["trip_date"] = local_arrival
                    # self.lowest_ticket["id"] = i

        return self.lowest_ticket

    def return_details(self, city_code, lowest_price):
        try:
            dt.datetime.strptime(self.lowest_ticket["trip_date"], "%Y-%m-%d")
        except KeyError:
            pass
        else:
            flight_date = dt.datetime.strptime(self.lowest_ticket["trip_date"], "%Y-%m-%d")
            mini_return = flight_date + dt.timedelta(days=7)
            print(flight_date)
            print(mini_return)
            mini_return_formated = mini_return.strftime("%d/%m/%Y")
            max_return = flight_date + dt.timedelta(days=21)
            print(max_return)
            max_return_formated = max_return.strftime("%d/%m/%Y")
            self.return_ = {
                "fly_from": f"{city_code}",
                "fly_to": "LON",
                "date_from": f"{mini_return_formated}",
                "date_to": f"{max_return_formated}"
            }
            self.return_response = requests.get(url=self.flight_search_api, headers=self.header, params=self.return_)
        finally:
            print(self.cheapest_flight_return(lowest_price))


    def cheapest_flight_return(self, lowest_price):

        self.return_lowest_ticket = {}

        for i in range(0, 100):
            try:
                self.return_response.json()["data"][i]["price"]
            except IndexError:
                pass
            else:
                return_short = self.return_response.json()["data"][i]
                return_flight = return_short["price"]
                if return_flight <= lowest_price:
                    try:
                        return_flight < self.return_lowest_ticket["lowest_price"]
                    except KeyError:
                        self.return_lowest_ticket["lowest_price"] = return_flight
                    else:
                        if return_flight < self.return_lowest_ticket["lowest_price"]:
                            self.lowest_ticket.clear()
                            self.lowest_ticket["lowest_price"] = return_flight
                    finally:
                        self.return_lowest_ticket["city_from"] = return_short["cityFrom"]
                        self.return_lowest_ticket["city_code_from"] = return_short["cityCodeFrom"]
                        self.return_lowest_ticket["city_to"] = return_short["cityTo"]
                        self.return_lowest_ticket["city_code_to"] = return_short["cityCodeTo"]
                        return_local_arrival = self.response.json()["data"][i]["local_arrival"].split("T")[0]
                        self.return_lowest_ticket["trip_date"] = return_local_arrival
                    # self.lowest_ticket["id"] = i

        return self.return_lowest_ticket


                    # print(f"Low Price alert! Only {lowest_price} or less to fly from {city_from}-{city_code_from} to {city_to}-{city_code_from}, from {local_arrival}")




