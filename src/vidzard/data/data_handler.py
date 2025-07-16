import json

from sympy import im

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

def process_important_ids():
    """Processes important IDs from a JSON file."""
    important_ids = load_json('important_ids.json')
    important_ids = [int(id) for id in important_ids]

    transcript = load_json('transcript.json')


    i = 0
    important_ids_adj_all = []
    while i < len(important_ids):
        important_ids_adj = []
        important_ids_adj.append(important_ids[i])
        while True and i + 1 < len(important_ids):
            if important_ids[i] == important_ids[i + 1] - 1:
                important_ids_adj.append(important_ids[i + 1])
                i += 1
            else:
                break
        important_ids_adj_all.append(important_ids_adj)
        i += 1
    
    videos_time_cut = []
    for entry in important_ids_adj_all:
        video_time_cut = {}
        
        first_segment = next((seg for seg in transcript if seg['id'] == entry[0]), None)
        last_segment = next((seg for seg in transcript if seg['id'] == entry[-1]), None)
        if first_segment and last_segment:
            video_time_cut['start'] = first_segment['start']
            video_time_cut['end'] = last_segment['end']
            videos_time_cut.append(video_time_cut)

    # Save the video time cuts to a JSON file
    save_json(videos_time_cut, 'videos_time_cut.json')


    
# process_important_ids()


