def line_count():
    # Opens the file.
    file = open('file.txt', 'r')
    # Lists all of the lines.
    lines = file.readlines()
    # Counts the amount of lines.
    line_count1 = len(lines)
    file.close()
    return line_count1