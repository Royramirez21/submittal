"""Utilities for generating CSI Division 07 Roofing submittals."""

from __future__ import annotations

import os
from typing import Any

import openai

SYSTEM_PROMPT = (
    "You are a helpful assistant specializing in creating CSI Division 07"
    " Roofing submittals. Provide concise, professional documentation."
)


def generate_roofing_submittal(
    project: str,
    roof_type: str,
    materials: str,
    manufacturer: str,
    standards: str,
) -> str:
    """Generate a Division 07 roofing submittal using OpenAI's API.

    Parameters
    ----------
    project: Project name.
    roof_type: Type of roof system.
    materials: Materials included in the roofing system.
    manufacturer: Manufacturer of the roofing products.
    standards: Applicable standards or references.

    Returns
    -------
    str
        Generated submittal document.

    Raises
    ------
    ValueError
        If the ``OPENAI_API_KEY`` environment variable is not set.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key

    prompt = f"""
Create a CSI Division 07 Roofing submittal with the following information:
Project: {project}
Roof Type: {roof_type}
Materials: {materials}
Manufacturer: {manufacturer}
Standards: {standards}

Include sections for Product Data, Installation, and Warranty.
"""

    response: Any = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=500,
    )

    return response["choices"][0]["message"]["content"].strip()
