# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bV6Lhu8XSBqDZ0Tr0Y57ZpQwjy7KOzYk
"""

!pip install mistralai

import os
import re
from mistralai import Mistral

api_key = "2i0tgxeGBl8J8VB4j9VU5jG79m7tHbCp"
model = "mistral-large-latest"

def is_paragraph_label(line: str) -> bool:
    keywords = {
        "DISPLAY", "IF", "ELSE", "END-IF", "ADD", "SUBTRACT", "ACCEPT",
        "STOP", "MOVE", "PERFORM", "COMPUTE", "EVALUATE", "WHEN", "END-EVALUATE"
    }
    line_strip = line.strip()
    label_match = re.match(r"^([A-Z0-9\-]+)(\s+|\.)", line_strip)
    if label_match:
        word = label_match.group(1)
        return word.upper() not in keywords
    return False

def extract_cobol_paragraph(file_path: str, paragraph_name: str) -> str:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    in_paragraph = False
    paragraph_lines = []

    for line in lines:
        line_strip = line.strip()

        if re.match(rf"^{paragraph_name}(\s+|\.)", line_strip, re.IGNORECASE):
            in_paragraph = True
            paragraph_lines.append(line.rstrip())
        elif in_paragraph:
            if is_paragraph_label(line_strip):
                break  # next paragraph starts
            paragraph_lines.append(line.rstrip())

    return '\n'.join(paragraph_lines) if paragraph_lines else f"Paragraph '{paragraph_name}' not found."

def build_chat_prompt(paragraph_code: str) -> list:
    return [
        {
            "role": "user",
            "content": (
                "Fix the issues in this COBOL paragraph:\n\n"
                f"{paragraph_code}\n\n"
                "Return only the corrected code — no explanations.\n"
                "Also, remove any markdown syntax like opening and closing triple backticks (```cobol ... ```)."
            )
        }
    ]

def call_mistral_fix(api_key: str, model: str, messages: list) -> str:
    client = Mistral(api_key=api_key)
    response = client.chat.complete(model=model, messages=messages)
    return response.choices[0].message.content

def model_pipeline(file_path, function_name):
    # file_path = "/content/Resources.Designer.cbl"
    # function_name = "method-id get property"

    # first, cobol code related to the function name is extracted.
    # the extracted paragraph_code is added to the prompt and messages curated
    # the messages is passed to the mistral call with api-key and model name

    paragraph_code = extract_cobol_paragraph(file_path, function_name)

    if "not found" not in paragraph_code:
        messages = build_chat_prompt(paragraph_code) # curating messages here
        fixed_code = call_mistral_fix(api_key=api_key, model=model, messages=messages)
        print(fixed_code)
        return fixed_code
    else:
        print("Unable to process returning code: \n")
        print(paragraph_code)
        return paragraph_code
