import google.generativeai as genai
import json

def get_important_segments(transcript_chunks, user_prompt, api_key):
    """Identifies important segments from transcript chunks using the Gemini API."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    important_ids = []
    for chunk in transcript_chunks:
        prompt = f"""Based on the following video transcript and the user's prompt, identify the most important segments. Return a comma-separated list of their IDs.

User Prompt: {user_prompt}

Transcript Chunk:
{json.dumps(chunk, indent=2)}

Important Segment IDs:"""
        
        response = model.generate_content(prompt)
        try:
            cleaned_response = ''.join(filter(str.isdigit, response.text.replace(',', ' ')))
            ids = [int(id) for id in cleaned_response.split()]
            important_ids.extend(ids)
        except (ValueError, AttributeError):
            print(f"Could not parse response from Gemini API: {response.text}")

    return important_ids
