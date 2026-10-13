from outetts.v0_1.interface import InterfaceHF, InterfaceGGUF

# Initialize the interface with the Hugging Face model
interface = InterfaceHF("OuteAI/OuteTTS-0.1-350M")

# Or initialize the interface with a GGUF model
# interface = InterfaceGGUF("path/to/model.gguf")

# Generate TTS output
# Without a speaker reference, the model generates speech with random speaker characteristics
output = interface.generate(
    text="Hello, am I working?",
    temperature=0.1,
    repetition_penalty=1.1,
    max_length=4096
)

# Play the generated audio
output.play()

# Save the generated audio to a file
output.save("output.wav")
