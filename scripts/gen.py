def request_images(
    api_key: str,
    prompt: str,
    model: str = "google/gemini-3.1-flash-image-preview",
) -> dict:
    """Generate an image via OpenRouter API. Tries image modality first, falls back to standard API."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    # First try with image modality
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "modalities": ["image"],
    }
    
    try:
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            method="POST",
            headers=headers,
            data=body,
        )
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # If 404 or unsupported modality, fall back to standard API
        if e.code == 404:
            # Retry without modalities parameter
            payload = {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            }
            body = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                url,
                method="POST",
                headers=headers,
                data=body,
            )
            try:
                with urllib.request.urlopen(req, timeout=300) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e2:
                payload = e2.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"OpenRouter API failed ({e2.code}): {payload}") from e2
        else:
            # Some other error (429 rate limit, etc.)
            payload = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenRouter API failed ({e.code}): {payload}") from e
