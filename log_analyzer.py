import logging,re
logging.basicConfig(
    filename="analyzer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def read_log_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Log file is empty")
            logging.info("Log file read successfully")
            return lines
    except FileNotFoundError:
        logging.error("File not found")
        print("Error: app.log file not found")
        return None
    except ValueError as e:
        logging.error(str(e))
        print("Error:", e)
        return None
def process_logs(lines):
    info_count = 0
    warning_count = 0
    error_count = 0
    error_messages = []

    log_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|WARNING|ERROR) .+"

    for line in lines:
        line = line.strip()
        if not line:
            logging.error("Empty line detected")
            continue
        if not re.match(log_pattern, line):
            logging.error(f"Incorrect log format: {line}")
            print("Incorrect format detected:", line)
            continue

        parts = line.split(" ", 3)
        log_type = parts[2]

        if log_type == "INFO":
            info_count += 1
        elif log_type == "WARNING":
            warning_count += 1
        elif log_type == "ERROR":
            error_count += 1
            error_messages.append(line)

    logging.info("Log processing completed")

    return info_count, warning_count, error_count, error_messages
def generate_report(info, warning, error, errors_list):
    try:
        with open("report.txt", "w") as report:
            report.write("Log Summary\n")
            report.write("-----------\n")
            report.write(f"INFO count: {info}\n")
            report.write(f"WARNING count: {warning}\n")
            report.write(f"ERROR count: {error}\n\n")
            report.write("Error Details:\n")
            report.write("--------------\n")
            for err in errors_list:
                report.write(err + "\n")
        logging.info("Report generated successfully")
    except Exception as e:
        logging.error(f"Report generation failed: {e}")
def main():
    filename = "app.log"
    lines = read_log_file(filename)
    if lines:
        info, warning, error, errors_list = process_logs(lines)
        generate_report(info, warning, error, errors_list)
if __name__ == "__main__":
    main()