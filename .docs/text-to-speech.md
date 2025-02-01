# Suno Bark Text-to-Speech Script

This Python script uses the Suno Bark model from 🤗HuggingFace to convert text input into audio files.

## Features

- Converts text to speech using the Suno Bark model
- Automatically sanitizes input text to create valid filenames
- Saves output as .wav files in the `output/text-to-speech/` directory

## Usage

1. Run the script from the root:

```bash
python tools/text-to-speech.py
```

2. Enter the text you want to convert when prompted

3. The audio file will be saved in the `output/text-to-speech/` directory

## File Structure

```text
.
├── tools/
│   └── suno-bark-tts.py    # Main script
└── output/
    └── suno-bark/          # Directory for audio output
```

## API Details

- Model: [suno/bark](https://huggingface.co/suno/bark)
- Endpoint: `https://api-inference.huggingface.co/models/suno/bark`
- Authorization: Bearer token required (`HF_TOKEN` in `.env`)

## Example

```bash
python tools/text-to-speech.py
```

## Terminal

#### Example Terminal output:

<img src = ".assets/text_to_speech_terminal.PNG" />

## Log File

#### Example log file entries:

```text
TIME:     1738361605
PROMPT:   Do me a favour son! You couldn't eat half a dog, let alone 7 of the b******s!
SAVED AS: output/text-to-speech/1738361605-Do_me_a_favour_son_You_couldnt_eat_half_a_dog_let_.wav

TIME:     1738361777
PROMPT:   I gave the Princess my last sock and now my foot is cold.
SAVED AS: output/text-to-speech/1738361777-I_gave_the_Princess_my_last_sock_and_now_my_foot_i.wav
```

## Script Notes

- Output files are saved as .wav format
- Filenames are automatically generated from input text:
  - Special characters are removed
  - Spaces are replaced with underscores
  - Length is limited to 50 characters
- Ensure the `output/text-to-speech/` directory exists before running the script
- The model is uncensored.

---

## Basic Text-to-Speech

To generate speech, simply provide the text you want the model to speak:

```plaintext
"I'll be perfectly honest, I could eat another six of those."
```

<audio controls src=".assets/1738362912-Ill_be_perfectly_honest_I_could_eat_another_six_of-converted.mp3"></audio>

---

## Changing the Speaker's Gender

To change the gender of the speaker, use the following syntax:

- **Male voice**: Add `[MALE]` before the text.
- **Female voice**: Add `[FEMALE]` before the text.

### Examples

```plaintext
[MALE] "This is possibly a male voice speaking."
[FEMALE] "This is possibly a female voice speaking."
```

<audio controls src=".assets/1738363175-MALE_This_is_possibly_a_male_voice_speaking-converted.mp3"></audio> <img src="../chuggingface_toolkit.png" width="40" alt="ChuggingFace"> <audio controls src=".assets/1738363507-FEMALE_This_is_possibly_a_female_voice_speaking-converted.mp3"></audio>
---

## Adding Effects

You can add effects like laughter, pauses, or emphasis by using special tags or symbols.

### Common Effects

1. **Laughter**: Use `[LAUGH]` or `[LAUGHTER]`.

   ```plaintext
   "That was actually pretty funny, Dave! [LAUGH]"
   ```

- <audio controls src=".assets/1738363638-That_was_actually_pretty_funny_Dave_LAUGH-converted.mp3"></audio>

2. **Pause**: Use `[PAUSE]` or `...` for a short pause.

   ```plaintext
   "Let me have a think... [PAUSE] Nope, I think I'd rather be trampled by bulls!"
   ```

- <audio controls src=".assets/1738363885-Let_me_have_a_think_PAUSE_Nope_I_think_Id_rather_b-converted.mp3"></audio>

3. **Whisper**: Use `[WHISPER]` for a whispered tone.

   ```plaintext
   "[WHISPER] This is a secret, so I suggest you go away."
   ```

- <audio controls src=".assets/1738363994-WHISPER_This_is_a_secret_so_I_suggest_you_go_away-converted.mp3"></audio>

4. **Shouting**: Use `[SHOUT]` for a louder, emphasized tone.

   ```plaintext
   "[SHOUT] Watch out! Frank's on the warpath with his crossbow. Frank's annoying."
   ```

- <audio controls src=".assets/1738364309-SHOUT_Watch_out_Franks_on_the_warpath_with_his_cro-converted.mp3"></audio>
- 😉 Turn your volume down a bit for this example.
---

## Adding Background Noise or Ambience

To include background noise or environmental sounds, use the following syntax:

- **Rain**: `[RAIN]`
- **Wind**: `[WIND]`
- **Crowd noise**: `[CROWD]`
- **Birds chirping**: `[BIRDS]`
- **Traffic noise**: `[TRAFFIC]`

### Background Noise Examples

```plaintext
"[RAIN] It's a rainy day, perfect for getting wet outside."
"[CROWD] The market is bustling with people, so I'm going home because people are mostly annoying."
```

<audio controls src=".assets/1738364555-RAIN_Its_a_rainy_day_perfect_for_getting_wet_outsi-converted.mp3"></audio> <img src="../chuggingface_toolkit.png" width="40" alt="ChuggingFace"> <audio controls src=".assets/1738364700-CROWD_The_market_is_bustling_with_people_so_Im_goi-converted.mp3"></audio>
---

## Combining Effects

You can combine multiple effects and background noises in a single prompt.

### Combined Effects Example

```plaintext
"[FEMALE] [RAIN] I love the sound of rain. [LAUGH] I can hear it with my ears!"
```
<audio controls src=".assets/1738367236-FEMALE_RAIN_I_love_the_sound_of_rain_LAUGH_I_can_h-converted.mp3"></audio>
---

## Advanced Usage

For more control over the output, you can experiment with:

- **Pitch modulation**: Use `[HIGH_PITCH]` or `[LOW_PITCH]`.
- **Speed**: Use `[SLOW]` or `[FAST]` to adjust the speaking rate.
- **Emotion**: Use `[HAPPY]`, `[SAD]`, or `[ANGRY]` to convey emotion.

### Advanced Example

```plaintext
"[MALE] [LOW_PITCH] [SLOW] This is a deep, slow voice. I reckon it could quite easily scare dogs."
"[FEMALE] [HIGH_PITCH] [HAPPY] I'm so excited! There's a load of new scared dogs at the shelter I can adopt!"
```
<audio controls src=".assets/1738366720-MALE_LOW_PITCH_SLOW_This_is_a_deep_slow_voice_I_re-converted.mp3"></audio> <img src="../chuggingface_toolkit.png" width="40" alt="ChuggingFace"> <audio controls src=".assets/1738367001-FEMALE_HIGH_PITCH_HAPPY_Im_so_excited_Theres_a_loa-converted.mp3"></audio> (!)
---

## Notes

- Always test your prompts to ensure the desired output.
- Combine effects sparingly to avoid unnatural results.
- Experiment with different tags and sequences for creative outputs.

---

<div align="center">

**ChuggingFace is very pleased...**

<img src=".assets/chuggingface_toolkit.png" width="512" alt="ChuggingFace">

---

**p9iaai** <img src=".assets/p9iaai.png" width="32" align="middle"> **2025**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

---

</div>
