{
  "openclaw": {
    "emoji": "🖼️",
    "requires": { "bins": ["python3"], "env": ["OPENROUTER_API_KEY"] },
    "primaryEnv": "OPENROUTER_API_KEY",
    "install": [
      {
        "id": "python-brew",
        "kind": "brew",
        "formula": "python",
        "bins": ["python3"],
        "label": "Install Python (brew)",
      }
    ]
  }
}

# OpenRouter Image Gen

Generate images via OpenRouter's image generation API (powered by Google Gemini Flash 2.5).

## Run

```bash
python3 {baseDir}/scripts/gen.py
open ~/Projects/tmp/claw-openrouter-image-gen-*/index.html  # if ~/Projects/tmp exists; else ./tmp/...
```

Useful flags:

```bash
# Generate multiple images with random prompts
python3 {baseDir}/scripts/gen.py --count 16

# Single prompt
python3 {baseDir}/scripts/gen.py --prompt "ultra-detailed studio photo of a lobster astronaut" --count 4

# Custom output directory
python3 {baseDir}/scripts/gen.py --out-dir ./out/images
```

## Model

The default model is `google/gemini-2.5-flash-image-preview`. This uses OpenRouter's multimodal API with the `modalities: ["image", "text"]` parameter to generate images.

## Output

- `*.png` images
- `prompts.json` (prompt → file mapping)
- `index.html` (thumbnail gallery)

## API Reference

See [OpenRouter Image Generation Docs](https://openrouter.ai/docs/guides/overview/multimodal/image-generation) for more information.
