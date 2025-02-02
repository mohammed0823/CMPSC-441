# Prompt Engineering Process

### Step 1
#### Intention
> Ensure the model is functioning properly without making any changes.

#### Action/Change
> Used the default settings from the demo and sent a simple "hello" message to confirm that the model was working.

#### Result
> The model responded as expected, and I exited the program.

#### Reflection/Analysis of the result. 
> I was fairly confident this would work, I just wanted to check fro any issues before making major changes.

---

### Step 2
#### Intention
> Adjust the model to properly handle a Dungeons and Dragons (DnD) scenario, since I have no prior experience with the game.

#### Action/Change
> Provided a highly specific prompt based on lab instructions to ensure the model set up the game correctly.  
> Adjusted the order of lines in the while loop so that the `\exit` command would work, requiring multiple test attempts.

#### Result
> The model functioned as expected based on the rubric.  
> The first game was engaging, with a creative and human-like storyline.  
> I played through 5 prompts before exiting.

#### Reflection/Analysis of the result. 
> I think this worked because I only adjusted the existing parameters to match the objective.

---

### Step 3
#### Intention
> Increase the model's creativity by adjusting the temperature setting.

#### Action/Change
> Increased the temperature from 0.5 to 0.8 to encourage more variation in responses.  
> Made only this single change to isolate its effect.

#### Result
> The model asked more questions before starting, providing additional customization options (e.g., setting, experience level).  
> It introduced more characters with unique backstories and started the adventure sooner.  
> The storyline was more detailed and dynamic.  
> Played through 5 prompts before exiting.

#### Reflection/Analysis of the result. 
> I think this worked because changing the temperature had the desired effect of increasing variation and creativity in the responses.

---

### Step 4
#### Intention
> Test whether the changes observed in the last iteration were directly due to the temperature adjustment.

#### Action/Change
> Lowered the temperature from 0.8 to 0.2 to see how it impacted the model’s behavior.

#### Result
> The model asked fewer questions and gave a more rigid, structured introduction.  
> The storyline, while still interesting, was less engaging and contained fewer characters.  
> The game felt less "magical" and had a more straightforward approach.  
> Noticed inconsistency in how response options were labeled throughout iterations (letters vs. numbers).  
> Played only 3 prompts before exiting due to preferring the previous iteration.

#### Reflection/Analysis of the result. 
> I went into this thinking it wouldn’t work in my favor, but I wanted to verify.
> It makes sense that it wouldn’t work, as a lower temperature corresponds to less variation and creativity.

---

### Step 5
#### Intention
> Encourage new ideas and branching storylines in the game.

#### Action/Change
> Reverted the temperature back to 0.8.  
> Introduced a new parameter, `presence_penalty`, set to 1.5 to promote new topics and segues.  

#### Result
> The introduction remained similar, but the AI's response structure changed.  
> The first turn allowed open-ended input rather than predefined choices, enhancing creative freedom.  
> A minor inconsistency was observed—an NPC’s brother suddenly became my brother in the next turn.  
> The change had a positive effect overall, creating the most engaging storyline so far.  
> Played through 5 prompts before exiting.

#### Reflection/Analysis of the result. 
> Aside from the identity shift, I believe this worked because the story became more engaging and allowed more creative freedom.

---

### Step 6
#### Intention
> Reduce repetition in responses, such as inventory lists and NPC stats.

#### Action/Change
> Added a `frequency_penalty` parameter set to 0.5 to discourage repeated words and phrases.

#### Result
> Improvements in reducing repetition, as that stopped being an issue from this point on.  
> Dice rolls occurred more frequently, though unsure if this was related to the change.  
> Responses were slightly shorter, but increasing `max_tokens` was avoided to prevent excessively long replies.  
> Overall, responses felt more natural and slightly faster.  
> Played through 5 prompts before exiting.

#### Reflection/Analysis of the result. 
> I would say it worked because the model is now faster and no longer repetitive.

---

### Step 7
#### Intention
> Test a different AI model to compare performance and response quality.

#### Action/Change
> Switched from `llama3.2 (3b)` to `llama3.1 (8b-instruct-q5_1)`, a larger model (6.1GB vs. 3GB) fine-tuned for instruction-following tasks.

#### Result
> The new model took noticeably longer to generate responses.  
> It allowed more customization at the start, such as choosing my character type and name.  
> Despite some improvements, the increased response time was not worth the trade-off.  
> Reverted back to `llama3.2 (3b)`.  
> Played through 5 prompts before exiting.

#### Reflection/Analysis of the result. 
> I think this didn’t work because the model was too large.
> I believe sticking with the lightweight model in llama3.2 (3b) is the right choice.