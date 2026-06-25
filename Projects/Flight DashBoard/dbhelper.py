import mysql.connector

class DB:
    
    def __init__(self):
        
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sahil@948",
                database = 'flights'
            )
            self.mycursor = self.conn.cursor()
            print("Connected to server")
        except:
            print('Connection Failed')

    
    def fetch_flights_city(self):
        lst = []
        self.mycursor.execute("""
SELECT distinct(Source) FROM flights.flights_data
union
select distinct(Destination) from flights.flights_data
""")
        data = self.mycursor.fetchall()
        for items in data:
            lst.append(items[0])

        return lst

    def fetch_Source_destination_details(self,source,destination):
        self.mycursor.execute("""
select Airline,Route,Dep_time,Duration,Price from flights.flights_data
where Source = '{}' and Destination = '{}'
""".format(source,destination))
        data = self.mycursor.fetchall()
        return data


    def fetch_Airline_frequency(self):
        airline = []
        frequency = []
        self.mycursor.execute("""
select Airline,count(*) as 'frequnecy' from flights.flights_data
group by Airline
""")
        data = self.mycursor.fetchall()
        for items in data:
            airline.append(items[0])
            frequency.append(items[1])

        return airline,frequency
    
    def busy_airpory_city(self):
        source = []
        frequency = []
        self.mycursor.execute("""
select Source,count(*) from(
select Source from flights.flights_data
union all
select Destination from flights.flights_data
) t1
group by t1.Source
order by count(*) desc
""")
        data = self.mycursor.fetchall()
        for items in data:
            source.append(items[0])
            frequency.append(items[1])

        return source,frequency


    def Fetch_avg_price(self):
        airline = []
        avg_price = []
        self.mycursor.execute("""
select Airline,Round(avg(Price)) from flights.flights_data
group by Airline
order by Round(avg(Price)) desc
""")
        data = self.mycursor.fetchall()
        for items in data:
            airline.append(items[0])
            avg_price.append(items[1])

        return airline,avg_price

        


