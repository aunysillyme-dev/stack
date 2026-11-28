# Compute stack: core tools and workflows

Curated by @aunysillyme · Reviewed 2026-11-28

Source: https://modal.com/

## Core tools (19)

- **[Modal](https://modal.com/):** Freemium. GPU and CPU cloud that bills per second. The pricing page includes $30 of monthly free credit.
- **[RunPod](https://www.runpod.io/):** Paid. On-demand GPUs and serverless compute for training, inference, and batch jobs.
- **[Lambda](https://lambda.com/):** Paid. Cloud GPUs and clusters for training and scaling models.
- **[Paperspace](https://www.paperspace.com/):** Paid. DigitalOcean GPU cloud that still serves NVIDIA GPUs on Paperspace.
- **[Lightning AI](https://lightning.ai/):** Paid. PyTorch-oriented cloud for training, on-demand GPUs, and deploying models.
- **[Vast.ai](https://vast.ai/):** Paid. Marketplace for renting cloud GPUs by the job.
- **[CoreWeave](https://www.coreweave.com/):** Paid. Cloud platform built for large AI training and inference workloads.
- **[Groq](https://groq.com/):** Freemium. Fast inference platform for running models at low latency.
- **[Cerebras](https://www.cerebras.ai/inference):** Freemium. Fast inference API. The product page offers $5 of free credit on a new account.
- **[OpenRouter](https://openrouter.ai/):** Freemium. One API that routes prompts across many models and prices.
- **[Hugging Face Inference](https://huggingface.co/docs/inference-providers/index):** Freemium. Inference Providers docs for running models through Hugging Face.
- **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/):** Freemium. Serverless model inference on Cloudflare's network.
- **[Google AI Studio](https://aistudio.google.com/):** Freemium. Browser console for prompting and shipping with the Gemini API.
- **[NVIDIA NIM](https://build.nvidia.com/):** Freemium. Catalog for trying NVIDIA NIM model APIs.
- **[Fireworks](https://fireworks.ai/):** Freemium. Platform for inference and for training specialized models.
- **[Together AI](https://www.together.ai/):** Freemium. Cloud for inference, fine-tuning, and GPU clusters.
- **[fal](https://fal.ai/):** Freemium. API for generative image, video, and audio models on serverless GPUs.
- **[Replicate](https://replicate.com/):** Freemium. Cloud API for running machine-learning models.
- **[DeepInfra](https://deepinfra.com/):** Freemium. Hosted inference for open models with usage-based pricing.

## Workflows (2)

### Burst a GPU job, then serve cheaper tokens

Source: https://modal.com/pricing

1. Put the training, batch image, or video job on a GPU cloud such as Modal, RunPod, Lambda, Lightning, or Vast.ai and set a runtime cap before it starts.
2. Write the weights or outputs to durable storage before the machine stops so the next step does not depend on that instance.
3. Serve the interactive text or small-model calls from an inference API such as Groq, Cerebras, OpenRouter, Workers AI, or Google AI Studio.
4. Run the same short prompt set on two providers, compare latency and cost, and keep the provider, model id, and sample response with the workflow.

### Prototype in a free inference console

Source: https://aistudio.google.com/

1. Draft the prompt in Google AI Studio, Groq, Cerebras, or NVIDIA NIM and write down the model id that produced the useful answer.
2. If the free quota is too small, send the same request shape to OpenRouter, Hugging Face Inference, Fireworks, Together, fal, Replicate, or DeepInfra.
3. Record the provider, model id, a sample response, and what the call costs before leaving the prototype on that route.
