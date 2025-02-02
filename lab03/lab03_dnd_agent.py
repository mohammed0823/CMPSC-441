from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Mohammmed Albattah'
model = 'llama3.2'
options = {'temperature': 0.8, 'max_tokens': 100, 'presence_penalty': 1.5, 'frequency_penalty': 0.5}
messages = [
  {'role': 'system', 'content': 'You are a Dungeons and Dragons Dungeon Master and do everything \
                                That a Dungeons and Dragons Dungeon Master must do. This includes \
                                generating a random story, creating NPC characters, managing the game world \
                                making changes to player character sheets, Implementing a turn-based combat system \
                                and more.'},
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  response = chat(model=model, messages=messages, stream=False, options=options)

  if messages[-1]['content'] == '/exit':
    break

  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

