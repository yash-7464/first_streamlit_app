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
fruits_selected = streamlit.multiselect("Picks some fruits: ", list(my_fruit_list), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table on the page
fruits_to_show = my_fruit_list.loc[fruits_selected]

