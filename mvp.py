import streamlit as st

# Function to calculate expected value
def calculate_expected_value(chance_mold, chance_no_sugar, chance_typical_sugar, chance_high_sugar):
     # Expected profit if not harvesting now, given the probabilities
    p_no_storm = 0.36  # Probability of predicting no sotrm
    p_no_storm_given_predicted_no_storm = 0.7  # Probability of no storm given predicted no storm
    expected_profit_not_harvest_no_storm = (chance_no_sugar * 960000 +
                                          chance_typical_sugar * 1410000 +
                                          chance_high_sugar * 1500000)
    expected_profit_not_harvest_storm = (chance_mold * 3300000 + (1 - chance_mold) * 420000)
    expected_profit_not_harvest = p_no_storm * (expected_profit_not_harvest_no_storm * p_no_storm_given_predicted_no_storm + 
                                    expected_profit_not_harvest_storm * (1 - p_no_storm_given_predicted_no_storm)) + (1 - p_no_storm) * 960000
    
    # Profit from harvesting now is a constant based on the provided data
    profit_harvest_now = 960000

    # Determine the recommended alternative based on the higher expected profit
    if expected_profit_not_harvest > profit_harvest_now:
        recommended_alternative = "Harvest Based on predicted result"
    else:
        recommended_alternative = "Harvest Now"

    return expected_profit_not_harvest, recommended_alternative

# Streamlit UI
st.title('Wine Harvest Decision Model')

# Sliders for likelihood adjustments
chance_of_botrytis = st.slider('Chance of Botrytis Mold (%)', 0, 100, 10)
chance_of_no_sugar = st.slider('Chance of No Sugar Level Increase (%)', 0, 100, 60)
chance_of_typical_sugar = st.slider('Chance of Typical Sugar Level Increase (%)', 0, 100, 30)
chance_of_high_sugar = st.slider('Chance of High Sugar Level Increase (%)', 0, 100, 10)

# Adjust the chances to probabilities
prob_botrytis = chance_of_botrytis / 100
prob_no_sugar = chance_of_no_sugar / 100
prob_typical_sugar = chance_of_typical_sugar / 100
prob_high_sugar = chance_of_high_sugar / 100

# Button to calculate expected value
if st.button('Calculate Expected Value'):
    expected_value, recommended_alternative = calculate_expected_value(prob_botrytis, prob_no_sugar, prob_typical_sugar, prob_high_sugar)
    st.write(f"Expected Value: ${expected_value}")
    st.write(f"Recommended Alternative: {recommended_alternative}")