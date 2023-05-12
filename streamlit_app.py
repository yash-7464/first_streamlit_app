import streamlit
import pandas

streamlit.title("Create first streamlit app")

streamlit.header("🥣 Breakfast Menu!!1")
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)


#let's put a pick here so they pick they want include
fruits_selected = streamlit.multiselect("Picks some fruits: ", list(my_fruit_list))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table on the page
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load conatanis:")
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('what fruit you like to add')
streamlit.write('Thanks for adding', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
