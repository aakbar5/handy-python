""" Watch a folder to detect change in files """

import os
import threading
import time

class WatchThread(threading.Thread):
    def __init__(self,
                 folder_to_watch,
                 file_exts=[],
                 watch_delay_seconds=0.500,
                 callback_files_added=None,
                 callback_files_removed=None):
        """ Thread to watch a folder
            - folder_to_watch: Path to the folder to watch.
            - file_exts: List of the file extensions to watch for.
            - watch_delay_seconds: Delay (Seconds) to detect changes in files.
            - callback_files_added: Callback to be called on having new files.
            - callback_files_removed: Callback to be called on having removed files.
        """

        self._folder = folder_to_watch
        self._file_exts = file_exts
        self._delay = watch_delay_seconds
        self._callback_files_added = callback_files_added
        self._callback_files_removed = callback_files_removed
        self._stop_event = threading.Event()
        threading.Thread.__init__(self)

    def scan_folder(self, folder):
        found_files = []

        if not os.path.exists(folder):
            return found_files

        with os.scandir(folder) as iterator:
            for entry in iterator:
                if entry.is_file() and self._file_exts is None or len(self._file_exts) == 0:
                    found_files.append(entry.path)

                elif entry.is_file() and entry.is_file() and os.path.splitext(entry.path)[1] in self._file_exts:
                    found_files.append(entry.path)

        return found_files

    def run(self):
        print("Start folder watcher...")

        if os.path.exists(self._folder) and os.path.isdir(self._folder):

            before = self.scan_folder(self._folder)

            while not self._stop_event.isSet():
                # Scan folder again
                after = self.scan_folder(self._folder)

                # Separate out files
                added = [f for f in after if not f in before]
                removed = [f for f in before if not f in after]

                if added and self._callback_files_added:
                    self._callback_files_added(added)

                if removed and self._callback_files_removed:
                    self._callback_files_removed(removed)

                before = after
                self._stop_event.wait(self._delay)

        print("Folder watcher is stopped")

    def stop(self):
        self._stop_event.set()

def _added(files):
    print("")
    print("\033[92m {}\033[00m" .format("**** Files are added ****"))
    for x in files:
        print(x)

def _removed(files):
    print("")
    print("\033[91m {}\033[00m" .format("**** Files are removed ****"))
    for x in files:
        print(x)

# Start folder watcher
print("--- watch a folder for all files ---")
folder_to_watch = '/path/to/folder/to/watch'
thread = WatchThread(folder_to_watch=folder_to_watch, callback_files_added=_added, callback_files_removed=_removed)
thread.start()
if thread.is_alive():
    time.sleep(0.5 * 60)

thread.stop()
thread.join()
print("Done")

# Start folder watcher
print("--- watch a folder for specific files ---")
folder_to_watch = '/path/to/folder/to/watch'
thread = WatchThread(folder_to_watch=folder_to_watch, file_exts=['.yml'], callback_files_added=_added, callback_files_removed=_removed)
thread.start()
if thread.is_alive():
    time.sleep(1 * 60)
thread.stop()
thread.join()
print("Done")
