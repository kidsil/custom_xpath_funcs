# Custom XPath Functions for lxml

This repository contains a Python script (`main.py`) that utilizes custom XPath functions defined in `helper.py`. These functions extend the capability of XPath expressions within the `lxml` library, allowing for custom string manipulations directly within XPath queries.

## Overview

`main.py` imports custom functions from `helper.py` and registers them within the `lxml` namespace for XPath. The script demonstrates how to use these custom functions by applying them to an example HTML string.

### `main.py`

- Imports helper functions.
- Registers custom XPath functions to the default namespace.
- Parses an example HTML string and applies custom XPath functions to extract and manipulate data.

### `helper.py`

- Contains the definitions of custom XPath functions that can be used within `lxml` XPath queries.
- `xpath_func_tokenize`: Splits a string based on a given delimiter.
- `xpath_func_make_title`: Converts a string to title case.

## Installation

Before running the script, ensure you have Python installed on your system and install the required dependencies:

```bash
pip install lxml
```

## Usage

To use the custom XPath functions in your project:

1. Import the `helper` module in your Python script.
2. Register the custom functions with the `etree.FunctionNamespace` as shown in `main.py`.
3. Use the registered functions in your XPath expressions.

### Running the Example

Execute `main.py` to see the custom XPath functions in action:

```bash
python main.py
```

This will output the results of the custom XPath functions applied to the `example_html` string.

## Custom Function Details

### `xpath_func_tokenize`

This function takes two arguments:
- `string`: The string to be tokenized.
- `split_token`: The delimiter to split the string by.

Example usage in XPath:

```xpath
tokenize(//p[@class="tokenize_me"]/text(),";")
```

### `xpath_func_make_title`

This function takes one argument:
- `string`: The string to convert to title case.

Example usage in XPath:

```xpath
make_title(//p[@class="title_me"]/text())
```

## Contributing

The main idea behind this little library, is to allow for more custom XPath functions.

Feel free to contribute custom XPath functions by following these steps:
1. Define a new function in `helper.py` with the prefix `xpath_func_`.
2. Ensure it takes `context` as the first argument, followed by any number of additional arguments.
3. Add the function to the namespace registration in `main.py`.
4. (optional) Create a PR.
