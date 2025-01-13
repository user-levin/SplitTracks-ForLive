import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from pydub import AudioSegment
from tqdm import tqdm  # Fortschrittsanzeige

# Farben für die Konsole
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# Funktion: Audio-Dateien splitten
def split_audio(file_path, output_folder, max_file_size_mb=2000):
    """Split a large FLAC or WAV file into smaller chunks based on max file size."""
    try:
        print(f"{Colors.OKBLUE}Processing file: {file_path}{Colors.ENDC}")

        # Lade die Audio-Datei (FLAC oder WAV)
        audio_format = "wav" if file_path.lower().endswith(".wav") else "flac"
        audio = AudioSegment.from_file(file_path, format=audio_format)
        total_duration = len(audio)  # Dauer in Millisekunden

        # Approximate Größe von einer Millisekunde Audio in Bytes
        file_size_per_ms = len(audio.raw_data) / total_duration

        # Maximale Dauer basierend auf der Dateigrößenbeschränkung (in Millisekunden)
        max_duration = int((max_file_size_mb * 1024 * 1024) / file_size_per_ms)

        # Anzahl der Teile berechnen
        num_parts = total_duration // max_duration + (1 if total_duration % max_duration else 0)

        # Ausgabeverzeichnis erstellen, falls es nicht existiert
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        base_name = os.path.splitext(os.path.basename(file_path))[0]

        # Fortschrittsanzeige mit tqdm
        with tqdm(total=num_parts, desc=f"Splitting {base_name}", ncols=80, colour="green") as pbar:
            for i in range(num_parts):
                start_time = i * max_duration
                end_time = min((i + 1) * max_duration, total_duration)

                # Teile extrahieren
                part = audio[start_time:end_time]
                output_file_name = f"{base_name} Cut {i + 1}.{audio_format}"
                output_file_path = os.path.join(output_folder, output_file_name)

                # Exportieren
                part.export(output_file_path, format=audio_format)
                pbar.update(1)
                print(f"{Colors.OKGREEN}Exported: {output_file_path}{Colors.ENDC}")

    except Exception as e:
        print(f"{Colors.FAIL}Error processing file {file_path}: {e}{Colors.ENDC}")

# Funktion: Ordner mit Dateien verarbeiten
def process_directory(input_path, output_folder, max_file_size_mb=2000):
    """Process all FLAC and WAV files in a directory."""
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith((".flac", ".wav")):
                file_path = os.path.join(root, file)
                split_audio(file_path, output_folder, max_file_size_mb)

# Funktion: Datei oder Ordner automatisch auswählen
def select_file_or_folder():
    """Prompt user to select a file or folder."""
    try:
        root = Tk()
        root.withdraw()  # Hauptfenster ausblenden
        root.call('wm', 'attributes', '.', '-topmost', True)  # Dialog in den Vordergrund bringen
        root.update_idletasks()  # Tkinter GUI aktualisieren

        print(f"{Colors.OKCYAN}Select a file or folder (audio file or directory)...{Colors.ENDC}")
        path = askopenfilename(filetypes=[("Audio Files", "*.flac *.wav")], title="Select a File or Folder")

        if not path:  # Wenn keine Datei ausgewählt wurde, nach Ordner fragen
            path = askdirectory(title="Select a Directory")

        root.destroy()

        if path:
            return path
        else:
            print(f"{Colors.FAIL}No file or folder selected. Exiting.{Colors.ENDC}")
            return None
    except Exception as e:
        print(f"{Colors.FAIL}Error initializing file dialog: {e}{Colors.ENDC}")
        return None

# Hauptfunktion
def main():
    print(f"{Colors.HEADER}Welcome to the FLAC/WAV Splitter!{Colors.ENDC}")

    # Datei oder Ordner auswählen
    input_path = select_file_or_folder()
    if not input_path:
        return

    print(f"{Colors.OKCYAN}Selected path: {input_path}{Colors.ENDC}")

    # Ausgabeverzeichnis festlegen
    output_folder = os.path.join(os.path.dirname(input_path) if os.path.isfile(input_path) else input_path, "Cut")
    print(f"{Colors.OKCYAN}Output folder: {output_folder}{Colors.ENDC}")

    # Verarbeitung starten
    if os.path.isfile(input_path):
        split_audio(input_path, output_folder, max_file_size_mb=2000)
    elif os.path.isdir(input_path):
        process_directory(input_path, output_folder, max_file_size_mb=2000)
    else:
        print(f"{Colors.FAIL}Invalid selection. Please select a valid file or folder.{Colors.ENDC}")

    print(f"{Colors.OKGREEN}All tasks completed successfully!{Colors.ENDC}")

if __name__ == "__main__":
    main()
