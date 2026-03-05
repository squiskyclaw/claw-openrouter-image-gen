name: openrouter-image-gen
description: Batch-generate images via OpenRouter API or local LiteLLM. Supports chat completions and images/generations API methods.
homepage: https://openrouter.ai/docs/guides/overview/multimodal/image-generation
metadata:
  {
    "openclaw": {
      "emoji": "🖼️",
      "requires": { "bins": ["python3"], "env": ["OPENROUTER_API_KEY", "OPENROUTER_BASE_URL"] },
      "primaryEnv": "OPENROUTER_API_KEY",
      "optionalEnv": ["OPENROUTER_BASE_URL"],
      "install": [
        {
          "id": "python-brew",
          "kind": "brew",
          "formula": "python",
          "bins": ["python3"],
          "label": "Install Python (brew)",
        }
      ],
    }
  }

# OpenRouter Image Gen

Generate images via OpenRouter's API or local LiteLLM deployment.

## Run

```bash
python3 {baseDir}/scripts/gen.py
open ~/Projects/tmp/claw-openrouter-image-gen-*/index.html  # if ~/Projects/tmp exists; else ./tmp/...
```

## API Methods

### Method 1: Chat Completions (default)
Uses `/v1/chat/completions` with `modalities` parameter. Best for OpenRouter.

```bash
python3 {baseDir}/scripts/gen.py --api-method chat --model google/gemini-3.1-flash-image-preview
```

### Method 2: Images Generations
Uses `/v1/images/generations` endpoint. Best for local LiteLLM with Flux or similar models.

```bash
python3 {baseDir}/scripts/gen.py --api-method images --model flux-9b --image-size 1024x1024
```

## Useful Flags

```bash
# Generate multiple images with random prompts
python3 {baseDir}/scripts/gen.py --count 16

# Single prompt
python3 {baseDir}/scripts/gen.py --prompt "ultra-detailed studio photo of a lobster astronaut" --count 4

# Custom output directory
python3 {baseDir}/scripts/gen.py --out-dir ./out/images

# Use images/generations API (for local Flux deployment)
python3 {baseDir}/scripts/gen.py --api-method images --model flux-9b --prompt "a cute cartoon penguin"

# Different image sizes (images API only)
python3 {baseDir}/scripts/gen.py --api-method images --model flux-9b --image-size 1792x1024 --prompt "landscape image"
```

## Supported Models

### Chat Completions (default):
- `google/gemini-3.1-flash-image-preview` (default, fastest)
- `sourceful/riverflow-v2-pro`
- `sourceful/riverflow-v2-fast`
- `black-forest-labs/flux.2-klein-4b`
- `black-forest-labs/flux.2-max`
- `black-forest-labs/flux.2-pro`
- `black-forest-labs/flux.2-flex`
- `bytedance-seed/seedream-4.5`
- `openai/gpt-5-image`

### Images Generations:
- Any model deployed behind LiteLLM that supports `/v1/images/generations`
- `flux-9b` (local)
- `gpt-image-1` (OpenAI via OpenRouter)
- `dall-e-3` (OpenAI via OpenRouter)

## Output

- `*.png` images
- `prompts.json` (prompt → file mapping)
- `index.html` (thumbnail gallery)

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENROUTER_API_KEY` | Yes | - | Your OpenRouter API key (or dummy for local) |
| `OPENROUTER_BASE_URL` | No | `https://openrouter.ai/api/v1` | Base URL for API (scheme://host:port/path) |

### Using a Local Endpoint

To use a local LiteLLM instance instead of OpenRouter:

```bash
# For chat completions API
export OPENROUTER_API_KEY="sk-dummy"  # LiteLLM doesn't need real key for local
export OPENROUTER_BASE_URL="http://your-lite-llm-host:4000"
python3 {baseDir}/scripts/gen.py --api-method chat --model flux-9b --prompt "your prompt"

# For images/generations API (recommended for Flux)
export OPENROUTER_API_KEY="sk-dummy"
export OPENROUTER_BASE_URL="http://your-lite-llm-host:4000"
python3 {baseDir}/scripts/gen.py --api-method images --model flux-9b --prompt "cute cartoon penguin"
```

## API Reference

- [OpenRouter Image Generation Docs](https://openrouter.ai/docs/guides/overview/multimodal/image-generation)
- [OpenAI Images Generations API](https://platform.openai.com/docs/api-reference/images/generate)
