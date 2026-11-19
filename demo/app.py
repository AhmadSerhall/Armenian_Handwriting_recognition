"""Minimal Streamlit entry point for the ArmScribe AI demonstration."""

import streamlit as st


def main() -> None:
    """Render the Phase 1 information screen."""
    st.set_page_config(page_title="ArmScribe AI", page_icon="✍️")
    st.title("ArmScribe AI")
    st.write("Armenian Handwritten Character Recognition")
    st.info(
        "Recognition functionality is under development. "
        "This Phase 1 screen confirms the Streamlit application is wired up."
    )


if __name__ == "__main__":
    main()
