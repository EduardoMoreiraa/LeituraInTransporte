from google.cloud import texttospeech
from model import PDFData
from controller import TextToSpeechConverter
from view import AudioSaver
    # Importação 

    # Chamada do main
if __name__ == "__main__":

    # Configurações
    pdf_file_path = "leitura.pdf"
    output_audio_file = "audio.mp3"
    language_code = "pt-BR"
    voice_name = "pt-BR-Wavenet-A"

    # Inicialização
    pdf_data = PDFData(pdf_file_path)
    client = texttospeech.TextToSpeechClient() # Credenciais Google Cloud 
    voice_config = texttospeech.VoiceSelectionParams(language_code=language_code, name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    converter = TextToSpeechConverter(client, voice_config, audio_config)
    saver = AudioSaver(output_audio_file)

    # Conversão
    audio_content = converter.convert_to_speech(pdf_data.text)

    # Salvamento
    saver.save_audio(audio_content)