import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class CustomLoggingEventHandler(LoggingEventHandler):
    def __init__(self, logger=None):
        super().__init__()
    def on_created(self, event):
        super().on_created(event)
        if not event.is_directory:
            if "jpg" in event.src_path:
                print("img created")

    def on_deleted(self, event):
        super().on_deleted(event)


    def on_modified(self, event):
        super().on_modified(event)


def monitor_folder(folder_path):
    path = folder_path
    event_handler = CustomLoggingEventHandler()
    observer = Observer()
    for p in path:
        observer.schedule(event_handler, p, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    monitor_folder(["C:\\Users\\huluh\\Downloads\\", "C:\\Users\\huluh\\Desktop"])