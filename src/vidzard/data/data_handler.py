import json

def load_json(file_path):
    """Loads a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    """Saves data to a JSON file."""
    try:
        for tr in data:
            # Delete seek and tokens
            del tr['seek']
            del tr['tokens']
            del tr['avg_logprob']
            del tr['temperature']
            del tr['compression_ratio']
            del tr['no_speech_prob']
    except Exception as e:
        pass
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)



