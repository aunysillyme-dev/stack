# Compute stack

GPU clouds and inference APIs for training, batch jobs, and cheap token serving. Reviewed 2026-11-28. Each entry below is name, link, one-line description, and a `free`, `freemium`, or `paid` tag. Check the provider before you rely on a price.

This stack has no separate illustrated guide yet.

- **Core tools and workflows:** [canonical.md](canonical.md) (plain text) · [canonical.json](canonical.json)
- **Full inventory (19):** [inventory.md](inventory.md) (plain text) · [inventory.json](inventory.json)
- **Resources by tier:** [free/](free/free.md) (`0`, [JSON](free/free.json)) · [freemium/](freemium/freemium.md) (`13`, [JSON](freemium/freemium.json)) · [premium/](premium/premium.md) (`6`, [JSON](premium/premium.json))
- **Community workflows:** [community/](community/). [Submit a workflow](../CONTRIBUTING.md).
- **Category metadata:** [stack.json](stack.json)

## GPU clouds

- [Modal](https://modal.com/): GPU and CPU cloud that bills per second. The pricing page includes $30 of monthly free credit. `freemium`
- [RunPod](https://www.runpod.io/): On-demand GPUs and serverless compute for training, inference, and batch jobs. `paid`
- [Lambda](https://lambda.com/): Cloud GPUs and clusters for training and scaling models. `paid`
- [Paperspace](https://www.paperspace.com/): DigitalOcean GPU cloud that still serves NVIDIA GPUs on Paperspace. `paid`
- [Lightning AI](https://lightning.ai/): PyTorch-oriented cloud for training, on-demand GPUs, and deploying models. `paid`
- [Vast.ai](https://vast.ai/): Marketplace for renting cloud GPUs by the job. `paid`
- [CoreWeave](https://www.coreweave.com/): Cloud platform built for large AI training and inference workloads. `paid`

## Inference APIs

- [Groq](https://groq.com/): Fast inference platform for running models at low latency. `freemium`
- [Cerebras](https://www.cerebras.ai/inference): Fast inference API. The product page offers $5 of free credit on a new account. `freemium`
- [OpenRouter](https://openrouter.ai/): One API that routes prompts across many models and prices. `freemium`
- [Hugging Face Inference](https://huggingface.co/docs/inference-providers/index): Inference Providers docs for running models through Hugging Face. `freemium`
- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/): Serverless model inference on Cloudflare's network. `freemium`
- [Google AI Studio](https://aistudio.google.com/): Browser console for prompting and shipping with the Gemini API. `freemium`
- [NVIDIA NIM](https://build.nvidia.com/): Catalog for trying NVIDIA NIM model APIs. `freemium`
- [Fireworks](https://fireworks.ai/): Platform for inference and for training specialized models. `freemium`
- [Together AI](https://www.together.ai/): Cloud for inference, fine-tuning, and GPU clusters. `freemium`
- [fal](https://fal.ai/): API for generative image, video, and audio models on serverless GPUs. `freemium`
- [Replicate](https://replicate.com/): Cloud API for running machine-learning models. `freemium`
- [DeepInfra](https://deepinfra.com/): Hosted inference for open models with usage-based pricing. `freemium`

## How a compute job runs

1. Put the heavy training, image, or video job on a GPU cloud and set a runtime cap before it starts.
2. Save weights and outputs to durable storage before that machine stops.
3. Serve interactive token calls from an inference API and keep the provider and model id with the result.
4. Compare two providers on the same short prompt set before you leave the prototype there.

[Browse community workflows](community/) · [Category metadata](stack.json)
