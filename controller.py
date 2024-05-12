from google.cloud import texttospeech

# ** Conversão do texto para voz ** 

class TextToSpeechConverter:
    def __init__(self, client, voice_config, audio_config):
        self.client = client
        self.voice_config = voice_config
        self.audio_config = audio_config

    def convert_to_speech(self, text):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice_config, audio_config=self.audio_config
        )
        return response.audio_content