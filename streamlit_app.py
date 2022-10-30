import streamlit
import pandas
import requests
#
#
#streamlit.header('Breakfast Menu')
#streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
#streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
#streamlit.text('🐔 Hard-Boiled Free-Range Egg')
#streamlit.text('🥑🍞 Avocado Toast')
#
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#
#fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#
#streamlit.dataframe(my_fruit_list.loc[fruits_selected])


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

