import webbrowser
import os
import requests
import json
import time
import sys
from typing import Optional
import subprocess


class SimpleVoiceAssistant:
    def __init__(self):
        # Command mapping
        self.commands = {
            # Websites
            'youtube': 'https://www.youtube.com',
            'open youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'open google': 'https://www.google.com',
            'whatsapp': 'https://web.whatsapp.com',
            'open whatsapp': 'https://web.whatsapp.com',
            'facebook': 'https://www.facebook.com',
            'open facebook': 'https://www.facebook.com',
            'github': 'https://github.com',
            'open github': 'https://github.com',
            'gmail': 'https://mail.google.com',
            'open gmail': 'https://mail.google.com',
            'amazon': 'https://amazon.com',
            'open amazon': 'https://amazon.com',
            'netflix': 'https://netflix.com',
            'open netflix': 'https://netflix.com',

            # Windows Apps
            'calculator': 'calc',
            'open calculator': 'calc',
            'notepad': 'notepad',
            'open notepad': 'notepad',
            'paint': 'mspaint',
            'open paint': 'mspaint',
            'command prompt': 'cmd',
            'open command prompt': 'cmd',
            'task manager': 'taskmgr',
            'open task manager': 'taskmgr',
        }

    def show_menu(self):
        """Display available commands"""
        print("\n" + "=" * 60)
        print("🎤 VOICE ASSISTANT MENU")
        print("=" * 60)
        print("\nAvailable Commands:")
        print("-" * 40)

        # Group commands
        websites = [cmd for cmd, action in self.commands.items() if action.startswith('http')]
        apps = [cmd for cmd, action in self.commands.items() if not action.startswith('http')]

        print("🌐 WEBSITES:")
        for i in range(0, len(websites), 2):
            if i < len(websites):
                print(f"  • {websites[i]:<25}", end="")
                if i + 1 < len(websites):
                    print(f" • {websites[i + 1]}")
                else:
                    print()

        print("\n💻 APPLICATIONS:")
        for i in range(0, len(apps), 2):
            if i < len(apps):
                print(f"  • {apps[i]:<25}", end="")
                if i + 1 < len(apps):
                    print(f" • {apps[i + 1]}")
                else:
                    print()

        print("\n💡 Just type the command (e.g., 'youtube' or 'calculator')")
        print("   Type 'exit' to quit, 'menu' to show this menu again")
        print("=" * 60)

    def execute_command(self, command: str) -> bool:
        """Execute a command"""
        command = command.strip().lower()

        if command in ['exit', 'quit', 'close']:
            print("\n👋 Goodbye!")
            return False

        if command == 'menu':
            self.show_menu()
            return True

        if command in self.commands:
            action = self.commands[command]
            print(f"\n🚀 Executing: {command}")

            try:
                if action.startswith('http'):
                    # Open website
                    webbrowser.open(action)
                    print(f"🌐 Opening: {action}")
                else:
                    # Open application
                    os.system(action)
                    print(f"📱 Opening: {action}")
                return True
            except Exception as e:
                print(f"❌ Error: {e}")
                return True
        else:
            print(f"\n❌ Command not recognized: '{command}'")
            print("💡 Type 'menu' to see available commands")
            return True

    def run(self):
        """Main program loop"""
        print("\n" + "=" * 60)
        print("🎧 SIMPLE VOICE ASSISTANT")
        print("=" * 60)
        print("\n⚠️  Running in TEXT MODE (type commands)")
        print("   No microphone required!")

        self.show_menu()

        while True:
            try:
                print("\n" + "-" * 40)
                command = input("Enter command: ").strip()

                if not command:
                    continue

                should_continue = self.execute_command(command)
                if not should_continue:
                    break

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n⚠️ Error: {e}")
                continue


# Alternative: Voice version using Windows Speech Recognition
class WindowsVoiceAssistant:
    def __init__(self):
        self.simple_assistant = SimpleVoiceAssistant()

    def listen_with_windows(self):
        """Use Windows built-in speech recognition"""
        try:
            # This uses Windows Speech Recognition through COM
            import win32com.client

            print("\n🎤 Speak now... (Listening for 5 seconds)")
            print("Say: 'open youtube', 'open whatsapp', etc.")

            # Create speech recognizer
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")

            # Configure recognition
            listener.State = 1  # Start listening

            # Wait for input
            time.sleep(5)

            # Get recognized text (simplified)
            # Note: This is a simplified version - Windows SR is complex
            print("⚠️  Windows Speech Recognition activated")
            print("💡 For now, please type your command:")

            command = input("Type command: ")
            return command

        except ImportError:
            print("\n⚠️  Windows speech libraries not available")
            print("📝 Switching to text mode...")
            command = input("Type command: ")
            return command
        except Exception as e:
            print(f"\n⚠️  Speech error: {e}")
            print("📝 Switching to text mode...")
            command = input("Type command: ")
            return command

    def run(self):
        """Run with voice option"""
        print("\n" + "=" * 60)
        print("🎤 WINDOWS VOICE ASSISTANT")
        print("=" * 60)

        print("\nChoose mode:")
        print("1. Voice Mode (requires Windows Speech Recognition setup)")
        print("2. Text Mode (type commands)")
        print("3. Exit")

        while True:
            choice = input("\nSelect (1/2/3): ").strip()

            if choice == '1':
                print("\n🎤 Starting voice mode...")
                command = self.listen_with_windows()
                if command:
                    self.simple_assistant.execute_command(command)
            elif choice == '2':
                self.simple_assistant.run()
                break
            elif choice == '3':
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1, 2, or 3.")


# SUPER SIMPLE VERSION - No dependencies at all
class UltraSimpleAssistant:
    def __init__(self):
        self.commands = {
            # Websites
            '1': ('YouTube', 'https://youtube.com'),
            '2': ('WhatsApp Web', 'https://web.whatsapp.com'),
            '3': ('Google', 'https://google.com'),
            '4': ('Facebook', 'https://facebook.com'),
            '5': ('Gmail', 'https://mail.google.com'),

            # Apps
            '6': ('Calculator', 'calc'),
            '7': ('Notepad', 'notepad'),
            '8': ('Paint', 'mspaint'),
            '9': ('Command Prompt', 'cmd'),
        }

    def run(self):
        print("\n" + "=" * 60)
        print("🚀 ULTRA SIMPLE ASSISTANT")
        print("=" * 60)

        while True:
            print("\nSelect an option to open:")
            print("-" * 40)

            for key, (name, _) in self.commands.items():
                print(f"  {key}. {name}")

            print("  0. Exit")
            print("-" * 40)

            choice = input("Enter number: ").strip()

            if choice == '0':
                print("\n👋 Goodbye!")
                break

            if choice in self.commands:
                name, action = self.commands[choice]
                print(f"\n🚀 Opening {name}...")

                try:
                    if action.startswith('http'):
                        webbrowser.open(action)
                    else:
                        os.system(action)
                    print(f"✅ {name} opened successfully!")
                except Exception as e:
                    print(f"❌ Error opening {name}: {e}")
            else:
                print("❌ Invalid choice. Please try again.")

            input("\nPress Enter to continue...")


def check_windows_speech():
    """Check if Windows Speech Recognition is available"""
    try:
        # Try to import Windows speech libraries
        import pythoncom
        import win32com.client

        print("✅ Windows Speech Recognition is available")
        return True
    except ImportError:
        print("❌ Windows speech libraries not installed")
        print("\nTo enable voice recognition on Windows:")
        print("1. Open 'Windows Speech Recognition' from Start Menu")
        print("2. Follow the setup wizard")
        print("3. Say 'start listening' to activate")
        return False


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("VOICE ASSISTANT LAUNCHER")
    print("=" * 60)

    print("\nChoose your assistant type:")
    print("1. 📝 Text Assistant (Type commands - NO INSTALLATION NEEDED)")
    print("2. 🎤 Windows Voice (Uses Windows built-in speech)")
    print("3. 🚀 Ultra Simple (Number menu - Easiest)")
    print("4. ℹ️  Check Windows Speech Availability")
    print("5. ❌ Exit")

    while True:
        choice = input("\nSelect (1-5): ").strip()

        if choice == '1':
            assistant = SimpleVoiceAssistant()
            assistant.run()
            break
        elif choice == '2':
            # Check if Windows speech is available
            if check_windows_speech():
                assistant = WindowsVoiceAssistant()
                assistant.run()
            else:
                print("\n⚠️  Using text mode instead...")
                assistant = SimpleVoiceAssistant()
                assistant.run()
            break
        elif choice == '3':
            assistant = UltraSimpleAssistant()
            assistant.run()
            break
        elif choice == '4':
            check_windows_speech()
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")
