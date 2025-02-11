import random
import streamlit as st

# Here I Define activities
warmer_activities = ["Speed dating", "Dance the Topic", "Pass the PASSel",
                      "OK, A bit foggy, No idea!", "Snowball", "Back to the board (Celebrity Head)"]
activity_1 = ["Jigsaw", "Moving Questions", "Lecture Summary", "KWLS Knowledge Reflection",
              "Teach Your Grandma", "Students Q, A & M"]
activity_2 = ["Interviewing", "Create a Webpage", "Flash Cards", "Tabulating",
              "Thumb balls", "Real World Examples"]
activity_3 = ["Elaborate", "Talk Word Charade", "Tabulating", "Create a Webpage",
              "Mind Maps", "Moving Questions"]
summary_activities = ["3-2-1 Summary", "Memetastic", "Kahoot",
                      "Haiku Poetry Summary", "Expansion Questions", "MentiMeter-Word Cloud"]

# Streamlit App
st.title("UniPASS Random Session Plan Generator 🎲")

if st.button("Generate Random Plan"):
    st.write("### Your Random UniPASS Session Plan:")
    st.write(f"**Warmer:** {random.choice(warmer_activities)}")
    st.write(f"**Activity 1:** {random.choice(activity_1)}")
    st.write(f"**Activity 2:** {random.choice(activity_2)}")
    st.write(f"**Activity 3:** {random.choice(activity_3)}")
    st.write(f"**Summary:** {random.choice(summary_activities)}")

    st.markdown("---")  # Horizontal line for separation
    st.caption("Courtesy of Abdel (Razzak)! 😊")
