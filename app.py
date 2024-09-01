# Core Pkgs
import streamlit as st
import pandas as pd
from faker import Faker
import base64
import time
import random
import seaborn as sns
import matplotlib.pyplot as plt
import io
# Utilse
timestr = time.strftime("%Y%m%d-%H%M%S")


# Fxn to Download Into A Format
def make_downloadable_df_format(data, format_type="csv"):
    if format_type == "csv":
        datafile = data.to_csv(index=False)
        b64 = base64.b64encode(datafile.encode()).decode()  # B64 encoding
        st.markdown("### ** Download CSV File ** ")
        new_filename = "fake_dataset_{}.csv".format(timestr)
        href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
        st.markdown(href, unsafe_allow_html=True)
    elif format_type == "json":
        datafile = data.to_json()
        b64 = base64.b64encode(datafile.encode()).decode()  # B64 encoding
        st.markdown("### ** Download JSON File  📩 ** ")
        new_filename = "fake_dataset_{}.json".format(timestr)
        href = f'<a href="data:file/json;base64,{b64}" download="{new_filename}">Click Here!</a>'
        st.markdown(href, unsafe_allow_html=True)
    elif format_type == "jpeg":
        # Convert DataFrame to a JPEG image representing a table
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=data.values, colLabels=data.columns, loc='center')

        # Save the plot to a BytesIO object
        buffer = io.BytesIO()
        plt.savefig(buffer, format='jpeg')
        buffer.seek(0)

        # Encode the image data into base64
        b64_image = base64.b64encode(buffer.getvalue()).decode()

        # Display the download link for the JPEG image
        st.markdown("### ** Download JPEG Image ** ")
        new_filename = "fake_dataset_{}.jpeg".format(timestr)
        href = f'<a href="data:image/jpeg;base64,{b64_image}" download="{new_filename}">Click Here!</a>'
        st.markdown(href, unsafe_allow_html=True)

nigerian_full_names = [
    "Chidinma Okonkwo", "Chiemeka Nwabueze", "Chijioke Obi", "Chinelo Nwankwo", "Chukwudi Eze", 
    "Chinyere Okafor", "Ezinne Ude", "Obinna Aliyu", "Oluchi Ani", "Uchechi Okafor", "Ifunanya Odumegwu", 
    "Ngozi Eze", "Onyeka Okoro", "Chioma Okonkwo", "Olamide Okeke", "Ayomide Lawal", "Adewale Mohammed", 
    "Adeola Abubakar", "Oluwaseun Adesina", "Olufemi Ibrahim", "Folasade Adebayo", "Folake Obafemi", 
    "Adetokunbo Adewale", "Oluwatobi Odumosu", "Oluwatoyin Adeniyi", "Femi Adeyemi", "Bukola Ogunleye", 
    "Oluwakemi Balogun", "Olukemi Bello", "Kehinde Agboola", "Taiwo Adeoti", "Kehinde Babatunde", 
    "Kehinde Dada", "Kemi Adekunle", "Dayo Adewusi"
]


# Generate A Customized Profile Per Locality
def generate_locale_profile(number, locale, random_seed=200):
    locale_fake = Faker(locale)
    Faker.seed(random_seed)
    data = []

    for i in range(number):
        profile = locale_fake.simple_profile()
        profile['name'] = locale_fake.random_element(nigerian_full_names)
        mat_no_suffix = ''.join(random.choices('0123456789', k=7))
        profile['mat_no'] = f"ENG{mat_no_suffix}"
        profile['exam_scores'] = locale_fake.random_int(min=0, max=70)
        profile['ca_scores'] = locale_fake.random_int(min=0, max=30)

        total_score = profile['exam_scores'] + profile['ca_scores']
        if total_score >= 70:
            profile['grade'] = 'A'
            profile['remarks'] = 'PASS'
        elif 60 <= total_score <= 69:
            profile['grade'] = 'B'
            profile['remarks'] = 'PASS'
        elif 50 <= total_score <= 59:
            profile['grade'] = 'C'
            profile['remarks'] = 'PASS'
        elif 45 <= total_score <= 49:
            profile['grade'] = 'D'
            profile['remarks'] = 'PASS'
        elif 40 <= total_score <= 44:
            profile['grade'] = 'E'
            profile['remarks'] = 'PASS'
        else:
            profile['grade'] = 'F'
            profile['remarks'] = 'FAIL'

        data.append(profile)
    for profile in data:
        del profile['address']
        del profile['username']
        del profile['mail']
        del profile['birthdate']

    df = pd.DataFrame(data)

    return df


def main():
    # st.markdown(
    #     """
    #     <style>
    #     .stApp {
    #         background-color: white;
    #         color: black
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    menu = ["Home", "Customize", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        number_to_gen = st.sidebar.number_input("Number", 10, 5000)
        localized_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de",
                               "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA",
                               "en_GB", "en_IE", "en_IN", "en_NZ", "en_NG", "ng_NG", "en_PH", "en_TH", "en_US",
                               "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA",
                               "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID",
                               "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV",
                               "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT",
                               "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH",
                               "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
        locale = st.sidebar.multiselect("Select Locale", localized_providers, default="en_US")
        dataformat = st.sidebar.selectbox("Save Data As", ["csv", "json", "jpeg"])

        df = generate_locale_profile(number_to_gen, locale)
        st.dataframe(df)
        with st.beta_expander("📩: Download"):
            make_downloadable_df_format(df, dataformat)

    elif choice == "Customize":
        st.subheader("Customize Your Fields")
        localized_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de",
                               "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA",
                               "en_GB", "en_IE", "en_IN", "en_NZ", "en_NG", "ng_NG", "en_PH", "en_TH", "en_US",
                               "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA",
                               "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID",
                               "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV",
                               "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT",
                               "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH",
                               "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
        locale = st.sidebar.multiselect("Select Locale", localized_providers, default="en_US")

        profile_options_list = ['name', 'sex', 'mail', 'birthdate', 'job', 'company', 'ssn', 'residence',
                                'current_location', 'blood_group', 'website']
        profile_fields = st.sidebar.multiselect("Fields", profile_options_list, default='name')

        number_to_gen = st.sidebar.number_input("Number", 10, 10000)
        dataformat = st.sidebar.selectbox("Save Data As", ["csv", "json"])

        custom_fake = Faker(locale)
        data = [custom_fake.profile(fields=profile_fields) for i in range(number_to_gen)]
        df = pd.DataFrame(data)

        st.dataframe(df)

        with st.beta_expander("🔍: View JSON "):
            st.json(data)

        with st.beta_expander("📩: Download"):
            make_downloadable_df_format(df, dataformat)

    else:
        st.subheader("About")
        st.success("Built with Streamlit")
        st.text("By Divine")


if __name__ == '__main__':
    main()
