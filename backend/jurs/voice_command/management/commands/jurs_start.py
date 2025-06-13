from django.core.management.base import BaseCommand
from assistant.jurs_engine import speak, listen, process_command

class Command(BaseCommand):
    help = "Run the JURS voice assistant"

    def handle(self, *args, **options):
        speak("Initializing JURS...")
        while True:
            command = listen()
            if command and "jurs" in command:
                speak("Yes?")
                command = listen()
                if command:
                    process_command(command)
            else:
                print("Waiting for wake word...")
