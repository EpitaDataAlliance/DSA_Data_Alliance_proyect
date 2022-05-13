import streamlit as st
import requests


# import data file csv
# df = pd.read_csv('merc.csv')
files = st.file_uploader(label="", accept_multiple_files=True, type="csv")
# if file:
#     st.write(f'{file} is uploaded')
#     # df = pd.read_csv(file.read())
#     df = pd.read_csv(file)
#     st.write(f'{df.info()}')
# set page title
# st.set_page_config('Mercedes Price Prediction App')


st.title("Mobile Phone Price Prediction")

menu_list = ["Exploratory Data Analysis", "Predict Price"]
menu = st.radio("Menu", menu_list)

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

if st.button("Predict"):
    if pred_json is not None:
        res = requests.get("http://0.0.0.0:8080/predict", json=pred_json)
        pred = res.json()
        pred_price = pred['predictions'][0]

        if pred_price == 0:
            estimation = 'VERY CHEAP'
        elif pred_price == 1:
            estimation = 'CHEAP'
        elif pred_price == 2:
            estimation = 'EXPENSIVE'
        else:
            estimation = 'VERY EXPENSIVE'

        st.markdown("<h2 style='text-align: left;'> Prediction </h2>", unsafe_allow_html=True)
        st.success(f"The price of the phone would be {estimation}")
    else:
            st.error("Something went wrong")