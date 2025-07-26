import pandas as pd

import folium

def main():

    # Create a map using the us-states.json file

    tn_map = folium.Map(location=[11.127123, 78.656891], zoom_start=7)

    # Add a tile layer to the map

    folium.TileLayer('Mapbox Bright', attr='Mapbox Bright').add_to(tn_map)

    # Read the Excel file into a DataFrame

    df = pd.read_excel("C:\\Users\\Admin\\Desktop\\tns.xlsx")

    # Loop through the rows in the DataFrame

    for index, row in df.iterrows():

        # Get the data for each state

        lat = row["Latitude"]

        lon = row["Longitude"]

        temp = row["Temperature"]
        print(temp)

        # Add a circle marker for each state

        folium.CircleMarker(location=[lat, lon], radius=10, popup=str(temp)+"°F", fill_color=get_color(temp), color="grey", fill_opacity=0.7).add_to(tn_map)

    # Save the map

    tn_map.save("tn_map.html")

def get_color(temp):

    # Use a conditional statement to set the marker color

    if temp < 80:

        return "green"

    elif temp < 95:

        return "orange"

    else:

        return "red"

if __name__ == "__main__":

    main()
