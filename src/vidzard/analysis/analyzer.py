import google.generativeai as genai
import json
import time
from google.api_core import exceptions

def get_important_segments(transcript_chunks, user_prompt, api_key):
    """Identifies important segments from transcript chunks using the Gemini API."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    important_ids = []
    important_ids_txt = []
    for i, chunk in enumerate(transcript_chunks):
        prompt = f"""Based on the following video transcript and the user's prompt, identify the most important segments. Return a comma-separated list of their IDs.

User Prompt: {user_prompt}

Transcript Chunk:
{json.dumps(chunk, indent=2)}

Important Segment IDs:"""
        
        while True:
            try:
                response = model.generate_content(prompt)
                break
            except exceptions.ResourceExhausted:
                print("Rate limit exceeded. Waiting for 60 seconds before retrying...")
                time.sleep(60)

        try:
            print("Process i", i)
            important_ids_txt.append(response.text)
            ids = [int(id) for id in response.text.split(",")]
            important_ids.extend(ids)
            print(important_ids)
        except (ValueError, AttributeError):
            print(f"Could not parse response from Gemini API: {response.text}")
            continue
    
    # save the important ids text to a file
    with open('important_ids.txt', 'w') as f:
        for txt in important_ids_txt:
            f.write(txt + '\n')
    return important_ids
