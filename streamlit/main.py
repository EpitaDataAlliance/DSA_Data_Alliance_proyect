import streamlit as st
import requests
import pandas as pd


st.title("Mobile Phone Price Prediction with ML")

# uploaded_file = st.file_uploader('', type=["csv"])
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write(df)
# if file:
#     st.write(f'{file} is uploaded')
#     # df = pd.read_csv(file.read())
#     df = pd.read_csv(file)
#     st.write(f'{df.info()}')
# set page title
# st.set_page_config('Mercedes Price Prediction App')



# menu_list = ["Exploratory Data Analysis", "Predict Price"]
# menu = st.radio("Menu", menu_list)

# if menu == "Exploratory Data Analysis":
# st.subheader("Exploratory Data Analysis")
# st.write("This is the Exploratory Data Analysis")

# st.subheader("Data")
# st.write(df.info())
# st.write(df.describe())
# st.write(df.head())
# st.write(df.tail())
# st.write(df.shape)

# # st.subheader("Data Visualization")
# # st.write("This is the Data Visualization")
# # st.write(df.hist(bins=50, figsize=(20,15)))
# # st.write(df.boxplot())
# # st.write(df.corr())
# # st.write(df.corr()['price'].sort_values(ascending=False))
# # st.write(df.corr()['price'].sort_values(ascending=False)[:5])
# # st.write(df.corr()['price'].sort_values(ascending=False)[-5:])

# # seaborn stuff
# st.subheader("Data Visualization (seaborn)")
# st.write("This is the Data Visualization (seaborn)")
# st.write(sns.pairplot(df))
# st.write(sns.heatmap(df.corr(), annot=True))
# st.pyplot()

# # plotly stuff
# st.write(py.iplot(df.iplot(kind='scatter', x='price', y='rating', size='size',
#                           color='color', size_max=60)))

st.subheader("Choose a file or adjust the params by your needs")

battery_power = st.slider("Battery Power", 501.0, 1998.0)
clock_speed = st.slider("Clock Speed", 0.5, 3.0)
fc = st.slider("Front Camera Resolution (MP)", 0.0, 19.0)
int_memory = st.slider("Internal Memory (GB)", 2.0, 64.0)
m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0)
mobile_wt = st.slider("Mobile Weight (gr)", 80.0, 200.0)
n_cores = st.slider("Number of Cores", 1.0, 8.0)
pc = st.slider("Primary Camera Resolution (MP)", 0.0, 20.0)
px_height = st.slider("Pixel Height (px)", 0.0, 1960.0)
px_width = st.slider("Pixel Width (px)", 500.0, 1998.0)
ram = st.slider("RAM (MB)", 256.0, 3998.0)
sc_h = st.slider("Screen Height (cm)", 5.0, 19.0)
sc_w = st.slider("Screen Width (cm)", 0.0, 18.0)
talk_time = st.slider("Talk Time (min)", 2.0, 20.0)
blue = st.checkbox("Bluetooth")
dual_sim = st.checkbox("Dual SIM")
four_g = st.checkbox("4G")
three_g = st.checkbox("3G")
touch_screen = st.checkbox("Touch Screen")
wifi = st.checkbox("WiFi")

if st.button("Predict"):
    pred_json = {
        "battery_power": battery_power,
        "clock_speed": clock_speed,
        "fc": fc,
        "int_memory": int_memory,
        "m_dep": m_dep,
        "mobile_wt": mobile_wt,
        "n_cores": n_cores,
        "pc": pc,
        "px_height": px_height,
        "px_width": px_width,
        "ram": ram,
        "sc_h": sc_h,
        "sc_w": sc_w,
        "talk_time": talk_time,
        "blue": blue,
        "dual_sim": dual_sim,
        "four_g": four_g,
        "three_g": three_g,
        "touch_screen": touch_screen,
        "wifi": wifi,
    }

    for key, value in pred_json.items():
        pred_json[key] = float(value)

    if pred_json is not None:
        # res = requests.get("http://0.0.0.0:5000/predict", json=pred_json)
        res = requests.get("http://fastapi:5000/predict", json=pred_json) # for docker version
        pred = res.json()
        pred_price = pred["predictions"][0]

        if pred_price == 0:
            estimation = "VERY CHEAP"
        elif pred_price == 1:
            estimation = "CHEAP"
        elif pred_price == 2:
            estimation = "EXPENSIVE"
        else:
            estimation = "VERY EXPENSIVE"

        st.markdown("<h2 style='text-align: left;'> Prediction </h2>", unsafe_allow_html=True)
        st.success(f"The price of the phone would be {estimation}")
    else:
        st.error("Something went wrong")


# if st.button("Predict From File"):
#     if uploaded_file is not None:
#         res = requests.get(
#             "http://0.0.0.0:8080/predictFile",
#             json=pred_json,
#             files={"file": open(uploaded_file, "rb")},
#         )
#         # st.write(res.json())
#         st.write(res.json())
#     else:
#         st.warning("File not found")


    # st.markdown("<h2 style='text-align: left;'> Prediction </h2>", unsafe_allow_html=True)
    # st.success(f"The price of the phone would be {estimation}")

# # upload the file and send it to the server then get the prediction
# if st.button("Predict File"):
#     if file is not None:
#         file_name = file.filename
#         file_data = file
#         file_data = file_data.decode("utf-8")
#         file_data = file_data.split("\n")
#         file_data = file_data[:-1]
#         file_data = [float(i) for i in file_data]
#         file_data = np.array(file_data)
#         file_data = file_data.reshape(1, -1)
#         res = requests.get("http://0.0.0.0:8080/predictFile", json=pred_json, files={"file": file_data})
#         st.write(res.json())
#         st.write(res.status_code)
#     else:
#         st.error("Something went wrong")

#     st.write(file)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=",")
    df_json = dataframe.to_json(orient='records')
    payload = {"dataframe1": df_json}
    # res = requests.post("http://0.0.0.0:5000/predictjson", json=payload)
    res = requests.post("http://fastapi:5000/predictjson", json=payload) # for docker version
    st.subheader("Predicted Array from File")
    st.success(res.json()['predictions'])


if __name__ == "__main__":
    pass