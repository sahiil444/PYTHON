import streamlit as st

st.title('Chai Ki Tapri')
st.subheader('Founder: DJ Bara')


with st.expander('How to Make Chai Like Dolly Chai Wala OR MBA Chai Wala'):
    st.write("""
1.  1 cup water
             
2.  1 cup milk
             
3.  1 teaspoon black tea leaves
             
4.  1–2 teaspoons sugar (adjust to taste)
             
5.  1-inch fresh ginger (crushed, optional)
             
6.  2–3 cardamom pods (crushed, optional)
""")

st.sidebar.title('Select Your Menu')
name = st.sidebar.text_input('Enter your Name')
flavour = st.sidebar.selectbox('Chose your Chai',['Chai Type','Masala Chai','Adrak Chai','Pink Tea'])

if flavour == 'Adrak Chai':
    st.title('All About Adrak Chai')
    st.write("""
<Description>

Adrak Chai is one of the most popular Indian teas, made by brewing fresh ginger with black tea, milk, sugar, and aromatic spices. The strong flavor of ginger gives the tea a warm, spicy taste that is both refreshing and comforting. It is especially enjoyed during rainy and winter seasons.

Ginger is known for its natural health benefits, including helping with digestion, relieving sore throat, reducing cold symptoms, and boosting immunity. Adrak Chai is commonly served at homes, tea stalls, and cafés across India.

""")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('#### Masal Chai')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf_ukz1hL6YV_eIgSDqUXlAmEglaxdtQ73oge6cJQxOQ&s=10',width=170)

    with col2:
        glass_type = st.selectbox('Chose Glass Type',['Plastic','Kulahad','Tadur','Glass'])
        st.slider(label='Numer of Glass',min_value=1,max_value=10,value=1)
        order = st.button('Order')
        if order:
            st.success(f"{name} your {flavour} order successfully")


elif flavour == 'Masala Chai':
    st.title('All About Masala Chai')
    st.write("""
Description:

Masala Chai is a traditional Indian tea made by brewing black tea with milk, sugar, and a blend of aromatic spices. The combination of spices such as cardamom, cinnamon, cloves, ginger, and black pepper creates a rich, flavorful, and comforting drink. It is one of the most loved beverages in India and is enjoyed in homes, cafés, and tea stalls throughout the day.

Masala Chai is known for its warming taste and natural health benefits. The spices help improve digestion, boost immunity, and provide a refreshing burst of energy. Whether served in the morning or during evening tea breaks, Masala Chai is a perfect companion with snacks like biscuits, samosas, or pakoras.

""")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('#### Masal Chai')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVCgHwYjqKwjIoJey_7f6Oc6PfDeW2haWmO51iv4SOiQ&s=10',width=170)

    with col2:
        glass_type = st.selectbox('Chose Glass Type',['Plastic','Kulahad','Tadur','Glass Cup'])
        st.slider(label='Numer of Glass',min_value=1,max_value=10,value=1)
        order = st.button('Order')
        if order:
            st.success(f"{name} Your {flavour} order successfully")

elif flavour == 'Pink Tea':
    st.title('All About Pink Tea')
    st.write("""
Pink Tea, also known as Kashmiri Chai or Noon Chai, is a traditional tea from the Kashmir region of India. It is famous for its beautiful pink color, creamy texture, and unique flavor. Unlike regular tea, it is prepared using special green tea leaves, milk, baking soda, water, and salt or sugar, depending on the recipe. It is often garnished with chopped almonds, pistachios, and saffron for a rich and luxurious taste.

Pink Tea is especially popular during winter because of its warm and comforting nature. It is commonly served during festivals, family gatherings, and special occasions.
""")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('#### Pink tea')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmzlH2oYRxwkbgru3a_A19La2TJLNJ4-G9_84KrLn1cQ&s=10',width=170)

    with col2:
        glass_type = st.selectbox('Chose Glass Type',['Plastic','Kulahad','Tadur','Glass'])
        st.slider(label='Numer of Glass',min_value=1,max_value=10,value=1)
        order = st.button('Order')
        if order:
            st.success(f"{name} Your {flavour} order successfully")

