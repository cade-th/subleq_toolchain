import pprint

errors = []

def error_log(test_name, expected, received, string):
    # pprint.pformat handles any nested python structures beautifully
    expected_formatted = pprint.pformat(expected, width=60)
    received_formatted = pprint.pformat(received, width=60)

    # Indent every line of the formatted output to align with the tab structure of the log
    expected_indented = expected_formatted.replace("\n", "\n\t\t\t")
    received_indented = received_formatted.replace("\n", "\n\t\t\t")

    error_line_1 = f"\tIncorrect {string} in {test_name}:\n"
    error_line_2 = f"\t\tExpected {string}:\n\t\t\t{expected_indented}\n"
    error_line_3 = f"\t\tReceived {string}:\n\t\t\t{received_indented}\n"

    error = error_line_1 + error_line_2 + error_line_3
    errors.append(error)

