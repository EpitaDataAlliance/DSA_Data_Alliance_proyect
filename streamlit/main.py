import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout='wide')
st.title("Mobile Phone Price Prediction")
st.subheader("Choose a file or adjust the parameters in the sidebar")

estimation = '...'
font_color = 'gray'

with st.sidebar:

    col1, col2 = st.columns(2)

    pc = st.slider("Primary Camera Resolution (MP)", 0, 20, value=10)
    fc = st.slider("Front Camera Resolution (MP)", 0, 20, value=10)
    n_cores = st.slider("Number of Cores", 1, 8, value=4)

    int_memory = st.selectbox("Internal Memory (GB)", (2, 4, 8, 16, 32, 64))
    ram = st.selectbox("RAM (MB)", (256, 512, 1024, 2048, 3072, 4096))

    with col1:
        four_g = st.checkbox("4G")
        blue = st.checkbox("Bluetooth")
        dual_sim = st.checkbox("Dual SIM")
        
    with col2:
        three_g = st.checkbox("3G")
        touch_screen = st.checkbox("Touch Screen")
        wifi = st.checkbox("WiFi")

    feature_expander = st.expander(label='Other features')

    with feature_expander:

        battery_power = st.slider("Battery Power", 500, 2000, step=100, value=1250)
        clock_speed = st.slider("Clock Speed", 0.5, 3.0, step=0.5, value=1.75)
        px_height = st.slider("Pixel Height (px)", 0, 2000, step=100, value=1000)
        px_width = st.slider("Pixel Width (px)", 0, 2000, step=100, value=1000)
        sc_h = st.slider("Screen Height (cm)", 0, 20, value=10)
        sc_w = st.slider("Screen Width (cm)", 0, 20, value=10)
        talk_time = st.slider("Talk Time (min)", 0, 20, value=10)
        m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0, step=0.1, value=0.5)
        mobile_wt = st.slider("Mobile Weight (gr)", 80, 200, step=20, value=140)

    col3, col4, col5 = st.columns(3)

    with col4:
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
                res = requests.get("http://0.0.0.0:5000/predict", json=pred_json)
                # res = requests.get("http://fastapi:5000/predict", json=pred_json) # for docker
                pred = res.json()
                pred_price = pred["predictions"][0]

                if pred_price == 0:
                    estimation = "VERY CHEAP"
                    font_color = 'green'
                elif pred_price == 1:
                    estimation = "CHEAP"
                    font_color = 'yellow'
                elif pred_price == 2:
                    estimation = "EXPENSIVE"
                    font_color = 'orange'
                else:
                    estimation = "VERY EXPENSIVE"
                    font_color = 'red'

            else:
                st.error("Something went wrong")

st.markdown("<h3 style='text-align:left; color:gray'> Prediction </h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align:left; color:{font_color}'>The price of the phone would be {estimation} </h4>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=",")
    df_json = dataframe.to_json(orient='records')
    payload = {"dataframe1": df_json}
    res = requests.post("http://fastapi:5000/predictjson", json=payload)
    st.subheader("Predicted prices from file")
    st.success(res.json()['predictions'])


# get the data from the database
st.subheader("Predicted prices from database")
res = requests.get("http://0.0.0.0:5000/predictions") # for local
st.success(res.json())



if __name__ == "__main__":
    pass
