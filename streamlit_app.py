import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
    streamlit.error()
  

streamlit.stop()

#import snowflake.connector

streamlit.header("The fruit load list conatins:")
# snowflake-related  functions
def get_fruit_load_list():
  with my_cnx.cursor as my_cur:
    my_cur.execute("selectt * from fruit_load_list")
    return my_cur.fetchall()
    
 #add a button to load fruit
if stramlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('what fruit you like to add')
streamlit.write('Thanks for adding', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")



  
