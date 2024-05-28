import subprocess

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv) sound name "Glass"
end run
'''

def notify(title: str, text: str):
    """
    Send a notification to the macOS system.
    """
    subprocess.call(['osascript', '-e', CMD, title, text])
