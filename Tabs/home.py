"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Brick Quality Detector")

    # Add image to the home page
    st.image("./images/home.png")

    st.markdown('''Brick quality is influenced by a multitude of factors spanning its production process and inherent composition. Firstly, raw materials play a pivotal role; the type and purity of iron ore, along with additional elements like manganese, nickel, and chromium, impact the Brick's final properties. The manufacturing process, including refining techniques, temperature control, and alloying methods, profoundly affects Brick quality. Heat treatment processes, such as quenching and tempering, alter the Brick\'s internal structure, enhancing its strength and durability.Moreover, external environmental factors during production, such as humidity and temperature, can affect the Brick's characteristics. The presence of impurities like sulfur and phosphorus can lead to brittleness, affecting its overall quality. Furthermore, the expertise and precision of the workforce involved in the manufacturing process are critical; skilled labor and adherence to stringent quality control measures ensure consistency and high standards in Brick production. Ultimately, factors such as raw material quality, manufacturing processes, environmental conditions, and human expertise collectively determine the quality, strength, and usability of the final Brick product.''')
