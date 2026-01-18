def parse_line(line):
    parts = line.split()

    # Check for an empty line or a line with only a timestamp
    if not parts:
        return None, None, None, "--> empty line"

    time_stamp = parts[0]

    # Initialize variables to None
    usser = None
    eveent = None

    # Loop through all parts *after* the timestamp
    # This handles any order (USER:A EVENT:B or EVENT:B USER:A)
    # and ignores extra fields.
    for item in parts[1:]:
        try:
            # Split each part into a key and value
            key, value = item.split(":", 1)  # Use maxsplit=1

            if key == "USER":
                usser = value
            elif key == "EVENT":
                eveent = value
        except ValueError:
            # This catches items that don't have a ":"
            # (e.g., "USER" instead of "USER:Alice")
            # We can just ignore these malformed parts.
            pass

    # After checking all parts, determine the error message
    error_message = None
    if usser is None and eveent is None:
        error_message = "--> missing USER and EVENT fields"
    elif usser is None:
        error_message = "--> missing USER field"
    elif eveent is None:
        error_message = "--> missing EVENT field"

    return time_stamp, usser, eveent, error_message


def process_logfile(filename):
    active_sessions = {}
    sessions = {}
    invalid = []
    anomalies = []
    incomplete = []
    with open(f"../{filename}", "r") as f:
        for line in f:
            line = line . strip()
            if not line:
                continue
            ts, user, event, error = parse_line(line)
            if error:
                invalid.append((line, error))
                continue
            if event == "login":
                if (user, "login") in sessions.items():
                    anomalies.append((line, "-> double login"))
                else:
                    active_sessions[user] = "login"
                    sessions[user] = "login"
            elif event != "logout":
                if (user, "login") in active_sessions.items():
                    already_what_is_done = sessions[user]
                    new_what_is_done = already_what_is_done + f"--> {event}"
                    sessions[user] = new_what_is_done
                elif (user, "logout") in active_sessions.items():
                    anomalies.append(
                        (line, "-> performed action after logout and not logging in again"))
                else:
                    anomalies.append(
                        (line, "-> performed action before login"))
            else:
                if (user, "login") in active_sessions.items():
                    final_what_is_done = sessions[user]
                    final_again = final_what_is_done + "-> logout"
                    sessions[user] = final_again
                    active_sessions[user] = "logout"
                elif (user, "logout") in active_sessions.items():
                    anomalies.append(
                        (line, "duplicate logout (user already logged out)"))
                else:
                    anomalies.append((line, "logout without login"))
        for key, value in active_sessions.items():
            if value != "logout":
                again_final = sessions[key]
                again_final_final = again_final + "-> (incomplete session)"
                sessions[key] = again_final_final
                incomplete.append(f"{key} -> session never closed")
        with open("../sessions.txt", "w") as f:
            for key, value in sessions.items():
                f.write(f"{key}: {value}\n")
        with open("../anomalies.txt", "w") as f:
            for item in anomalies:
                f.write(f"{item}\n")
        with open("../invalid.txt", "w") as f:
            for item in invalid:
                f.write(f"{item}\n")
        with open("../incomplete.txt", "w") as f:
            for item in incomplete:
                f.write(f"{item}\n")
        with open(filename, "r") as f:
            lines_of_file = f.readlines()
    return f"Processed {len(lines_of_file)} lines:\n {len(lines_of_file)-len(invalid)-len(anomalies)} valid entries\n {len(invalid)+len(anomalies)} invalid or anomalous lines recorded\n\nSession Report Generated:\n - sessions.txt(reconstructed user sesisons)\n - anomalies.txt(logic errors)\n - invalid.txt(badly formatted lines)\n - incomplete.txt(unclosed sessions)"


print(process_logfile("trial input.txt"))
