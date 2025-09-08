"""Streamlit app for generating Division 07 roofing submittals."""

import streamlit as st

from division7_agent import generate_roofing_submittal

st.title("🏗️ Division 07 Roofing Submittal Generator")

with st.form("submittal_form"):
    project = st.text_input("Project name")
    roof_type = st.text_input("Roof type")
    materials = st.text_area("Materials")
    manufacturer = st.text_input("Manufacturer")
    standards = st.text_input("Standards")
    submitted = st.form_submit_button("Generate submittal")

if submitted:
    try:
        result = generate_roofing_submittal(
            project=project,
            roof_type=roof_type,
            materials=materials,
            manufacturer=manufacturer,
            standards=standards,
        )
        st.subheader("Generated Submittal")
        st.write(result)
    except Exception as exc:  # noqa: BLE001
        st.error(f"Error: {exc}")
