import openlit

response = openlit.get_prompt(
    name="test",  # Fetch the prompt by name
    should_compile=True,  # Compile the prompt with provided variables
    variables={
        "name": "John",  # Pass variables for prompt compilation
    }
)

print("get_prompt",response)  # Print or process the fetched and compiled prompt


import openlit

response = openlit.get_secrets(
  should_set_env=True
)

print("get_secrets", response)

