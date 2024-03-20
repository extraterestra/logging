import datetime
from log_levels import LogLevel

def log_message(log_file: str, message: str, log_level: LogLevel) -> None:
    """
    Function writing in log file logging events:
    :param log_file: Name of the log file, e.g. application.log
    :param message: Message string describing event
    :param log_level: Log level name, one of the enum LogLevel values:
    DEBUG, INFO, WARNING, ERROR, CRITICAL
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if isinstance(log_level, LogLevel):
        log_entry = f"[{timestamp}] [{log_level.name}] {message}\n"
    else:
        error_message = f"not existent log level {log_level}"
        log_entry = f"[{timestamp}] [{LogLevel.ERROR}] {error_message} {message}\n"

    with open(log_file, "a") as f:
        f.write(log_entry)

# Example usage
log_message("application.log", "User logged in", LogLevel.INFO)
log_message("application.log", "Bla bla", "INVALID")
log_message("application.log", "Empty error level", "")
log_message("server.log", "500 Internal server error", LogLevel.ERROR)
log_message("server.log", "403 Forbidden", LogLevel.ERROR)
log_message("server.log", "", LogLevel.ERROR)