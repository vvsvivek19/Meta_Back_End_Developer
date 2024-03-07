import importlib
import fileChanges

def changes():
    try:
        importlib.reload(fileChanges)
        fileChanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit Enter to Reload...")
