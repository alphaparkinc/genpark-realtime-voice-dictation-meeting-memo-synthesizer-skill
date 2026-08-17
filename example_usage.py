from client import RealtimeVoiceDictationMeetingMemoSynthesizerClient

def main():
    client = RealtimeVoiceDictationMeetingMemoSynthesizerClient()
    res = client.synthesize_memo("audio_stream_chunk_902.wav", ["Chris", "Alex"])
    print(f"Latency: {res['latency_ms']}ms")
    print(f"Action Items: {res['action_items_count']}")
    print("\nFormatted Memo:")
    print(res["formatted_markdown_memo"])

if __name__ == "__main__":
    main()
