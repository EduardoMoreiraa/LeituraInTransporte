
# ** Geração do áudio (arquivo .mp3) **

class AudioSaver:
    def __init__(self, output_file):
        self.output_file = output_file

    def save_audio(self, audio_content):
        with open(self.output_file, "wb") as out:
            out.write(audio_content)
        print(f'Áudio gerado com sucesso: {self.output_file}')