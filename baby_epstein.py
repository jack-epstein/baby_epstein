import streamlit as st

GENDER = "boy"  # pick "boy" or "girl" once we know

if "gender" not in st.session_state:
    st.session_state.gender = "None"

if st.session_state.gender == "girl":
    st.markdown("# :violet[Baby Epstein is a ...]")
elif st.session_state.gender == "boy":
    st.markdown("# :blue[Baby Epstein is a ...]")
else:
    st.markdown("# Baby Epstein is a ...")
st.markdown("# 🤰🏻")

gender_button = st.button("Click here to see")

if gender_button:
    st.session_state.gender = GENDER
    if st.session_state.gender == "girl":
        st.markdown("""# :heartpulse: :violet[GIRL!!!!!] :heartpulse:""")
    elif st.session_state.gender == "boy":
        st.markdown("""# :blue_heart: :blue[BOY!!!!!] :blue_heart:""")
    else:
        st.markdown("""# we still don't know""")
    st.balloons()
